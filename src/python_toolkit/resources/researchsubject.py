from typing import Optional

from base import Reference
from base import Identifier
from base import Reference
from base import Period
from base import Reference
from base import DomainResource


class ResearchSubject(DomainResource):
	actualArm: Optional[str] = None
	assignedArm: Optional[str] = None
	consent: Optional[Reference] = None
	identifier: list[Identifier] = []
	individual: Reference
	period: Optional[Period] = None
	status: str
	study: Reference

