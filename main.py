import flask

import os
from flask import request, jsonify, send_from_directory, render_template, stream_with_context


app = flask.Flask(__name__)
app.config["DEBUG"] = True
# add views directory


# Index route to index.html
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run()