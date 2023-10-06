from typing import Optional

from base import Period
from base import CodeableConcept
from base import BackboneElement
from base import BackboneElement
from base import CodeableConcept
from base import Period
from base import Reference
from base import CodeableConcept
from base import Identifier
from base import Reference
from base import CodeableConcept
from base import Reference
from base import DomainResource


class MedicinalProductAuthorization(DomainResource):
	dataExclusivityPeriod: Optional[Period] = None
	restoreDate: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	jurisdictionalAuthorization: list[BackboneElement] = []
	procedure: Optional[BackboneElement] = None
	legalBasis: Optional[CodeableConcept] = None
	validityPeriod: Optional[Period] = None
	regulator: Optional[Reference] = None
	status: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	statusDate: Optional[str] = None
	dateOfFirstAuthorization: Optional[str] = None
	internationalBirthDate: Optional[str] = None
	holder: Optional[Reference] = None
	country: list[CodeableConcept] = []
	subject: Optional[Reference] = None

