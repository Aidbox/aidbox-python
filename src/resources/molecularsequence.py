from typing import Optional

from base import Reference
from base import BackboneElement
from base import BackboneElement
from base import BackboneElement
from base import Reference
from base import Reference
from base import Identifier
from base import BackboneElement
from base import Reference
from base import Quantity
from base import BackboneElement
from base import Reference
from base import DomainResource


class MolecularSequence(DomainResource):
	patient: Optional[Reference] = None
	structureVariant: list[BackboneElement] = []
	repository: list[BackboneElement] = []
	variant: list[BackboneElement] = []
	specimen: Optional[Reference] = None
	type: Optional[str] = None
	pointer: list[Reference] = []
	observedSeq: Optional[str] = None
	identifier: list[Identifier] = []
	quality: list[BackboneElement] = []
	device: Optional[Reference] = None
	quantity: Optional[Quantity] = None
	coordinateSystem: int
	referenceSeq: Optional[BackboneElement] = None
	performer: Optional[Reference] = None
	readCoverage: Optional[int] = None

