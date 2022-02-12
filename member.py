class Member:
    def __init__(self, pid: int, firstname: str, lastname: str, email: str, role: str, department: str ):
        self.pid = pid
        self.firstname = firstname.lower().title()
        self.lastname = lastname.lower().title()
        self.email = email
        self.role = role
        self.department = department

    def display_info(self):
        print("ID: " + str(self.pid))
        print("Name: " + self.firstname + " " + self.lastname)
        print("Email: " + self.email)
        print("Role: " + self.role)
        print("Department: " + self.department)

    def update(self, to_update: str, data: str):


