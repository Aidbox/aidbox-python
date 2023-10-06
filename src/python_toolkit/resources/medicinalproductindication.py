from typing import Optional

from base import CodeableConcept
from base import Reference
from base import Quantity
from base import BackboneElement
from base import CodeableConcept
from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import Population
from base import DomainResource


class MedicinalProductIndication(DomainResource):
	diseaseSymptomProcedure: Optional[CodeableConcept] = None
	undesirableEffect: list[Reference] = []
	duration: Optional[Quantity] = None
	otherTherapy: list[BackboneElement] = []
	comorbidity: list[CodeableConcept] = []
	intendedEffect: Optional[CodeableConcept] = None
	population: list[Population] = []
	diseaseStatus: Optional[CodeableConcept] = None
	subject: list[Reference] = []

