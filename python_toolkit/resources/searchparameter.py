from typing import Optional
from base import *

class SearchParameter_Component(BackboneElement):
	definition: str
	expression: str

class SearchParameter(DomainResource):
	description: str
	date: Optional[str] = None
	expression: Optional[str] = None
	modifier: list[str] = []
	publisher: Optional[str] = None
	multipleAnd: Optional[bool] = None
	jurisdiction: list[CodeableConcept] = []
	derivedFrom: Optional[str] = None
	purpose: Optional[str] = None
	multipleOr: Optional[bool] = None
	name: str
	useContext: list[UsageContext] = []
	xpath: Optional[str] = None
	xpathUsage: Optional[str] = None
	type: str
	experimental: Optional[bool] = None
	component: list[SearchParameter_Component] = []
	status: str
	chain: list[str] = []
	url: str
	code: str
	comparator: list[str] = []
	target: list[str] = []
	base: list[str]
	version: Optional[str] = None
	contact: list[ContactDetail] = []

