from db.run_sql import run_sql
from models.booking import Booking
import repositories.member_repositories as member_repositories 
import repositories.sesion_repositories as sesion_repositories

def create_bookings(booking):
    sql = "INSERT INTO bookings( members_id , sesions_id) VALUES (%s, %s) RETURNING id "
    values = [booking.member.id, booking.sesion.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking