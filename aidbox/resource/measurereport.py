from pydantic import *
from typing import Optional, List
from ..base import *

class MeasureReport_Group_Population(BackboneElement):
	code: Optional[CodeableConcept] = None
	count: Optional[int] = None
	subjectResults: Optional[Reference] = None

class MeasureReport_Group_Stratifier_Stratum_Component(BackboneElement):
	code: CodeableConcept
	value: CodeableConcept

class MeasureReport_Group_Stratifier_Stratum_Population(BackboneElement):
	code: Optional[CodeableConcept] = None
	count: Optional[int] = None
	subjectResults: Optional[Reference] = None

class MeasureReport_Group_Stratifier_Stratum(BackboneElement):
	value: Optional[CodeableConcept] = None
	component: Optional[List[MeasureReport_Group_Stratifier_Stratum_Component]] = None
	population: Optional[List[MeasureReport_Group_Stratifier_Stratum_Population]] = None
	measureScore: Optional[Quantity] = None

class MeasureReport_Group_Stratifier(BackboneElement):
	code: Optional[List[CodeableConcept]] = None
	stratum: Optional[List[MeasureReport_Group_Stratifier_Stratum]] = None

class MeasureReport_Group(BackboneElement):
	code: Optional[CodeableConcept] = None
	population: Optional[List[MeasureReport_Group_Population]] = None
	measureScore: Optional[Quantity] = None
	stratifier: Optional[List[MeasureReport_Group_Stratifier]] = None

class MeasureReport(DomainResource):
	evaluatedResource: Optional[List[Reference]] = None
	date: Optional[str] = None
	group: Optional[List[MeasureReport_Group]] = None
	type: str
	measure: str
	reporter: Optional[Reference] = None
	status: str
	identifier: Optional[List[Identifier]] = None
	period: Period
	improvementNotation: Optional[CodeableConcept] = None
	subject: Optional[Reference] = None