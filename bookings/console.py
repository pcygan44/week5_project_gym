import pdb
from models.member import Member
from models.booking import Booking
from models.sesion import Sesion

import repositories.member_repositories as member_repositories
import repositories.sesion_repositories as sesion_repositories
import repositories.booking_repositories as booking_repositories

member_repositories.delete_all()
sesion_repositories.delete_all()


member1 = Member('Jim','Black',True, True)
member_repositories.create_member(member1)

member2 = Member('Tom','Green',True, True)
member_repositories.create_member(member2)

member3 = Member('Jack', 'Orange', True, True)

sesion1 = Sesion('swimming',30,'01/10/2022' ,"11:00", 4 ,True)
sesion_repositories.create_sesion(sesion1)

sesion2 = Sesion('Spining', 45,'10/10/2022',"12:00", 1, True)
sesion_repositories.create_sesion(sesion2)

booking1 = Booking(member2, sesion2)
booking_repositories.create_bookings(booking1)

# print(sesion_repositories.select_all())

# resoult = member_repositories.select()
# print(resoult.last_name)



# pdb.set_trace()
