from typing import Optional
from base import *

class MedicinalProductIngredient_SpecifiedSubstance_Strength_ReferenceStrength(BackboneElement):
	country: list[CodeableConcept] = []
	measurementPoint: Optional[str] = None
	strength: Ratio
	strengthLowLimit: Optional[Ratio] = None
	substance: Optional[CodeableConcept] = None

class MedicinalProductIngredient_SpecifiedSubstance_Strength(BackboneElement):
	concentration: Optional[Ratio] = None
	concentrationLowLimit: Optional[Ratio] = None
	country: list[CodeableConcept] = []
	measurementPoint: Optional[str] = None
	presentation: Ratio
	presentationLowLimit: Optional[Ratio] = None
	referenceStrength: list[MedicinalProductIngredient_SpecifiedSubstance_Strength_ReferenceStrength] = []

class MedicinalProductIngredient_SpecifiedSubstance(BackboneElement):
	code: CodeableConcept
	confidentiality: Optional[CodeableConcept] = None
	group: CodeableConcept
	strength: list[MedicinalProductIngredient_SpecifiedSubstance_Strength] = []

class MedicinalProductIngredient_Substance(BackboneElement):
	code: CodeableConcept
	strength: list[str] = []

class MedicinalProductIngredient(DomainResource):
	allergenicIndicator: Optional[bool] = None
	identifier: Optional[Identifier] = None
	manufacturer: list[Reference] = []
	role: CodeableConcept
	specifiedSubstance: list[MedicinalProductIngredient_SpecifiedSubstance] = []
	substance: Optional[MedicinalProductIngredient_Substance] = None

