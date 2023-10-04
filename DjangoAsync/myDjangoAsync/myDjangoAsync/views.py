from django.shortcuts import render
from django.http import HttpResponse
import time
from datetime import datetime
import os


def index(request):
    return HttpResponse("Hello world!")


def check(request):
    return HttpResponse("using {}".format(os.environ.get('SERVER_GATEWAY_INTERFACE')))


def test1(request):
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
    return HttpResponse("Hello world! \nDuration: "+str(duration_in_seconds)+" \nStarting time: " + str(start_time_readable) + "\nEnding time: " + str(end_time_readable))
