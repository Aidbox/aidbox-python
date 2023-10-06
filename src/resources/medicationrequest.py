from typing import Optional

from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import Reference
from base import BackboneElement
from base import Reference
from base import Reference
from base import BackboneElement
from base import CodeableConcept
from base import CodeableConcept
from base import CodeableConcept
from base import Annotation
from base import Reference
from base import Reference
from base import Reference
from base import Identifier
from base import Reference
from base import Identifier
from base import Reference
from base import Reference
from base import Reference
from base import CodeableConcept
from base import Reference
from base import Reference
from base import Reference
from base import DomainResource


class MedicationRequest(DomainResource):
	performerType: Optional[CodeableConcept] = None
	category: list[CodeableConcept] = []
	insurance: list[Reference] = []
	instantiatesCanonical: list[str] = []
	eventHistory: list[Reference] = []
	instantiatesUri: list[str] = []
	substitution: Optional[BackboneElement] = None
	detectedIssue: list[Reference] = []
	encounter: Optional[Reference] = None
	dispenseRequest: Optional[BackboneElement] = None
	reasonCode: list[CodeableConcept] = []
	medicationCodeableConcept: Optional[CodeableConcept] = None
	statusReason: Optional[CodeableConcept] = None
	authoredOn: Optional[str] = None
	note: list[Annotation] = []
	requester: Optional[Reference] = None
	supportingInformation: list[Reference] = []
	reportedReference: Optional[Reference] = None
	priority: Optional[str] = None
	status: str
	dosageInstruction: list[str] = []
	groupIdentifier: Optional[Identifier] = None
	recorder: Optional[Reference] = None
	reportedBoolean: Optional[bool] = None
	identifier: list[Identifier] = []
	doNotPerform: Optional[bool] = None
	intent: str
	basedOn: list[Reference] = []
	priorPrescription: Optional[Reference] = None
	medicationReference: Optional[Reference] = None
	courseOfTherapyType: Optional[CodeableConcept] = None
	subject: Reference
	performer: Optional[Reference] = None
	reasonReference: list[Reference] = []

