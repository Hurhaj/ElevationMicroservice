from typing import List

import srtm
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class Location(BaseModel):
    latitude: float
    longitude: float

class Elevations(BaseModel):
    eleva: List[float]
# load environment variables

# initialize FastAPI
app = FastAPI()


@app.get("/")
def index():
    return {"data": "Microservice elevation ran successfully -version 0.0.2"}


@app.post("/elevation")
async def return_elevation(locations: List[Location]):
    elevation_data = srtm.get_data()
    elevations = []
    for lo in locations:
        elevations.append(elevation_data.get_elevation(lo.latitude, lo.longitude))
    return Elevations(eleva=elevations)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
