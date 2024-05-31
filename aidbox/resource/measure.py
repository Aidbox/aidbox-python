from pydantic import *
from typing import Optional, List
from ..base import *

class Measure_Group_Population(BackboneElement):
	code: Optional[CodeableConcept] = None
	description: Optional[str] = None
	criteria: Expression

class Measure_Group_Stratifier_Component(BackboneElement):
	code: Optional[CodeableConcept] = None
	description: Optional[str] = None
	criteria: Expression

class Measure_Group_Stratifier(BackboneElement):
	code: Optional[CodeableConcept] = None
	description: Optional[str] = None
	criteria: Optional[Expression] = None
	component: Optional[List[Measure_Group_Stratifier_Component]] = None

class Measure_Group(BackboneElement):
	code: Optional[CodeableConcept] = None
	description: Optional[str] = None
	population: Optional[List[Measure_Group_Population]] = None
	stratifier: Optional[List[Measure_Group_Stratifier]] = None

class Measure_SupplementalData(BackboneElement):
	code: Optional[CodeableConcept] = None
	usage: Optional[List[CodeableConcept]] = None
	description: Optional[str] = None
	criteria: Expression

class Measure(DomainResource):
	description: Optional[str] = None
	definition: Optional[List[str]] = None
	date: Optional[str] = None
	group: Optional[List[Measure_Group]] = None
	endorser: Optional[List[ContactDetail]] = None
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	compositeScoring: Optional[CodeableConcept] = None
	disclaimer: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	name: Optional[str] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	guidance: Optional[str] = None
	type: Optional[List[CodeableConcept]] = None
	experimental: Optional[bool] = None
	topic: Optional[List[CodeableConcept]] = None
	title: Optional[str] = None
	supplementalData: Optional[List[Measure_SupplementalData]] = None
	library: Optional[List[str]] = None
	author: Optional[List[ContactDetail]] = None
	usage: Optional[str] = None
	rationale: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	url: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	lastReviewDate: Optional[str] = None
	editor: Optional[List[ContactDetail]] = None
	riskAdjustment: Optional[str] = None
	scoring: Optional[CodeableConcept] = None
	reviewer: Optional[List[ContactDetail]] = None
	version: Optional[str] = None
	relatedArtifact: Optional[List[RelatedArtifact]] = None
	contact: Optional[List[ContactDetail]] = None
	subjectReference: Optional[Reference] = None
	improvementNotation: Optional[CodeableConcept] = None
	rateAggregation: Optional[str] = None
	effectivePeriod: Optional[Period] = None
	clinicalRecommendationStatement: Optional[str] = None