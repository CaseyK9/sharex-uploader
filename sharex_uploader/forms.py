from flask_wtf import Form
from flask_wtf.file import FileField
from wtforms.validators import DataRequired


class UploadForm(Form):
    file = FileField('Upload file: ', validators=[DataRequired()])
