from typing import Optional

from base import BackboneElement
from base import BackboneElement
from base import Reference
from base import BackboneElement
from base import CodeableConcept
from base import BackboneElement
from base import Reference
from base import Reference
from base import BackboneElement
from base import CodeableConcept
from base import BackboneElement
from base import Identifier
from base import Reference
from base import Reference
from base import CodeableConcept
from base import Reference
from base import DomainResource


class SubstanceSpecification(DomainResource):
	description: Optional[str] = None
	property: list[BackboneElement] = []
	name: list[BackboneElement] = []
	referenceInformation: Optional[Reference] = None
	relationship: list[BackboneElement] = []
	type: Optional[CodeableConcept] = None
	moiety: list[BackboneElement] = []
	source: list[Reference] = []
	nucleicAcid: Optional[Reference] = None
	structure: Optional[BackboneElement] = None
	status: Optional[CodeableConcept] = None
	comment: Optional[str] = None
	code: list[BackboneElement] = []
	identifier: Optional[Identifier] = None
	molecularWeight: list[str] = []
	polymer: Optional[Reference] = None
	protein: Optional[Reference] = None
	domain: Optional[CodeableConcept] = None
	sourceMaterial: Optional[Reference] = None

