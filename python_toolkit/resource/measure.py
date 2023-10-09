from typing import Optional
from base import *

class Measure_Group_Population(BackboneElement):
	code: Optional[CodeableConcept] = None
	criteria: Expression
	description: Optional[str] = None

class Measure_Group_Stratifier_Component(BackboneElement):
	code: Optional[CodeableConcept] = None
	criteria: Expression
	description: Optional[str] = None

class Measure_Group_Stratifier(BackboneElement):
	code: Optional[CodeableConcept] = None
	component: list[Measure_Group_Stratifier_Component] = []
	criteria: Optional[Expression] = None
	description: Optional[str] = None

class Measure_Group(BackboneElement):
	code: Optional[CodeableConcept] = None
	description: Optional[str] = None
	population: list[Measure_Group_Population] = []
	stratifier: list[Measure_Group_Stratifier] = []

class Measure_SupplementalData(BackboneElement):
	code: Optional[CodeableConcept] = None
	criteria: Expression
	description: Optional[str] = None
	usage: list[CodeableConcept] = []

class Measure(DomainResource):
	description: Optional[str] = None
	definition: list[str] = []
	date: Optional[str] = None
	group: list[Measure_Group] = []
	endorser: list[ContactDetail] = []
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	compositeScoring: Optional[CodeableConcept] = None
	disclaimer: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	guidance: Optional[str] = None
	type: list[CodeableConcept] = []
	experimental: Optional[bool] = None
	topic: list[CodeableConcept] = []
	title: Optional[str] = None
	supplementalData: list[Measure_SupplementalData] = []
	library: list[str] = []
	author: list[ContactDetail] = []
	usage: Optional[str] = None
	rationale: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	url: Optional[str] = None
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	editor: list[ContactDetail] = []
	riskAdjustment: Optional[str] = None
	scoring: Optional[CodeableConcept] = None
	reviewer: list[ContactDetail] = []
	version: Optional[str] = None
	relatedArtifact: list[RelatedArtifact] = []
	contact: list[ContactDetail] = []
	subjectReference: Optional[Reference] = None
	improvementNotation: Optional[CodeableConcept] = None
	rateAggregation: Optional[str] = None
	effectivePeriod: Optional[Period] = None
	clinicalRecommendationStatement: Optional[str] = None

