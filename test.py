from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 允许跨域


@app.route('/', methods=["POST"])
def index():
    data = request.get_json()
    tel = data["tel"]
    pwd = data["pwd"]
    res_data = {}
    if (tel=='13639490306' and pwd=='123456'):
        res_data = {'code': 1, 'mag': '登陆成功'}
    else:
        res_data = {'code': 2, 'mag': '登陆失败'}
    return jsonify(res_data)


if __name__ == '__main__':
    app.run(debug=True)


