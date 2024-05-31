from pydantic import *
from typing import Optional, List
from ..base import *

class MedicinalProductContraindication_OtherTherapy(BackboneElement):
	therapyRelationshipType: CodeableConcept
	medicationCodeableConcept: Optional[CodeableConcept] = None
	medicationReference: Optional[Reference] = None

class MedicinalProductContraindication(DomainResource):
	subject: Optional[List[Reference]] = None
	disease: Optional[CodeableConcept] = None
	diseaseStatus: Optional[CodeableConcept] = None
	comorbidity: Optional[List[CodeableConcept]] = None
	therapeuticIndication: Optional[List[Reference]] = None
	otherTherapy: Optional[List[MedicinalProductContraindication_OtherTherapy]] = None
	population: Optional[List[Population]] = None