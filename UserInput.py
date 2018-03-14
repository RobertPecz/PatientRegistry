import re

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
        isMatch=None
        while (isMatch == None):
            self.FirstName=input("First name:")
            isMatch = re.fullmatch(r"^[A-Z]{1}[a-z]{0,}[? ]{0,}([A-Z]{1}[a-z]{0,}|[^ ])$", self.FirstName)
            if isMatch == None:
                print("Please provide the first name in correct format (eg.:'Smith' or 'Smith-Black' or 'Smith Black')")

        isMatch=None
        while (isMatch == None):
            self.LastName=input("Last Name:")
            isMatch = re.fullmatch(r"^[A-Z]{1}[a-z]{0,}[?.]{0,1}([ ][A-Z]{1}[a-z]{0,}[.]|[ ][A-Z]{1}[a-z]{0,})|([ ][A-Z]{1}[a-z]{0,}|[-][A-Z]{1}[a-z]{0,}|[A-Z]{1}[a-z]{0,}[^ ])$", self.LastName)
            if isMatch == None:
                print("Please provide the first name in correct format (eg.:'John' or 'J.' or 'Smith Black')")

        isInRange=False
        while isInRange == False:
            self.Age=input("Age:")
            self.Age=UserInput.safe_cast(self,self.Age,int)
            if self.Age == None:
                print("Not a number or not in the correct format. Please give a number between 0 and 150.")
            else:
                if(self.Age>=0 and self.Age<=150):
                    isInRange=True
                else:
                    print("Not a number or not in the correct format. Please give a number between 0 and 150.")

        #self.PhoneNumber=input("Phone number:")
        #self.AppointmentDate=input("Appointment date:")