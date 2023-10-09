from typing import Optional
from ..base import *

class MedicinalProduct_ManufacturingBusinessOperation(BackboneElement):
	authorisationReferenceNumber: Optional[Identifier] = None
	confidentialityIndicator: Optional[CodeableConcept] = None
	effectiveDate: Optional[str] = None
	manufacturer: list[Reference] = []
	operationType: Optional[CodeableConcept] = None
	regulator: Optional[Reference] = None

class MedicinalProduct_Name_CountryLanguage(BackboneElement):
	country: CodeableConcept
	jurisdiction: Optional[CodeableConcept] = None
	language: CodeableConcept

class MedicinalProduct_Name_NamePart(BackboneElement):
	part: str
	type: Coding

class MedicinalProduct_Name(BackboneElement):
	countryLanguage: list[MedicinalProduct_Name_CountryLanguage] = []
	namePart: list[MedicinalProduct_Name_NamePart] = []
	productName: str

class MedicinalProduct_SpecialDesignation(BackboneElement):
	date: Optional[str] = None
	species: Optional[CodeableConcept] = None
	type: Optional[CodeableConcept] = None
	intendedUse: Optional[CodeableConcept] = None
	status: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	indicationCodeableConcept: Optional[CodeableConcept] = None
	indicationReference: Optional[Reference] = None

class MedicinalProduct(DomainResource):
	additionalMonitoringIndicator: Optional[CodeableConcept] = None
	manufacturingBusinessOperation: list[MedicinalProduct_ManufacturingBusinessOperation] = []
	combinedPharmaceuticalDoseForm: Optional[CodeableConcept] = None
	clinicalTrial: list[Reference] = []
	productClassification: list[CodeableConcept] = []
	name: list[MedicinalProduct_Name]
	masterFile: list[Reference] = []
	pharmaceuticalProduct: list[Reference] = []
	type: Optional[CodeableConcept] = None
	marketingStatus: list[MarketingStatus] = []
	specialMeasures: list[str] = []
	specialDesignation: list[MedicinalProduct_SpecialDesignation] = []
	packagedMedicinalProduct: list[Reference] = []
	identifier: list[Identifier] = []
	crossReference: list[Identifier] = []
	attachedDocument: list[Reference] = []
	domain: Optional[Coding] = None
	legalStatusOfSupply: Optional[CodeableConcept] = None
	paediatricUseIndicator: Optional[CodeableConcept] = None
	contact: list[Reference] = []

