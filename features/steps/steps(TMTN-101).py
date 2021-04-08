from behave import given, then, when


@given('Open the my account page')
def open_my_account(context):
    context.app.account_page.open_my_account()


@when('User tries log in with {email} and {pw}')
def login_try(context, email, pw):
    context.app.account_page.login_try(email, pw)


@then('Verify login was failed')
def verify_login_failed(context):
    context.app.account_page.verify_login_failed()


@then('Verify correct error message was displayed')
def verify_error_msg(context):
    context.app.account_page.verify_error_msg()