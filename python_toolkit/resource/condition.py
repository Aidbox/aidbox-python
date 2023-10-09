from typing import Optional
from ..base import *

class Condition_Stage(BackboneElement):
	assessment: list[Reference] = []
	summary: Optional[CodeableConcept] = None
	type: Optional[CodeableConcept] = None

class Condition_Evidence(BackboneElement):
	code: list[CodeableConcept] = []
	detail: list[Reference] = []

class Condition(DomainResource):
	category: list[CodeableConcept] = []
	clinicalStatus: Optional[CodeableConcept] = None
	abatementAge: Optional[str] = None
	onsetRange: Optional[Range] = None
	onsetAge: Optional[str] = None
	stage: list[Condition_Stage] = []
	encounter: Optional[Reference] = None
	evidence: list[Condition_Evidence] = []
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

