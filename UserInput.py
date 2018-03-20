import re
from _datetime import *


class UserInput:
    """Patientregistry input by the user"""
    #todo:not just alldata but all kind of data, not just creating it but modifying
    #todo:complete regex phonenumber and appointmentdate

    def safe_cast(self,val,to_type, default=None):
        try:
            return to_type(val)
        except (ValueError, TypeError):
            return default

    def adding_alldata(self):
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
            is_match = re.fullmatch(r"^[A-Z]{1}[a-z]{0,}[.]([ ][A-Z]{1}[a-z]{0,}[-][A-Z]{1}[a-z]{0,}|[ ][A-Z]{1}[a-z]{0,}[ ][A-Z]{1}[a-z]{0,}|[ ][A-Z]{1}[a-z]{0,})?|([A-Z]{1}[a-z]{0,}[-][A-Z]{1}[a-z]{0,}|[A-Z]{1}[a-z]{0,}[ ][A-Z][a-z]{0,}|[A-Z]{1}[a-z]{0,})$", self.LastName)
            if is_match is None:
                print("Please provide the first name in correct format (eg.:'John' or 'J.' or 'Smith Black')")

        is_in_range = False
        while is_in_range == False:
            self.Age=input("Age:")
            self.Age=UserInput.safe_cast(self,self.Age,int)
            if self.Age is None:
                print("Not a number or not in the correct format. Please give a number between 0 and 150.")
            else:
                if(self.Age>=0 and self.Age<=150):
                    is_in_range = True
                else:
                    print("Not a number or not in the correct format. Please give a number between 0 and 150.")

        is_match = None
        while is_match is None:
            self.Phonenumber=input("Phone number(correct format: +36-00-000-0000):")
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
            self.AppointmentTime=input("Appointment time (correct format: 00:00):")
            is_match = re.fullmatch(r"^[0-9]{2}[:][0-9]{2}$", self.AppointmentTime)
            if is_match is None:
                print("Please provide a correct time format (08:00).")

