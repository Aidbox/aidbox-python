from pydantic import *
from typing import Optional, List
from ..base import *

class ResearchSubject(DomainResource):
	identifier: Optional[List[Identifier]] = None
	status: str
	period: Optional[Period] = None
	study: Reference
	individual: Reference
	assignedArm: Optional[str] = None
	actualArm: Optional[str] = None
	consent: Optional[Reference] = None