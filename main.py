from PatientModify import *
from UserInput import *

userin = UserInput()

userin.adding_alldata()

#adding a customer from userinputs input
customer1 = PatientModding(userin.FirstName,userin.LastName,userin.Age,userin.PhoneNumber,userin.AppointmentDate)

customer1.adding_Customer()
