
# 核心依赖‌：路由和调试由 Werkzeug 提供，模板引擎用的是 Jinja2。‌‌
# 内置服务器仅用于开发调试，生产环境需要搭配 Gunicorn 或 uWSGI 等 WSGI 服务器。‌‌

from flask import Flask 
from flask import url_for
from flask import request
from markupsafe import escape
from flask import render_template
from werkzeug.utils import secure_filename
from flask import make_response
from flask import abort, redirect, url_for
from flask import session

app = Flask(__name__)

@app.route("/")
def index():
    #  username = request.cookies.get('username')
     # use cookies.get(key) instead of cookies[key] to not get a
     # KeyError if the cookie is missing.
    # return 'index'
    # resp = make_response(render_template('index.html'))
    # return redirect(url_for('login'))
    pass

@app.route('/login')
def login():
    return 'login'
    # abort(401)
    # this_is_never_executed()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do_the_login'
        # return do_the_login()
    else:
        return 'show_the_login_form'
        # return show_the_login_form()

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)


# searchword = request.args.get('key', '')

# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)
    # resp = make_response(render_template('hello.html', person=name))
    # resp.set_cookie('username', 'the username')
    # return resp

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# url_for('static', filename='style.css')

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')



# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['the_file']
#         file.save(f"/var/www/uploads/{secure_filename(file.filename)}")
  


# @app.errorhandler(404)
# def not_found(error):
#     return render_template('error.html'), 404
# 可以使用 make_response() 包裹返回表达式，获得响应对象， 并对该对象进行修改，然后再返回:

# @app.errorhandler(404)
# def not_found(error):
#     resp = make_response(render_template('error.html'), 404)
#     resp.headers['X-Something'] = 'A value'
#     return resp  


# @app.route("/me")
# def me_api():
#     user = get_current_user()
#     return {
#         "username": user.username,
#         "theme": user.theme,
#         "image": url_for("user_image", filename=user.image),
#     }

# @app.route("/users")
# def users_api():
#     users = get_all_users()
#     return [user.to_json() for user in users]   




# Set the secret key to some random bytes. Keep this really secret!
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# @app.route('/')
# def index():
#     if 'username' in session:
#         return f'Logged in as {session["username"]}'
#     return 'You are not logged in'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return '''
#         <form method="post">
#             <p><input type=text name=username>
#             <p><input type=submit value=Login>
#         </form>
#     '''

# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))


# get_flashed_messages() 


# app.logger.debug('A value for debugging')
# app.logger.warning('A warning occurred (%d apples)', 42)
# app.logger.error('An error occurred')


# from werkzeug.middleware.proxy_fix import ProxyFix
# app.wsgi_app = ProxyFix(app.wsgi_app)
# 用 app.wsgi_app 来包装，而不用 app 包装，意味着 app 仍旧 指向您的 Flask 应用，而不是指向中间件。这样可以继续直接使用和配置 app 。


# Flask-SQLAlchemy 
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


    # with app.test_request_context('/hello', method='POST'):
    # # now you can do something with the request until the
    # # end of the with block, such as basic assertions:
    # assert request.path == '/hello'
    # assert request.method == 'POST'


    # with app.request_context(environ):
    # assert request.method == 'POST'





if __name__ == "__main__":
    app.run()



# 关于响应对象

# 如果视图返回的是一个响应对象，那么就直接返回它。

# 如果返回的是一个字符串，那么根据这个字符串和缺省参数生成一个用于 返回的响应对象。

# 如果返回的是一个迭代器或者生成器，那么返回字符串或者字节，作为流 响应对待。

# 如果返回的是一个字典或者列表，那么使用 jsonify() 创建一个响应对象。

# 如果返回的是一个元组，那么元组中的项目可以提供额外的信息。元组中 必须至少包含一个项目，且项目应当由 (response, status) 、 (response, headers) 或者 (response, status, headers) 组 成。 status 的值会重载状态代码， headers 是一个由额外头部 值组成的列表或字典。

# 如果以上都不是，那么 Flask 会假定返回值是一个有效的 WSGI 应用并把 它转换为一个响应对象。

