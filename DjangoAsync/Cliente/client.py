import requests as r
import httpx
import os
import asyncio
import time
from datetime import datetime
import json


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


def sync_get(url):
    response = r.get(url)
    return response


def sync_post(url, data):
    response = r.post(url, data=json.dumps(data))
    return response


def sync_gets(urls):
    responses = []
    for u in urls:
        responses.append(sync_get(u))
    return responses


def sync_posts(urls, data_list):
    responses = []
    for u, d in zip(urls, data_list):
        responses.append(sync_post(u, d))
    return responses


async def async_get(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=30)
        return response


async def async_post(url, data):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=json.dumps(data), timeout=30)
        return response


async def async_gets(urls):
    tasks = []
    for u in urls:
        tasks.append(asyncio.create_task(async_get(u)))
    # Run the tasks:
    res = []
    for t in tasks:
        res.append(await t)
    return res


async def async_posts(urls, data_list):
    tasks = []
    for u, d in zip(urls, data_list):
        tasks.append(asyncio.create_task(async_post(u, d)))
    # Run the tasks:
    res = []
    for t in tasks:
        res.append(await t)
    return res


async def main():
    # URL de la API en tu servidor local
    main_url = 'http://127.0.0.1:8000/'

    print("----------ASYNC----------")

    # urls = [
    #     main_url + 'get1/',
    #     main_url + 'get2/',
    # ]

    # res = await calc_time(async_gets, urls, asyn=True)
    # print("Response:", res)

    # print("--------------------")

    # urls = [
    #     main_url + 'get2/',
    #     main_url + 'get1/',
    # ]

    # res = await calc_time(async_gets, urls, asyn=True)
    # print("Response:", res)

    # print("--------------------")

    # urls = [
    #     main_url + 'get1/',
    #     main_url + 'get1/',
    # ]

    # res = await calc_time(async_gets, urls, asyn=True)
    # print("Response:", res)

    # print("--------------------")

    # urls = [
    #     main_url + 'get2/',
    #     main_url + 'get2/',
    # ]

    # res = await calc_time(async_gets, urls, asyn=True)
    # print("Response:", res)

    # print("--------------------")
    # urls = [
    #     main_url + 'get4/',
    #     main_url + 'get4/',
    # ]

    # res = await calc_time(async_gets, urls, asyn=True)
    # # Print the responses with the json attached in a readable way. (code\njson)
    # print("Responses: {}".format(
    #     '\n'.join([str(r.status_code) + '\n' + str(r.json()) for r in res])))

    print("--------------------")
    # NOW THE POST REQUESTS
    urls = [
        main_url + 'post1/',
        main_url + 'post2/',
    ]

    # The data to send
    data = {
        'names': ['Danel', 'Ander', 'Iñigo', 'Oier']
    }

    data_list = [data, data]

    res = await calc_time(async_posts, urls, data_list, asyn=True)

    # Print the responses with the json attached in a readable way. (code\njson)
    print("Responses: {}".format(
        '\n'.join([str(r.status_code) + '\n' + str(r.json()) for r in res])))

    print("--------------------")
    urls = [
        main_url + 'post2/',
        main_url + 'post2/',
    ]

    # The data to send
    data = {
        'names': ['Danel', 'Ander', 'Iñigo', 'Oier']
    }

    data_list = [data, data]

    res = await calc_time(async_posts, urls, data_list, asyn=True)

    # Print the responses with the json attached in a readable way. (code\njson)
    print("Responses: {}".format(
        '\n'.join([str(r.status_code) + '\n' + str(r.json()) for r in res])))

    print("----------SYNC----------")

    urls = [
        main_url + 'get1/',
        main_url + 'get2/',
    ]

    res = await calc_time(sync_gets, urls, asyn=False)
    print("Response:", res)

    print("--------------------")

    urls = [
        main_url + 'get2/',
        main_url + 'get1/',
    ]

    res = await calc_time(sync_gets, urls, asyn=False)
    print("Response:", res)

    print("--------------------")

    urls = [
        main_url + 'get1/',
        main_url + 'get1/',
    ]

    res = await calc_time(sync_gets, urls, asyn=False)
    print("Response:", res)

    print("--------------------")

    urls = [
        main_url + 'get2/',
        main_url + 'get2/',
    ]

    res = await calc_time(sync_gets, urls, asyn=False)
    print("Response:", res)

    print("--------------------")
    # NOW THE JSON RESPONSES
    urls = [
        main_url + 'get3/',
        main_url + 'get4/',
    ]

    res = await calc_time(sync_gets, urls, asyn=False)
    # Print the responses with the json attached in a readable way. (code\njson)
    print("Responses: {}".format(
        '\n'.join([str(r.status_code) + '\n' + str(r.json()) for r in res])))

    print("--------------------")
    urls = [
        main_url + 'get3/',
        main_url + 'get3/',
    ]

    res = await calc_time(sync_gets, urls, asyn=False)
    # Print the responses with the json attached in a readable way. (code\njson)
    print("Responses: {}".format(
        '\n'.join([str(r.status_code) + '\n' + str(r.json()) for r in res])))

    print("--------------------")
    # NOW THE POST REQUESTS
    urls = [
        main_url + 'post1/',
        main_url + 'post2/',
    ]

    # The data to send
    data = {
        'names': ['Danel', 'Ander', 'Iñigo', 'Oier']
    }

    data_list = [data, data]

    res = await calc_time(sync_posts, urls, data_list, asyn=False)

    # Print the responses with the json attached in a readable way. (code\njson)
    print("Responses: {}".format(
        '\n'.join([str(r.status_code) + '\n' + str(r.json()) for r in res])))

    print("--------------------")
    urls = [
        main_url + 'post2/',
        main_url + 'post2/',
    ]

    # The data to send
    data = {
        'names': ['Danel', 'Ander', 'Iñigo', 'Oier']
    }

    data_list = [data, data]

    res = await calc_time(sync_posts, urls, data_list, asyn=False)

    # Print the responses with the json attached in a readable way. (code\njson)
    print("Responses: {}".format(
        '\n'.join([str(r.status_code) + '\n' + str(r.json()) for r in res])))

    print("----------FIN----------")

# Ejecutar el bucle de eventos de asyncio
asyncio.run(main())
# asyncio.run(async_call('http://127.0.0.1:8000/test1/'))
# url = 'http://127.0.0.1:8000/'
# sync_call(url)
