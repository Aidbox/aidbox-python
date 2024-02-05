from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class Immunization_ProtocolApplied(BackboneElement):
	seriesDosesPositiveInt: Optional[str] = None
	doseNumberPositiveInt: Optional[str] = None
	series: Optional[str] = None
	authority: Optional[Reference] = None
	doseNumberString: Optional[str] = None
	seriesDosesString: Optional[str] = None
	targetDisease: Optional[List[CodeableConcept]] = None

class Immunization_Education(BackboneElement):
	documentType: Optional[str] = None
	reference: Optional[str] = None
	publicationDate: Optional[str] = None
	presentationDate: Optional[str] = None

class Immunization_Reaction(BackboneElement):
	date: Optional[str] = None
	detail: Optional[Reference] = None
	reported: Optional[bool] = None

class Immunization_Performer(BackboneElement):
	function: Optional[CodeableConcept] = None
	actor: Reference

class UsCoreImmunization(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/core/StructureDefinition/us-core-immunization"])
	patient: Reference
	isSubpotent: Optional[bool] = None
	reportOrigin: Optional[CodeableConcept] = None
	protocolApplied: Optional[List[Immunization_ProtocolApplied]] = None
	site: Optional[CodeableConcept] = None
	encounter: Optional[Reference] = None
	vaccineCode: CodeableConcept
	doseQuantity: Optional[Quantity] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	statusReason: Optional[CodeableConcept] = None
	route: Optional[CodeableConcept] = None
	recorded: Optional[str] = None
	programEligibility: Optional[List[CodeableConcept]] = None
	note: Optional[List[Annotation]] = None
	primarySource: bool
	status: str
	lotNumber: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	manufacturer: Optional[Reference] = None
	education: Optional[List[Immunization_Education]] = None
	occurrenceString: Optional[str] = None
	reaction: Optional[List[Immunization_Reaction]] = None
	location: Optional[Reference] = None
	occurrenceDateTime: Optional[str] = None
	fundingSource: Optional[CodeableConcept] = None
	subpotentReason: Optional[List[CodeableConcept]] = None
	expirationDate: Optional[str] = None
	performer: Optional[List[Immunization_Performer]] = None
	reasonReference: Optional[List[Reference]] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None