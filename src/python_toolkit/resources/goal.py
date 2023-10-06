from typing import Optional

from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import Reference
from base import CodeableConcept
from base import Annotation
from base import CodeableConcept
from base import CodeableConcept
from base import CodeableConcept
from base import Identifier
from base import BackboneElement
from base import Reference
from base import Reference
from base import DomainResource


class Goal(DomainResource):
	description: CodeableConcept
	category: list[CodeableConcept] = []
	addresses: list[Reference] = []
	expressedBy: Optional[Reference] = None
	startDate: Optional[str] = None
	achievementStatus: Optional[CodeableConcept] = None
	statusReason: Optional[str] = None
	note: list[Annotation] = []
	startCodeableConcept: Optional[CodeableConcept] = None
	priority: Optional[CodeableConcept] = None
	outcomeCode: list[CodeableConcept] = []
	identifier: list[Identifier] = []
	statusDate: Optional[str] = None
	target: list[BackboneElement] = []
	outcomeReference: list[Reference] = []
	subject: Reference
	lifecycleStatus: str

