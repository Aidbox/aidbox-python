from typing import Optional
from ..base import *

class MedicinalProductIndication_OtherTherapy(BackboneElement):
	medicationCodeableConcept: Optional[CodeableConcept] = None
	medicationReference: Optional[Reference] = None
	therapyRelationshipType: CodeableConcept

class MedicinalProductIndication(DomainResource):
	diseaseSymptomProcedure: Optional[CodeableConcept] = None
	undesirableEffect: list[Reference] = []
	duration: Optional[Quantity] = None
	otherTherapy: list[MedicinalProductIndication_OtherTherapy] = []
	comorbidity: list[CodeableConcept] = []
	intendedEffect: Optional[CodeableConcept] = None
	population: list[Population] = []
	diseaseStatus: Optional[CodeableConcept] = None
	subject: list[Reference] = []

