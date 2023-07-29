import requests
import json


def picsum(seed, w, h):
    picsum_response = json.loads(
        requests.get(f"https://picsum.photos/seed/{seed}/info").text
    )

    picsum_response_url: str = picsum_response["download_url"]

    result_picsum_url: str = picsum_response_url[
        0:picsum_response_url.rfind("/", 0, picsum_response_url.rfind("/"))
    ]
    result_picsum_url += f"/{w}/{h}"

    result_picsum_response = requests.get(result_picsum_url)

    return {
        "data": result_picsum_response.content,
        "Content-Type": result_picsum_response.headers["Content-Type"]
    }
