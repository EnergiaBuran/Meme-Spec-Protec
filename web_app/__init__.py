from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for
)

from .meme import fake_talents


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/', methods=['POST'])
    def process_url():
        try:
            code = fake_talents(request.form['url'])
        except ValueError:
            return render_template('home.html', invalid=True, old_url=request.form['url'])
        return render_template('output.html', code='\n'.join(code), lines_of_code=len(code))

    return app
