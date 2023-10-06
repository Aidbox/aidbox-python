from typing import Optional

from base import BackboneElement
from base import CodeableConcept
from base import Period
from base import Reference
from base import Reference
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import CodeableConcept
from base import Annotation
from base import Reference
from base import Reference
from base import Identifier
from base import CodeableConcept
from base import Identifier
from base import Reference
from base import BackboneElement
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import DomainResource


class Task(DomainResource):
	restriction: Optional[BackboneElement] = None
	description: Optional[str] = None
	performerType: list[CodeableConcept] = []
	executionPeriod: Optional[Period] = None
	insurance: list[Reference] = []
	instantiatesCanonical: Optional[str] = None
	instantiatesUri: Optional[str] = None
	relevantHistory: list[Reference] = []
	encounter: Optional[Reference] = None
	reasonCode: Optional[CodeableConcept] = None
	statusReason: Optional[CodeableConcept] = None
	authoredOn: Optional[str] = None
	output: list[BackboneElement] = []
	businessStatus: Optional[CodeableConcept] = None
	note: list[Annotation] = []
	for_: Optional[Reference] = None
	requester: Optional[Reference] = None
	lastModified: Optional[str] = None
	priority: Optional[str] = None
	status: str
	groupIdentifier: Optional[Identifier] = None
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	intent: str
	focus: Optional[Reference] = None
	input: list[BackboneElement] = []
	basedOn: list[Reference] = []
	partOf: list[Reference] = []
	location: Optional[Reference] = None
	owner: Optional[Reference] = None
	reasonReference: Optional[Reference] = None

