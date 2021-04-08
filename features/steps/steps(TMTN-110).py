from behave import given, then, when


@given('Open {category} Category page')
def open_category_page(context, category):
    context.app.category_page.open_category_page(category)


@then('Only items of correct category are shown')
def verify_items_have_correct_category(context):
    context.app.category_page.verify_items_have_correct_category()


@then('"Showing all N results" is present and reflects correct amount of items')
def verify_result_message(context):
    context.app.category_page.verify_result_message()


@then('Verify all items have Category, Name and Price')
def verify_items_have(context):
    context.app.category_page.verify_items_have()


@then('User can click on Quick View for all items and close it by clicking on closing X')
def click_quick_view(context):
    context.app.category_page.open_and_close_quick_view()


@then('User can click on Quick View for all items and add product to cart')
def add_product_from_quick_view_to_cart(context):
    context.app.category_page.add_product_from_quick_view_to_cart()
