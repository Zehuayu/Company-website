from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
       return render_template('index.html') 

# @app.route('/route_name', methods=['GET', 'POST'])
# def method_name():
#    pass


if __name__ == "__main__":
    app.run(debug = True, port=8000) ##同事也可以输入主机地址和端口
    