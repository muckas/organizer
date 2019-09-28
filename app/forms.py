from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField

class EditForm(FlaskForm):
  submit = SubmitField('Submit')
  content = TextAreaField('', render_kw = {'rows': 12, 'cols': 30})

class NewForm(FlaskForm):
  submit = SubmitField('Submit')
  name = StringField('Name')
  content = TextAreaField('', render_kw = {'rows': 12, 'cols': 30})
