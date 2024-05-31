from pydantic import *
from typing import Optional, List
from ..base import *

class NutritionOrder_OralDiet_Nutrient(BackboneElement):
	modifier: Optional[CodeableConcept] = None
	amount: Optional[Quantity] = None

class NutritionOrder_OralDiet_Texture(BackboneElement):
	modifier: Optional[CodeableConcept] = None
	foodType: Optional[CodeableConcept] = None

class NutritionOrder_OralDiet(BackboneElement):
	type: Optional[List[CodeableConcept]] = None
	schedule: Optional[List[Timing]] = None
	nutrient: Optional[List[NutritionOrder_OralDiet_Nutrient]] = None
	texture: Optional[List[NutritionOrder_OralDiet_Texture]] = None
	fluidConsistencyType: Optional[List[CodeableConcept]] = None
	instruction: Optional[str] = None

class NutritionOrder_EnteralFormula_Administration(BackboneElement):
	schedule: Optional[Timing] = None
	quantity: Optional[Quantity] = None
	rateQuantity: Optional[Quantity] = None
	rateRatio: Optional[Ratio] = None

class NutritionOrder_EnteralFormula(BackboneElement):
	additiveType: Optional[CodeableConcept] = None
	maxVolumeToDeliver: Optional[Quantity] = None
	baseFormulaType: Optional[CodeableConcept] = None
	routeofAdministration: Optional[CodeableConcept] = None
	additiveProductName: Optional[str] = None
	caloricDensity: Optional[Quantity] = None
	administrationInstruction: Optional[str] = None
	administration: Optional[List[NutritionOrder_EnteralFormula_Administration]] = None
	baseFormulaProductName: Optional[str] = None

class NutritionOrder_Supplement(BackboneElement):
	type: Optional[CodeableConcept] = None
	productName: Optional[str] = None
	schedule: Optional[List[Timing]] = None
	quantity: Optional[Quantity] = None
	instruction: Optional[str] = None

class NutritionOrder(DomainResource):
	patient: Reference
	oralDiet: Optional[NutritionOrder_OralDiet] = None
	instantiatesCanonical: Optional[List[str]] = None
	instantiatesUri: Optional[List[str]] = None
	instantiates: Optional[List[str]] = None
	encounter: Optional[Reference] = None
	note: Optional[List[Annotation]] = None
	dateTime: str
	enteralFormula: Optional[NutritionOrder_EnteralFormula] = None
	foodPreferenceModifier: Optional[List[CodeableConcept]] = None
	status: str
	excludeFoodModifier: Optional[List[CodeableConcept]] = None
	identifier: Optional[List[Identifier]] = None
	intent: str
	orderer: Optional[Reference] = None
	supplement: Optional[List[NutritionOrder_Supplement]] = None
	allergyIntolerance: Optional[List[Reference]] = None