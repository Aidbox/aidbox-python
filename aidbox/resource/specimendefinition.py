from typing import Optional
from ..base import *

class SpecimenDefinition_TypeTested_Container_Additive(BackboneElement):
	additiveCodeableConcept: Optional[CodeableConcept] = None
	additiveReference: Optional[Reference] = None

class SpecimenDefinition_TypeTested_Container(BackboneElement):
	description: Optional[str] = None
	capacity: Optional[Quantity] = None
	minimumVolumeQuantity: Optional[Quantity] = None
	type: Optional[CodeableConcept] = None
	cap: Optional[CodeableConcept] = None
	preparation: Optional[str] = None
	material: Optional[CodeableConcept] = None
	additive: list[SpecimenDefinition_TypeTested_Container_Additive] = []
	minimumVolumeString: Optional[str] = None

class SpecimenDefinition_TypeTested_Handling(BackboneElement):
	instruction: Optional[str] = None
	maxDuration: Optional[str] = None
	temperatureQualifier: Optional[CodeableConcept] = None
	temperatureRange: Optional[Range] = None

class SpecimenDefinition_TypeTested(BackboneElement):
	container: Optional[SpecimenDefinition_TypeTested_Container] = None
	handling: list[SpecimenDefinition_TypeTested_Handling] = []
	isDerived: Optional[bool] = None
	preference: str
	rejectionCriterion: list[CodeableConcept] = []
	requirement: Optional[str] = None
	retentionTime: Optional[str] = None
	type: Optional[CodeableConcept] = None

class SpecimenDefinition(DomainResource):
	collection: list[CodeableConcept] = []
	identifier: Optional[Identifier] = None
	patientPreparation: list[CodeableConcept] = []
	timeAspect: Optional[str] = None
	typeCollected: Optional[CodeableConcept] = None
	typeTested: list[SpecimenDefinition_TypeTested] = []

