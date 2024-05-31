from pydantic import *
from typing import Optional, List
from ..base import *

class EnrollmentResponse(DomainResource):
	identifier: Optional[List[Identifier]] = None
	status: Optional[str] = None
	request: Optional[Reference] = None
	outcome: Optional[str] = None
	disposition: Optional[str] = None
	created: Optional[str] = None
	organization: Optional[Reference] = None
	requestProvider: Optional[Reference] = None