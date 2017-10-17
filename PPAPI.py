from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=['POST'])
def checkout():
    body = request.json
    if len(body) == 2 and 'arg1' in body and 'arg2' in body:
        if type(body['arg1']) == str and type(body['arg2']) == str:
            if body['arg1'][0] == 'a' or body['arg1'][0] == 'A':
                arg1_a = 'an '
            else:
                arg1_a = 'a '
            if body['arg2'][0] == 'a' or body['arg2'][0] == 'A':
                arg2_a = 'an '
            else:
                arg2_a = 'a '

            return jsonify({'Error': False, 'PPAP': 'I have ' + arg1_a+body['arg1'] + "!"
                                                    + ' I have ' + arg2_a + body['arg2'] + "!"})
    return jsonify({'Error': True})


if __name__ == '__main__':
    app.run(debug=True)
