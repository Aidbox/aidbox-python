from typing import Optional
from ..base import *

class AllergyIntolerance_Reaction(BackboneElement):
	description: Optional[str] = None
	exposureRoute: Optional[CodeableConcept] = None
	manifestation: list[CodeableConcept]
	note: list[Annotation] = []
	onset: Optional[str] = None
	severity: Optional[str] = None
	substance: Optional[CodeableConcept] = None

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
	reaction: list[AllergyIntolerance_Reaction] = []

