from flask import Flask, request
from api import get_projects, copy_projects, get_project_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def myapp():
    return 'WebServer'

@app.route('/myprojects', methods=['GET'])
def myprojects():
    return get_projects()

@app.route('/project', methods=['GET'])
def projectDetail():
    print(request.args.get('projectId'))
    return get_project_data(request.args.get('projectId'))

@app.route('/copyproject', methods=['POST','GET'])
def copyproject():
    return copy_projects(request.args.get('projectId'))