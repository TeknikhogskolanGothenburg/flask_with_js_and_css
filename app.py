from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=["GET"])
def get_index():
    if len(request.args) > 0:
        user = request.args['user']
        return render_template('index.html', user=user)
    else:
        return render_template('index.html')


@app.route('/', methods=["POST"])
def post_index():
    first_name = request.form['first']
    last_name = request.form['last']
    email_address = request.form['email']

    return redirect(url_for('get_index', user=first_name))


if __name__ == '__main__':
    app.run()


