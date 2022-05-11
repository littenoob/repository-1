from models import app

@app.after_request
def add_allowed_orgin(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'content-type: application/json; charset=utf-8'
    return response
