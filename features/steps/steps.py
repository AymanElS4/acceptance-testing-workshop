from behave import given, when, then

#Add a product and remove a product that does not exist
""" Parte de Christian
@given('the inventory is empty')
def step_impl(context):
    context.inventory = []

@when('the user adds a product "{product}"')
def step_impl(context, product):
    context.inventory.append(product)

@then('the inventory should contain "{product}"')
def step_impl(context, product):
    assert product in context.inventory, f'Product "{product}" not found in the inventory'
"""

#List, remove, and update

@given('the inventory contains products:')
def step_impl(context):
    context.inventory = []
    for row in context.table:
        context.inventory.append(row['Product'])

@when('the user lists all products')
def step_impl(context):
    # Simulamos la salida de listar los productos
    context.output = "Products:\n"
    for product in context.inventory:
        context.output += f"- {product}\n"

@then('the output should contain:')
def step_impl(context):
    # context.text captura el bloque de texto multilinea del Then
    assert context.text.strip() in context.output.strip(), "The expected output does not match the actual output"

@when('the user updates product "{product}" to quantity "{quantity}"')
def step_impl(context, product, quantity):
    # Aquí simulamos el cambio en el output para la prueba.
    if product in context.inventory:
        context.output = f'Product "{product}" with quantity "{quantity}"'
    else:
        context.output = "Product not found"

@then('the inventory should show product "{product}" with quantity "{quantity}"')
def step_impl(context, product, quantity):
    expected_message = f'Product "{product}" with quantity "{quantity}"'
    assert context.output == expected_message, f'Expected {expected_message}, but got {context.output}'

@when('the user removes the product "{product}"')
def step_impl(context, product):
    if product in context.inventory:
        context.inventory.remove(product)
        context.output = f'Product {product} was removed'
    else:
        context.output = f'Product {product} was not found'

@then('the inventory should not contain "{product}"')
def step_impl(context, product):
    assert product not in context.inventory, f'Product "{product}" is still in the inventory'

@then('the output should be "{message}"')
def step_impl(context, message):
    assert context.output == message, f'Expected "{message}" but got "{context.output}"'