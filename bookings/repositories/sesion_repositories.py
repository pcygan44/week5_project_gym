from db.run_sql import run_sql
from models.sesion import Sesion
from models.booking import Booking
from models.member import Member

def create_sesion (sesion):
    sql = "INSERT INTO sesions (sesion_name, duration, sesion_date, sesion_time, capacity, active_status) VALUES (%s,%s,%s,%s,%s,%s) RETURNING id"
    values = [sesion.sesion_name, sesion.duration, sesion.sesion_date, sesion.sesion_time,sesion.capacity , sesion.active_status]
    results = run_sql(sql , values)
    # print(" IAAM RESULT =============",results)
    sesion.id = results[0]['id']
    return sesion 

    