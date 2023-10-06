from typing import Optional

from base import Reference
from base import Reference
from base import BackboneElement
from base import BackboneElement
from base import Reference
from base import BackboneElement
from base import BackboneElement
from base import Reference
from base import BackboneElement
from base import BackboneElement
from base import BackboneElement
from base import CodeableConcept
from base import BackboneElement
from base import BackboneElement
from base import Reference
from base import Period
from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import BackboneElement
from base import Reference
from base import Period
from base import Identifier
from base import Attachment
from base import CodeableConcept
from base import CodeableConcept
from base import Period
from base import CodeableConcept
from base import Reference
from base import BackboneElement
from base import Reference
from base import BackboneElement
from base import Reference
from base import DomainResource


class ExplanationOfBenefit(DomainResource):
	patient: Reference
	claimResponse: Optional[Reference] = None
	insurance: list[BackboneElement]
	benefitBalance: list[BackboneElement] = []
	facility: Optional[Reference] = None
	processNote: list[BackboneElement] = []
	diagnosis: list[BackboneElement] = []
	preAuthRef: list[str] = []
	adjudication: list[str] = []
	enterer: Optional[Reference] = None
	supportingInfo: list[BackboneElement] = []
	use: str
	payment: Optional[BackboneElement] = None
	item: list[BackboneElement] = []
	type: CodeableConcept
	created: str
	procedure: list[BackboneElement] = []
	outcome: str
	related: list[BackboneElement] = []
	disposition: Optional[str] = None
	referral: Optional[Reference] = None
	preAuthRefPeriod: list[Period] = []
	total: list[BackboneElement] = []
	insurer: Reference
	fundsReserve: Optional[CodeableConcept] = None
	priority: Optional[CodeableConcept] = None
	accident: Optional[BackboneElement] = None
	status: str
	payee: Optional[BackboneElement] = None
	prescription: Optional[Reference] = None
	billablePeriod: Optional[Period] = None
	identifier: list[Identifier] = []
	form: Optional[Attachment] = None
	subType: Optional[CodeableConcept] = None
	fundsReserveRequested: Optional[CodeableConcept] = None
	benefitPeriod: Optional[Period] = None
	precedence: Optional[str] = None
	formCode: Optional[CodeableConcept] = None
	provider: Reference
	addItem: list[BackboneElement] = []
	originalPrescription: Optional[Reference] = None
	careTeam: list[BackboneElement] = []
	claim: Optional[Reference] = None

