from pydantic import *
from typing import Optional, List, Literal
from ..base import *

class Location_HoursOfOperation(BackboneElement):
	daysOfWeek: Optional[List[str]] = None
	allDay: Optional[bool] = None
	openingTime: Optional[str] = None
	closingTime: Optional[str] = None

class Location_Position(BackboneElement):
	longitude: float
	latitude: float
	altitude: Optional[float] = None

class UsCoreLocation(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/core/StructureDefinition/us-core-location"])
	description: Optional[str] = None
	address: Optional[Address] = None
	managingOrganization: Optional[Reference] = None
	name: str
	mode: Optional[str] = None
	type: Optional[List[CodeableConcept]] = None
	alias: Optional[List[str]] = None
	status: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	hoursOfOperation: Optional[List[Location_HoursOfOperation]] = None
	availabilityExceptions: Optional[str] = None
	position: Optional[Location_Position] = None
	telecom: Optional[List[ContactPoint]] = None
	operationalStatus: Optional[Coding] = None
	partOf: Optional[Reference] = None
	physicalType: Optional[CodeableConcept] = None
	endpoint: Optional[List[Reference]] = None