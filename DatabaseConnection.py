import pyodbc


class ConnectingToDatabase:
    # Connecting to a database

    def connect_database(self):
        # Connect to the database
        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=.\SQLEXPRESS;"
                              "Database=PatientRegistry;"
                              "Trusted_Connection=yes;")

        cursor = cnxn.cursor()
        return cnxn, cursor
