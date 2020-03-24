from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', index_content = 'Hello world')


@app.route('/home/')
def home():
    return render_template('index.html', index_content = 'This is my Index Page....xxx')

@app.route('/about/')
def about():

    context={}
    context['title'] = 'About us'
    context['index_content'] = 'I am About page , welcome you...'

    return render_template('about.html', **context)


if __name__ == '__main__':
    app.run(host = '0.0.0.0')
