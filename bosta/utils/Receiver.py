class Receiver:
    def __init__(self, firstName, lastName, email, phone):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone

    def get_firstName(self, firstName):
        return self.firstName

    def get_lastName(self, lastName):
        return self.lastName

    def get_email(self, email):
        return self.email

    def get_phone(self, phone):
        return self.phone

    def toJson(self):
        return {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "phone": self.phone
        }


if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
