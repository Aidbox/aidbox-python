from typing import Optional

from base import CodeableConcept
from base import Reference
from base import BackboneElement
from base import BackboneElement
from base import CodeableConcept
from base import Reference
from base import BackboneElement
from base import Reference
from base import Identifier
from base import BackboneElement
from base import Reference
from base import DomainResource


class Composition(DomainResource):
	category: list[CodeableConcept] = []
	date: str
	encounter: Optional[Reference] = None
	section: list[BackboneElement] = []
	attester: list[BackboneElement] = []
	type: CodeableConcept
	title: str
	author: list[Reference]
	event: list[BackboneElement] = []
	custodian: Optional[Reference] = None
	status: str
	identifier: Optional[Identifier] = None
	relatesTo: list[BackboneElement] = []
	subject: Optional[Reference] = None
	confidentiality: Optional[str] = None

