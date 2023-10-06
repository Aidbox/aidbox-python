from typing import Optional

from base import Reference
from base import CodeableConcept
from base import Range
from base import Reference
from base import Period
from base import Reference
from base import Annotation
from base import Reference
from base import CodeableConcept
from base import Identifier
from base import CodeableConcept
from base import BackboneElement
from base import DomainResource


class AllergyIntolerance(DomainResource):
	patient: Reference
	category: list[str] = []
	criticality: Optional[str] = None
	clinicalStatus: Optional[CodeableConcept] = None
	onsetRange: Optional[Range] = None
	onsetAge: Optional[str] = None
	encounter: Optional[Reference] = None
	onsetPeriod: Optional[Period] = None
	type: Optional[str] = None
	asserter: Optional[Reference] = None
	note: list[Annotation] = []
	recordedDate: Optional[str] = None
	onsetString: Optional[str] = None
	recorder: Optional[Reference] = None
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	onsetDateTime: Optional[str] = None
	lastOccurrence: Optional[str] = None
	verificationStatus: Optional[CodeableConcept] = None
	reaction: list[BackboneElement] = []

