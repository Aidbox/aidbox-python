from pydantic import *
from typing import Optional, List
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
	additive: Optional[List[SpecimenDefinition_TypeTested_Container_Additive]] = None
	minimumVolumeString: Optional[str] = None

class SpecimenDefinition_TypeTested_Handling(BackboneElement):
	temperatureQualifier: Optional[CodeableConcept] = None
	temperatureRange: Optional[Range] = None
	maxDuration: Optional[Duration] = None
	instruction: Optional[str] = None

class SpecimenDefinition_TypeTested(BackboneElement):
	isDerived: Optional[bool] = None
	type: Optional[CodeableConcept] = None
	preference: str
	container: Optional[SpecimenDefinition_TypeTested_Container] = None
	requirement: Optional[str] = None
	retentionTime: Optional[Duration] = None
	rejectionCriterion: Optional[List[CodeableConcept]] = None
	handling: Optional[List[SpecimenDefinition_TypeTested_Handling]] = None

class SpecimenDefinition(DomainResource):
	identifier: Optional[Identifier] = None
	typeCollected: Optional[CodeableConcept] = None
	patientPreparation: Optional[List[CodeableConcept]] = None
	timeAspect: Optional[str] = None
	collection: Optional[List[CodeableConcept]] = None
	typeTested: Optional[List[SpecimenDefinition_TypeTested]] = None