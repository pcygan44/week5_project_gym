import pdb
from models.member import Member
from models.booking import Booking
from models.sesion import Sesion

import repositories.member_repositories as member_repositories
import repositories.sesion_repositories as sesion_repositories

member1 = Member('Jim','Black',True, True)
member_repositories.create_member(member1)

member2 = Member('Tom','Green',True, True)
member_repositories.create_member(member2)

sesion1 = Sesion('swimming',30,'01/10/2022' ,"11:00", 4 ,True)
sesion_repositories.create_sesion(sesion1)