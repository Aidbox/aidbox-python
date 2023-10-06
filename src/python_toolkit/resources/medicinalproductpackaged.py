from typing import Optional

from base import Reference
from base import Identifier
from base import Reference
from base import CodeableConcept
from base import BackboneElement
from base import Reference
from base import BackboneElement
from base import MarketingStatus
from base import DomainResource


class MedicinalProductPackaged(DomainResource):
	description: Optional[str] = None
	marketingStatus: list[MarketingStatus] = []
	marketingAuthorization: Optional[Reference] = None
	identifier: list[Identifier] = []
	manufacturer: list[Reference] = []
	legalStatusOfSupply: Optional[CodeableConcept] = None
	batchIdentifier: list[BackboneElement] = []
	subject: list[Reference] = []
	packageItem: list[BackboneElement]

