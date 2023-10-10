from typing import Optional
from ..base import *


class EffectEvidenceSynthesis_EffectEstimate_PrecisionEstimate(BackboneElement):
    from_: Optional[str] = None
    level: Optional[str] = None
    to: Optional[str] = None
    type: Optional[CodeableConcept] = None


class EffectEvidenceSynthesis_EffectEstimate(BackboneElement):
    description: Optional[str] = None
    precisionEstimate: list[
        EffectEvidenceSynthesis_EffectEstimate_PrecisionEstimate
    ] = []
    type: Optional[CodeableConcept] = None
    unitOfMeasure: Optional[CodeableConcept] = None
    value: Optional[str] = None
    variantState: Optional[CodeableConcept] = None


class EffectEvidenceSynthesis_SampleSize(BackboneElement):
    description: Optional[str] = None
    numberOfParticipants: Optional[int] = None
    numberOfStudies: Optional[int] = None


class EffectEvidenceSynthesis_Certainty_CertaintySubcomponent(BackboneElement):
    note: list[Annotation] = []
    rating: list[CodeableConcept] = []
    type: Optional[CodeableConcept] = None


class EffectEvidenceSynthesis_Certainty(BackboneElement):
    certaintySubcomponent: list[
        EffectEvidenceSynthesis_Certainty_CertaintySubcomponent
    ] = []
    note: list[Annotation] = []
    rating: list[CodeableConcept] = []


class EffectEvidenceSynthesis_ResultsByExposure(BackboneElement):
    description: Optional[str] = None
    exposureState: Optional[str] = None
    riskEvidenceSynthesis: Reference
    variantState: Optional[CodeableConcept] = None


class EffectEvidenceSynthesis(DomainResource):
    description: Optional[str] = None
    exposureAlternative: Reference
    date: Optional[str] = None
    effectEstimate: list[EffectEvidenceSynthesis_EffectEstimate] = []
    endorser: list[ContactDetail] = []
    publisher: Optional[str] = None
    approvalDate: Optional[str] = None
    jurisdiction: list[CodeableConcept] = []
    sampleSize: Optional[EffectEvidenceSynthesis_SampleSize] = None
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
    certainty: list[EffectEvidenceSynthesis_Certainty] = []
    reviewer: list[ContactDetail] = []
    exposure: Reference
    resultsByExposure: list[EffectEvidenceSynthesis_ResultsByExposure] = []
    version: Optional[str] = None
    relatedArtifact: list[RelatedArtifact] = []
    contact: list[ContactDetail] = []
    effectivePeriod: Optional[Period] = None
