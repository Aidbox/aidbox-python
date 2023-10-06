from typing import Optional

from base import CodeableConcept
from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import Reference
from base import Reference
from base import Population
from base import DomainResource


class MedicinalProductContraindication(DomainResource):
	comorbidity: list[CodeableConcept] = []
	disease: Optional[CodeableConcept] = None
	diseaseStatus: Optional[CodeableConcept] = None
	otherTherapy: list[BackboneElement] = []
	population: list[Population] = []
	subject: list[Reference] = []
	therapeuticIndication: list[Reference] = []

