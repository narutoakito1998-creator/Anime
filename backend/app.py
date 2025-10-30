from flask import Flask

app = Flask(__name__)

@app.route('/api/hello')
def hello_world():
    return {'message': 'Привет от бэкенда uwurposting!'}

if __name__ == '__main__':
    app.run(debug=True)
