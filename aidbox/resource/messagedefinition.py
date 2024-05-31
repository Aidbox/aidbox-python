from pydantic import *
from typing import Optional, List
from ..base import *

class MessageDefinition_AllowedResponse(BackboneElement):
	message: str
	situation: Optional[str] = None

class MessageDefinition_Focus(BackboneElement):
	code: str
	profile: Optional[str] = None
	min: NonNegativeInt
	max: Optional[str] = None

class MessageDefinition(DomainResource):
	description: Optional[str] = None
	category: Optional[str] = None
	date: str
	publisher: Optional[str] = None
	parent: Optional[List[str]] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	name: Optional[str] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	status: str
	allowedResponse: Optional[List[MessageDefinition_AllowedResponse]] = None
	graph: Optional[List[str]] = None
	url: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	focus: Optional[List[MessageDefinition_Focus]] = None
	replaces: Optional[List[str]] = None
	responseRequired: Optional[str] = None
	base: Optional[str] = None
	version: Optional[str] = None
	contact: Optional[List[ContactDetail]] = None
	eventUri: Optional[str] = None
	eventCoding: Optional[Coding] = None