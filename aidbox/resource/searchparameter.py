from pydantic import *
from typing import Optional, List
from ..base import *

class SearchParameter_Component(BackboneElement):
	definition: str
	expression: str

class SearchParameter(DomainResource):
	description: str
	date: Optional[str] = None
	expression: Optional[str] = None
	modifier: Optional[List[str]] = None
	publisher: Optional[str] = None
	multipleAnd: Optional[bool] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	derivedFrom: Optional[str] = None
	purpose: Optional[str] = None
	multipleOr: Optional[bool] = None
	name: str
	useContext: Optional[List[UsageContext]] = None
	xpath: Optional[str] = None
	xpathUsage: Optional[str] = None
	type: str
	experimental: Optional[bool] = None
	component: Optional[List[SearchParameter_Component]] = None
	status: str
	chain: Optional[List[str]] = None
	url: str
	code: str
	comparator: Optional[List[str]] = None
	target: Optional[List[str]] = None
	base: List[str]
	version: Optional[str] = None
	contact: Optional[List[ContactDetail]] = None