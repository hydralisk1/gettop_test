from behave import then, when


@then('"{message}" message shown if no products match selected filters')
def verify_no_product(context, message):
    context.app.shop_page.verify_no_product(message)

