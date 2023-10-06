from typing import Optional

from base import BackboneElement
from base import BackboneElement
from base import CodeableConcept
from base import BackboneElement
from base import CodeableConcept
from base import CodeableConcept
from base import CodeableConcept
from base import Identifier
from base import Identifier
from base import CodeableConcept
from base import DomainResource


class SubstanceSourceMaterial(DomainResource):
	parentSubstanceName: list[str] = []
	organism: Optional[BackboneElement] = None
	partDescription: list[BackboneElement] = []
	developmentStage: Optional[CodeableConcept] = None
	fractionDescription: list[BackboneElement] = []
	sourceMaterialState: Optional[CodeableConcept] = None
	countryOfOrigin: list[CodeableConcept] = []
	sourceMaterialType: Optional[CodeableConcept] = None
	organismId: Optional[Identifier] = None
	organismName: Optional[str] = None
	parentSubstanceId: list[Identifier] = []
	geographicalLocation: list[str] = []
	sourceMaterialClass: Optional[CodeableConcept] = None

