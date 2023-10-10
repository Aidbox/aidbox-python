from typing import Optional
from ..base import *

class EnrollmentResponse(DomainResource):
	created: Optional[str] = None
	disposition: Optional[str] = None
	identifier: list[Identifier] = []
	organization: Optional[Reference] = None
	outcome: Optional[str] = None
	request: Optional[Reference] = None
	requestProvider: Optional[Reference] = None
	status: Optional[str] = None

