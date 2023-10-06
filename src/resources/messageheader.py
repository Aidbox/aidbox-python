from typing import Optional

from base import BackboneElement
from base import Reference
from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import Reference
from base import Reference
from base import Reference
from base import BackboneElement
from base import Coding
from base import DomainResource


class MessageHeader(DomainResource):
	response: Optional[BackboneElement] = None
	definition: Optional[str] = None
	enterer: Optional[Reference] = None
	source: BackboneElement
	author: Optional[Reference] = None
	reason: Optional[CodeableConcept] = None
	responsible: Optional[Reference] = None
	sender: Optional[Reference] = None
	focus: list[Reference] = []
	eventUri: Optional[str] = None
	destination: list[BackboneElement] = []
	eventCoding: Optional[Coding] = None

