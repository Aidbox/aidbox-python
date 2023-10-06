from typing import Optional

from base import Reference
from base import CodeableConcept
from base import Reference
from base import Annotation
from base import CodeableConcept
from base import CodeableConcept
from base import Identifier
from base import BackboneElement
from base import Reference
from base import DomainResource


class List(DomainResource):
	date: Optional[str] = None
	encounter: Optional[Reference] = None
	orderedBy: Optional[CodeableConcept] = None
	mode: str
	source: Optional[Reference] = None
	title: Optional[str] = None
	note: list[Annotation] = []
	emptyReason: Optional[CodeableConcept] = None
	status: str
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	entry: list[BackboneElement] = []
	subject: Optional[Reference] = None

