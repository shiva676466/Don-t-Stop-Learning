from flask import render_template, redirect, url_for, flash, request
from . import auth
from .forms import LoginForm, RegisterForm
from .. import db
from ..models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # placeholder: in real app validate password
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('Logged in (placeholder).')
            return redirect(url_for('main.dashboard'))
        flash('Invalid credentials')
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registered (placeholder).')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/logout')
def logout():
    flash('Logged out (placeholder).')
    return redirect(url_for('main.index'))
