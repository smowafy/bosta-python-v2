from typing import Optional

class Receiver:
    def __init__(
            self, firstName: str, lastName: str, email: str,
            phone: str, secondPhone: Optional[str] = None
    ):
        """ Initialize new instance from Receiver class

        Parameters:
        firstName (str)
        lastName (str)
        email (str)
        phone (str)
        secondPhone (str) [optional]

        Returns: New instance from Receiver class
        """
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.secondPhone = secondPhone

    def get_firstName(self):
        return self.firstName

    def get_lastName(self):
        return self.lastName

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_secondPhone(self):
        return self.secondPhone

    def toJSON(self):
        """
        Returns:
        JSON object from current instance

        """
        receiverObj = {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "phone": self.phone
        }

        if self.secondPhone is not None:
            receiverObj["secondPhone"] = self.secondPhone

        return receiverObj


if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
