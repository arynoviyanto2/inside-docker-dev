from typing import Union
import redis
import debugpy

from fastapi import FastAPI

app = FastAPI()

r = redis.Redis(host="redis", port=6379)

debugpy.listen(("0.0.0.0", 5678))

@app.get("/")
def read_root():
    return {"msg": "Hello World!!"}

@app.get("/counter")
def read_root():
    r.incr("counter_key")
    return {"msg": r.get("counter_key")}