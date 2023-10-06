from typing import Optional

from base import Reference
from base import BackboneElement
from base import Reference
from base import BackboneElement
from base import Reference
from base import BackboneElement
from base import BackboneElement
from base import CodeableConcept
from base import BackboneElement
from base import BackboneElement
from base import Reference
from base import Money
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import BackboneElement
from base import Reference
from base import Period
from base import Identifier
from base import CodeableConcept
from base import Reference
from base import Reference
from base import BackboneElement
from base import DomainResource


class Claim(DomainResource):
	patient: Reference
	insurance: list[BackboneElement]
	facility: Optional[Reference] = None
	diagnosis: list[BackboneElement] = []
	enterer: Optional[Reference] = None
	supportingInfo: list[BackboneElement] = []
	use: str
	item: list[BackboneElement] = []
	type: CodeableConcept
	created: str
	procedure: list[BackboneElement] = []
	related: list[BackboneElement] = []
	referral: Optional[Reference] = None
	total: Optional[Money] = None
	insurer: Optional[Reference] = None
	fundsReserve: Optional[CodeableConcept] = None
	priority: CodeableConcept
	accident: Optional[BackboneElement] = None
	status: str
	payee: Optional[BackboneElement] = None
	prescription: Optional[Reference] = None
	billablePeriod: Optional[Period] = None
	identifier: list[Identifier] = []
	subType: Optional[CodeableConcept] = None
	provider: Reference
	originalPrescription: Optional[Reference] = None
	careTeam: list[BackboneElement] = []

