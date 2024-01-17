def calculate_total(quantity_a, is_gift_a, quantity_b, is_gift_b, quantity_c, is_gift_c):
    prices = {
        'A': 20,
        'B': 40,
        'C': 50
    }

    flat_10_discount = 10
    bulk_5_discount = 0.05
    bulk_10_discount = 0.10
    tiered_50_discount = 0.50

    total_amount = 0
    cart_total = 0
    discount_applied = ''
    discount_amount = 0
    shipping_fee = 0
    gift_wrap_fee = 0

    # Calculate the discount based on quantity
    def calculate_discount(quantity, discount):
        result = prices[discount] * quantity if quantity > 10 else 0
        return result

    # Calculate tiered discount
    def calculate_tiered_discount(quantity, price):
        return (quantity - 15) * price * tiered_50_discount if quantity > 15 else 0

    # Calculate shipping fee based on quantity
    def calculate_shipping_fee(quantity):
        return (quantity // 10) * 5

    # Calculate gift wrap fee based on quantity and is_gift flag
    def calculate_gift_wrap_fee(quantity, is_gift):
        return quantity if is_gift else 0

    # Apply discount if the calculated amount is higher
    def apply_discount(discount_name, amount):
        nonlocal discount_amount, discount_applied
        if amount > discount_amount:
            discount_amount = amount
            discount_applied = discount_name

    # Calculate total for a product, including gift wrap fee
    def calculate_product_total(quantity, price, is_gift):
        nonlocal total_amount, cart_total
        product_total = quantity * price
        gift_wrap_fee = calculate_gift_wrap_fee(quantity, is_gift)
        total_amount += product_total + gift_wrap_fee
        cart_total += product_total
        return product_total + gift_wrap_fee

    # Calculate the total for the entire cart and apply relevant discounts
    def calculate_cart_total():
        nonlocal cart_total
        total_quantity = quantity_a + quantity_b + quantity_c

        if total_quantity > 30 and (quantity_a > 15 or quantity_b > 15 or quantity_c > 15):
            tiered_discount = calculate_tiered_discount(total_quantity, prices['A'])
            apply_discount('tiered_50_discount', tiered_discount)
        elif total_quantity > 20:
            bulk_discount = cart_total * bulk_10_discount
            apply_discount('bulk_10_discount', bulk_discount)
        elif quantity_a > 10:
            bulk_discount_a = calculate_discount(quantity_a, 'A')
            apply_discount('bulk_5_discount', bulk_discount_a)
        elif quantity_b > 10:
            bulk_discount_b = calculate_discount(quantity_b, 'B')
            apply_discount('bulk_5_discount', bulk_discount_b)
        elif quantity_c > 10:
            bulk_discount_c = calculate_discount(quantity_c, 'C')
            apply_discount('bulk_5_discount', bulk_discount_c)

        if cart_total > 200:
            apply_discount('flat_10_discount', flat_10_discount)

    calculate_cart_total()

    # Calculate total for each product
    product_a_total = calculate_product_total(quantity_a, prices['A'], is_gift_a)
    product_b_total = calculate_product_total(quantity_b, prices['B'], is_gift_b)
    product_c_total = calculate_product_total(quantity_c, prices['C'], is_gift_c)

    # Calculate shipping fee and final totals
    shipping_fee = calculate_shipping_fee(total_amount)

    subtotal = cart_total - discount_amount
    grand_total = subtotal + shipping_fee

    # Display results
    print(f"Product A: Quantity - {quantity_a}, Total - ${product_a_total}")
    print(f"Product B: Quantity - {quantity_b}, Total - ${product_b_total}")
    print(f"Product C: Quantity - {quantity_c}, Total - ${product_c_total}")
    print(f"Subtotal: ${subtotal}")
    print(f"Discount Applied: {discount_applied} - ${discount_amount}")
    print(f"Shipping Fee: ${shipping_fee}")
    print(f"Total: ${grand_total}")

# Example usage
calculate_total(50, True, 120, False, 80, True)
