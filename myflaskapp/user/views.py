# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, session, flash, redirect, url_for, request
from flask_login import login_required
from myflaskapp.extraction.forms import RequestForm
from myflaskapp.utils import flash_errors

blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@blueprint.route('/')
@login_required
def members():
    """List members."""
    return render_template('users/members.html', session=session)


# @blueprint.route('/requests/', methods=['GET', 'POST'])
# def requests():
#     """Register new user."""
#     form = RegisterForm(request.form, csrf_enabled=False)
#     if form.validate_on_submit():
#         User.create(username=form.username.data, email=form.email.data, password=form.password.data, active=True)
#         flash('Thank you for registering. You can now log in.', 'success')
#         return redirect(url_for('public.home'))
#     else:
#         flash_errors(form)
#     return render_template('public/register.html', form=form)
        
        
@blueprint.route('/make_request/', methods=['GET', 'POST'])
@login_required
def make_request():
    """Request data."""
    form = RequestForm(request.form)
    if request.method == 'POST':
        print "1"
        if form.validate_on_submit():
            print "2"
            # User.create(username=form.username.data, email=form.email.data, password=form.password.data, active=True)
            flash('Successful request.', 'success')
            redirect_url = url_for('users.members')
            return redirect(redirect_url)
        else:
            print "3"
            flash_errors(form)
    return render_template('users/make_request.html', form=form)


#
# @blueprint.route('/register/', methods=['GET', 'POST'])
# def register():
#     """Register new user."""
#     form = RegisterForm(request.form, csrf_enabled=False)
#     if form.validate_on_submit():
#         User.create(username=form.username.data, email=form.email.data, password=form.password.data, active=True)
#         flash('Thank you for registering. You can now log in.', 'success')
#         return redirect(url_for('public.home'))
#     else:
#         flash_errors(form)
#     return render_template('public/register.html', form=form)