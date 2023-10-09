from typing import Optional
from base import *

class ImmunizationRecommendation_Recommendation_DateCriterion(BackboneElement):
	code: CodeableConcept
	value: str

class ImmunizationRecommendation_Recommendation(BackboneElement):
	description: Optional[str] = None
	seriesDosesPositiveInt: Optional[str] = None
	contraindicatedVaccineCode: list[CodeableConcept] = []
	doseNumberPositiveInt: Optional[str] = None
	series: Optional[str] = None
	vaccineCode: list[CodeableConcept] = []
	doseNumberString: Optional[str] = None
	seriesDosesString: Optional[str] = None
	forecastStatus: CodeableConcept
	forecastReason: list[CodeableConcept] = []
	dateCriterion: list[ImmunizationRecommendation_Recommendation_DateCriterion] = []
	targetDisease: Optional[CodeableConcept] = None
	supportingImmunization: list[Reference] = []
	supportingPatientInformation: list[Reference] = []

class ImmunizationRecommendation(DomainResource):
	authority: Optional[Reference] = None
	date: str
	identifier: list[Identifier] = []
	patient: Reference
	recommendation: list[ImmunizationRecommendation_Recommendation]

