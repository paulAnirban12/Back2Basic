# 🏥 Real-Life Scenario: Patient Health Record System
# --------------------------------------------------------------

# 👤 Class: PatientRecord                     | 🔐 Encapsulation Type
# Public Attrs: name, age                    | Public
# Protected Attr: _medical_history           | Protected
# Private Attr: __insurance_id               | Private

from dataclasses import dataclass, field
import random

@dataclass
class PatientRecord:
    name: str
    age: int
    __insurance_id: str  # Private attribute
    _medical_history: list = field(default_factory=list)  # Protected attribute
    __id: int = field(default_factory=lambda: random.randint(10000, 99999), init=False)

    def __post_init__(self):
        if self.__validate_insurance():
            print(f"Information of Patient number {self.__id}, {self.name} has been added to the database.")
        else:
            print("🚨 Unauthorized insurance id detected!")

    # Getter Method                      | get_basic_info() → returns name & age
    def get_basic_info(self):
        return self.name, self.age

    # Protected Setter Method            | _update_medical_history(entry) → adds history
    @property
    def medical_history(self):
        return self._medical_history

    @medical_history.setter
    def medical_history(self, new_history):
        self._medical_history.append(new_history)
        print(f"{new_history} has been added to the medical history of {self.name}")

    # Private Method (Internal Check)    | __validate_insurance() → checks insurance
    def __validate_insurance(self):
        return len(self.__insurance_id) == 13

    # Public Method                      | get_latest_diagnosis() → returns most recent record
    def get_latest_diagnosis(self):
        if self._medical_history:
            print(self._medical_history[-1])
        else:
            print("No medical history found.")

# Example patient usage
patient = PatientRecord("X", 25, "INS2025041234", ["diabetes", "asthma"])
patient_name, patient_age = patient.get_basic_info()
print(f"""Patient Name: {patient_name}
Patient Age: {patient_age}
Medical History: {patient.medical_history}""")
patient.medical_history = "Dizziness"
print(patient.medical_history)
patient.get_latest_diagnosis()

# 🩺 Class: DoctorAccess (inherits PatientRecord)
# Method: add_diagnosis(diagnosis)           | Adds diagnosis to _medical_history
# Method: recommend_treatment()              | Suggests treatment using history

class DoctorAccess(PatientRecord):

    def add_diagnosis(self, diagnosis):
        self._medical_history.append(diagnosis)
        print(f"{diagnosis} has been added to the medical history of {self.name}")

    def recommend_treatment(self, patient):
        history_str = " ".join(patient.medical_history).lower()

        if "diabetes" in history_str:
            print("Sugar is restricted until it is under control.")
        if "asthma" in history_str:
            print("Always carry the pump with you.")
        if any(term in history_str for term in ["high blood pressure", "high bp", "bp"]):
            print("Avoid direct salt.")
        if any(term in history_str for term in ["dizziness", "feeling dizzy"]):
            print("Increase protein intake.")
        if "heart" in history_str:
            print("Avoid red meat and alcohol.")
        if "kidney" in history_str:
            print("Drink more water.")

# Example doctor usage
patient2 = PatientRecord("A", 45, "INS2025841234", ["diabetes", "asthma", "BP"])
Doctor = DoctorAccess("X", 25, "INS2025041234", ["diabetes", "asthma"])
Doctor.add_diagnosis("Heart")
Doctor.recommend_treatment(patient2)
