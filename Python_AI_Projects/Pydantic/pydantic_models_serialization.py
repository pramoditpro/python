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

print("<<<<<<<<<<<<<<serialization>>>>>>>>>>>>>>> ")


temp = patient1.model_dump(exclude_unset=True)

print(temp)
print(type(temp))

temp1 = Patient.model_validate(temp)
print(temp1)
print(type(temp1))

temp2 = patient1.model_dump_json(exclude_unset=True)        
print(temp2)
print(type(temp2))

temp3 = patient1.model_dump_json(exclude={'address': {'House_no'} })        
print(temp3)
print(type(temp3))