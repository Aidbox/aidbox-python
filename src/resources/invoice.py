from typing import Optional

from base import Money
from base import Reference
from base import CodeableConcept
from base import Money
from base import BackboneElement
from base import Annotation
from base import Reference
from base import BackboneElement
from base import Identifier
from base import Reference
from base import Reference
from base import DomainResource


class Invoice(DomainResource):
	date: Optional[str] = None
	totalNet: Optional[Money] = None
	recipient: Optional[Reference] = None
	totalPriceComponent: list[str] = []
	type: Optional[CodeableConcept] = None
	totalGross: Optional[Money] = None
	participant: list[BackboneElement] = []
	note: list[Annotation] = []
	account: Optional[Reference] = None
	status: str
	lineItem: list[BackboneElement] = []
	identifier: list[Identifier] = []
	issuer: Optional[Reference] = None
	cancelledReason: Optional[str] = None
	paymentTerms: Optional[str] = None
	subject: Optional[Reference] = None

