class UserInput:
    """Patientregistry input by the user"""
    #todo:not just alldata but all kind of data, not just creating it but modifying
    def adding_alldata(self):
        print("Please provide the following data's: First name, Last name, Age, Phone number, Appointment date")
        self.FirstName=input("First name:")
        self.LastName=input("Last name:")
        self.Age=input("Age:")
        self.PhoneNumber=input("Phone number:")
        self.AppointmentDate=input("Appointment date:")