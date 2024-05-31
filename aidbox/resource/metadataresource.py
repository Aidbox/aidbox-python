from pydantic import *
from typing import Optional, List
from ..base import *

class MetadataResource(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	name: Optional[str] = None
	useContext: Optional[List[UsageContext]] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	status: str
	url: Optional[str] = None
	version: Optional[str] = None
	contact: Optional[List[ContactDetail]] = None