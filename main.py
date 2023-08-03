from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from hashmap import hashmap
from picsum import picsum
from typing import Optional

from time import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get('/')
async def _root():
    return {'message': 'Hello World'}


@app.get('/hashmap')
@app.get('/hashmap/{seed}')
@app.get('/hashmap/{seed}/{w}')
@app.get('/hashmap/{seed}/{w}x{h}')
@app.get('/hashmap/{seed}/{w}/{h}')
async def _hashmap(seed: Optional[str] = "", w: Optional[int] = 7, h: Optional[None | int] = None):
    if seed == "":
        seed = str(int(time()))
    if h is None:
        h = w
    if w > 100 or w < 1 or h > 100 or h < 1:
        return JSONResponse(
            content=jsonable_encoder({"message": "Both width and height must be in range 1..100"}),
            status_code=status.HTTP_400_BAD_REQUEST
        )

    return hashmap(seed, w, h)


@app.get('/picsum')
@app.get('/picsum/{seed}')
@app.get('/picsum/{seed}/{w}')
@app.get('/picsum/{seed}/{w}x{h}')
@app.get('/picsum/{seed}/{w}/{h}')
async def _picsum(seed: Optional[str] = "", w: Optional[int] = 64, h: Optional[None | int] = None):
    if seed == "":
        seed = str(int(time()))
    if h is None:
        h = w
    if w < 1 or h < 1:
        return JSONResponse(
            content=jsonable_encoder({"message": "Both width and height must > 0"}),
            status_code=status.HTTP_400_BAD_REQUEST
        )

    return picsum(seed, w, h)
