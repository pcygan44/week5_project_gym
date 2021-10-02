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

def select_all():
    sesions = []
    sql = "SELECT * FROM sesions"
    results =run_sql(sql)
    for row in results:
        sesion = Sesion(row['sesion_name'], row['duration'], row['sesion_date'], row['sesion_time'], row['capacity'], row['active_status'],row['id'])
        sesions.append(sesion)
    return sesions

def select(id):
    sesion = None
    sql= "SELECT * FROM sesions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        sesion = Sesion (result['sesion_name'],result['duration'],result['sesion_date'],result['sesion_time'],result['capacity'],result['active_status'],result['id'])
    return sesion

def delete_all():
    sql = "DELETE FROM sesions"
    run_sql(sql)

def member(sesion):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = member.id WHERE sesion_id = %s"
    values = [sesion.id]

    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'],row['last_name'],row['membership'],row['active_status'],row['id'])
        members.append(member)
    return members