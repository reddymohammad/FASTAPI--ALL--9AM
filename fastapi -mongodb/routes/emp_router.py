from fastapi import APIRouter,HTTPException
from models.employee import Employee as EmployeeModel
from pymongo import MongoClient
router=APIRouter(prefix='/emp')

#Establish Database connection and get the collection object
client=MongoClient('mongodb://localhost:27017/')
db=client['db11']
emp_col=db['employees']




""" 
usage: create new employee
Rest API URL: http://127.0.0.1:8000/emp/create
Method Type:POST
Required Fields:eid,ename,esal,gender
Access Type:Public 
"""

@router.post("/create")
def create_employee(emp:EmployeeModel):
    emp_col.insert_one(emp.dict())
    return {'msg':'Employee Object inserted successfully'}

"""
usage: fetch all employees
Rest API URL: http://127.0.0.1:8000/emp/read
Method Type:GET
Required Fields:None
Access Type:Public
"""

@router.get("/read")
def get_employee():
    return list(emp_col.find({},{'_id':0}))



"""
usage: fetch employee by eid
Rest API URL: http://127.0.0.1:8000/emp/read/101
Method Type:GET
Required Fields:None
Access Type:Public
"""

@router.get("/read/{eid}")
def get_employee(eid:int):
    employee=emp_col.find_one({"eid":eid},{"_id":0})
    if not employee:
       raise HTTPException(status_code=404,detail="employee not found")
    return employee






"""
usage: delete employee by eid
Rest API URL: http://127.0.0.1:8000/emp/delete/101
Method Type:DELETE
Required Fields:None
Access Type:Public
"""

@router.delete("/delete/{eid}")
def delete_employee(eid:int):
    emp_col.delete_one({'eid':eid})
    return {'msg':'employee deleted successfully'}



"""
usage: update employee by eid
Rest API URL: http://127.0.0.1:8000/emp/update/101
Method Type:PUT
Required Fields:eid,ename,esal,gender
Access Type:Public
"""


@router.put("/udpate/{eid}")
def update_employee(eid:int,emp:EmployeeModel):
    emp_col.update_one({'eid':eid},{'$set':emp.dict()})
    return {"msg":"update successfully"}