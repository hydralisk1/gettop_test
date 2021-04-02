from behave import given, then


@given('Open GetTop page')
def open_gettop_page(context):
    context.app.main_page.open_main_page()


@then('Verify {category1}, {category2}, {category3} categories are shown in the footer')
def verify_categories(context, category1, category2, category3):
    context.app.main_page.verify_categories(category1, category2, category3)


@then('Verify all products in the footer have price, name, star-rating')
def verify_products(context):
    context.app.main_page.verify_products()


@then('Verify "{text}" is shown in the footer')
def verify_string(context, text):
    context.app.main_page.verify_string(text)


@then('Verify the footer has a button to go back to top')
def verify_button_to_top(context):
    context.app.main_page.verify_button_to_top()


@then('Verify the footer has working links to all product categories')
def verify_all_links_working(context):
    context.app.main_page.verify_all_links_working()
