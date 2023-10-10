# Python Toolkit

## Install

```shell
pip install git+https://github.com/Aidbox/python-toolkit
```

## Auth

Environment has to contain three variables `AIDBOX_URL`, `AIDBOX_CLIENT_USERNAME` and `AIDBOX_CLIENT_PASSWORD`
(username and password from aidbox basic client). It can be solved with code below that loads
variables from the `.env` file.

```
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), "./.env")
load_dotenv(dotenv_path)
```

## Example

```python
from python_toolkit.resource.appointment import Appointment, Appointment_Participant
from python_toolkit.resource import Patient, Practitioner
from python_toolkit.base import Reference, HumanName

import requests

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
