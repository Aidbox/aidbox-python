from typing import Optional
from base import *

class MedicinalProductContraindication_OtherTherapy(BackboneElement):
	medicationCodeableConcept: Optional[CodeableConcept] = None
	medicationReference: Optional[Reference] = None
	therapyRelationshipType: CodeableConcept

class MedicinalProductContraindication(DomainResource):
	comorbidity: list[CodeableConcept] = []
	disease: Optional[CodeableConcept] = None
	diseaseStatus: Optional[CodeableConcept] = None
	otherTherapy: list[MedicinalProductContraindication_OtherTherapy] = []
	population: list[Population] = []
	subject: list[Reference] = []
	therapeuticIndication: list[Reference] = []

