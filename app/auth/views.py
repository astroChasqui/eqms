from flask import render_template, session, redirect, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .. import db
from .forms import LoginForm, RegistrationForm

@auth.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(url_for('main.index'))
        flash('Email o contraseña incorrectas')
    return render_template('auth/login.html', form=form)

@auth.route('/salir')
@login_required
def salir():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data,
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Ahora puede ingresar')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form) 
