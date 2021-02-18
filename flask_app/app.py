from flask import Flask, request, abort, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def upload():
    if not request.is_json:
        abort(400)

    content = request.get_json()

    security_groups = set()

    for module in content['modules']:
    	resources = module['resources']
    	sgs = [x for x in resources.values() if 'type' in x and x['type'] == 'aws_security_group']
    	security_groups.update(x['primary']['id'] for x in sgs)

    return jsonify(list(security_groups))

@app.route('/', methods=['GET'])
def resp():
    return 'Use curl -X POST -H "Content-Type: application/json" -d @terraform_state_for_interview.json localhost:5000\n'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
