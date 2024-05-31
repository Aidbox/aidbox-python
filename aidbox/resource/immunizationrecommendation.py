from pydantic import *
from typing import Optional, List
from ..base import *

class ImmunizationRecommendation_Recommendation_DateCriterion(BackboneElement):
	code: CodeableConcept
	value: str

class ImmunizationRecommendation_Recommendation(BackboneElement):
	description: Optional[str] = None
	seriesDosesPositiveInt: Optional[PositiveInt] = None
	contraindicatedVaccineCode: Optional[List[CodeableConcept]] = None
	doseNumberPositiveInt: Optional[PositiveInt] = None
	series: Optional[str] = None
	vaccineCode: Optional[List[CodeableConcept]] = None
	doseNumberString: Optional[str] = None
	seriesDosesString: Optional[str] = None
	forecastStatus: CodeableConcept
	forecastReason: Optional[List[CodeableConcept]] = None
	dateCriterion: Optional[List[ImmunizationRecommendation_Recommendation_DateCriterion]] = None
	targetDisease: Optional[CodeableConcept] = None
	supportingImmunization: Optional[List[Reference]] = None
	supportingPatientInformation: Optional[List[Reference]] = None

class ImmunizationRecommendation(DomainResource):
	identifier: Optional[List[Identifier]] = None
	patient: Reference
	date: str
	authority: Optional[Reference] = None
	recommendation: List[ImmunizationRecommendation_Recommendation]