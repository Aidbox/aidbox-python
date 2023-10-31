# Aidbox-Py

## Install

```shell
pip install git+https://github.com/Aidbox/aidbox-python
```

## Auth

Environment has to contain three variables `AIDBOX_URL`, `AIDBOX_CLIENT_USERNAME` and `AIDBOX_CLIENT_PASSWORD`
(username and password from aidbox basic client). It can be solved with code below that loads
variables from the `.env` file.

```python
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
```

## Example

```python
from aidbox.resource.appointment import Appointment, Appointment_Participant
from aidbox.resource import Patient, Practitioner
from aidbox.base import Reference, HumanName

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

## API

#### Save resource to aidbox `.save()`

```python
from aidbox.resource.patient import Patient
from aidbox.base import HumanName

patient = Patient()
patient.name = [HumanName(family="Bourne", given=["Jason"])]

patient.save()
```

#### Delete resource by id `.delete()`

```python
from aidbox.resource.patient import Patient

patient = Patient(id="patient-1")
patient.delete()
```

#### Get resource by id `.from_id()`

```python
from aidbox.resource.patient import Patient

patient = Patient.from_id("patient-1")
```

#### Get resource list `.get()`

```python
from aidbox.resource.patient import Patient
from aidbox.base import Page, Count, Sort, Where

patients = Patient.get(Where('active', True), Count(10), Page(3), Sort('created_at', 'desc'))
```

#### Serialize to JSON `dumps()`

```python
from aidbox.resource.patient import Patient
from aidbox.base import Page, Count, Sort, Where

patient = Patient.from_id('patient-1')
patient_json = patient.dumps(exclude_unset=True)
```

#### Bundle `.bundle()`

```python
from aidbox.base import API

entry = []

entry.append(
    {
        "resource": patient.dumps(exclude_unset=True),
        "request": {"method": "POST", "url": "Patient"},
    },
    {
        "resource": patient.dumps(exclude_unset=True),
        "request": {"method": "POST", "url": "Patient"},
    },
)

try:
    API.bundle(entry=entry, type="transaction")
except requests.exceptions.RequestException as e:
    if e.response is not None:
        print(e.response.json())
```
