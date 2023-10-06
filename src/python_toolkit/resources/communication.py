from typing import Optional

from base import CodeableConcept
from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import CodeableConcept
from base import Annotation
from base import Reference
from base import Identifier
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import DomainResource


class Communication(DomainResource):
	category: list[CodeableConcept] = []
	received: Optional[str] = None
	instantiatesCanonical: list[str] = []
	payload: list[BackboneElement] = []
	instantiatesUri: list[str] = []
	encounter: Optional[Reference] = None
	medium: list[CodeableConcept] = []
	recipient: list[Reference] = []
	reasonCode: list[CodeableConcept] = []
	statusReason: Optional[CodeableConcept] = None
	topic: Optional[CodeableConcept] = None
	sent: Optional[str] = None
	note: list[Annotation] = []
	priority: Optional[str] = None
	status: str
	sender: Optional[Reference] = None
	identifier: list[Identifier] = []
	inResponseTo: list[Reference] = []
	basedOn: list[Reference] = []
	partOf: list[Reference] = []
	subject: Optional[Reference] = None
	about: list[Reference] = []
	reasonReference: list[Reference] = []

