from behave import given, then


@given('Open the {product} product page')
def open_product_page(context, product):
    context.app.product_page.open_product_page(product)


@then('"{block_title}" block is shown')
def verify_block(context, block_title):
    context.app.product_page.verify_block(block_title)


@then('It contains products')
def verify_products(context):
    context.app.product_page.verify_products()


@then('Verify all product links under the block are clickable and take to correct pages')
def verify_links(context):
    context.app.product_page.verify_links()