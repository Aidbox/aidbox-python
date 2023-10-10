from typing import Optional
from ..base import *

class Schedule(DomainResource):
	active: Optional[bool] = None
	actor: list[Reference]
	comment: Optional[str] = None
	identifier: list[Identifier] = []
	planningHorizon: Optional[Period] = None
	serviceCategory: list[CodeableConcept] = []
	serviceType: list[CodeableConcept] = []
	specialty: list[CodeableConcept] = []

