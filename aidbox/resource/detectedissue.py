from pydantic import *
from typing import Optional, List
from ..base import *

class DetectedIssue_Evidence(BackboneElement):
	code: Optional[List[CodeableConcept]] = None
	detail: Optional[List[Reference]] = None

class DetectedIssue_Mitigation(BackboneElement):
	action: CodeableConcept
	date: Optional[str] = None
	author: Optional[Reference] = None

class DetectedIssue(DomainResource):
	patient: Optional[Reference] = None
	evidence: Optional[List[DetectedIssue_Evidence]] = None
	mitigation: Optional[List[DetectedIssue_Mitigation]] = None
	author: Optional[Reference] = None
	identifiedDateTime: Optional[str] = None
	reference: Optional[str] = None
	status: str
	severity: Optional[str] = None
	code: Optional[CodeableConcept] = None
	identifier: Optional[List[Identifier]] = None
	implicated: Optional[List[Reference]] = None
	identifiedPeriod: Optional[Period] = None
	detail: Optional[str] = None