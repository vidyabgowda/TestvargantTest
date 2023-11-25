class ShoppingCart:
    Basket = [
        {"product": "Leather wallet", "unit_price": 1100, "gst_percentage": 18, "quantity": 1},
        {"product": "Umbrella", "unit_price": 900, "gst_percentage": 12, "quantity": 4},
        {"product": "Cigarette", "unit_price": 200, "gst_percentage": 28, "quantity": 3},
        {"product": "Honey", "unit_price": 100, "gst_percentage": 0, "quantity": 2},
    ]
    def calculate_max_gst(Basket):
        total_amount = 0
        max_gst_product= None
        max_gst_amount = 0
        for product in Basket:
            unit_price = product["unit_price"]
            gst_percentage = product["gst_percentage"]
            quantity = product["quantity"]
            total_amount += unit_price * quantity
            gst_amount = (unit_price * gst_percentage / 100) * quantity
            if gst_amount > max_gst_amount:
                max_gst_amount = gst_amount
                max_gst_product = product["product"]
        return total_amount, max_gst_product
    total_amount, max_gst_product = calculate_max_gst(Basket)
    print(f"Total amount to be paid to shopkeeper:rs.{total_amount}")
    print(f"Product with maximum GST: {max_gst_product}")
