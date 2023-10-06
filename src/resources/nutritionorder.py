from typing import Optional

from base import Reference
from base import BackboneElement
from base import Reference
from base import Annotation
from base import BackboneElement
from base import CodeableConcept
from base import CodeableConcept
from base import Identifier
from base import Reference
from base import BackboneElement
from base import Reference
from base import DomainResource


class NutritionOrder(DomainResource):
	patient: Reference
	oralDiet: Optional[BackboneElement] = None
	instantiatesCanonical: list[str] = []
	instantiatesUri: list[str] = []
	instantiates: list[str] = []
	encounter: Optional[Reference] = None
	note: list[Annotation] = []
	dateTime: str
	enteralFormula: Optional[BackboneElement] = None
	foodPreferenceModifier: list[CodeableConcept] = []
	status: str
	excludeFoodModifier: list[CodeableConcept] = []
	identifier: list[Identifier] = []
	intent: str
	orderer: Optional[Reference] = None
	supplement: list[BackboneElement] = []
	allergyIntolerance: list[Reference] = []

