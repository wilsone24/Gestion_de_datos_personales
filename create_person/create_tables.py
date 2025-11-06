from database import Base, engine
from models.user_model import User
from models.patient_model import Patient
from models.appointment_model import Appointment
from models.doctor_model import Doctor
from models.specialty_model import Specialty

Base.metadata.create_all(bind=engine)