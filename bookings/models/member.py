class Member:

    def __init__ (self, first_name, last_name, membership, active_status, id = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.membership = membership
        self.active_status = active_status