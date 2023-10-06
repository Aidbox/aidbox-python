from typing import Optional

from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import CodeableConcept
from base import Annotation
from base import Identifier
from base import Reference
from base import Reference
from base import Period
from base import Ratio
from base import CodeableConcept
from base import Identifier
from base import CodeableConcept
from base import Range
from base import Quantity
from base import Reference
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import Reference
from base import Reference
from base import DomainResource


class ServiceRequest(DomainResource):
	performerType: Optional[CodeableConcept] = None
	category: list[CodeableConcept] = []
	insurance: list[Reference] = []
	instantiatesCanonical: list[str] = []
	instantiatesUri: list[str] = []
	relevantHistory: list[Reference] = []
	supportingInfo: list[Reference] = []
	encounter: Optional[Reference] = None
	patientInstruction: Optional[str] = None
	specimen: list[Reference] = []
	reasonCode: list[CodeableConcept] = []
	authoredOn: Optional[str] = None
	occurrenceTiming: Optional[str] = None
	note: list[Annotation] = []
	asNeededBoolean: Optional[bool] = None
	requisition: Optional[Identifier] = None
	locationReference: list[Reference] = []
	requester: Optional[Reference] = None
	priority: Optional[str] = None
	occurrencePeriod: Optional[Period] = None
	status: str
	quantityRatio: Optional[Ratio] = None
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	doNotPerform: Optional[bool] = None
	bodySite: list[CodeableConcept] = []
	intent: str
	quantityRange: Optional[Range] = None
	quantityQuantity: Optional[Quantity] = None
	replaces: list[Reference] = []
	orderDetail: list[CodeableConcept] = []
	basedOn: list[Reference] = []
	locationCode: list[CodeableConcept] = []
	occurrenceDateTime: Optional[str] = None
	subject: Reference
	asNeededCodeableConcept: Optional[CodeableConcept] = None
	performer: list[Reference] = []
	reasonReference: list[Reference] = []

