from pydantic import *
from typing import Optional, List
from ..base import *

class EffectEvidenceSynthesis_EffectEstimate_PrecisionEstimate(BackboneElement):
	type: Optional[CodeableConcept] = None
	level: Optional[float] = None
	from_: Optional[float] = None
	to: Optional[float] = None

class EffectEvidenceSynthesis_EffectEstimate(BackboneElement):
	description: Optional[str] = None
	type: Optional[CodeableConcept] = None
	variantState: Optional[CodeableConcept] = None
	value: Optional[float] = None
	unitOfMeasure: Optional[CodeableConcept] = None
	precisionEstimate: Optional[List[EffectEvidenceSynthesis_EffectEstimate_PrecisionEstimate]] = None

class EffectEvidenceSynthesis_SampleSize(BackboneElement):
	description: Optional[str] = None
	numberOfStudies: Optional[int] = None
	numberOfParticipants: Optional[int] = None

class EffectEvidenceSynthesis_Certainty_CertaintySubcomponent(BackboneElement):
	type: Optional[CodeableConcept] = None
	rating: Optional[List[CodeableConcept]] = None
	note: Optional[List[Annotation]] = None

class EffectEvidenceSynthesis_Certainty(BackboneElement):
	rating: Optional[List[CodeableConcept]] = None
	note: Optional[List[Annotation]] = None
	certaintySubcomponent: Optional[List[EffectEvidenceSynthesis_Certainty_CertaintySubcomponent]] = None

class EffectEvidenceSynthesis_ResultsByExposure(BackboneElement):
	description: Optional[str] = None
	exposureState: Optional[str] = None
	variantState: Optional[CodeableConcept] = None
	riskEvidenceSynthesis: Reference

class EffectEvidenceSynthesis(DomainResource):
	description: Optional[str] = None
	exposureAlternative: Reference
	date: Optional[str] = None
	effectEstimate: Optional[List[EffectEvidenceSynthesis_EffectEstimate]] = None
	endorser: Optional[List[ContactDetail]] = None
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	sampleSize: Optional[EffectEvidenceSynthesis_SampleSize] = None
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
	certainty: Optional[List[EffectEvidenceSynthesis_Certainty]] = None
	reviewer: Optional[List[ContactDetail]] = None
	exposure: Reference
	resultsByExposure: Optional[List[EffectEvidenceSynthesis_ResultsByExposure]] = None
	version: Optional[str] = None
	relatedArtifact: Optional[List[RelatedArtifact]] = None
	contact: Optional[List[ContactDetail]] = None
	effectivePeriod: Optional[Period] = None