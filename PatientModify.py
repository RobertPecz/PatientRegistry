import pyodbc
from UserInput import *

class PatientModding:
    """Modifying a Patient include add, modify appoint date, delete appointment"""

    def __init__(self):
        self.firstName = None
        self.lastName = None
        self.dateOfBirth = None
        self.phoneNumber = None
        self.motherMaidenName = None
        self.appointmentDate = None
        self.pastAppDate = None
        self.pastIsAppear = None

    # Adding data to the class
    def upload_all_data(self,first_name, last_name, date_of_birth, mother_maidenname, phone_number, appointment_date, past_app_date, past_is_appear):
        self.firstName = first_name
        self.lastName = last_name
        self.dateOfBirth = date_of_birth
        self.motherMaidenName = mother_maidenname
        self.phoneNumber = phone_number
        self.appointmentDate = appointment_date
        self.pastAppDate = past_app_date
        self.pastIsAppear = past_is_appear

    #def upload_for_searching(self, firstName):

    def connect_database(self):
        # Connect to the database
        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=.\SQLEXPRESS;"
                              "Database=PatientRegistry;"
                              "Trusted_Connection=yes;")

        cursor = cnxn.cursor()
        return cnxn,cursor

    def adding_Customer(self):
        # Upload a customer to the tables

        # Get the new patient necessary data from UserInput
        userin = UserInput()
        userin.adding_new_patient()
        self.upload_all_data(userin.FirstName,
                        userin.LastName,
                        userin.Dob,
                        userin.MotherMaidenName,
                        userin.Phone_number,
                        userin.AppointmentDate,
                        userin.AppointmentDate,
                        "No")

        # Connect to the database
        cnxn,cursor = self.connect_database()

        # Select the last PK ID from Patient table and +1 to it.
        id_last_number_query_patient = "SELECT TOP 1 ID FROM Patient ORDER BY ID Desc;"
        cursor.execute(id_last_number_query_patient)
        row = cursor.fetchone()
        id_Number_patient = row[0]+1

        # Select the last PK ID from PastAppointments table and +1 to is
        id_last_number_query_patient = "SELECT TOP 1 ID FROM PastAppointments ORDER BY ID Desc;"
        cursor.execute(id_last_number_query_patient)
        row = cursor.fetchone()
        id_Number_pastappointments = row[0]+1

        # Insert Patient data's into the Patient table
        query_Insert = "INSERT INTO Patient(ID, FirstName, LastName, DateOfBirth, MotherMaidenName, PhoneNumber, AppointmentDate) VALUES(?,?,?,?,?,?,?);"
        cursor.execute(query_Insert, id_Number_patient, self.firstName, self.lastName, self.dateOfBirth, self.motherMaidenName, self.phoneNumber, self.appointmentDate)
        cnxn.commit()

        # Select PK ID Where the firstname and lastname which is passed as variable
        id_current_query = "SELECT ID FROM Patient WHERE FirstName=? and LastName=?;"
        cursor.execute(id_current_query, self.firstName, self.lastName)
        row = cursor.fetchone()
        id_current_query = row[0]

        # Insert the past appointments to the PastAppointments table set the Isappear column default to No.
        query_Insert = "INSERT INTO PastAppointments(ID, PatientID, PastAppTime, IsAppear) VALUES(?,?,?,?);"
        cursor.execute(query_Insert, id_Number_pastappointments, id_current_query, self.pastAppDate, self.pastIsAppear)
        cnxn.commit()

    def search_customer(self):
        # Searching customer by first name + last name + mother maiden name + dob return PK ID


        # Connect to the database
        cnxn, cursor = self.connect_database()
        return

