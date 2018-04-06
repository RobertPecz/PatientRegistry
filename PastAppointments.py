from SearchCustomer import *
from DatabaseConnection import *


class PastAppointments:
    """Handling the past appointments date from PastAppointments table"""

    def get_all_past_appointments(self):
        # Selecting all Past appointments date from a specified patient

        # Searching for the patient
        search = SearchingCustomer()
        query_result = search.search_customer()

        # Connecting to the database
        cnxn, cursor = ConnectingToDatabase.connect_database(self)

        # Querying the data from database, getting all the appointments
        # which is connected the patient unique foreign key what is a PK in the Patient table
        query_search = "SELECT PastAppTime FROM PastAppointments WHERE PatientID=?;"
        cursor.execute(query_search, query_result)
        rows = cursor.fetchall()

        # Returning all the data or None
        return rows
