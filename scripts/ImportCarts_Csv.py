import csv
import io
import random
from datetime import datetime

def process(items):
    result_items = []

    for item in items:
        output_item = {"json": {}}
        carts = item.get("json", {}).get("carts", [])

        if not carts:
            output_item["json"]["error"] = "No carts found"
            result_items.append(output_item)
            continue

        # Add user_id as second column
        fieldnames = [
            "cart_id", "user_id", "product_id", "title", "price", "quantity",
            "total", "discountPercentage", "discountedTotal", "thumbnail"
        ]

        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=",", quoting=csv.QUOTE_ALL)
        writer.writeheader()

        # Dictionary to store consistent user_id per cart_id
        cart_user_map = {}

        for cart in carts:
            cart_id = cart.get("id")

            # Assign a random user_id per cart_id
            if cart_id not in cart_user_map:
                cart_user_map[cart_id] = random.randint(1, 208)

            user_id = cart_user_map[cart_id]

            for product in cart.get("products", []):
                row = {
                    "cart_id": cart_id,
                    "user_id": user_id,
                    "product_id": product.get("id"),
                    "title": product.get("title"),
                    "price": f'{product.get("price", 0):.2f}',
                    "quantity": product.get("quantity"),
                    "total": f'{product.get("total", 0):.2f}',
                    "discountPercentage": f'{product.get("discountPercentage", 0):.2f}',
                    "discountedTotal": f'{product.get("discountedTotal", 0):.2f}',
                    "thumbnail": product.get("thumbnail"),
                }
                writer.writerow(row)

        csv_content = output.getvalue()
        output_item["json"]["csv"] = csv_content
        output_item["json"]["fileName"] = f"carts_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
        result_items.append(output_item)

    return result_items

return process(items)
