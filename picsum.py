from fastapi import Response, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import requests
from json.decoder import JSONDecodeError
import json


def picsum(seed, w, h):
    try:
        picsum_response = json.loads(
            requests.get(f"https://picsum.photos/seed/{seed}/info").text
        )
    except JSONDecodeError:
        return JSONResponse(
            content=jsonable_encoder({"message": "Probably location not allowed"}),
            status_code=status.HTTP_400_BAD_REQUEST
        )

    picsum_response_url: str = picsum_response["download_url"]

    result_picsum_url: str = picsum_response_url[
                             0:picsum_response_url.rfind("/", 0, picsum_response_url.rfind("/"))
                             ]
    result_picsum_url += f"/{w}/{h}"

    result_picsum_response = requests.get(result_picsum_url)

    return Response(
        content=result_picsum_response.content,
        headers={
            "Content-Type": result_picsum_response.headers["Content-Type"]
        }
    )
