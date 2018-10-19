from wtforms import Form, StringField, TextAreaField, HiddenField

class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')

class EditForm(PostForm):
    id = HiddenField('id')