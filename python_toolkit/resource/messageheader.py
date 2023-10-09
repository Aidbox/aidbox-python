from typing import Optional
from ..base import *

class MessageHeader_Response(BackboneElement):
	code: str
	details: Optional[Reference] = None
	identifier: str

class MessageHeader_Source(BackboneElement):
	contact: Optional[ContactPoint] = None
	endpoint: str
	name: Optional[str] = None
	software: Optional[str] = None
	version: Optional[str] = None

class MessageHeader_Destination(BackboneElement):
	endpoint: str
	name: Optional[str] = None
	receiver: Optional[Reference] = None
	target: Optional[Reference] = None

class MessageHeader(DomainResource):
	response: Optional[MessageHeader_Response] = None
	definition: Optional[str] = None
	enterer: Optional[Reference] = None
	source: MessageHeader_Source
	author: Optional[Reference] = None
	reason: Optional[CodeableConcept] = None
	responsible: Optional[Reference] = None
	sender: Optional[Reference] = None
	focus: list[Reference] = []
	eventUri: Optional[str] = None
	destination: list[MessageHeader_Destination] = []
	eventCoding: Optional[Coding] = None

