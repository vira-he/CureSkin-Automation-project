from behave import given, when, then


@when("Open the first product in search")
def open_first_prod(context):
    context.app.search_result_page.open_first_prod()


@then("Verify the fist product in Sunscreen")
def verify_search_result(context):
    context.app.search_result_page.verify_search_result()


