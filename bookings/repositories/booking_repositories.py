from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
from models.sesion import Sesion

import repositories.booking_repositories as booking_repositories
import repositories.member_repositories as member_repositories
import repositories.sesion_repositories as sesion_repositories 

def create_booking(booking):
    sql = "INSERT INTO bookings(members_id ,sesions_id ) VALUES (%s,%s) RETURNING id"
    values = [booking.member, booking.sesion]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking

