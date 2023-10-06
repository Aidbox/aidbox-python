from typing import Optional

from base import BackboneElement
from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import Identifier
from base import Reference
from base import Reference
from base import DomainResource


class ObservationDefinition(DomainResource):
	quantitativeDetails: Optional[BackboneElement] = None
	category: list[CodeableConcept] = []
	method: Optional[CodeableConcept] = None
	validCodedValueSet: Optional[Reference] = None
	qualifiedInterval: list[BackboneElement] = []
	abnormalCodedValueSet: Optional[Reference] = None
	code: CodeableConcept
	identifier: list[Identifier] = []
	permittedDataType: list[str] = []
	multipleResultsAllowed: Optional[bool] = None
	normalCodedValueSet: Optional[Reference] = None
	preferredReportName: Optional[str] = None
	criticalCodedValueSet: Optional[Reference] = None

