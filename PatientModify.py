import pyodbc
import time

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
    def upload_all_data(self,firstName, lastName, dateofbirth, motherMaidenName, phoneNumber, appointmentDate, pastAppDate, pastIsAppear):
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateofbirth
        self.motherMaidenName = motherMaidenName
        self.phoneNumber = phoneNumber
        self.appointmentDate = appointmentDate
        self.pastAppDate = pastAppDate
        self.pastIsAppear = pastIsAppear

    def adding_Customer(self):
        # Upload a customer to the tables

        # Connect to the database
        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=.\SQLEXPRESS;"
                              "Database=PatientRegistry;"
                              "Trusted_Connection=yes;")

        cursor = cnxn.cursor()

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
        return
