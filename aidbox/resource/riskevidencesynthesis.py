from pydantic import *
from typing import Optional, List
from ..base import *

class RiskEvidenceSynthesis_SampleSize(BackboneElement):
	description: Optional[str] = None
	numberOfStudies: Optional[int] = None
	numberOfParticipants: Optional[int] = None

class RiskEvidenceSynthesis_Certainty_CertaintySubcomponent(BackboneElement):
	type: Optional[CodeableConcept] = None
	rating: Optional[List[CodeableConcept]] = None
	note: Optional[List[Annotation]] = None

class RiskEvidenceSynthesis_Certainty(BackboneElement):
	rating: Optional[List[CodeableConcept]] = None
	note: Optional[List[Annotation]] = None
	certaintySubcomponent: Optional[List[RiskEvidenceSynthesis_Certainty_CertaintySubcomponent]] = None

class RiskEvidenceSynthesis_RiskEstimate_PrecisionEstimate(BackboneElement):
	type: Optional[CodeableConcept] = None
	level: Optional[float] = None
	from_: Optional[float] = None
	to: Optional[float] = None

class RiskEvidenceSynthesis_RiskEstimate(BackboneElement):
	description: Optional[str] = None
	type: Optional[CodeableConcept] = None
	value: Optional[float] = None
	unitOfMeasure: Optional[CodeableConcept] = None
	denominatorCount: Optional[int] = None
	numeratorCount: Optional[int] = None
	precisionEstimate: Optional[List[RiskEvidenceSynthesis_RiskEstimate_PrecisionEstimate]] = None

class RiskEvidenceSynthesis(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	endorser: Optional[List[ContactDetail]] = None
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	sampleSize: Optional[RiskEvidenceSynthesis_SampleSize] = None
	name: Optional[str] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	studyType: Optional[CodeableConcept] = None
	outcome: Reference
	topic: Optional[List[CodeableConcept]] = None
	title: Optional[str] = None
	note: Optional[List[Annotation]] = None
	author: Optional[List[ContactDetail]] = None
	synthesisType: Optional[CodeableConcept] = None
	status: str
	population: Reference
	url: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	lastReviewDate: Optional[str] = None
	editor: Optional[List[ContactDetail]] = None
	certainty: Optional[List[RiskEvidenceSynthesis_Certainty]] = None
	reviewer: Optional[List[ContactDetail]] = None
	exposure: Optional[Reference] = None
	version: Optional[str] = None
	relatedArtifact: Optional[List[RelatedArtifact]] = None
	contact: Optional[List[ContactDetail]] = None
	riskEstimate: Optional[RiskEvidenceSynthesis_RiskEstimate] = None
	effectivePeriod: Optional[Period] = None