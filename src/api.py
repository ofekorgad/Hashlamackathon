import base64

from lead_alg import LeadAlg
from flask import Flask, request


OK = 200
BAD_REQUEST = 400


api = Flask(__name__)


@api.route("/run", methods=["POST"])
def get_result():
    if request.headers.get("Content-Type") != "application/json":
        # Bad request HTTP response
        return '', BAD_REQUEST

    try:
        request_dict = request.get_json()

        text = base64.decodebytes(request_dict["data"].encode())
        strict = request_dict["metadata"]["strict"]
        text_type = request_dict["metadata"]["type"]

        return str(LeadAlg.run(text, strict, text_type)), OK

    except KeyError:
        return '', BAD_REQUEST


if __name__ == "__main__":
    LeadAlg.init()
    api.run()
