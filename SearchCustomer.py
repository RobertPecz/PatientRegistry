from DatabaseConnection import *
from UserInput import *


class SearchingCustomer:

    def __init__(self):
        self.firstName = None
        self.lastName = None
        self.dateOfBirth = None
        self.motherMaidenName = None
        self.phoneNumber = None
        self.appointmentDate = None
        self.pastAppDate = None

    def upload_for_searching(self, first_name, last_name, date_of_birth, mother_maiden_name, phone_number=None, appointment_date=None):
        self.firstName = first_name
        self.lastName = last_name
        self.dateOfBirth = date_of_birth
        self.motherMaidenName = mother_maiden_name
        self.phoneNumber = phone_number
        self.appointmentDate = appointment_date
        self.pastAppDate = appointment_date

    def search_customer(self):
        # Searching customer by first name + last name + mother maiden name + dob return PK ID
        # Connect to the database
        cnxn, cursor = ConnectingToDatabase.connect_database(self)

        # Searching the patient giving back patient not found if there are no records in the table
        userin = UserInput()
        userin.change_first_name()
        userin.change_last_name()
        userin.change_dob()
        userin.change_mother_maiden_name()
        self.upload_for_searching(userin.FirstName,
                                  userin.LastName,
                                  userin.Dob,
                                  userin.MotherMaidenName)

        # Querying the result in the patient table
        query_search = "SELECT ID FROM Patient WHERE FirstName=? and LastName=? and DateOfBirth=? and MotherMaidenName=?;"
        cursor.execute(query_search, self.firstName, self.lastName, self.dateOfBirth, self.motherMaidenName)
        row = cursor.fetchone()
        try:
            id_current_query = row[0]
            return id_current_query
        except:
            return None

    def search_customer_duplicate_checker(self):
        # Check the new customer if it's already in the table, preventing from upload

        # Connect to the database
        cnxn, cursor = ConnectingToDatabase.connect_database(self)

        userin = UserInput()
        userin.adding_new_patient()
        self.upload_for_searching(userin.FirstName,
                                  userin.LastName,
                                  userin.Dob,
                                  userin.MotherMaidenName,
                                  userin.Phone_number,
                                  userin.AppointmentDate,
                                  )
        # Querying the result in the patient table
        query_search = "SELECT ID FROM Patient WHERE FirstName=? and LastName=? and DateOfBirth=? and MotherMaidenName=?;"
        cursor.execute(query_search, self.firstName, self.lastName, self.dateOfBirth, self.motherMaidenName)
        row = cursor.fetchone()
        try:
            id_current_query = row[0]
            return id_current_query
        except:
            return None
