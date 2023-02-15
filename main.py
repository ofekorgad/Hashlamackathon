import base64
import requests


API = "http://127.0.0.1:5000/run"


s = {
    "metadata": {
        "strict": 0,
        "type": 1
    },
    "data": base64.encodebytes(b"This is my text to filter.").decode()
}


def main():
    response = requests.post(API, json=s)
    print(response.content)


if __name__ == "__main__":
    main()
