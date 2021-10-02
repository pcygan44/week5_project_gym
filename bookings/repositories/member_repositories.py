from db.run_sql import run_sql
from models.member import Member
from models.sesion import Sesion
from models.booking import Booking


def create_member(member):
    sql = "INSERT INTO members (first_name, last_name , membership , active_status) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [member.first_name , member.last_name, member.membership, member.active_status]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member
    
def select_all():
    members = []

    sql= "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'],row['membership'], row['active_status'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None 
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member (result['first_name'],result['last_name'],result['membership'],result['active_status'], result['id'])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def sesions(member):
    sesions = []
    sql = "SELECT sesions.* FROM sesions INNER JOIN bookings ON bookings.sesion_id = sesion.id WHERE member_id = %s"
    values = [member.id]

    results = run_sql(sql, values)

    for row in results:
        sesion = Sesion( row['sesion_name'],row['duration'],row['sesion_date'],row['sesion_time'],row['capacity'],row['active_status'],row['id'])
        sesions.append(sesion)
    return sesions

def update(member):
    sql = "UPDATE members SET(first_name, last_name, membership, active_status) = (%s,%s,%s,%s) WHERE id - %s"
    values = [member.first_name, member.last_name, member.membership, member.active_status, member.id]
    run_sql(sql, values)