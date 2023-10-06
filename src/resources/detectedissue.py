from typing import Optional

from base import Reference
from base import BackboneElement
from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import Identifier
from base import Reference
from base import Period
from base import DomainResource


class DetectedIssue(DomainResource):
	patient: Optional[Reference] = None
	evidence: list[BackboneElement] = []
	mitigation: list[BackboneElement] = []
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

