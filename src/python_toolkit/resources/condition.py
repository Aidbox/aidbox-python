from typing import Optional

from base import CodeableConcept
from base import CodeableConcept
from base import Range
from base import BackboneElement
from base import Reference
from base import BackboneElement
from base import Period
from base import Period
from base import Reference
from base import Annotation
from base import Range
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import Identifier
from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import DomainResource


class Condition(DomainResource):
	category: list[CodeableConcept] = []
	clinicalStatus: Optional[CodeableConcept] = None
	abatementAge: Optional[str] = None
	onsetRange: Optional[Range] = None
	onsetAge: Optional[str] = None
	stage: list[BackboneElement] = []
	encounter: Optional[Reference] = None
	evidence: list[BackboneElement] = []
	onsetPeriod: Optional[Period] = None
	abatementPeriod: Optional[Period] = None
	asserter: Optional[Reference] = None
	note: list[Annotation] = []
	abatementString: Optional[str] = None
	abatementRange: Optional[Range] = None
	recordedDate: Optional[str] = None
	onsetString: Optional[str] = None
	recorder: Optional[Reference] = None
	severity: Optional[CodeableConcept] = None
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	onsetDateTime: Optional[str] = None
	bodySite: list[CodeableConcept] = []
	abatementDateTime: Optional[str] = None
	verificationStatus: Optional[CodeableConcept] = None
	subject: Reference

