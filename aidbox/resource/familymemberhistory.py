from typing import Optional
from ..base import *

class FamilyMemberHistory_Condition(BackboneElement):
	onsetRange: Optional[Range] = None
	onsetAge: Optional[str] = None
	contributedToDeath: Optional[bool] = None
	onsetPeriod: Optional[Period] = None
	outcome: Optional[CodeableConcept] = None
	note: list[Annotation] = []
	onsetString: Optional[str] = None
	code: CodeableConcept

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
	condition: list[FamilyMemberHistory_Condition] = []
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

