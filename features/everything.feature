Feature: Add a product to the inventory
    Scenario: Add a product to the inventory
        Given the inventory is empty
        When the user adds a product "Coffee"
        Then the inventory should contain "Coffee"

Feature: List all products in the inventory
    Scenario: List all products in the inventory
        Given the inventory contains products:
            | Product |
            | Coffee |
            | Sugar |
        When the user lists all products
        Then the output should contain:
    Products:
    - Coffee
    - Sugar