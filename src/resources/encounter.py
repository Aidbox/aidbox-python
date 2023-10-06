from typing import Optional

from base import Reference
from base import BackboneElement
from base import Reference
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import CodeableConcept
from base import Reference
from base import BackboneElement
from base import CodeableConcept
from base import Coding
from base import Identifier
from base import BackboneElement
from base import Period
from base import Reference
from base import Reference
from base import BackboneElement
from base import Reference
from base import BackboneElement
from base import Reference
from base import DomainResource


class Encounter(DomainResource):
	appointment: list[Reference] = []
	diagnosis: list[BackboneElement] = []
	serviceProvider: Optional[Reference] = None
	episodeOfCare: list[Reference] = []
	reasonCode: list[CodeableConcept] = []
	type: list[CodeableConcept] = []
	participant: list[BackboneElement] = []
	serviceType: Optional[CodeableConcept] = None
	account: list[Reference] = []
	classHistory: list[BackboneElement] = []
	priority: Optional[CodeableConcept] = None
	status: str
	class_: Coding
	length: Optional[str] = None
	identifier: list[Identifier] = []
	hospitalization: Optional[BackboneElement] = None
	period: Optional[Period] = None
	basedOn: list[Reference] = []
	partOf: Optional[Reference] = None
	location: list[BackboneElement] = []
	subject: Optional[Reference] = None
	statusHistory: list[BackboneElement] = []
	reasonReference: list[Reference] = []

