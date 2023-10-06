from typing import Optional

from base import Reference
from base import BackboneElement
from base import Reference
from base import Identifier
from base import CodeableConcept
from base import BackboneElement
from base import BackboneElement
from base import BackboneElement
from base import DomainResource


class BiologicallyDerivedProduct(DomainResource):
	request: list[Reference] = []
	processing: list[BackboneElement] = []
	parent: list[Reference] = []
	status: Optional[str] = None
	identifier: list[Identifier] = []
	productCode: Optional[CodeableConcept] = None
	storage: list[BackboneElement] = []
	quantity: Optional[int] = None
	productCategory: Optional[str] = None
	manipulation: Optional[BackboneElement] = None
	collection: Optional[BackboneElement] = None

