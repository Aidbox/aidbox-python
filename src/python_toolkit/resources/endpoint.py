from typing import Optional

from base import Coding
from base import Reference
from base import CodeableConcept
from base import Identifier
from base import Period
from base import ContactPoint
from base import DomainResource


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

