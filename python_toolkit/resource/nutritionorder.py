from typing import Optional
from base import *

class NutritionOrder_OralDiet_Nutrient(BackboneElement):
	amount: Optional[Quantity] = None
	modifier: Optional[CodeableConcept] = None

class NutritionOrder_OralDiet_Texture(BackboneElement):
	foodType: Optional[CodeableConcept] = None
	modifier: Optional[CodeableConcept] = None

class NutritionOrder_OralDiet(BackboneElement):
	fluidConsistencyType: list[CodeableConcept] = []
	instruction: Optional[str] = None
	nutrient: list[NutritionOrder_OralDiet_Nutrient] = []
	schedule: list[str] = []
	texture: list[NutritionOrder_OralDiet_Texture] = []
	type: list[CodeableConcept] = []

class NutritionOrder_EnteralFormula_Administration(BackboneElement):
	quantity: Optional[Quantity] = None
	rateQuantity: Optional[Quantity] = None
	rateRatio: Optional[Ratio] = None
	schedule: Optional[str] = None

class NutritionOrder_EnteralFormula(BackboneElement):
	additiveType: Optional[CodeableConcept] = None
	maxVolumeToDeliver: Optional[Quantity] = None
	baseFormulaType: Optional[CodeableConcept] = None
	routeofAdministration: Optional[CodeableConcept] = None
	additiveProductName: Optional[str] = None
	caloricDensity: Optional[Quantity] = None
	administrationInstruction: Optional[str] = None
	administration: list[NutritionOrder_EnteralFormula_Administration] = []
	baseFormulaProductName: Optional[str] = None

class NutritionOrder_Supplement(BackboneElement):
	instruction: Optional[str] = None
	productName: Optional[str] = None
	quantity: Optional[Quantity] = None
	schedule: list[str] = []
	type: Optional[CodeableConcept] = None

class NutritionOrder(DomainResource):
	patient: Reference
	oralDiet: Optional[NutritionOrder_OralDiet] = None
	instantiatesCanonical: list[str] = []
	instantiatesUri: list[str] = []
	instantiates: list[str] = []
	encounter: Optional[Reference] = None
	note: list[Annotation] = []
	dateTime: str
	enteralFormula: Optional[NutritionOrder_EnteralFormula] = None
	foodPreferenceModifier: list[CodeableConcept] = []
	status: str
	excludeFoodModifier: list[CodeableConcept] = []
	identifier: list[Identifier] = []
	intent: str
	orderer: Optional[Reference] = None
	supplement: list[NutritionOrder_Supplement] = []
	allergyIntolerance: list[Reference] = []

