from pydantic import *
from typing import Optional, List
from ..base import *

class CompartmentDefinition_Resource(BackboneElement):
	code: str
	param: Optional[List[str]] = None
	documentation: Optional[str] = None

class CompartmentDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	purpose: Optional[str] = None
	name: str
	useContext: Optional[List[UsageContext]] = None
	experimental: Optional[bool] = None
	search: bool
	status: str
	resource: Optional[List[CompartmentDefinition_Resource]] = None
	url: str
	code: str
	version: Optional[str] = None
	contact: Optional[List[ContactDetail]] = None