from typing import Optional

from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import Population
from base import DomainResource


class MedicinalProductUndesirableEffect(DomainResource):
	classification: Optional[CodeableConcept] = None
	frequencyOfOccurrence: Optional[CodeableConcept] = None
	population: list[Population] = []
	subject: list[Reference] = []
	symptomConditionEffect: Optional[CodeableConcept] = None

