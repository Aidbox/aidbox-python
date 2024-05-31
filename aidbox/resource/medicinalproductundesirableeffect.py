from pydantic import *
from typing import Optional, List
from ..base import *

class MedicinalProductUndesirableEffect(DomainResource):
	subject: Optional[List[Reference]] = None
	symptomConditionEffect: Optional[CodeableConcept] = None
	classification: Optional[CodeableConcept] = None
	frequencyOfOccurrence: Optional[CodeableConcept] = None
	population: Optional[List[Population]] = None