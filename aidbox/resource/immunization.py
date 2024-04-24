from typing import Optional
from ..base import *

class Immunization_ProtocolApplied(BackboneElement):
	seriesDosesPositiveInt: Optional[int] = None
	doseNumberPositiveInt: Optional[int] = None
	series: Optional[str] = None
	authority: Optional[Reference] = None
	doseNumberString: Optional[str] = None
	seriesDosesString: Optional[str] = None
	targetDisease: list[CodeableConcept] = []

class Immunization_Education(BackboneElement):
	documentType: Optional[str] = None
	presentationDate: Optional[str] = None
	publicationDate: Optional[str] = None
	reference: Optional[str] = None

class Immunization_Reaction(BackboneElement):
	date: Optional[str] = None
	detail: Optional[Reference] = None
	reported: Optional[bool] = None

class Immunization_Performer(BackboneElement):
	actor: Reference
	function: Optional[CodeableConcept] = None

class Immunization(DomainResource):
	patient: Reference
	isSubpotent: Optional[bool] = None
	reportOrigin: Optional[CodeableConcept] = None
	protocolApplied: list[Immunization_ProtocolApplied] = []
	site: Optional[CodeableConcept] = None
	encounter: Optional[Reference] = None
	vaccineCode: CodeableConcept
	doseQuantity: Optional[Quantity] = None
	reasonCode: list[CodeableConcept] = []
	statusReason: Optional[CodeableConcept] = None
	route: Optional[CodeableConcept] = None
	recorded: Optional[str] = None
	programEligibility: list[CodeableConcept] = []
	note: list[Annotation] = []
	primarySource: Optional[bool] = None
	status: str
	lotNumber: Optional[str] = None
	identifier: list[Identifier] = []
	manufacturer: Optional[Reference] = None
	education: list[Immunization_Education] = []
	occurrenceString: Optional[str] = None
	reaction: list[Immunization_Reaction] = []
	location: Optional[Reference] = None
	occurrenceDateTime: Optional[str] = None
	fundingSource: Optional[CodeableConcept] = None
	subpotentReason: list[CodeableConcept] = []
	expirationDate: Optional[str] = None
	performer: list[Immunization_Performer] = []
	reasonReference: list[Reference] = []

