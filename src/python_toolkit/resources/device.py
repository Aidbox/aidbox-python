from typing import Optional

from base import Reference
from base import Reference
from base import Reference
from base import BackboneElement
from base import BackboneElement
from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import Annotation
from base import CodeableConcept
from base import Identifier
from base import BackboneElement
from base import Reference
from base import ContactPoint
from base import Reference
from base import BackboneElement
from base import DomainResource


class Device(DomainResource):
	patient: Optional[Reference] = None
	definition: Optional[Reference] = None
	serialNumber: Optional[str] = None
	parent: Optional[Reference] = None
	deviceName: list[BackboneElement] = []
	property: list[BackboneElement] = []
	partNumber: Optional[str] = None
	modelNumber: Optional[str] = None
	type: Optional[CodeableConcept] = None
	statusReason: list[CodeableConcept] = []
	specialization: list[BackboneElement] = []
	distinctIdentifier: Optional[str] = None
	note: list[Annotation] = []
	status: Optional[str] = None
	safety: list[CodeableConcept] = []
	lotNumber: Optional[str] = None
	url: Optional[str] = None
	identifier: list[Identifier] = []
	manufacturer: Optional[str] = None
	version: list[BackboneElement] = []
	location: Optional[Reference] = None
	contact: list[ContactPoint] = []
	manufactureDate: Optional[str] = None
	owner: Optional[Reference] = None
	expirationDate: Optional[str] = None
	udiCarrier: list[BackboneElement] = []

