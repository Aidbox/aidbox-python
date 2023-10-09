from typing import Optional
from ..base import *

class NamingSystem_UniqueId(BackboneElement):
	comment: Optional[str] = None
	period: Optional[Period] = None
	preferred: Optional[bool] = None
	type: str
	value: str

class NamingSystem(DomainResource):
	description: Optional[str] = None
	date: str
	publisher: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	name: str
	useContext: list[UsageContext] = []
	type: Optional[CodeableConcept] = None
	responsible: Optional[str] = None
	usage: Optional[str] = None
	status: str
	kind: str
	uniqueId: list[NamingSystem_UniqueId]
	contact: list[ContactDetail] = []

