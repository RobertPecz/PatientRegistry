from SearchCustomer import *
from UserInput import *
from DatabaseConnection import *


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
    def upload_all_data(self,first_name, last_name, date_of_birth, mother_maiden_name, phone_number, appointment_date, past_app_date, past_is_appear):
        self.firstName = first_name
        self.lastName = last_name
        self.dateOfBirth = date_of_birth
        self.motherMaidenName = mother_maiden_name
        self.phoneNumber = phone_number
        self.appointmentDate = appointment_date
        self.pastAppDate = past_app_date
        self.pastIsAppear = past_is_appear

    def adding_customer(self):
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
        cnxn,cursor = ConnectingToDatabase.connect_database(self)

        # Select the last PK ID from Patient table and +1 to it.
        id_last_number_query_patient = "SELECT TOP 1 ID FROM Patient ORDER BY ID Desc;"
        cursor.execute(id_last_number_query_patient)
        row = cursor.fetchone()
        id_number_patient = row[0]+1

        # Select the last PK ID from PastAppointments table and +1 to is
        id_last_number_query_patient = "SELECT TOP 1 ID FROM PastAppointments ORDER BY ID Desc;"
        cursor.execute(id_last_number_query_patient)
        row = cursor.fetchone()
        id_number_pastappointments = row[0]+1

        # Insert Patient data's into the Patient table
        query_insert = "INSERT INTO Patient(ID, FirstName, LastName, DateOfBirth, MotherMaidenName, PhoneNumber, AppointmentDate) VALUES(?,?,?,?,?,?,?);"
        cursor.execute(query_insert, id_number_patient, self.firstName, self.lastName, self.dateOfBirth, self.motherMaidenName, self.phoneNumber, self.appointmentDate)
        cnxn.commit()

        # Select PK ID Where the firstname and lastname which is passed as variable
        id_current_query = "SELECT ID FROM Patient WHERE FirstName=? and LastName=?;"
        cursor.execute(id_current_query, self.firstName, self.lastName)
        row = cursor.fetchone()
        id_current_query = row[0]

        # Insert the past appointments to the PastAppointments table set the Isappear column default to No.
        query_insert = "INSERT INTO PastAppointments(ID, PatientID, PastAppTime, IsAppear) VALUES(?,?,?,?);"
        cursor.execute(query_insert, id_number_pastappointments, id_current_query, self.pastAppDate, self.pastIsAppear)
        cnxn.commit()

    def modifying_first_name(self):
        # Change the first name and update in the table
        search = SearchingCustomer()
        customer = search.search_customer()
        if customer is not None:
            change_first_name = UserInput()
            change_name = change_first_name.change_first_name()
            cnxn, cursor = ConnectingToDatabase.connect_database(self)
            query_mod_first_name = "UPDATE Patient SET FirstName=? WHERE ID=?;"
            cursor.execute(query_mod_first_name,change_name,customer)
            cnxn.commit()
    #Add all with data (last name, date of birth, mother maiden name, phone number, appointment date)

    def modifying_last_name(self):
        # Change the last name and update in the table
        search = SearchingCustomer()
        customer = search.search_customer()
        if customer is not None:
            change_last_name = UserInput()
            change_name = change_last_name.change_last_name()
            cnxn, cursor = ConnectingToDatabase.connect_database(self)
            query_mod_last_name = "UPDATE Patient SET LastName=? WHERE ID=?;"
            cursor.execute(query_mod_last_name,change_name, customer)
            cnxn.commit()

    def modifying_phone_number(self):
        # Change the phone number and update in the table
        search = SearchingCustomer()
        customer = search.search_customer()
        if customer is not None:
            change_phone_number = UserInput()
            change_pnumber = change_phone_number.change_phonenumber()
            cnxn, cursor = ConnectingToDatabase.connect_database(self)
            query_mod_phone_number = "UPDATE Patient SET PhoneNumber=? WHERE ID=?;"
            cursor.execute(query_mod_phone_number, change_pnumber, customer)
            cnxn.commit()

    def modifying_dob(self):
        # Change the date of birth and update in the table
        search = SearchingCustomer()
        customer = search.search_customer()
        if customer is not None:
            change_date_of_birth = UserInput()
            change_dob = change_date_of_birth.change_dob()
            cnxn, cursor = ConnectingToDatabase.connect_database(self)
            query_mod_dob = "UPDATE Patient SET DateOfBirth=? WHERE ID=?;"
            cursor.execute(query_mod_dob, change_dob, customer)
            cnxn.commit()

    def modifying_mother_maiden_name(self):
        # Change mother maiden name and update in the table
        search = SearchingCustomer()
        customer = search.search_customer()
        if customer is not None:
            change_mother_maiden_name = UserInput()
            change_mothername = change_mother_maiden_name.change_mother_maiden_name()
            cnxn, cursor = ConnectingToDatabase.connect_database(self)
            query_mod_mother_maiden_name = "UPDATE Patient SET MotherMaidenName=? WHERE ID=?;"
            cursor.execute(query_mod_mother_maiden_name, change_mothername, customer)
            cnxn.commit()

    def modifying_appointment_date(self):
        # Change appointment date and update in the table
        search = SearchingCustomer()
        customer = search.search_customer()
        if customer is not None:
            change_appointment_date = UserInput()
            change_appointmentdate = change_appointment_date.change_appointment_date()
            cnxn, cursor = ConnectingToDatabase.connect_database(self)
            query_mod_appointment_date = "UPDATE Patient SET AppointmentDate=? WHERE ID=?;"
            cursor.execute(query_mod_appointment_date, change_appointmentdate, customer)
            cnxn.commit()