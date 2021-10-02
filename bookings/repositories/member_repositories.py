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
    