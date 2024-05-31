from pydantic import *
from typing import Optional, List
from ..base import *

class EnrollmentRequest(DomainResource):
	identifier: Optional[List[Identifier]] = None
	status: Optional[str] = None
	created: Optional[str] = None
	insurer: Optional[Reference] = None
	provider: Optional[Reference] = None
	candidate: Optional[Reference] = None
	coverage: Optional[Reference] = None