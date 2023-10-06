from typing import Optional

from base import Reference
from base import Period
from base import CodeableConcept
from base import Reference
from base import Annotation
from base import Identifier
from base import CodeableConcept
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import DomainResource


class DeviceUseStatement(DomainResource):
	derivedFrom: list[Reference] = []
	timingPeriod: Optional[Period] = None
	reasonCode: list[CodeableConcept] = []
	source: Optional[Reference] = None
	note: list[Annotation] = []
	timingDateTime: Optional[str] = None
	timingTiming: Optional[str] = None
	status: str
	recordedOn: Optional[str] = None
	identifier: list[Identifier] = []
	bodySite: Optional[CodeableConcept] = None
	device: Reference
	basedOn: list[Reference] = []
	subject: Reference
	reasonReference: list[Reference] = []

