import csv
import io
import base64
from datetime import datetime

def process(items):
    result_items = []

    for item in items:
        output_item = {"json": {}, "binary": {}}
        products = item.get("json", {}).get("products", [])

        if not products:
            output_item["json"]["error"] = "No products found"
            result_items.append(output_item)
            continue

        # Get all possible fieldnames from the first product
        sample_product = products[0]
        fieldnames = list(sample_product.keys())
        
        # Add flattened dimensions
        fieldnames += ["dimensions_width", "dimensions_height", "dimensions_depth"]
        
        # Add review fields
        fieldnames += [
            f"review_{i}_{field}"
            for i in range(1,4)
            for field in ["rating", "comment", "reviewer"]
        ]
        
        # Remove original nested fields
        fieldnames = [f for f in fieldnames if f not in {"dimensions", "reviews", "tags"}]
        fieldnames.append("tags")  # Re-add as joined string

        output = io.StringIO()
        writer = csv.DictWriter(
            output,
            fieldnames=fieldnames,
            delimiter=",",
            quoting=csv.QUOTE_ALL  # Quote all fields for safety
        )
        writer.writeheader()

        for product in products:
            flat = {}
            
            # Handle simple fields
            for key in ["id", "title", "availabilityStatus", "brand", "category",
                       "description", "discountPercentage", "minimumOrderQuantity",
                       "price", "rating", "returnPolicy", "shippingInformation",
                       "sku", "stock", "thumbnail", "warrantyInformation", "weight"]:
                flat[key] = product.get(key)

            # Handle dimensions
            dimensions = product.get("dimensions", {})
            flat.update({
                "dimensions_width": dimensions.get("width"),
                "dimensions_height": dimensions.get("height"),
                "dimensions_depth": dimensions.get("depth")
            })

            # Handle tags
            flat["tags"] = ", ".join(product.get("tags", []))

            # Handle reviews
            reviews = product.get("reviews", [])
            for i, review in enumerate(reviews[:3], 1):
                flat.update({
                    f"review_{i}_rating": review.get("rating"),
                    f"review_{i}_comment": review.get("comment"),
                    f"review_{i}_reviewer": review.get("reviewerName")
                })

            writer.writerow(flat)

        csv_content = output.getvalue()
        csv_content = output.getvalue()
        output_item["json"]["csv"] = csv_content
        output_item["json"]["fileName"]=f"products_consistent_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
        result_items.append(output_item)

    return result_items

return process(items)