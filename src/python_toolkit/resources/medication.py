from typing import Optional

from base import Ratio
from base import BackboneElement
from base import CodeableConcept
from base import CodeableConcept
from base import Identifier
from base import BackboneElement
from base import Reference
from base import DomainResource


class Medication(DomainResource):
	amount: Optional[Ratio] = None
	batch: Optional[BackboneElement] = None
	code: Optional[CodeableConcept] = None
	form: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	ingredient: list[BackboneElement] = []
	manufacturer: Optional[Reference] = None
	status: Optional[str] = None

