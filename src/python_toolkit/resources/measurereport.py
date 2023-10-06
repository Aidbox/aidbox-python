from typing import Optional

from base import Reference
from base import BackboneElement
from base import Reference
from base import Identifier
from base import Period
from base import CodeableConcept
from base import Reference
from base import DomainResource


class MeasureReport(DomainResource):
	evaluatedResource: list[Reference] = []
	date: Optional[str] = None
	group: list[BackboneElement] = []
	type: str
	measure: str
	reporter: Optional[Reference] = None
	status: str
	identifier: list[Identifier] = []
	period: Period
	improvementNotation: Optional[CodeableConcept] = None
	subject: Optional[Reference] = None

