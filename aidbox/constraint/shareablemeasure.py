from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


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

class Shareablemeasure(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/shareablemeasure"])
	description: str
	definition: Optional[List[str]] = None
	date: Optional[str] = None
	group: Optional[List[Measure_Group]] = None
	endorser: Optional[List[ContactDetail]] = None
	publisher: str
	approvalDate: Optional[str] = None
	compositeScoring: Optional[CodeableConcept] = None
	disclaimer: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	name: str
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	guidance: Optional[str] = None
	type: Optional[List[CodeableConcept]] = None
	experimental: bool
	topic: Optional[List[CodeableConcept]] = None
	title: Optional[str] = None
	supplementalData: Optional[List[Measure_SupplementalData]] = None
	library: Optional[List[str]] = None
	author: Optional[List[ContactDetail]] = None
	usage: Optional[str] = None
	rationale: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	url: str
	identifier: Optional[List[Identifier]] = None
	lastReviewDate: Optional[str] = None
	editor: Optional[List[ContactDetail]] = None
	riskAdjustment: Optional[str] = None
	scoring: Optional[CodeableConcept] = None
	reviewer: Optional[List[ContactDetail]] = None
	version: str
	relatedArtifact: Optional[List[RelatedArtifact]] = None
	contact: Optional[List[ContactDetail]] = None
	subjectReference: Optional[Reference] = None
	improvementNotation: Optional[CodeableConcept] = None
	rateAggregation: Optional[str] = None
	effectivePeriod: Optional[Period] = None
	clinicalRecommendationStatement: Optional[str] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None