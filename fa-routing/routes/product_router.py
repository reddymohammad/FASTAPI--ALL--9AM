from fastapi import APIRouter
router=APIRouter(prefix="/product")

'''
Rest API - End Point: 3
--------------------------
Usage: create new product
Rest API URL: http://127.0.0.1:8000/product/create
Method Type:POST
Requried Fields : pid,pname,price
Access Type:Public 

'''

@router.post("/create")
def create_product():
    return {'msg':'New Product created'}

@router.put("/update")
def update_product():
    return {'msg':' product update successfully'}

@router.delete("/delete")
def delete_product():
    return {'msg':'product delete successfully'}
