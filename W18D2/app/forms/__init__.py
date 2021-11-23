from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    rating = SelectField('Rating', choices=["New favorite" "Great", "Good", "Underwhelming", "Bad", "Horrible"])
    submit = SubmitField('Add Book')