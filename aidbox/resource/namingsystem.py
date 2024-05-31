from pydantic import *
from typing import Optional, List
from ..base import *

class NamingSystem_UniqueId(BackboneElement):
	type: str
	value: str
	preferred: Optional[bool] = None
	comment: Optional[str] = None
	period: Optional[Period] = None

class NamingSystem(DomainResource):
	description: Optional[str] = None
	date: str
	publisher: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	name: str
	useContext: Optional[List[UsageContext]] = None
	type: Optional[CodeableConcept] = None
	responsible: Optional[str] = None
	usage: Optional[str] = None
	status: str
	kind: str
	uniqueId: List[NamingSystem_UniqueId]
	contact: Optional[List[ContactDetail]] = None