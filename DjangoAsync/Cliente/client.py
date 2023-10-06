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

    res = None

    # Call the function with provided arguments
    if asyn:
        res = await func(*args)
    else:
        res = func(*args)

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
    return res


def sync_call(url):
    response = r.get(url)
    return response


def sync_calls(urls):
    responses = []
    for u in urls:
        responses.append(sync_call(u))
    return responses


async def async_call(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=30)
        return response


async def async_calls(urls):
    tasks = []
    for u in urls:
        tasks.append(asyncio.create_task(async_call(u)))
    # Run the tasks:
    res = []
    for t in tasks:
        res.append(await t)
    return res


async def main():
    # URL de la API en tu servidor local
    main_url = 'http://127.0.0.1:8000/'

    print("----------ASYNC----------")

    urls = [
        main_url + 'test1/',
        main_url + 'test2/',
    ]

    res = await calc_time(async_calls, urls, asyn=True)
    print("Response:", res)

    print("--------------------")

    urls = [
        main_url + 'test2/',
        main_url + 'test1/',
    ]

    res = await calc_time(async_calls, urls, asyn=True)
    print("Response:", res)

    print("--------------------")

    urls = [
        main_url + 'test1/',
        main_url + 'test1/',
    ]

    res = await calc_time(async_calls, urls, asyn=True)
    print("Response:", res)

    print("--------------------")

    urls = [
        main_url + 'test2/',
        main_url + 'test2/',
    ]

    res = await calc_time(async_calls, urls, asyn=True)
    print("Response:", res)

    print("----------SYNC----------")

    urls = [
        main_url + 'test1/',
        main_url + 'test2/',
    ]

    res = await calc_time(sync_calls, urls, asyn=False)
    print("Response:", res)

    print("--------------------")

    urls = [
        main_url + 'test2/',
        main_url + 'test1/',
    ]

    res = await calc_time(sync_calls, urls, asyn=False)
    print("Response:", res)

    print("--------------------")

    urls = [
        main_url + 'test1/',
        main_url + 'test1/',
    ]

    res = await calc_time(sync_calls, urls, asyn=False)
    print("Response:", res)

    print("--------------------")

    urls = [
        main_url + 'test2/',
        main_url + 'test2/',
    ]

    res = await calc_time(sync_calls, urls, asyn=False)
    print("Response:", res)

    print("----------FIN----------")
# Ejecutar el bucle de eventos de asyncio
asyncio.run(main())
# asyncio.run(async_call('http://127.0.0.1:8000/test1/'))
# url = 'http://127.0.0.1:8000/'
# sync_call(url)
