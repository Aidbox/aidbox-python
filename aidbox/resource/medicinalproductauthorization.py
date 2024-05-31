from pydantic import *
from typing import Optional, List
from ..base import *

class MedicinalProductAuthorization_JurisdictionalAuthorization(BackboneElement):
	identifier: Optional[List[Identifier]] = None
	country: Optional[CodeableConcept] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	legalStatusOfSupply: Optional[CodeableConcept] = None
	validityPeriod: Optional[Period] = None

class MedicinalProductAuthorization_Procedure(BackboneElement):
	identifier: Optional[Identifier] = None
	type: CodeableConcept
	datePeriod: Optional[Period] = None
	dateDateTime: Optional[str] = None
	application: Optional[List[str]] = None

class MedicinalProductAuthorization(DomainResource):
	dataExclusivityPeriod: Optional[Period] = None
	restoreDate: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	jurisdictionalAuthorization: Optional[List[MedicinalProductAuthorization_JurisdictionalAuthorization]] = None
	procedure: Optional[MedicinalProductAuthorization_Procedure] = None
	legalBasis: Optional[CodeableConcept] = None
	validityPeriod: Optional[Period] = None
	regulator: Optional[Reference] = None
	status: Optional[CodeableConcept] = None
	identifier: Optional[List[Identifier]] = None
	statusDate: Optional[str] = None
	dateOfFirstAuthorization: Optional[str] = None
	internationalBirthDate: Optional[str] = None
	holder: Optional[Reference] = None
	country: Optional[List[CodeableConcept]] = None
	subject: Optional[Reference] = None