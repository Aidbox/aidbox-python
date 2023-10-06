from typing import Optional

from base import CodeableConcept
from base import BackboneElement
from base import Reference
from base import Identifier
from base import Reference
from base import BackboneElement
from base import CodeableConcept
from base import DomainResource


class MedicinalProductPharmaceutical(DomainResource):
	administrableDoseForm: CodeableConcept
	characteristics: list[BackboneElement] = []
	device: list[Reference] = []
	identifier: list[Identifier] = []
	ingredient: list[Reference] = []
	routeOfAdministration: list[BackboneElement]
	unitOfPresentation: Optional[CodeableConcept] = None

