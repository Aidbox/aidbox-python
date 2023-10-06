from typing import Optional

from base import Address
from base import Reference
from base import CodeableConcept
from base import Identifier
from base import BackboneElement
from base import BackboneElement
from base import ContactPoint
from base import Coding
from base import Reference
from base import CodeableConcept
from base import Reference
from base import DomainResource


class Location(DomainResource):
	description: Optional[str] = None
	address: Optional[Address] = None
	managingOrganization: Optional[Reference] = None
	name: Optional[str] = None
	mode: Optional[str] = None
	type: list[CodeableConcept] = []
	alias: list[str] = []
	status: Optional[str] = None
	identifier: list[Identifier] = []
	hoursOfOperation: list[BackboneElement] = []
	availabilityExceptions: Optional[str] = None
	position: Optional[BackboneElement] = None
	telecom: list[ContactPoint] = []
	operationalStatus: Optional[Coding] = None
	partOf: Optional[Reference] = None
	physicalType: Optional[CodeableConcept] = None
	endpoint: list[Reference] = []

