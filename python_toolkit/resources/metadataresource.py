from typing import Optional
from base import *

class MetadataResource(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	experimental: Optional[bool] = None
	title: Optional[str] = None
	status: str
	url: Optional[str] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []

