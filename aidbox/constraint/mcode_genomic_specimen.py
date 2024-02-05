from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


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

class McodeGenomicSpecimen(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-genomic-specimen"])
	request: Optional[List[Reference]] = None
	receivedTime: Optional[str] = None
	processing: Optional[List[Specimen_Processing]] = None
	parent: Optional[List[Reference]] = None
	type: CodeableConcept
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