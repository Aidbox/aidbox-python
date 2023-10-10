from typing import Optional
from ..base import *

class EnrollmentRequest(DomainResource):
	candidate: Optional[Reference] = None
	coverage: Optional[Reference] = None
	created: Optional[str] = None
	identifier: list[Identifier] = []
	insurer: Optional[Reference] = None
	provider: Optional[Reference] = None
	status: Optional[str] = None

