from typing import Optional

from base import CodeableConcept
from base import BackboneElement
from base import CodeableConcept
from base import Reference
from base import Identifier
from base import Reference
from base import Identifier
from base import BackboneElement
from base import BackboneElement
from base import CodeableConcept
from base import Reference
from base import Reference
from base import DomainResource


class DocumentReference(DomainResource):
	description: Optional[str] = None
	category: list[CodeableConcept] = []
	date: Optional[str] = None
	docStatus: Optional[str] = None
	content: list[BackboneElement]
	type: Optional[CodeableConcept] = None
	author: list[Reference] = []
	masterIdentifier: Optional[Identifier] = None
	custodian: Optional[Reference] = None
	status: str
	identifier: list[Identifier] = []
	relatesTo: list[BackboneElement] = []
	context: Optional[BackboneElement] = None
	securityLabel: list[CodeableConcept] = []
	subject: Optional[Reference] = None
	authenticator: Optional[Reference] = None

