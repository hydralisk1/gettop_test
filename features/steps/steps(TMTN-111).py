from behave import given, then, when


@then('Verify correct categories exists under Browser')
def verify_correct_categories_under_browse(context):
    context.app.shop_page.verify_correct_categories_under_browse()


@then('Verify correct pages open when clicking on categories under Browse')
def verify_correct_page_under_browse(context):
    context.app.shop_page.verify_correct_page_under_browse()
