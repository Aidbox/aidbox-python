from typing import Optional

from base import Reference
from base import CodeableConcept
from base import Annotation
from base import Reference
from base import Identifier
from base import CodeableConcept
from base import Identifier
from base import BackboneElement
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import DomainResource


class RequestGroup(DomainResource):
	instantiatesCanonical: list[str] = []
	instantiatesUri: list[str] = []
	encounter: Optional[Reference] = None
	reasonCode: list[CodeableConcept] = []
	authoredOn: Optional[str] = None
	note: list[Annotation] = []
	author: Optional[Reference] = None
	priority: Optional[str] = None
	status: str
	groupIdentifier: Optional[Identifier] = None
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	intent: str
	action: list[BackboneElement] = []
	replaces: list[Reference] = []
	basedOn: list[Reference] = []
	subject: Optional[Reference] = None
	reasonReference: list[Reference] = []

