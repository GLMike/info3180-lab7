from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed, DataRequired
from wtforms import TextAreaField


class UploadForm(FlaskForm):

    description = TextAreaField('Description', 
                                validators=[DataRequired()])

    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])