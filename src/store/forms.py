from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField, FloatField, IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Length, Email, InputRequired
from store.models import Customer, Supplier
from flask_login import current_user


class RegistrationForm(FlaskForm):
    role=SelectField("Select role", coerce=str, choices=[("1","Customer"), ("2","Supplier")])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        if self.role.data == "1":
            table = Customer
        elif self.role.data == "2":
            table = Supplier
        if table.query.filter_by(email=email.data).first():
            raise ValidationError("Duplicate email")


class LoginForm(FlaskForm):
    role = SelectField("Select role",coerce=str,choices=[("1","Customer"),("2","Supplier")])
    email = StringField('Mail',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField('Sign in')


class UpdateInfo(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Mail',validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_email(self, email):
        if current_user.table_name == "Customer":
            table = Customer
        elif current_user.table_name == "Supplier":
            table = Supplier
        user = table.query.filter_by(email=email.data).first()
        if user and user.username !=current_user.username:
            raise ValidationError("Duplicate email")


class UpdatePasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Update')


class UpdateConsigneeForm(FlaskForm):
    consignee = StringField("Consignee",validators=[InputRequired(),Length(min=2,max=20)])
    address = StringField("Address",validators=[InputRequired(),Length(min=10,max=40)])
    telephone = StringField("Telephone",validators=[InputRequired(),Length(max=20,min=9)])
    submit = SubmitField("Update")


class UpdateShipperForm(FlaskForm):
    shipper = StringField('Company name',validators=[InputRequired(), Length(min=5, max=40)])
    address = StringField('Company address',validators=[InputRequired(),Length(min=5, max=40)])
    telephone = StringField("Telephone", validators=[InputRequired(), Length(max=20, min=9)])
    submit = SubmitField('Update')


class ProductForm(FlaskForm):
    name = StringField('Product name',validators=[DataRequired(), Length(min=2, max=40)])
    price =FloatField("Product price", validators=[DataRequired()])
    count = IntegerField("Product count", validators=[DataRequired()])
    confirm = IntegerField("Confirm Product count",validators=[DataRequired(), EqualTo("count")])
    submit = SubmitField("Add")


class UpdateProductForm(FlaskForm):
    name = StringField('Product name',validators=[InputRequired(), Length(min=2, max=40)])
    price = FloatField("Product price", validators=[InputRequired()])
    count = IntegerField("Product count", validators=[InputRequired()])
    confirm = IntegerField("Confirm Product count", validators=[InputRequired(), EqualTo("count")])
    submit = SubmitField("Update")
