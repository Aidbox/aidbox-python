from typing import Optional
from base import *

class ResearchSubject(DomainResource):
	actualArm: Optional[str] = None
	assignedArm: Optional[str] = None
	consent: Optional[Reference] = None
	identifier: list[Identifier] = []
	individual: Reference
	period: Optional[Period] = None
	status: str
	study: Reference

