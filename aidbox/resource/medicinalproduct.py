from pydantic import *
from typing import Optional, List
from ..base import *

class MedicinalProduct_ManufacturingBusinessOperation(BackboneElement):
	operationType: Optional[CodeableConcept] = None
	authorisationReferenceNumber: Optional[Identifier] = None
	effectiveDate: Optional[str] = None
	confidentialityIndicator: Optional[CodeableConcept] = None
	manufacturer: Optional[List[Reference]] = None
	regulator: Optional[Reference] = None

class MedicinalProduct_Name_NamePart(BackboneElement):
	part: str
	type: Coding

class MedicinalProduct_Name_CountryLanguage(BackboneElement):
	country: CodeableConcept
	jurisdiction: Optional[CodeableConcept] = None
	language: CodeableConcept

class MedicinalProduct_Name(BackboneElement):
	productName: str
	namePart: Optional[List[MedicinalProduct_Name_NamePart]] = None
	countryLanguage: Optional[List[MedicinalProduct_Name_CountryLanguage]] = None

class MedicinalProduct_SpecialDesignation(BackboneElement):
	date: Optional[str] = None
	species: Optional[CodeableConcept] = None
	type: Optional[CodeableConcept] = None
	intendedUse: Optional[CodeableConcept] = None
	status: Optional[CodeableConcept] = None
	identifier: Optional[List[Identifier]] = None
	indicationCodeableConcept: Optional[CodeableConcept] = None
	indicationReference: Optional[Reference] = None

class MedicinalProduct(DomainResource):
	additionalMonitoringIndicator: Optional[CodeableConcept] = None
	manufacturingBusinessOperation: Optional[List[MedicinalProduct_ManufacturingBusinessOperation]] = None
	combinedPharmaceuticalDoseForm: Optional[CodeableConcept] = None
	clinicalTrial: Optional[List[Reference]] = None
	productClassification: Optional[List[CodeableConcept]] = None
	name: List[MedicinalProduct_Name]
	masterFile: Optional[List[Reference]] = None
	pharmaceuticalProduct: Optional[List[Reference]] = None
	type: Optional[CodeableConcept] = None
	marketingStatus: Optional[List[MarketingStatus]] = None
	specialMeasures: Optional[List[str]] = None
	specialDesignation: Optional[List[MedicinalProduct_SpecialDesignation]] = None
	packagedMedicinalProduct: Optional[List[Reference]] = None
	identifier: Optional[List[Identifier]] = None
	crossReference: Optional[List[Identifier]] = None
	attachedDocument: Optional[List[Reference]] = None
	domain: Optional[Coding] = None
	legalStatusOfSupply: Optional[CodeableConcept] = None
	paediatricUseIndicator: Optional[CodeableConcept] = None
	contact: Optional[List[Reference]] = None