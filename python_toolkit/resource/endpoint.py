from typing import Optional
from ..base import *

class Endpoint(DomainResource):
	connectionType: Coding
	address: str
	managingOrganization: Optional[Reference] = None
	name: Optional[str] = None
	payloadMimeType: list[str] = []
	payloadType: list[CodeableConcept]
	header: list[str] = []
	status: str
	identifier: list[Identifier] = []
	period: Optional[Period] = None
	contact: list[ContactPoint] = []

