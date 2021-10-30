from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

SECRET_KEY = 'lkajfljfl'


class GetCommand(FlaskForm):
    """
    Форма получения команды для отправки на роутер
    """
    command = StringField('Форма отправки команды на роутер',
                          validators=[DataRequired()],
                          render_kw={"class": "form-control",
                                     "placeholder": "Введите команду"})
    command_type = BooleanField('Config-mode', default=False)
    submit = SubmitField('Send Command',
                         render_kw={"class": "btn btn-secondary"})
