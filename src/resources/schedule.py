from typing import Optional

from base import Reference
from base import Identifier
from base import Period
from base import CodeableConcept
from base import CodeableConcept
from base import CodeableConcept
from base import DomainResource


class Schedule(DomainResource):
	active: Optional[bool] = None
	actor: list[Reference]
	comment: Optional[str] = None
	identifier: list[Identifier] = []
	planningHorizon: Optional[Period] = None
	serviceCategory: list[CodeableConcept] = []
	serviceType: list[CodeableConcept] = []
	specialty: list[CodeableConcept] = []

