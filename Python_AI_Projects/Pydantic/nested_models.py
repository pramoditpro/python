from pydantic import BaseModel

class Address(BaseModel):
    House_no: str
    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'noida', 'state': 'uttar-pradesh', 'pin': '201301', 'House_no': '1234'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Pramod', 'gender': 'male', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
























# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed