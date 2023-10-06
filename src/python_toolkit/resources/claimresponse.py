from typing import Optional

from base import Reference
from base import Reference
from base import CodeableConcept
from base import BackboneElement
from base import Reference
from base import BackboneElement
from base import BackboneElement
from base import BackboneElement
from base import CodeableConcept
from base import Period
from base import Reference
from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import Identifier
from base import BackboneElement
from base import Attachment
from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import DomainResource


class ClaimResponse(DomainResource):
	patient: Reference
	requestor: Optional[Reference] = None
	payeeType: Optional[CodeableConcept] = None
	insurance: list[BackboneElement] = []
	request: Optional[Reference] = None
	processNote: list[BackboneElement] = []
	preAuthRef: Optional[str] = None
	adjudication: list[str] = []
	use: str
	payment: Optional[BackboneElement] = None
	item: list[BackboneElement] = []
	type: CodeableConcept
	created: str
	preAuthPeriod: Optional[Period] = None
	outcome: str
	disposition: Optional[str] = None
	communicationRequest: list[Reference] = []
	total: list[BackboneElement] = []
	insurer: Reference
	fundsReserve: Optional[CodeableConcept] = None
	status: str
	identifier: list[Identifier] = []
	error: list[BackboneElement] = []
	form: Optional[Attachment] = None
	subType: Optional[CodeableConcept] = None
	formCode: Optional[CodeableConcept] = None
	addItem: list[BackboneElement] = []

