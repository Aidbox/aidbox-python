from typing import Optional
from base import *

class MedicinalProductUndesirableEffect(DomainResource):
	classification: Optional[CodeableConcept] = None
	frequencyOfOccurrence: Optional[CodeableConcept] = None
	population: list[Population] = []
	subject: list[Reference] = []
	symptomConditionEffect: Optional[CodeableConcept] = None

