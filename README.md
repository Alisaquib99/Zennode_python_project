# Zennode_python_project
**Calculate Total Function**
This Python code defines a function calculate_total that calculates the total cost of a shopping cart with three different products (A, B, and C). The function takes into account various discount rules based on quantities and offers optional gift wrap services.

**Usage**
To use the function, call calculate_total with the quantities of each product and their respective gift wrap flags. For example:
calculate_total(50, True, 120, False, 80, True)
This example signifies a shopping cart with 50 units of Product A (with gift wrap), 120 units of Product B (without gift wrap), and 80 units of Product C (with gift wrap).

**Discounts**
The code applies the following discounts:

Bulk Discount: 5% discount for quantities greater than 10 for each product.
Tiered Discount: 50% discount for the entire cart if the total quantity exceeds 30, and at least one product has a quantity greater than 15.
Flat 10% Discount: Applied if the cart total exceeds $200.

**Additional Fees**
The code also calculates additional fees:

Gift Wrap Fee: $1 per unit for products with gift wrap.
Shipping Fee: $5 for every 10 units, based on the total quantity in the cart.

**Output**
The function prints a detailed breakdown of each product's cost, the subtotal, applied discounts, shipping fee, and the final total.

**Function Breakdown**
calculate_discount: Calculates bulk discounts for each product.
calculate_tiered_discount: Calculates the tiered discount for the entire cart.
calculate_shipping_fee: Determines the shipping fee based on the total quantity.
calculate_gift_wrap_fee: Calculates the gift wrap fee for each product.
apply_discount: Applies the highest applicable discount to the cart.
calculate_product_total: Calculates the total cost of a product, including gift wrap fees.
calculate_cart_total: Determines the overall cart total and applies relevant discounts.

**Note**
This code assumes a fixed price for each product and fixed discount rates. Modify the prices and discount variables if there are changes in pricing or discount policies.

Feel free to adapt and use this code as a foundation for a more complex shopping cart system or integrate it into an existing project.








