import uvicorn
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
import numpy as np
import tensorflow as tf

from application import functions
print(functions.myfunc())


app_desc = "this page is dummy page"
app = FastAPI(title='Tensorflow FastAPI', description=app_desc)
absolute_path = 'C:/Users/Anditya/Desktop/tensorflow-fastapi-starter-pack/application/server'
model = None


def load_model():
    global model
    if model is None:
        model = tf.keras.models.load_model(f'{absolute_path}/model')


def predict(headline, text):

    # preprocessing
    model_input = headline + '. ' + text
    print(model_input)
    model_input = tf.expand_dims(tf.constant(model_input), axis=0)

    # predict
    if model is None:
        return 'model error', 'model error'
    prediction = model(model_input)
    prediction = float(prediction[0][0])
    confidence = (.5 + abs(prediction-.5))*100
    if prediction > .5:
        prediction = f'Selaras'
    else:
        prediction = f'Tidak Selaras/Clickbait'
    return prediction, confidence


@app.post('/predict/clickbait')
async def predict_clickbait(request: Request):
    form_data = await request.form()
    headline = form_data['inputHeadline']
    text = form_data['inputText']
    prediction, confidence = predict(headline, text)
    return {'prediction': prediction, 'confidence': confidence}


@app.get("/dashboard")
async def read_html():
    load_model()
    print('model loaded')
    with open(f"{absolute_path}/static/index.html", "r") as f:
        html = f.read()
    return HTMLResponse(content=html)


if __name__ == "__main__":
    uvicorn.run(app, debug=True)
