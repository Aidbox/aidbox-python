from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class Condition_Stage(BackboneElement):
	summary: Optional[CodeableConcept] = None
	assessment: Optional[List[Reference]] = None
	type: Optional[CodeableConcept] = None

class Condition_Evidence(BackboneElement):
	code: Optional[List[CodeableConcept]] = None
	detail: Optional[List[Reference]] = None

class UsCoreCondition(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition"])
	category: List[CodeableConcept]
	clinicalStatus: Optional[CodeableConcept] = None
	abatementAge: Optional[str] = None
	onsetRange: Optional[Range] = None
	onsetAge: Optional[str] = None
	stage: Optional[List[Condition_Stage]] = None
	encounter: Optional[Reference] = None
	evidence: Optional[List[Condition_Evidence]] = None
	onsetPeriod: Optional[Period] = None
	abatementPeriod: Optional[Period] = None
	asserter: Optional[Reference] = None
	note: Optional[List[Annotation]] = None
	abatementString: Optional[str] = None
	abatementRange: Optional[Range] = None
	recordedDate: Optional[str] = None
	onsetString: Optional[str] = None
	recorder: Optional[Reference] = None
	severity: Optional[CodeableConcept] = None
	code: CodeableConcept
	identifier: Optional[List[Identifier]] = None
	onsetDateTime: Optional[str] = None
	bodySite: Optional[List[CodeableConcept]] = None
	abatementDateTime: Optional[str] = None
	verificationStatus: Optional[CodeableConcept] = None
	subject: Reference
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None