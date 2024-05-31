from pydantic import *
from typing import Optional, List
from ..base import *

class MessageHeader_Response(BackboneElement):
	identifier: str
	code: str
	details: Optional[Reference] = None

class MessageHeader_Source(BackboneElement):
	name: Optional[str] = None
	software: Optional[str] = None
	version: Optional[str] = None
	contact: Optional[ContactPoint] = None
	endpoint: str

class MessageHeader_Destination(BackboneElement):
	name: Optional[str] = None
	target: Optional[Reference] = None
	endpoint: str
	receiver: Optional[Reference] = None

class MessageHeader(DomainResource):
	response: Optional[MessageHeader_Response] = None
	definition: Optional[str] = None
	enterer: Optional[Reference] = None
	source: MessageHeader_Source
	author: Optional[Reference] = None
	reason: Optional[CodeableConcept] = None
	responsible: Optional[Reference] = None
	sender: Optional[Reference] = None
	focus: Optional[List[Reference]] = None
	eventUri: Optional[str] = None
	destination: Optional[List[MessageHeader_Destination]] = None
	eventCoding: Optional[Coding] = None