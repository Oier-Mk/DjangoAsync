from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
import time
import os
import json
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello world!")


def check(request):
    if (os.environ.get('SERVER_GATEWAY_INTERFACE') == "Web"):
        return HttpResponse("using WSGI")
    else:
        return HttpResponse("using ASGI")


def get1(request):
    start_time = time.time()
    start_time_readable = datetime.fromtimestamp(
        start_time).strftime('%Y-%m-%d %H:%M:%S')
    print("Starting time: " + str(start_time_readable))
    time.sleep(2)
    end_time = time.time()
    end_time_readable = datetime.fromtimestamp(
        end_time).strftime('%Y-%m-%d %H:%M:%S')
    print("Ending time: " + str(end_time_readable))
    duration_in_seconds = end_time - start_time
    return HttpResponse("Hello world! \nDuration: "+str(duration_in_seconds)+" \nStarting time: " + str(start_time_readable) + "\nEnding time: " + str(end_time_readable))


def get2(request):
    start_time = time.time()
    start_time_readable = datetime.fromtimestamp(
        start_time).strftime('%Y-%m-%d %H:%M:%S')
    print("Starting time: " + str(start_time_readable))
    time.sleep(5)
    end_time = time.time()
    end_time_readable = datetime.fromtimestamp(
        end_time).strftime('%Y-%m-%d %H:%M:%S')
    print("Ending time: " + str(end_time_readable))
    duration_in_seconds = end_time - start_time
    return HttpResponse("Hello world! \nDuration: "+str(duration_in_seconds)+" \nStarting time: " + str(start_time_readable) + "\nEnding time: " + str(end_time_readable))


def get3(request):
    start_time = time.time()
    start_time_readable = datetime.fromtimestamp(
        start_time).strftime('%Y-%m-%d %H:%M:%S')
    print("Starting time: " + str(start_time_readable))
    time.sleep(2)
    end_time = time.time()
    end_time_readable = datetime.fromtimestamp(
        end_time).strftime('%Y-%m-%d %H:%M:%S')
    print("Ending time: " + str(end_time_readable))
    duration_in_seconds = end_time - start_time
    response_data = {
        'message': 'Hello world!',
        'duration': duration_in_seconds,
        'start_time': start_time_readable,
        'end_time': end_time_readable
    }
    return JsonResponse(response_data)


def get4(request):
    start_time = time.time()
    start_time_readable = datetime.fromtimestamp(
        start_time).strftime('%Y-%m-%d %H:%M:%S')
    print("Starting time: " + str(start_time_readable))
    time.sleep(5)
    end_time = time.time()
    end_time_readable = datetime.fromtimestamp(
        end_time).strftime('%Y-%m-%d %H:%M:%S')
    print("Ending time: " + str(end_time_readable))
    duration_in_seconds = end_time - start_time
    response_data = {
        'message': 'Hello world!',
        'duration': duration_in_seconds,
        'start_time': start_time_readable,
        'end_time': end_time_readable
    }
    return JsonResponse(response_data)


@csrf_exempt
def post1(request):
    '''Post view, receives a json with a list of names and returns a json with a list of greetings'''
    start_time = time.time()
    start_time_readable = datetime.fromtimestamp(
        start_time).strftime('%Y-%m-%d %H:%M:%S')
    print("Starting time: " + str(start_time_readable))
    time.sleep(2)

    # Process the jsone
    json_data = json.loads(request.body)
    names = json_data['names']
    greetings = []
    for n in names:
        greetings.append("Hello "+n+"!")

    end_time = time.time()
    end_time_readable = datetime.fromtimestamp(
        end_time).strftime('%Y-%m-%d %H:%M:%S')
    print("Ending time: " + str(end_time_readable))

    duration_in_seconds = end_time - start_time

    print("Duration: "+str(duration_in_seconds) +
          " \nStarting time: " + str(start_time_readable) + "\nEnding time: " + str(end_time_readable))

    response_data = {
        'greetings': greetings
    }

    return JsonResponse(response_data)


@csrf_exempt
def post2(request):
    '''Post view, receives a json with a list of names and returns a json with a list of greetings'''
    start_time = time.time()
    start_time_readable = datetime.fromtimestamp(
        start_time).strftime('%Y-%m-%d %H:%M:%S')
    print("Starting time: " + str(start_time_readable))
    time.sleep(5)

    # Process the json
    json_data = json.loads(request.body)
    names = json_data['names']
    greetings = []
    for n in names:
        greetings.append("Hello "+n+"!")

    end_time = time.time()
    end_time_readable = datetime.fromtimestamp(
        end_time).strftime('%Y-%m-%d %H:%M:%S')
    print("Ending time: " + str(end_time_readable))

    duration_in_seconds = end_time - start_time

    print("Duration: "+str(duration_in_seconds) +
          " \nStarting time: " + str(start_time_readable) + "\nEnding time: " + str(end_time_readable))

    response_data = {
        'greetings': greetings
    }

    return JsonResponse(response_data)
