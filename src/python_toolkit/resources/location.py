from typing import Optional
from base import *

class Location_HoursOfOperation(BackboneElement):
	allDay: Optional[bool] = None
	closingTime: Optional[str] = None
	daysOfWeek: list[str] = []
	openingTime: Optional[str] = None

class Location_Position(BackboneElement):
	altitude: Optional[str] = None
	latitude: str
	longitude: str

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
	hoursOfOperation: list[Location_HoursOfOperation] = []
	availabilityExceptions: Optional[str] = None
	position: Optional[Location_Position] = None
	telecom: list[ContactPoint] = []
	operationalStatus: Optional[Coding] = None
	partOf: Optional[Reference] = None
	physicalType: Optional[CodeableConcept] = None
	endpoint: list[Reference] = []

