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

    def safe_cast(self,val,to_type, default=None):
        try:
            return to_type(val)
        except (ValueError, TypeError):
            return default

    def adding_new_patient(self):
        # Adding a new customer
        print("Please provide the following data's: First name, Last name, Age, Phone number, Appointment date")
        is_match = None
        while is_match is None:
            self.FirstName=input("First name:")
            is_match = re.fullmatch(r"^[A-Z]{1}[a-z]{0,}[? ]{0,}([A-Z]{1}[a-z]{0,}|[^ ])$", self.FirstName)
            if is_match is None:
                print("Please provide the first name in correct format (eg.:'Smith' or 'Smith-Black' or 'Smith Black')")

        is_match = None
        while is_match is None:
            self.LastName=input("Last Name:")
            is_match = re.fullmatch(r"^([A-Z][a-z]{0,})?(?(1)([.][ ][A-Z][a-z]{0,}[.][ ][A-Z][a-z]{0,}|[.][ ][A-Z][a-z]{0,}[.][ ][A-Z][a-z]{0,}[-][A-Z][a-z]{0,}|[.][ ][A-Z][a-z]{0,}[.]|[.][ ][A-Z][a-z]{0,}[-][A-Z][a-z]{0,}|[.][ ][A-Z][a-z]{0,}|[-][A-Z][a-z]{0,})|[A-Z][a-z]{0,})$", self.LastName)
            if is_match is None:
                print("Please provide the first name in correct format (eg.:'John' or 'J.' or 'Smith Black')")

        is_match = None
        while is_match is None:
            self.Dob = input("Date of Birth (correct format: 1900-01-01):")
            is_match = re.fullmatch(r"^[1-2][0-9]{3}[-][0-1][0-9]{1}[-][0-9]{2}$", self.Dob)
            try:
                dob_date = datetime.strptime(self.AppointmentDate, '%Y-%m-%d')
            except ValueError:
                print("Please provide a valid date between 01-01 and 12-31.")
                continue
            if dob_date < datetime(year=1900, month=1, day=1) or dob_date >= datetime.now():
                is_match = None
                print("Please provide the date at least today")
            if is_match is None:
                print("Please provide a correct date format (1900-01-01).")

        is_match = None
        while is_match is None:
            self.Phone_number = input("Phone number(correct format: +36-00-000-0000):")
            is_match = re.fullmatch(r"^[+][3][6][-][0-9]{2}[-][0-9]{3}[-][0-9]{4}$", self.Phonenumber)
            if is_match is None:
                print("Please provide a correct phone number format (+36-00-000-0000).")

        is_match = None
        while is_match is None :
            self.AppointmentDate = input("Appointment Date (correct format: 1900-01-01):")
            is_match = re.fullmatch(r"^[2][0-9]{3}[-][0-1][0-9]{1}[-][0-9]{2}$", self.AppointmentDate)
            try:
                appointment_date = datetime.strptime(self.AppointmentDate,'%Y-%m-%d')
            except ValueError:
                print("Please provide a valid date between 01-01 and 12-31.")
                continue
            if appointment_date < datetime.now() - timedelta(days=1):
                is_match = None
                print("Please provide the date at least today")
            if is_match is None:
                print("Please provide a correct date format (1900-01-01).")

        is_match=None
        while is_match is None :
            self.AppointmentTime = input("Appointment time (correct format: 00:00):")
            is_match = re.fullmatch(r"^[0-9]{2}[:][0-9]{2}$", self.AppointmentTime)
            start_time = datetime.strptime('08:00','%H:%M')
            end_time = datetime.strptime('16:00','%H:%M')
            try:
                appointment_time = datetime.strptime(self.AppointmentTime,'%H:%M')
            except ValueError:
                print("Please provide a valid time between 08:00 and 16:00")
                is_match = None
                continue
            if appointment_time < start_time or appointment_time > end_time:
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
            is_match = re.fullmatch(r"^[A-Z]{1}[a-z]{0,}[? ]{0,}([A-Z]{1}[a-z]{0,}|[^ ])$", self.FirstName)
            if is_match is None:
                print("Please provide the first name in correct format (eg.:'Smith' or 'Smith-Black' or 'Smith Black')")

    def change_last_name(self):
        # Changing the last name
        print("Please provide last name.")
        is_match = None
        while is_match is None:
            self.LastName = input("Last Name:")
            is_match = re.fullmatch(
                r"^([A-Z][a-z]{0,})?(?(1)([.][ ][A-Z][a-z]{0,}[.][ ][A-Z][a-z]{0,}|[.][ ][A-Z][a-z]{0,}[.][ ][A-Z][a-z]{0,}[-][A-Z][a-z]{0,}|[.][ ][A-Z][a-z]{0,}[.]|[.][ ][A-Z][a-z]{0,}[-][A-Z][a-z]{0,}|[.][ ][A-Z][a-z]{0,}|[-][A-Z][a-z]{0,})|[A-Z][a-z]{0,})$",
                self.LastName)
            if is_match is None:
                print("Please provide the first name in correct format (eg.:'John' or 'J.' or 'Smith Black')")

    def change_dob(self):
        # Changing the Date of birth
        print("Provide the date of birth.")
        is_match = None
        while is_match is None:
            self.Dob = input("Date of Birth (correct format: 1900-01-01):")
            is_match = re.fullmatch(r"^[1-2][0-9]{3}[-][0-1][0-9]{1}[-][0-9]{2}$", self.Dob)
            try:
                dob_date = datetime.strptime(self.AppointmentDate, '%Y-%m-%d')
            except ValueError:
                print("Please provide a valid date between 01-01 and 12-31.")
                continue
            if dob_date < datetime(year=1900,month=1,day=1) or dob_date >= datetime.now():
                is_match = None
                print("Please provide the date at least today")
            if is_match is None:
                print("Please provide a correct date format (1900-01-01).")

    def change_appointment_date(self):
        # Change appointment date
        print("Provide appointment date.")
        is_match = None
        while is_match is None:
            self.Phonenumber = input("Phone number(correct format: +36-00-000-0000):")
            is_match = re.fullmatch(r"^[+][3][6][-][0-9]{2}[-][0-9]{3}[-][0-9]{4}$", self.Phonenumber)
            if is_match is None:
                print("Please provide a correct phone number format (+36-00-000-0000).")

    def change_appointment_time(self):
        # Change appointment time
        print("Provide appointment time")
        is_match = None
        while is_match is None:
            self.AppointmentTime = input("Appointment time (correct format: 00:00):")
            is_match = re.fullmatch(r"^[0-9]{2}[:][0-9]{2}$", self.AppointmentTime)
            start_time = datetime.strptime('08:00', '%H:%M')
            end_time = datetime.strptime('16:00', '%H:%M')
            try:
                appointment_time = datetime.strptime(self.AppointmentTime, '%H:%M')
            except ValueError:
                print("Please provide a valid time between 08:00 and 16:00")
                is_match = None
                continue
            if appointment_time < start_time or appointment_time > end_time:
                is_match = None
                print("Please provide a valid time between 08:00 and 16:00")
            if is_match is None:
                print("Please provide a correct time format (08:00).")