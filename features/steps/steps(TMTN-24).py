from behave import given, then, when


@given('Open the shop page')
def open_shop_page(context):
    context.app.shop_page.open_shop_page()


@given('Open the shop page via https://gettop.us/shop/{direct_link}')
def open_shop_page_directly(context, direct_link):
    context.app.shop_page.open_shop_page_directly(direct_link)


@when('Choose {option} from the select box')
def choose_one_from_select_box(context, option):
    context.app.shop_page.choose_one_from_select_box(option)


@then('Verify products are displayed in correct order')
def verify_products_in_correct_order(context):
    context.app.shop_page.verify_products_in_correct_order()


@then("Verify the Select box displays correct option")
def verify_option(context):
    context.app.shop_page.verify_option()
