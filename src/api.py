import base64
from lead_alg import LeadAlg
from flask import Flask, request


# HTTP response codes
OK = 200
BAD_REQUEST = 400


api = Flask(__name__)


@api.route("/run", methods=["POST"])
def get_result():
    """
    Routes the post request into the API's main functionality.
    Expects the post request to contain a JSON dict of the following format:
    {
        "metadata": {
            "strict": Number 0-3 (see enums/strictness.py),
            "text_type": Number 1-3 (see enums/text_types.py)
            "is_zip": If true, alerts the lead_alg to unpack the zip and return array of results.
        },
        "data": Base64 encoded data that is the text files to convert.
    }

    :return:    Tuple, response content and HTTP response code.
                If the data is valid and can be processed, the response will be a number (percentage from 1-100)
                and the response code will be 200 (OK).
                Otherwise, the response will be blank and the response code will be 400 (Bad request).
    """
    if request.headers.get("Content-Type") != "application/json":
        # Bad request HTTP response
        return '', BAD_REQUEST

    try:
        request_dict = request.get_json()

        # Unpack JSON
        text = base64.decodebytes(request_dict["data"].encode())
        strict = request_dict["metadata"]["strict"]
        text_type = request_dict["metadata"]["type"]
        is_zip = request_dict["metadata"]["is_zip"]

        try:
            return str(LeadAlg.run(text, strict, text_type, is_zip)), OK
        except Exception as e:
            return '', BAD_REQUEST

    except KeyError:
        return '', BAD_REQUEST


if __name__ == "__main__":
    LeadAlg.init()
    api.run()
