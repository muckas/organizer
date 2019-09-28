from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, SelectField

class EditForm(FlaskForm):
  submit = SubmitField('Submit')
  content = TextAreaField('', render_kw = {'rows': 12, 'cols': 30})

class AddForm(FlaskForm):
  submit = SubmitField('Submit')
  name = StringField('Name')
  content = TextAreaField('', render_kw = {'rows': 12, 'cols': 30})

class DelForm(FlaskForm):
  submit = SubmitField('Submit')
  result = RadioField('Are you sure?', choices=[('yes', 'Yes'), ('no', 'No')])
