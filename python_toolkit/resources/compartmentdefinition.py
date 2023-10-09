from typing import Optional
from base import *

class CompartmentDefinition_Resource(BackboneElement):
	code: str
	documentation: Optional[str] = None
	param: list[str] = []

class CompartmentDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	purpose: Optional[str] = None
	name: str
	useContext: list[UsageContext] = []
	experimental: Optional[bool] = None
	search: bool
	status: str
	resource: list[CompartmentDefinition_Resource] = []
	url: str
	code: str
	version: Optional[str] = None
	contact: list[ContactDetail] = []

