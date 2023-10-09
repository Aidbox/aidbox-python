from typing import Optional
from base import *

class MessageDefinition_AllowedResponse(BackboneElement):
	message: str
	situation: Optional[str] = None

class MessageDefinition_Focus(BackboneElement):
	code: str
	max: Optional[str] = None
	min: str
	profile: Optional[str] = None

class MessageDefinition(DomainResource):
	description: Optional[str] = None
	category: Optional[str] = None
	date: str
	publisher: Optional[str] = None
	parent: list[str] = []
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	status: str
	allowedResponse: list[MessageDefinition_AllowedResponse] = []
	graph: list[str] = []
	url: Optional[str] = None
	identifier: list[Identifier] = []
	focus: list[MessageDefinition_Focus] = []
	replaces: list[str] = []
	responseRequired: Optional[str] = None
	base: Optional[str] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []
	eventUri: Optional[str] = None
	eventCoding: Optional[Coding] = None

