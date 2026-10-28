from medical_app.patient_management.records import patients
from medical_app.doctor_management.records import doctors
from medical_app.billing.records import bills
from medical_app.medical_records.records import medical_records

print("Patients:", patients())
print("Doctors:", doctors())
print("Bills:", bills())
print("Medical records:", medical_records())
