from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check-string', methods=['POST'])
def check_string():
    """
    Endpoint for validating if a posted string is a pangram
    """

    # Forcing check for valid json and headers with Content-Type:application/json
    content = request.get_json(silent=False, force=True)

    payload = content.get('data', None)
    
    if not payload:
        return response_handler(
            {"error": "'data' key missing from JSON payload."},
            400
        )
    if not isinstance(payload, basestring):
        return response_handler(
            {"error": "Value of 'data' key is not of type 'string'."},
            400
        )
    
    pangram = analyze_string(payload)
    if not pangram:
        return response_handler(
            {"error": False},
            400
        )

    return response_handler(
        {"success": True},
        200
    )

def analyze_string(data):
    """
    Helper function to determine if a string is a pangram
    """
    import re

    # definition of alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # remove non alpha characters from string
    # we could also just use data.strip() here if we know our string will be fairly small and uncomplex
    regex = re.compile('[^a-zA-Z]')
    stripped_data = regex.sub('', data)

    if len(set(alphabet)) - len(set(stripped_data.lower())) == 0:
        return True
    
    return False

def response_handler(r_data, status_code):
    """
    Helper function to form response payload
    """
    import json

    r_json = json.dumps(r_data)

    r = Response(
        response=r_json,
        status=status_code,
        content_type='application/json'
    )

    return r

app.run(host='0.0.0.0',port= 8000, debug=True)