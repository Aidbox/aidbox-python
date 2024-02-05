from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *

class CodingTUMOR(Coding):
	system: Literal["http://terminology.hl7.org/CodeSystem/v2-0487"] = "http://terminology.hl7.org/CodeSystem/v2-0487"
	code: Literal["TUMOR"] = "TUMOR"

class McodeTumorSpecimenType(CodeableConcept):
	coding: List[CodingTUMOR] = [CodingTUMOR()]


class Specimen_Processing(BackboneElement):
	description: Optional[str] = None
	procedure: Optional[CodeableConcept] = None
	additive: Optional[List[Reference]] = None
	timeDateTime: Optional[str] = None
	timePeriod: Optional[Period] = None

class Specimen_Container(BackboneElement):
	identifier: Optional[List[Identifier]] = None
	description: Optional[str] = None
	type: Optional[CodeableConcept] = None
	capacity: Optional[Quantity] = None
	specimenQuantity: Optional[Quantity] = None
	additiveCodeableConcept: Optional[CodeableConcept] = None
	additiveReference: Optional[Reference] = None

class Specimen_Collection(BackboneElement):
	collectedDateTime: Optional[str] = None
	fastingStatusCodeableConcept: Optional[CodeableConcept] = None
	method: Optional[CodeableConcept] = None
	fastingStatusDuration: Optional[str] = None
	duration: Optional[str] = None
	collector: Optional[Reference] = None
	bodySite: Optional[CodeableConcept] = None
	quantity: Optional[Quantity] = None
	collectedPeriod: Optional[Period] = None

class McodeTumorSpecimen(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-tumor-specimen"])
	request: Optional[List[Reference]] = None
	receivedTime: Optional[str] = None
	processing: Optional[List[Specimen_Processing]] = None
	parent: Optional[List[Reference]] = None
	type: McodeTumorSpecimenType = McodeTumorSpecimenType()
	note: Optional[List[Annotation]] = None
	status: Optional[str] = None
	condition: Optional[List[CodeableConcept]] = None
	container: Optional[List[Specimen_Container]] = None
	identifier: Optional[List[Identifier]] = None
	accessionIdentifier: Optional[Identifier] = None
	collection: Optional[Specimen_Collection] = None
	subject: Optional[Reference] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None