from flask_wtf import FlaskForm
from wtforms import DateField,StringField,FloatField,SubmitField
from wtforms.validators import DataRequired,Length,ValidationError
from datetime import date

class MovementsForm(FlaskForm):
    date = DateField('Fecha', validators=[DataRequired(message='La fecha es requerida')])
    concept = StringField('Concepto', validators=[DataRequired(message='El concepto es requerido'),Length(min=4,message='Más de 4 carácteres por favor')])
    quantity = FloatField('Monto', validators=[DataRequired(message='El monto es requerido, debe ser mayor a 0')])

    submit = SubmitField('Guardar')

    def validate_date(form,field):
        if field.data > date.today():
            raise ValidationError('Fecha Invalida: La fecha no debe ser mayor a hoy')