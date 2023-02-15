import requests


API = "http://127.0.0.1:5000/result"

myfiles = {
    'data': open('text.txt', 'rb'),
    'meta': open('metadata.json', 'rb')
}

s = {
    "metadata": {
        "strict": 0,
        "type": 1
    },
    "data": "This is my text to filter."
}


def main():
    response = requests.post(API, json=s)
    print(response.content)


if __name__ == "__main__":
    main()
