from typing import Optional
from ..base import *

class DetectedIssue_Evidence(BackboneElement):
	code: list[CodeableConcept] = []
	detail: list[Reference] = []

class DetectedIssue_Mitigation(BackboneElement):
	action: CodeableConcept
	author: Optional[Reference] = None
	date: Optional[str] = None

class DetectedIssue(DomainResource):
	patient: Optional[Reference] = None
	evidence: list[DetectedIssue_Evidence] = []
	mitigation: list[DetectedIssue_Mitigation] = []
	author: Optional[Reference] = None
	identifiedDateTime: Optional[str] = None
	reference: Optional[str] = None
	status: str
	severity: Optional[str] = None
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	implicated: list[Reference] = []
	identifiedPeriod: Optional[Period] = None
	detail: Optional[str] = None

