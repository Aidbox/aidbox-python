from typing import Optional

from base import Reference
from base import Reference
from base import Money
from base import BackboneElement
from base import Identifier
from base import Identifier
from base import Period
from base import Reference
from base import CodeableConcept
from base import BackboneElement
from base import DomainResource


class PaymentReconciliation(DomainResource):
	requestor: Optional[Reference] = None
	request: Optional[Reference] = None
	paymentAmount: Money
	processNote: list[BackboneElement] = []
	created: str
	outcome: Optional[str] = None
	disposition: Optional[str] = None
	paymentIdentifier: Optional[Identifier] = None
	status: str
	paymentDate: str
	identifier: list[Identifier] = []
	period: Optional[Period] = None
	paymentIssuer: Optional[Reference] = None
	formCode: Optional[CodeableConcept] = None
	detail: list[BackboneElement] = []

