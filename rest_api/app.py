# !flask/bin/python
from flask import Flask, jsonify, request
from flask import make_response, abort, url_for
from workers.invoke_workers import Workers
from entities.MapperEntity import MapperEntity

workers = Workers()
app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to the Data Mapper REST API"


def create_mapper_entity(source, payload, query_type):
    mapper_entity = MapperEntity()
    mapper_entity.query_type = query_type
    mapper_entity.payload = payload
    mapper_entity.source = source
    return mapper_entity


@app.route('/mapper/api/v1.0/', methods=['POST'])
def perform_mapper_action():
    data = request.get_json()
    if not data or 'source' not in data or 'payload' not in data or 'query_type' not in data:
        abort(400)
    if len(data['source']) == 0 or len(data['payload']) == 0 or len(data['query_type']) == 0:
        abort(400)
    mapper_entity = create_mapper_entity(data['source'], data['payload'], data['query_type'])
    response = workers.invoke(mapper_entity)
    try:
        # This is a very rudimentary manner of handling JSON responses and is mostly wrong
        response = jsonify(response)
    except Exception as e:
        print(e)
        response = str(response)
    return jsonify({"response": str(response)}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
    # return jsonify({'error' : 'Not found'})


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


if __name__ == '__main__':
    app.run(debug=True)
