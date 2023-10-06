from typing import Optional

from base import Reference
from base import Reference
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import Reference
from base import Reference
from base import BackboneElement
from base import Identifier
from base import Period
from base import DomainResource


class Coverage(DomainResource):
	policyHolder: Optional[Reference] = None
	beneficiary: Reference
	contract: list[Reference] = []
	relationship: Optional[CodeableConcept] = None
	type: Optional[CodeableConcept] = None
	costToBeneficiary: list[BackboneElement] = []
	subrogation: Optional[bool] = None
	subscriber: Optional[Reference] = None
	payor: list[Reference]
	status: str
	class_: list[BackboneElement] = []
	identifier: list[Identifier] = []
	order: Optional[str] = None
	network: Optional[str] = None
	period: Optional[Period] = None
	dependent: Optional[str] = None
	subscriberId: Optional[str] = None

