from PatientModify import *
from UserInput import *

userin = UserInput()

userin.adding_new_patient()

#adding a customer from userinputs input
customer1 = PatientModding()
customer1.upload_all_data(userin.FirstName,
                          userin.LastName,
                          userin.Dob,
                          userin.MotherMaidenName,
                          userin.Phone_number,
                          userin.AppointmentDate,
                          userin.AppointmentDate,
                          "No")

customer1.adding_Customer()
