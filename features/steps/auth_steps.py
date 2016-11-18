from behave import *

@given(u'myflaskapp is set up')
def myflaskapp_is_setup(context):
    assert context.client