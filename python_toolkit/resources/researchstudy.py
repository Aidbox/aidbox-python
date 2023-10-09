from typing import Optional
from base import *

class ResearchStudy_Arm(BackboneElement):
	description: Optional[str] = None
	name: str
	type: Optional[CodeableConcept] = None

class ResearchStudy_Objective(BackboneElement):
	name: Optional[str] = None
	type: Optional[CodeableConcept] = None

class ResearchStudy(DomainResource):
	description: Optional[str] = None
	category: list[CodeableConcept] = []
	enrollment: list[Reference] = []
	arm: list[ResearchStudy_Arm] = []
	site: list[Reference] = []
	protocol: list[Reference] = []
	principalInvestigator: Optional[Reference] = None
	phase: Optional[CodeableConcept] = None
	reasonStopped: Optional[CodeableConcept] = None
	title: Optional[str] = None
	note: list[Annotation] = []
	keyword: list[CodeableConcept] = []
	status: str
	condition: list[CodeableConcept] = []
	identifier: list[Identifier] = []
	primaryPurposeType: Optional[CodeableConcept] = None
	focus: list[CodeableConcept] = []
	objective: list[ResearchStudy_Objective] = []
	period: Optional[Period] = None
	partOf: list[Reference] = []
	relatedArtifact: list[RelatedArtifact] = []
	location: list[CodeableConcept] = []
	contact: list[ContactDetail] = []
	sponsor: Optional[Reference] = None

