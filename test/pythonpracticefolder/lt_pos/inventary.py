"""This module have necessary functions to handle an Inventary.
"""
###ITEMS:list[dict[str,object]]=[]
ITEMS:list[dict] =[]
def add_items(itemname:str,
              description:str,
              price:int|float,
              quantity:int)->bool:
"""Add items to the inventory
Args:
    name(str): name of the product
    description(str): description.
    price(int|float): price.
    quantity(int): quantity.

Returns:
      bool: Returns true if added False otherwise.
"""
#Validate
if price < 1 and quantity < 1:
   return False
unique_id = len(ITEMS)+1
ITEMS.append({
    "id": unique_id,
    "description": description,
    "itemname": itemname,
    "price": price,
    "quantity": quantity 
    })
return True


