from typing import Optional

from base import CodeableConcept
from base import UsageContext
from base import CodeableConcept
from base import BackboneElement
from base import ContactDetail
from base import DomainResource


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
	uniqueId: list[BackboneElement]
	contact: list[ContactDetail] = []

