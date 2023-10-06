from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

from resources import Patient, Appointment
from base import Address, Period, HumanName, ContactPoint, Identifier, BackboneElement
from base import Where, Page, Sort, Count

import json



data = """{
    "id": "patient-1",
    "active": true,
    "gender": "female",
    "name": [{ "use": "official", "given": ["John"], "family": "Smith" }],
    "address": [{"use": "home", "type": "physical", "country": "Montenegro", "city": "Podgorica", "period": {"start": "1999-09-06", "end": "2023-09-06"}}],
    "birthDate": "2023-09-06",
    "telecom": [{ "use": "work", "system": "email", "value": "+1234567890" }],
    "photo": [{ "url": "https://en.gravatar.com/userimage/217345214/5360247794f8ef859628fcff8bee731a.jpeg" }],
    "identifier": [
        {
            "type": { "coding": [{ "system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "SS" }] },
            "system": "http://hl7.org/fhir/sid/us-ssn",
            "value": "0501340392"
        },
        {
            "type": { "coding": [{ "system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR" }] },
            "system": "http://hospital.smarthealthit.org",
            "value": "123451"
        }
    ]
}"""


patient1 = Patient(**json.loads(data))
patient1.save()

# print(patient1.address[0].model_dump(exclude_unset=True))

# print(patient1.model_dump(exclude_unset=True))

patient2 = Patient(
    address=[
        Address(
            city="Budva",
            use="home",
            type="both",
            period=Period(start="1999-09-06", end="2023-09-06"),
        )
    ],
    name=[HumanName(use="official", family="Smith", given=["Will"])],
    gender="female",
    active=True,
    telecom=[
        ContactPoint(system="phone", use="mobile", value="+1234567890"),
        ContactPoint(system="email", use="work", value="example@health-samurai.io"),
    ],
    identifier=[
        Identifier(system="http://hl7.org/fhir/sid/us-ssn", value="0501340392"),
        Identifier(system="http://hospital.smarthealthit.org", value="123451"),
    ],
)

print(patient1.model_dump_json(exclude_unset=True))
# patient2.save()
# patient = patient2.from_id("patient-1")
# patient.gender = "male"
# patient.save()

# patients_list = Patient.get(
#     Where('active', True),
#     Where('address-city', 'Podgorica'),
#     Sort('last_updated', 'asc'),
#     Count(10),
#     Page(1)
# )

# patient3 = Patient.from_id("patient-1")


# patient.delete()