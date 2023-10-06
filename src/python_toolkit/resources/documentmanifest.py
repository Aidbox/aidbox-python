from typing import Optional

from base import Reference
from base import Reference
from base import CodeableConcept
from base import BackboneElement
from base import Reference
from base import Identifier
from base import Identifier
from base import Reference
from base import DomainResource


class DocumentManifest(DomainResource):
	description: Optional[str] = None
	content: list[Reference]
	recipient: list[Reference] = []
	type: Optional[CodeableConcept] = None
	created: Optional[str] = None
	related: list[BackboneElement] = []
	source: Optional[str] = None
	author: list[Reference] = []
	masterIdentifier: Optional[Identifier] = None
	status: str
	identifier: list[Identifier] = []
	subject: Optional[Reference] = None

