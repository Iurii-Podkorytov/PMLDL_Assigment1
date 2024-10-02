from fastapi import FastAPI, File
from PIL import Image
import joblib
import io
import numpy as np
import uvicorn

app = FastAPI(title="Digit Recognition API")

model = joblib.load('model.joblib') 

@app.get("/")
def root():
    return {"message": "Digit Recognition API"}

@app.post("/predict")
async def predict(file: bytes = File(...)):
    img = Image.open(io.BytesIO(file)).convert('L')
    image_array = np.array(img).reshape((1, -1))
    prediction = model.predict(image_array)
    return {"predicted_digit": int(prediction[0])}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)