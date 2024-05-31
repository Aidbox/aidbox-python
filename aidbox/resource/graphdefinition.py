from pydantic import *
from typing import Optional, List
from ..base import *

class GraphDefinition_Link_Target_Compartment(BackboneElement):
	use: str
	code: str
	rule: str
	expression: Optional[str] = None
	description: Optional[str] = None

class GraphDefinition_Link_Target(BackboneElement):
	type: str
	params: Optional[str] = None
	profile: Optional[str] = None
	compartment: Optional[List[GraphDefinition_Link_Target_Compartment]] = None
	link: Optional[List[str]] = None

class GraphDefinition_Link(BackboneElement):
	path: Optional[str] = None
	sliceName: Optional[str] = None
	min: Optional[int] = None
	max: Optional[str] = None
	description: Optional[str] = None
	target: Optional[List[GraphDefinition_Link_Target]] = None

class GraphDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	name: str
	start: str
	useContext: Optional[List[UsageContext]] = None
	experimental: Optional[bool] = None
	status: str
	link: Optional[List[GraphDefinition_Link]] = None
	url: Optional[str] = None
	version: Optional[str] = None
	contact: Optional[List[ContactDetail]] = None
	profile: Optional[str] = None