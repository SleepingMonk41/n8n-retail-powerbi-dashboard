import csv
import io
from datetime import datetime

def process(items):
    result_items = []

    for item in items:
        output_item = {"json": {}}
        users = item.get("json", {}).get("users", [])

        if not users:
            output_item["json"]["error"] = "No users found"
            result_items.append(output_item)
            continue

        # Define all the columns we want
        fieldnames = [
            "id", "firstName", "lastName", "maidenName", "age", "gender",
            "email", "phone", "username", "password", "birthDate", "image",
            "bloodGroup", "height", "weight", "eyeColor",
            "hair_color", "hair_type",
            "ip",
            "address_address", "address_city", "address_postalCode",
            "address_state", "address_coordinates_lat", "address_coordinates_lng"
        ]

        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        for user in users:
            flat = {
                "id": user.get("id"),
                "firstName": user.get("firstName"),
                "lastName": user.get("lastName"),
                "maidenName": user.get("maidenName"),
                "age": user.get("age"),
                "gender": user.get("gender"),
                "email": user.get("email"),
                "phone": user.get("phone"),
                "username": user.get("username"),
                "password": user.get("password"),
                "birthDate": user.get("birthDate"),
                "image": user.get("image"),
                "bloodGroup": user.get("bloodGroup"),
                "height": f'{user.get("height", 0):.2f}',
                "weight": f'{user.get("weight", 0):.2f}',
                "eyeColor": user.get("eyeColor"),
                "hair_color": user.get("hair", {}).get("color"),
                "hair_type": user.get("hair", {}).get("type"),
                "ip": user.get("ip"),
                "address_address": user.get("address", {}).get("address"),
                "address_city": user.get("address", {}).get("city"),
                "address_postalCode": user.get("address", {}).get("postalCode"),
                "address_state": user.get("address", {}).get("state"),
                "address_coordinates_lat": user.get("address", {}).get("coordinates", {}).get("lat"),
                "address_coordinates_lng": user.get("address", {}).get("coordinates", {}).get("lng")
            }

            writer.writerow(flat)

        csv_content = output.getvalue()
        output_item["json"]["csv"] = csv_content
        output_item["json"]["fileName"] = f"users_export_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
        result_items.append(output_item)

    return result_items

return process(items)
