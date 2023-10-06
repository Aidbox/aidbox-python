from typing import Optional

from base import CodeableConcept
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import Annotation
from base import Reference
from base import BackboneElement
from base import Reference
from base import Identifier
from base import Reference
from base import Period
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import DomainResource


class CarePlan(DomainResource):
	description: Optional[str] = None
	category: list[CodeableConcept] = []
	addresses: list[Reference] = []
	instantiatesCanonical: list[str] = []
	instantiatesUri: list[str] = []
	supportingInfo: list[Reference] = []
	encounter: Optional[Reference] = None
	goal: list[Reference] = []
	created: Optional[str] = None
	title: Optional[str] = None
	note: list[Annotation] = []
	author: Optional[Reference] = None
	activity: list[BackboneElement] = []
	contributor: list[Reference] = []
	status: str
	identifier: list[Identifier] = []
	intent: str
	replaces: list[Reference] = []
	period: Optional[Period] = None
	basedOn: list[Reference] = []
	partOf: list[Reference] = []
	subject: Reference
	careTeam: list[Reference] = []

