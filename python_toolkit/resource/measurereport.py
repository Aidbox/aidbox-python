from typing import Optional
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
	component: list[MeasureReport_Group_Stratifier_Stratum_Component] = []
	measureScore: Optional[Quantity] = None
	population: list[MeasureReport_Group_Stratifier_Stratum_Population] = []
	value: Optional[CodeableConcept] = None

class MeasureReport_Group_Stratifier(BackboneElement):
	code: list[CodeableConcept] = []
	stratum: list[MeasureReport_Group_Stratifier_Stratum] = []

class MeasureReport_Group(BackboneElement):
	code: Optional[CodeableConcept] = None
	measureScore: Optional[Quantity] = None
	population: list[MeasureReport_Group_Population] = []
	stratifier: list[MeasureReport_Group_Stratifier] = []

class MeasureReport(DomainResource):
	evaluatedResource: list[Reference] = []
	date: Optional[str] = None
	group: list[MeasureReport_Group] = []
	type: str
	measure: str
	reporter: Optional[Reference] = None
	status: str
	identifier: list[Identifier] = []
	period: Period
	improvementNotation: Optional[CodeableConcept] = None
	subject: Optional[Reference] = None

