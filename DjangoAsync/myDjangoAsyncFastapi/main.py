from fastapi import FastAPI
import time
from datetime import datetime
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test1")
async def test1():
    start_time = time.time()
    start_time_readable = datetime.fromtimestamp(
        start_time).strftime('%Y-%m-%d %H:%M:%S')
    print("Starting time: " + str(start_time_readable))
    time.sleep(10)
    # i = 0
    # while time.time() < start_time + 10:
    #     print(i)
    #     i+=1
    end_time = time.time()
    end_time_readable = datetime.fromtimestamp(
        end_time).strftime('%Y-%m-%d %H:%M:%S')
    print("Ending time: " + str(end_time_readable))
    duration_in_seconds = end_time - start_time
    return {"Hello world! \nDuration: "+str(duration_in_seconds)+" \nStarting time: " + str(start_time_readable) + "\nEnding time: " + str(end_time_readable)}
