from behave import given, then, when
# from time import sleep


@when('Click on the {number} product on the page')
def click_product(context, number):
    context.app.shop_page.click_product(number)


@then('Open the shop page again')
def open_shop_page_directly(context):
    context.app.shop_page.open_shop_page()


@then('Verify the recently viewed item is on top in the item list')
def verify_recently_viewed_item(context):
    context.app.shop_page.verify_recently_viewed_item()


@when('Click on the recently viewed item on top')
def click_viewed_item(context):
    context.app.shop_page.click_viewed_item()


@then('Verify the correct page is open')
def verify_page(context):
    context.app.shop_page.verify_page()
