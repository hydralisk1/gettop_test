from behave import then, when


@when('User sets the price filter to {min_price} dollars and {max_price} dollars using the slide bar')
def set_filter(context, min_price, max_price):
    context.app.shop_page.set_filter(min_price, max_price)


@then('Click on the filter button')
def click_filter_button(context):
    context.app.shop_page.click_filter_button()


@then('Verify the Price filter worked')
def verify_price_filter(context):
    context.app.shop_page.verify_price_filter()


@when('Click on X from the {which} price filter to remove it')
def click_x_button(context, which):
    context.app.shop_page.click_x_button(which)


@then('Verify {which} price filter slider handle position resents')
def verify_price_filter_handle(context, which):
    context.app.shop_page.verify_price_filter_handle(which)
