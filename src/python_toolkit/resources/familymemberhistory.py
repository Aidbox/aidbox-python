from typing import Optional

from base import Reference
from base import CodeableConcept
from base import Range
from base import CodeableConcept
from base import CodeableConcept
from base import Annotation
from base import BackboneElement
from base import Identifier
from base import Range
from base import Period
from base import CodeableConcept
from base import Reference
from base import DomainResource


class FamilyMemberHistory(DomainResource):
	deceasedAge: Optional[str] = None
	patient: Reference
	date: Optional[str] = None
	instantiatesCanonical: list[str] = []
	instantiatesUri: list[str] = []
	sex: Optional[CodeableConcept] = None
	ageRange: Optional[Range] = None
	bornString: Optional[str] = None
	deceasedBoolean: Optional[bool] = None
	name: Optional[str] = None
	relationship: CodeableConcept
	reasonCode: list[CodeableConcept] = []
	note: list[Annotation] = []
	status: str
	condition: list[BackboneElement] = []
	identifier: list[Identifier] = []
	ageString: Optional[str] = None
	deceasedRange: Optional[Range] = None
	deceasedDate: Optional[str] = None
	bornPeriod: Optional[Period] = None
	deceasedString: Optional[str] = None
	ageAge: Optional[str] = None
	bornDate: Optional[str] = None
	dataAbsentReason: Optional[CodeableConcept] = None
	reasonReference: list[Reference] = []
	estimatedAge: Optional[bool] = None

