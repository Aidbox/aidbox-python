from typing import Optional
from ..base import *

class RiskEvidenceSynthesis_SampleSize(BackboneElement):
	description: Optional[str] = None
	numberOfParticipants: Optional[int] = None
	numberOfStudies: Optional[int] = None

class RiskEvidenceSynthesis_Certainty_CertaintySubcomponent(BackboneElement):
	note: list[Annotation] = []
	rating: list[CodeableConcept] = []
	type: Optional[CodeableConcept] = None

class RiskEvidenceSynthesis_Certainty(BackboneElement):
	certaintySubcomponent: list[RiskEvidenceSynthesis_Certainty_CertaintySubcomponent] = []
	note: list[Annotation] = []
	rating: list[CodeableConcept] = []

class RiskEvidenceSynthesis_RiskEstimate_PrecisionEstimate(BackboneElement):
	from: Optional[str] = None
	level: Optional[str] = None
	to: Optional[str] = None
	type: Optional[CodeableConcept] = None

class RiskEvidenceSynthesis_RiskEstimate(BackboneElement):
	denominatorCount: Optional[int] = None
	description: Optional[str] = None
	numeratorCount: Optional[int] = None
	precisionEstimate: list[RiskEvidenceSynthesis_RiskEstimate_PrecisionEstimate] = []
	type: Optional[CodeableConcept] = None
	unitOfMeasure: Optional[CodeableConcept] = None
	value: Optional[str] = None

class RiskEvidenceSynthesis(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	endorser: list[ContactDetail] = []
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	sampleSize: Optional[RiskEvidenceSynthesis_SampleSize] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	studyType: Optional[CodeableConcept] = None
	outcome: Reference
	topic: list[CodeableConcept] = []
	title: Optional[str] = None
	note: list[Annotation] = []
	author: list[ContactDetail] = []
	synthesisType: Optional[CodeableConcept] = None
	status: str
	population: Reference
	url: Optional[str] = None
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	editor: list[ContactDetail] = []
	certainty: list[RiskEvidenceSynthesis_Certainty] = []
	reviewer: list[ContactDetail] = []
	exposure: Optional[Reference] = None
	version: Optional[str] = None
	relatedArtifact: list[RelatedArtifact] = []
	contact: list[ContactDetail] = []
	riskEstimate: Optional[RiskEvidenceSynthesis_RiskEstimate] = None
	effectivePeriod: Optional[Period] = None

