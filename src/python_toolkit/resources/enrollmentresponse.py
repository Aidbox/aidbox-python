from typing import Optional

from base import Identifier
from base import Reference
from base import Reference
from base import Reference
from base import DomainResource


class EnrollmentResponse(DomainResource):
	created: Optional[str] = None
	disposition: Optional[str] = None
	identifier: list[Identifier] = []
	organization: Optional[Reference] = None
	outcome: Optional[str] = None
	request: Optional[Reference] = None
	requestProvider: Optional[Reference] = None
	status: Optional[str] = None

