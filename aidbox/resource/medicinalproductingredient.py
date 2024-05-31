from pydantic import *
from typing import Optional, List
from ..base import *

class MedicinalProductIngredient_SpecifiedSubstance_Strength_ReferenceStrength(BackboneElement):
	substance: Optional[CodeableConcept] = None
	strength: Ratio
	strengthLowLimit: Optional[Ratio] = None
	measurementPoint: Optional[str] = None
	country: Optional[List[CodeableConcept]] = None

class MedicinalProductIngredient_SpecifiedSubstance_Strength(BackboneElement):
	presentation: Ratio
	presentationLowLimit: Optional[Ratio] = None
	concentration: Optional[Ratio] = None
	concentrationLowLimit: Optional[Ratio] = None
	measurementPoint: Optional[str] = None
	country: Optional[List[CodeableConcept]] = None
	referenceStrength: Optional[List[MedicinalProductIngredient_SpecifiedSubstance_Strength_ReferenceStrength]] = None

class MedicinalProductIngredient_SpecifiedSubstance(BackboneElement):
	code: CodeableConcept
	group: CodeableConcept
	confidentiality: Optional[CodeableConcept] = None
	strength: Optional[List[MedicinalProductIngredient_SpecifiedSubstance_Strength]] = None

class MedicinalProductIngredient_Substance(BackboneElement):
	code: CodeableConcept
	strength: Optional[List[str]] = None

class MedicinalProductIngredient(DomainResource):
	identifier: Optional[Identifier] = None
	role: CodeableConcept
	allergenicIndicator: Optional[bool] = None
	manufacturer: Optional[List[Reference]] = None
	specifiedSubstance: Optional[List[MedicinalProductIngredient_SpecifiedSubstance]] = None
	substance: Optional[MedicinalProductIngredient_Substance] = None