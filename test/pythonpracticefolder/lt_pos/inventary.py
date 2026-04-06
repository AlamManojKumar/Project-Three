"""This module have necessary functions to handle an Inventary.
"""
###ITEMS:list[dict[str,object]]=[]
ITEMS:list[dict] =[]
def add_items(item_name:str,
              description:str,
              price:int|float,
              quantity:int)->bool:
    """Add items to the inventory

    Args:
         itemname: Name of the product.
         description: Description of the product.
         price: Price of the product.
         quantity: Quantity of the product.

    Returns:
           True if added, False otherwise.
    """
#Validate
    if price < 1 and quantity < 1:
        return False
unique_id = len(ITEMS)+1
ITEMS.append({
    "item_id": unique_id,
    "description": description,
    "item_name": itemname,
    "price": price,
    "quantity": quantity 
    })
return True

def delete_items(item)->bool:
    """Delete item from the inventary.

    Args:
       item_id(int): itemid
    
    Returns:
       bool: True if deleted False otherwise
    """
    if item_id in ITEMS:
        del ITEMS[item_id]
        return True
    else:
        return False

def update_items(item_id:int,
                 item_name:str,
                 description:str,
                 quantity:int,
                 price:int|float,
                 )->bool:
    """update items to the inventory

    Args:
        item_id(int): id of the product.
        item_name(str): name of the product
        description(str): description.
        price(int|float): price.
        quantity(int): quantity.

    Returns:
          bool: Returns true if added False otherwise.
    """
#Validate
    if price < 1 and quantity < 1:
        return False
    ITEMS[item_id] = {
    "itemid" :item_id,
    "name": item_name,
    "description": description,
    "quantity": quantity,
    "price": price
    }
def search_item_by_name(item_name:str)->list[dict]|None:
       """This method is used to search item by name

       Args:
           item_name: name of the product

       Returns:
             list[dict]| None: items found, or None if no match

       """
       results = []
       for  item in ITEMS:
           if item_name.lower() in item['name'].lower():
              results.append(item)
       return results or None
 
       
   


