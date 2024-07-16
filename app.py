from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
from scripts.make_prediction import make_single_prediction
from pydantic import BaseModel
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/prediction", response_class=JSONResponse)
async def prediction(
    pickup_datetime: str = Form(...),
    pickup_longitude: str = Form(...),
    pickup_latitude: str = Form(...),
    dropoff_longitude: str = Form(...),
    dropoff_latitude: str = Form(...),
    passenger_count: str = Form(...)
):
    # Convert strings to correct types and perform prediction
    prediction = make_single_prediction(pickup_datetime, float(pickup_longitude), float(pickup_latitude), 
                                        float(dropoff_longitude), float(dropoff_latitude), int(passenger_count))

    return JSONResponse(content={"prediction": float(prediction)})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)
