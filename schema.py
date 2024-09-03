def serielaize_data(data):
        for result in data:
            return {"name": result["name"],
                    "age": result["age"],
                    "phone_no": result["phone_no"],
                    "marital_status": result["marital_status"],
                    "shopping_zone": result["shopping_zone"],
                    "address": result["address"]
                    }