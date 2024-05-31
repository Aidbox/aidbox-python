from pydantic import *
from typing import Optional, List
from ..base import *

class AllergyIntolerance_Reaction(BackboneElement):
	substance: Optional[CodeableConcept] = None
	manifestation: List[CodeableConcept]
	description: Optional[str] = None
	onset: Optional[str] = None
	severity: Optional[str] = None
	exposureRoute: Optional[CodeableConcept] = None
	note: Optional[List[Annotation]] = None

class AllergyIntolerance(DomainResource):
	patient: Reference
	category: Optional[List[str]] = None
	criticality: Optional[str] = None
	clinicalStatus: Optional[CodeableConcept] = None
	onsetRange: Optional[Range] = None
	onsetAge: Optional[Age] = None
	encounter: Optional[Reference] = None
	onsetPeriod: Optional[Period] = None
	type: Optional[str] = None
	asserter: Optional[Reference] = None
	note: Optional[List[Annotation]] = None
	recordedDate: Optional[str] = None
	onsetString: Optional[str] = None
	recorder: Optional[Reference] = None
	code: Optional[CodeableConcept] = None
	identifier: Optional[List[Identifier]] = None
	onsetDateTime: Optional[str] = None
	lastOccurrence: Optional[str] = None
	verificationStatus: Optional[CodeableConcept] = None
	reaction: Optional[List[AllergyIntolerance_Reaction]] = None