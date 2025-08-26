from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host="redis", port=6379)

import debugpy
debugpy.listen(("0.0.0.0", 5678))
print("Debugger is active. Attach VS Code to port 5678 to debug.")
# If we want to wait for a debug session to continue or we can add a breakpoint
# debugpy.wait_for_client()

@app.get("/")
def read_root():
    return {"Message": "Hello World, from DevContainers!"}

@app.get("/hits")
def read_root():
    r.incr("hits")
    return {"number of hits": r.get("hits")}
