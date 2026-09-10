from fastapi import APIRouter
from models.employee import Employee
from databases.database import get_db_connection

router = APIRouter(prefix="/emp")


@router.post("/create")
def create_employee(emp: Employee):

    dbcon = get_db_connection()
    cursor = dbcon.cursor()

    sql_st = """
        INSERT INTO employee(eid, ename, esal, gender)
        VALUES (%s, %s, %s, %s)
    """

    values = (
        emp.eid,
        emp.ename,
        emp.esal,
        emp.gender
    )

    cursor.execute(sql_st, values)
    dbcon.commit()

    cursor.close()
    dbcon.close()

    return {
        "msg": "employee created successfully"
    }


@router.get("/read")
def get_Employees():
     dbcon=get_db_connection()
     cursor=dbcon.cursor(dictionary=True)
     sql_st=''' select *from employee '''
     cursor.execute(sql_st)
     employees=cursor.fetchall()

     return employees


     






