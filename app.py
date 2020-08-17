#!/bin/python

# Dependencies:
# pip install flask
# pip install redis

from sanic import Sanic
from sanic import response
from sanic.response import json
import requests
import requests
import redis
import time
import json
import sys
import os
from settings import *
from sanic.log import logger

from provider import get_weather


def get_redis():
    try:
        url = os.getenv('REDIS_URL')
        if url:
            db = redis.Redis.from_url(url)
        else: 
            db = redis.Redis(host='localhost') #connect to server
        
        db.get("test")
        return db
    except Exception as e:
        logger.error(f"Could not start Redis: {e}")
        print("could not connect to redis")
        sys.exit(1)

api_key = os.environ.get("API_KEY")
app = Sanic(__name__)
app.debug = True
db = get_redis()

@app.get("/")
async def home(request):
    return response.json({"hello":True})

@app.get("/health")
async def health(request):
    try:
        pong = db.get("test")
        return response.json({"status":"OK"})
    except Exception as e:
        logger.error(f"Error with health check service: {e}")
        return response.json({"status":f"Error: {e}"})

@app.get("/weather/<city>")
async def home(request, city):
    key = f"{CACHE_PREFIX}-{city}"
    weather = db.get(key) #conider pickle or some other serialization
    
    if not weather:
        status, weather, err = get_weather(city, api_key)
        if err:
            return response.json({"error":"Could not get weather"})
        
        db.set(key, json.dumps(weather), ex=TTL)
    else:
        weather = json.loads(weather)
    return response.json(weather)


   
