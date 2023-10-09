from typing import Optional
from base import *

class MedicinalProductAuthorization_JurisdictionalAuthorization(BackboneElement):
	country: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	jurisdiction: list[CodeableConcept] = []
	legalStatusOfSupply: Optional[CodeableConcept] = None
	validityPeriod: Optional[Period] = None

class MedicinalProductAuthorization_Procedure(BackboneElement):
	application: list[str] = []
	dateDateTime: Optional[str] = None
	datePeriod: Optional[Period] = None
	identifier: Optional[Identifier] = None
	type: CodeableConcept

class MedicinalProductAuthorization(DomainResource):
	dataExclusivityPeriod: Optional[Period] = None
	restoreDate: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	jurisdictionalAuthorization: list[MedicinalProductAuthorization_JurisdictionalAuthorization] = []
	procedure: Optional[MedicinalProductAuthorization_Procedure] = None
	legalBasis: Optional[CodeableConcept] = None
	validityPeriod: Optional[Period] = None
	regulator: Optional[Reference] = None
	status: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	statusDate: Optional[str] = None
	dateOfFirstAuthorization: Optional[str] = None
	internationalBirthDate: Optional[str] = None
	holder: Optional[Reference] = None
	country: list[CodeableConcept] = []
	subject: Optional[Reference] = None

