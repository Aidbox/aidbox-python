from typing import Optional

from base import BackboneElement
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import CodeableConcept
from base import Annotation
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import Identifier
from base import BackboneElement
from base import Reference
from base import Reference
from base import Period
from base import DomainResource


class ClinicalImpression(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	investigation: list[BackboneElement] = []
	protocol: list[str] = []
	assessor: Optional[Reference] = None
	supportingInfo: list[Reference] = []
	encounter: Optional[Reference] = None
	problem: list[Reference] = []
	statusReason: Optional[CodeableConcept] = None
	note: list[Annotation] = []
	summary: Optional[str] = None
	effectiveDateTime: Optional[str] = None
	prognosisCodeableConcept: list[CodeableConcept] = []
	status: str
	previous: Optional[Reference] = None
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	finding: list[BackboneElement] = []
	prognosisReference: list[Reference] = []
	subject: Reference
	effectivePeriod: Optional[Period] = None

