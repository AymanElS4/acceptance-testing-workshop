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
        """
        Products:
        - Coffee
        - Sugar
        """

Feature: Update the quantity of a product
    Scenario: Update the quantity of a product
        Given the inventory contains products:
            | Product | Quantity |
            | Coffee | 10 |
        When the user updates product "Coffee" to quantity "25"
        Then the inventory should show product "Coffee" with quantity "25"

Feature: Remove a product from the inventory
  Scenario: Remove a product from the inventory
    Given the inventory contains products:
      | Product |
      | Coffee  |
      | Sugar   |
    When the user removes the product "Coffee"
    Then the inventory should not contain "Coffee"