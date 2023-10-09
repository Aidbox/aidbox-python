from typing import Optional
from ..base import *

class GraphDefinition_Link_Target_Compartment(BackboneElement):
	code: str
	description: Optional[str] = None
	expression: Optional[str] = None
	rule: str
	use: str

class GraphDefinition_Link_Target(BackboneElement):
	compartment: list[GraphDefinition_Link_Target_Compartment] = []
	link: list[str] = []
	params: Optional[str] = None
	profile: Optional[str] = None
	type: str

class GraphDefinition_Link(BackboneElement):
	description: Optional[str] = None
	max: Optional[str] = None
	min: Optional[int] = None
	path: Optional[str] = None
	sliceName: Optional[str] = None
	target: list[GraphDefinition_Link_Target] = []

class GraphDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: str
	start: str
	useContext: list[UsageContext] = []
	experimental: Optional[bool] = None
	status: str
	link: list[GraphDefinition_Link] = []
	url: Optional[str] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []
	profile: Optional[str] = None

