from typing import Optional

from base import Reference
from base import Identifier
from base import BackboneElement
from base import Reference
from base import Reference
from base import DomainResource


class VisionPrescription(DomainResource):
	created: str
	dateWritten: str
	encounter: Optional[Reference] = None
	identifier: list[Identifier] = []
	lensSpecification: list[BackboneElement]
	patient: Reference
	prescriber: Reference
	status: str

