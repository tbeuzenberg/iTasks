import json


def json_decode_string(str_in):
    return json.loads(str_in)


def json_decode_file(file_in):
    return json.load(file_in)
