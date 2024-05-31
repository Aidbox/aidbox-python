from pydantic import *
from typing import Optional, List
from ..base import *

class Schedule(DomainResource):
	identifier: Optional[List[Identifier]] = None
	active: Optional[bool] = None
	serviceCategory: Optional[List[CodeableConcept]] = None
	serviceType: Optional[List[CodeableConcept]] = None
	specialty: Optional[List[CodeableConcept]] = None
	actor: List[Reference]
	planningHorizon: Optional[Period] = None
	comment: Optional[str] = None