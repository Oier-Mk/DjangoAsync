import requests as r
import httpx
import os
import asyncio
import time
from datetime import datetime

async def calc_time(func, *args, asyn=False, verbose=True):
    '''
    Wrapper for calculating how much time does the func take
    '''
    # Get start time
    start_time = time.time()
    start_time_readable = datetime.fromtimestamp(
        start_time).strftime('%Y-%m-%d %H:%M:%S')
    if verbose:
        print("Starting time:", start_time_readable)

    # Call the function with provided arguments
    if asyn:
        await func(*args)
    else:
        func(*args)
        
    # Get end time and calculate duration
    end_time = time.time()
    end_time_readable = datetime.fromtimestamp(
        end_time).strftime('%Y-%m-%d %H:%M:%S')
    if verbose:
        print("Ending time:", end_time_readable)
    duration_in_seconds = end_time - start_time

    if verbose:
        print("FINISHED\nDuration: {}s \nStarting time: {}s\nEnding time:{}".format(
            duration_in_seconds,
            start_time_readable,
            end_time_readable
        ))


def sync_call(url):
    response = r.get(url)
    return response

async def async_call(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout = 30)
        return response

async def async_calls(urls):
    tasks = []
    for u in urls:
        tasks.append(asyncio.create_task(async_call(u)))
    # Run the tasks:
    res = []
    for t in tasks:
        res.append(await t)
    #FIXME: res no se usa

async def main():
    # URL de la API en tu servidor local
    main_url = 'http://127.0.0.1:8000/'

    print("----------COMIENZO----------")
    
    urls=[
        main_url + 'test1/',
        main_url + 'test2/',
    ]

    await calc_time(async_calls,urls, asyn=True)

    print("--------------------")
    
    urls=[
        main_url + 'test2/',
        main_url + 'test1/',
    ]

    await calc_time(async_calls,urls, asyn=True)

    print("--------------------")    

    urls=[
        main_url + 'test1/',
        main_url + 'test1/',
    ]

    await calc_time(async_calls,urls, asyn=True)

    print("--------------------")
        
    urls=[
        main_url + 'test2/',
        main_url + 'test2/',
    ]

    await calc_time(async_calls,urls, asyn=True)

    print("----------FIN----------")

asyncio.run(main())