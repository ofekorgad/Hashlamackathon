import base64
import requests
from enums.text_types import TextType


API = "http://127.0.0.1:5000/run"


s = {
    "metadata": {
        "strict": 0,
        "type": TextType.Generic.value
    },
    "data": base64.encodebytes(b"Please help. I no good.").decode()
}


def main():
    response = requests.post(API, json=s)
    print(response.content)


if __name__ == "__main__":
    main()
