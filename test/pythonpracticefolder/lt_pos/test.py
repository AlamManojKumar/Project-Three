"""This module is only for testing functions
"""
from inventary import add_items,ITEMS,update_items,delete_item,search_item_by_name,add_items
def test_add_products():
    if len(ITEMS) == 0:
        print("it is working correctly ")
    add_items(item_id="t001",
              item_name="Tajmahaltea",
              description="Tajmahaltea",
              price=100,
              quantity=10)
    add_items(item_id="Th-002",
              item_name="Threerosestea",
              description="Threerosestea",
              price=150,
              quantity=20)
    add_items(item_id="c001",
              item_name="cintholSoap",
              description="cintholSoap",
              price=50,
              quantity=14)
    add_items(item_id="t002",
              item_name="tofucheese",
              description="tofucheese",
              price=30,
              quantity=20)
    # lets verify the count
    if len(ITEMS) == 2:
        print("it is working correctly")
def test_update_products():
     if len(ITEMS) == 1:              
        print("precondition is working")  
     update_items(item_id= "t001",
                  item_name="Tajmahaltea",
                  description="Tajmahaltea",
                  price=110,
                  quantity=22)
     update_items(item_id="t002",
                  item_name="Tofucheese",
                  description="Tofucheese",
                  price=60,
                  quantity=25)
     update_items(item_id="c001",
                  item_name="cintholSoap",
                  description="cintholSoap",
                  price=75,
                  quantity=30)
     update_items(item_id="Th-002",
                  item_name="Threerosestea",
                  description="Threerosestea",
                  price=120,
                  quantity=35)
def test_delete_products():
    if len(ITEMS) == 3:
        print("precondition is working")
    delete_item(item_id="t001")
    if len(ITEMS) == 2:
        print("delete items work correctly") 
    delete_item(item_id="t002")   
def test_search_item_by_name()->None:  
    #### Empty the list and start fresh with no item
    ITEMS.clear()
    ### Add the four items to the list.
    ITEMS.append({"name": "Appleiphone14", "price": 999})
    ITEMS.append({"name": "Samsunggalaxy","price": 555})
    ITEMS.append({"name": "AppleMacbookpro","price": 1000})
    ITEMS.append({"name": "PocoSmartPhones","price": 2000})
    results = search_item_by_name("Appleiphone14")
    print("Results", results)
    print("Type:", type(results))
    assert results == [{"name": "Appleiphone14", "price": 999}]
    ### Search for Samsung galaxy product and checks if found correctly
    results = search_item_by_name("Samsunggalaxy")
    print("Results",results)
    assert results == [{"name":"Samsunggalaxy","price": 555}]
    ### Search the item PocoSmartPhones and checks if found correctly
    results = search_item_by_name("PocoSmartPhones")
    print("Results",results)
    print("Type:",type(results))
    assert results == [{"name":"PocoSmartPhones","price": 2000}]
    print("All tests passed! ")           
if __name__ == "__main__":
# lets try adding products
    test_add_products()
    test_update_products()
    test_delete_products()
    test_search_item_by_name()
