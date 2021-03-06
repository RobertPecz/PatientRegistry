import re
from datetime import *


class UserInput:
    """Patient registry input by the user"""

    def __init__(self):
        self.FirstName = None
        self.LastName = None
        self.Dob = None
        self.Phone_number = None
        self.AppointmentDate = None
        self.AppointmentTime = None
        self.MotherMaidenName = None

    def safe_cast(self,val,to_type, default=None):
        try:
            return to_type(val)
        except (ValueError, TypeError):
            return default

    def adding_new_patient(self):
        # Adding a new customer

        # Adding the first name
        print("Please provide the following data's: First name, Last name, Age, Phone number, Appointment date")
        is_match = None
        while is_match is None:
            self.FirstName=input("First name:")
            is_match = re.fullmatch(r"^([A-Z][a-z]{0,})?(?(1)([ ][A-Z][a-z]{0,}|[ ][A-Z][a-z]{0,}[ ][A-Z][a-z]{0,}|[ ][A-Z][.]|[.][ ][A-Z][a-z]{0,}|)|NOTVALID)$", self.FirstName)
            if is_match is None:
                print("Please provide the first name in correct format (eg.:'Smith' or 'Smith-Black' or 'Smith Black')")

        # Adding the last name
        is_match = None
        while is_match is None:
            self.LastName=input("Last Name:")
            is_match = re.fullmatch(r"^([A-Z][a-z]{0,})?(?(1)([.][ ][A-Z][a-z]{0,}[.][ ][A-Z][a-z]{0,}|[.][ ][A-Z][a-z]{0,}[.][ ][A-Z][a-z]{0,}[-][A-Z][a-z]{0,}|[.][ ][A-Z][a-z]{0,}[.]|[.][ ][A-Z][a-z]{0,}[-][A-Z][a-z]{0,}|[.][ ][A-Z][a-z]{0,}|[-][A-Z][a-z]{0,})|[A-Z][a-z]{0,})$", self.LastName)
            if is_match is None:
                print("Please provide the first name in correct format (eg.:'John' or 'J.' or 'Smith Black')")

        # Adding the Date of birth
        is_match = None
        while is_match is None:
            self.Dob = input("Date of Birth (correct format: 1900-01-01):")
            is_match = re.fullmatch(r"^[1-2][0-9]{3}[-][0-1][0-9]{1}[-][0-9]{2}$", self.Dob)
            try:
                dob_date = datetime.strptime(self.Dob, '%Y-%m-%d')
            except ValueError:
                print("Please provide a valid date between 01-01 and 12-31.")
                continue
            if dob_date < datetime(year=1900, month=1, day=1) or dob_date >= datetime.now():
                is_match = None
                print("Please provide the date at least today")
            if is_match is None:
                print("Please provide a correct date format (1900-01-01).")

        # Adding the mother maiden name
        is_match = None
        while is_match is None:
            self.MotherMaidenName = input("Mother Maiden name (correct format: Sue Doe or Sue Doe-Black or Sue Doe Black or Sue D. Black.):")
            is_match = re.fullmatch(r"^([A-Z][a-z]{0,})?(?(1)([ ][A-Z][a-z]{0,}|[ ][A-Z][a-z]{0,}[-][A-Z][a-z]{0,}|[ ][A-Z][a-z]{0,}[ ][A-Z][a-z]{0,}|[ ][A-Z][.][ ][A-Z][a-z]{0,}|[ ][A-Z][a-z]{0,}[ ][A-Z][.])|NOTVALID)$", self.MotherMaidenName)
            if is_match is None:
                print("Please provide the mother maiden name in a correct form eg.: Sue Doe or Sue Doe-Black or Sue Doe Black or Sue D. Black")

        # Adding the phone number
        is_match = None
        while is_match is None:
            self.Phone_number = input("Phone number(correct format: +36-00-000-0000):")
            is_match = re.fullmatch(r"^[+][3][6][-][0-9]{2}[-][0-9]{3}[-][0-9]{4}$", self.Phone_number)
            if is_match is None:
                print("Please provide a correct phone number format (+36-00-000-0000).")

        # Adding the appointment date and time
        is_match = None
        while is_match is None:
            self.AppointmentDate = input("Appointment Date (correct format: 1900-01-01):")
            is_match = re.fullmatch(r"^[2][0-9]{3}[-][0-1][0-9]{1}[-][0-9]{2}$", self.AppointmentDate)
            try:
                self.AppointmentDate = datetime.strptime(self.AppointmentDate, '%Y-%m-%d')
            except ValueError:
                print("Please provide a valid date between 01-01 and 12-31.")
                continue
            if self.AppointmentDate < datetime.now() - timedelta(days=1):
                is_match = None
                print("Please provide the date at least today")
            if is_match is None:
                print("Please provide a correct date format (1900-01-01).")

            self.AppointmentTime = input("Appointment time (correct format: 00:00):")
            is_match = re.fullmatch(r"^[0-9]{2}[:][0-9]{2}$", self.AppointmentTime)
            start_time = time(hour=8, minute=0)
            end_time = time(hour=16, minute=0)
            try:
                self.AppointmentTime = datetime.strptime(self.AppointmentTime, '%H:%M').time()
                self.AppointmentDate = datetime.combine(self.AppointmentDate, self.AppointmentTime)
            except ValueError:
                print("Please provide a valid time between 08:00 and 16:00")
                is_match = None
                continue
            if self.AppointmentTime < start_time or self.AppointmentTime > end_time:
                is_match = None
                print("Please provide a valid time between 08:00 and 16:00")
            if is_match is None:
                print("Please provide a correct time format (08:00).")

    def change_first_name(self):
        # Changing the first name
        print("Please provide first name.")
        is_match = None
        while is_match is None:
            self.FirstName = input("First name:")
            is_match = re.fullmatch(r"^([A-Z][a-z]{0,})?(?(1)([ ][A-Z][a-z]{0,}|[ ][A-Z][a-z]{0,}[ ][A-Z][a-z]{0,}|[ ][A-Z][.]|[.][ ][A-Z][a-z]{0,}|)|NOTVALID)$", self.FirstName)
            if is_match is None:
                print("Please provide the first name in correct format (eg.:'Smith' or 'Smith-Black' or 'Smith Black')")

        return self.FirstName

    def change_last_name(self):
        # Changing the last name
        print("Please provide last name.")
        is_match = None
        while is_match is None:
            self.LastName = input("Last Name:")
            is_match = re.fullmatch(r"^([A-Z][a-z]{0,})?(?(1)([.][ ][A-Z][a-z]{0,}[.][ ][A-Z][a-z]{0,}|[.][ ][A-Z][a-z]{0,}[.][ ][A-Z][a-z]{0,}[-][A-Z][a-z]{0,}|[.][ ][A-Z][a-z]{0,}[.]|[.][ ][A-Z][a-z]{0,}[-][A-Z][a-z]{0,}|[.][ ][A-Z][a-z]{0,}|[-][A-Z][a-z]{0,})|[A-Z][a-z]{0,})$", self.LastName)
            if is_match is None:
                print("Please provide the first name in correct format (eg.:'John' or 'J.' or 'Smith Black')")

        return self.LastName

    def change_dob(self):
        # Changing the Date of birth
        print("Provide the date of birth.")
        is_match = None
        while is_match is None:
            self.Dob = input("Date of Birth (correct format: 1900-01-01):")
            is_match = re.fullmatch(r"^[1-2][0-9]{3}[-][0-1][0-9]{1}[-][0-9]{2}$", self.Dob)
            try:
                dob_date = datetime.strptime(self.Dob, '%Y-%m-%d')
            except ValueError:
                print("Please provide a valid date between 01-01 and 12-31.")
                continue
            if dob_date < datetime(year=1900,month=1,day=1) or dob_date >= datetime.now():
                is_match = None
                print("Please provide the date at least today")
            if is_match is None:
                print("Please provide a correct date format (1900-01-01).")

        return self.Dob

    def change_mother_maiden_name(self):
        # Changing mother maiden name.
        print("Provide mother maiden name.")
        is_match = None
        while is_match is None:
            self.MotherMaidenName = input("Mother Maiden name (correct format: Sue Doe or Sue Doe-Black or Sue Doe Black or Sue D. Black.):")
            is_match = re.fullmatch(r"^([A-Z][a-z]{0,})?(?(1)([ ][A-Z][a-z]{0,}|[ ][A-Z][a-z]{0,}[-][A-Z][a-z]{0,}|[ ][A-Z][a-z]{0,}[ ][A-Z][a-z]{0,}|[ ][A-Z][.][ ][A-Z][a-z]{0,}|[ ][A-Z][a-z]{0,}[ ][A-Z][.])|NOTVALID)$", self.MotherMaidenName)
            if is_match is None:
                print("Please provide the mother maiden name in a correct form eg.: Sue Doe or Sue Doe-Black or Sue Doe Black or Sue D. Black")

        return self.MotherMaidenName

    def change_phonenumber(self):
        # Changing phone number.
        print("Provide phone number.")
        is_match = None
        while is_match is None:
            self.Phone_number = input("Phone number(correct format: +36-00-000-0000):")
            is_match = re.fullmatch(r"^[+][3][6][-][0-9]{2}[-][0-9]{3}[-][0-9]{4}$", self.Phone_number)
            if is_match is None:
                print("Please provide a correct phone number format (+36-00-000-0000).")

        return self.Phone_number

    def change_appointment_date(self):
        # Change appointment date and time
        is_match = None
        while is_match is None:
            self.AppointmentDate = input("Appointment Date (correct format: 1900-01-01):")
            is_match = re.fullmatch(r"^[2][0-9]{3}[-][0-1][0-9]{1}[-][0-9]{2}$", self.AppointmentDate)
            try:
                self.AppointmentDate = datetime.strptime(self.AppointmentDate, '%Y-%m-%d')
            except ValueError:
                print("Please provide a valid date between 01-01 and 12-31.")
                continue
            if self.AppointmentDate < datetime.now() - timedelta(days=1):
                is_match = None
                print("Please provide the date at least today")
            if is_match is None:
                print("Please provide a correct date format (1900-01-01).")

            self.AppointmentTime = input("Appointment time (correct format: 00:00):")
            is_match = re.fullmatch(r"^[0-9]{2}[:][0-9]{2}$", self.AppointmentTime)
            start_time = time(hour=8, minute=0)
            end_time = time(hour=16, minute=0)
            try:
                self.AppointmentTime = datetime.strptime(self.AppointmentTime, '%H:%M').time()
                self.AppointmentDate = datetime.combine(self.AppointmentDate, self.AppointmentTime)
            except ValueError:
                print("Please provide a valid time between 08:00 and 16:00")
                is_match = None
                continue
            if self.AppointmentTime < start_time or self.AppointmentTime > end_time:
                is_match = None
                print("Please provide a valid time between 08:00 and 16:00")
            if is_match is None:
                print("Please provide a correct time format (08:00).")

        return self.AppointmentDate
