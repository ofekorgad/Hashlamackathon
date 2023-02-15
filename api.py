from flask import Flask, request


api = Flask(__name__)


@api.route("/run", methods=["POST"])
def get_result():
    if request.headers.get("Content-Type") != "application/json":
        return '', 405

    try:
        request_dict = request.get_json()
        # TODO: Call Algorithm wrapper with response parameters
        return b'100', 200

    except KeyError:
        return '', 400
