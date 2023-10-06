from typing import Optional

from base import Reference
from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import Annotation
from base import CodeableConcept
from base import BackboneElement
from base import Identifier
from base import Identifier
from base import BackboneElement
from base import Reference
from base import DomainResource


class Specimen(DomainResource):
	request: list[Reference] = []
	receivedTime: Optional[str] = None
	processing: list[BackboneElement] = []
	parent: list[Reference] = []
	type: Optional[CodeableConcept] = None
	note: list[Annotation] = []
	status: Optional[str] = None
	condition: list[CodeableConcept] = []
	container: list[BackboneElement] = []
	identifier: list[Identifier] = []
	accessionIdentifier: Optional[Identifier] = None
	collection: Optional[BackboneElement] = None
	subject: Optional[Reference] = None

