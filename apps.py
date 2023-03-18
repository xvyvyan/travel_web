from flask import request,render_template,Flask


app = Flask(__name__)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 验证用户名和密码
        # ...
        # 如果验证成功，返回登录成功的页面
        return '登录成功'
    return render_template('login.html')

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=10001, debug=False)
