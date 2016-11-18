# -*- coding: utf-8 -*-
"""Extraction forms."""
from flask_wtf import Form
from wtforms import PasswordField, StringField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RequestForm(Form):
    """Request form."""
    
    source = SelectField(u'Data Source', choices=[('twitter', 'Twitter'), ('flickr', 'Flickr')])
    
    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(RequestForm, self).__init__(*args, **kwargs)
        self.user = None
    
    def validate(self):
        """Validate the form."""
        initial_validation = super(RequestForm, self).validate()
        if not initial_validation:
            return False
        
        if not self.source.data:
            return False
        return True
