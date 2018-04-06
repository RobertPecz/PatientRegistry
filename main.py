from PastAppointments import *

# Asking the customer all past appointments date
past_appointments = PastAppointments()
query_result = past_appointments.get_all_past_appointments()
print(query_result)
