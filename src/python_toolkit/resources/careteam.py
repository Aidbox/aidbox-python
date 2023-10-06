from typing import Optional

from base import CodeableConcept
from base import Reference
from base import Reference
from base import CodeableConcept
from base import BackboneElement
from base import Annotation
from base import Identifier
from base import ContactPoint
from base import Period
from base import Reference
from base import Reference
from base import DomainResource


class CareTeam(DomainResource):
	category: list[CodeableConcept] = []
	managingOrganization: list[Reference] = []
	encounter: Optional[Reference] = None
	name: Optional[str] = None
	reasonCode: list[CodeableConcept] = []
	participant: list[BackboneElement] = []
	note: list[Annotation] = []
	status: Optional[str] = None
	identifier: list[Identifier] = []
	telecom: list[ContactPoint] = []
	period: Optional[Period] = None
	subject: Optional[Reference] = None
	reasonReference: list[Reference] = []

