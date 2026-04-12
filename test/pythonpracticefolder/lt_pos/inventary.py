"""This module have necessary functions to handle an Inventary."""
ITEMS: list[dict] = []
def add_items(item_id: str,
              item_name: str,
              description: str,
              price: int | float,
              quantity: int) -> bool:
    if price < 1 and quantity < 1:
        return False
    ITEMS.append({
        "item_id": item_id,
        "name": item_name,          
        "description": description,
        "price": price,
        "quantity": quantity
    })
    return True

def delete_item(item_id: str) -> bool:
    for item in ITEMS:
        if item.get("item_id") == item_id:
            ITEMS.remove(item)
            return True
    return False

def update_items(item_id: str,
                 item_name: str,
                 description: str,
                 quantity: int,
                 price: int | float) -> bool:
    for item in ITEMS:
        if item.get("item_id") == item_id:
            item["name"] = item_name
            item["description"] = description
            item["quantity"] = quantity
            item["price"] = price
            return True
    return False
def search_item_by_name(item_name: str) -> list[dict] | None:
    results = []
    for item in ITEMS:
        if item.get('name') and item_name.lower() == item['name'].lower():  # ✅ ==
            results.append(item)
    return results or None

    
 
       
   


