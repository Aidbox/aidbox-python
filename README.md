# Python Toolkit

## Install

```shell
pip install git+https://github.com/Aidbox/python-toolkit
```

## Example

```python
from python_toolkit.resource.appointment import Appointment, Appointment_Participant
from python_toolkit.resource import Patient, Practitioner
from python_toolkit.base import Reference, HumanName

patient = Patient(name=[HumanName(family="Bourne", given=["Jason"])])
practitioner = Practitioner(name=[HumanName(family="Smith", given=["John"])])

patient.save()
practitioner.save()

try:
    Appointment(
        status="booked",
        participant=[
            Appointment_Participant(
                status="accepted",
                actor=Reference(reference="Practitioner/" + (practitioner.id or "")),
            ),
            Appointment_Participant(
                status="accepted",
                actor=Reference(reference="Patient/" + (patient.id or "")),
            ),
        ],
    ).save()
except requests.exceptions.RequestException as e:
    if e.response is not None:
        print(e.response.json())
```
