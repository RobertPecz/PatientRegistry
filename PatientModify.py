import pyodbc

class PatientModding:
    """Modifying a Patient include add, modify appoint date, delete appointment"""

    def __init__(self,firstName,lastName,age,phoneNumber,appointmentDate):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.phoneNumber = phoneNumber
        self.appointmentDate = appointmentDate

    def adding_Customer(self):

        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=.\SQLEXPRESS;"
                              "Database=PatientRegistry;"
                              "Trusted_Connection=yes;")
        cursor = cnxn.cursor()
        id_Number_Query = ("SELECT TOP 1 ID FROM Patient ORDER BY ID Desc;")
        cursor.execute(id_Number_Query)

        row = cursor.fetchone()
        id_Number = row[0]+1
        query_Insert = "INSERT INTO Patient(ID,FirstName,LastName,Age,PhoneNumber,AppointmentDate) VALUES(?,?,?,?,?,?);"
        cursor.execute(query_Insert, id_Number,self.firstName,self.lastName,self.age,self.phoneNumber,self.appointmentDate)
        cnxn.commit()
        return
