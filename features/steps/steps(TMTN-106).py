from behave import then, when


@when('Hover over {category} Category Menu')
def hover_over_category(context, category):
    context.app.main_page.hover_over_category(category)


@then('User can see all items under the category')
def verify_items_under_category(context):
    context.app.main_page.verify_items_under_category()


@then('Verify correct pages open when clicking on each product')
def verify_links_on_dropdown(context):
    context.app.main_page.verify_links_on_dropdown()

