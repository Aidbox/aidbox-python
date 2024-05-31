from pydantic import *
from typing import Optional, List
from ..base import *

class Endpoint(DomainResource):
	connectionType: Coding
	address: str
	managingOrganization: Optional[Reference] = None
	name: Optional[str] = None
	payloadMimeType: Optional[List[str]] = None
	payloadType: List[CodeableConcept]
	header: Optional[List[str]] = None
	status: str
	identifier: Optional[List[Identifier]] = None
	period: Optional[Period] = None
	contact: Optional[List[ContactPoint]] = None