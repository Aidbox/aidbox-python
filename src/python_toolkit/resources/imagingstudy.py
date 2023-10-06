from typing import Optional

from base import Reference
from base import BackboneElement
from base import Reference
from base import Reference
from base import CodeableConcept
from base import Coding
from base import Annotation
from base import Reference
from base import Identifier
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import CodeableConcept
from base import DomainResource


class ImagingStudy(DomainResource):
	description: Optional[str] = None
	started: Optional[str] = None
	numberOfSeries: Optional[str] = None
	interpreter: list[Reference] = []
	series: list[BackboneElement] = []
	procedureReference: Optional[Reference] = None
	encounter: Optional[Reference] = None
	reasonCode: list[CodeableConcept] = []
	modality: list[Coding] = []
	note: list[Annotation] = []
	referrer: Optional[Reference] = None
	status: str
	identifier: list[Identifier] = []
	basedOn: list[Reference] = []
	location: Optional[Reference] = None
	endpoint: list[Reference] = []
	subject: Reference
	numberOfInstances: Optional[str] = None
	reasonReference: list[Reference] = []
	procedureCode: list[CodeableConcept] = []

