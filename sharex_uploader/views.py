import os, string, random
from sharex_uploader import app
from flask import render_template, redirect, url_for, request, send_from_directory, abort
from werkzeug.utils import secure_filename


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['DISALLOWED_EXTENSIONS']


@app.errorhandler(403)
def accessdenied(e):
    return render_template('403.html'), 403


@app.errorhandler(500)
def errored(e):
    return render_template('403.html'), 500


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    password = request.form.get('password')
    if password == app.config['PASSWORD']:
        file = request.files['file']
        if file and not allowed_file(file.filename):
            filename = secure_filename(file.filename)
            extension = '.' in filename and filename.rsplit('.', 1)[1]
            filename = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in
                               range(app.config['RANDSTRING_LENGTH']))
            filename = filename + "." + extension
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
        else:
            abort(403)
    else:
        abort(403)


@app.route('/i/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
