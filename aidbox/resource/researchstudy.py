from pydantic import *
from typing import Optional, List
from ..base import *

class ResearchStudy_Arm(BackboneElement):
	name: str
	type: Optional[CodeableConcept] = None
	description: Optional[str] = None

class ResearchStudy_Objective(BackboneElement):
	name: Optional[str] = None
	type: Optional[CodeableConcept] = None

class ResearchStudy(DomainResource):
	description: Optional[str] = None
	category: Optional[List[CodeableConcept]] = None
	enrollment: Optional[List[Reference]] = None
	arm: Optional[List[ResearchStudy_Arm]] = None
	site: Optional[List[Reference]] = None
	protocol: Optional[List[Reference]] = None
	principalInvestigator: Optional[Reference] = None
	phase: Optional[CodeableConcept] = None
	reasonStopped: Optional[CodeableConcept] = None
	title: Optional[str] = None
	note: Optional[List[Annotation]] = None
	keyword: Optional[List[CodeableConcept]] = None
	status: str
	condition: Optional[List[CodeableConcept]] = None
	identifier: Optional[List[Identifier]] = None
	primaryPurposeType: Optional[CodeableConcept] = None
	focus: Optional[List[CodeableConcept]] = None
	objective: Optional[List[ResearchStudy_Objective]] = None
	period: Optional[Period] = None
	partOf: Optional[List[Reference]] = None
	relatedArtifact: Optional[List[RelatedArtifact]] = None
	location: Optional[List[CodeableConcept]] = None
	contact: Optional[List[ContactDetail]] = None
	sponsor: Optional[Reference] = None