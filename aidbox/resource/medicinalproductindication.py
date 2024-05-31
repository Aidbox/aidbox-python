from pydantic import *
from typing import Optional, List
from ..base import *

class MedicinalProductIndication_OtherTherapy(BackboneElement):
	therapyRelationshipType: CodeableConcept
	medicationCodeableConcept: Optional[CodeableConcept] = None
	medicationReference: Optional[Reference] = None

class MedicinalProductIndication(DomainResource):
	diseaseSymptomProcedure: Optional[CodeableConcept] = None
	undesirableEffect: Optional[List[Reference]] = None
	duration: Optional[Quantity] = None
	otherTherapy: Optional[List[MedicinalProductIndication_OtherTherapy]] = None
	comorbidity: Optional[List[CodeableConcept]] = None
	intendedEffect: Optional[CodeableConcept] = None
	population: Optional[List[Population]] = None
	diseaseStatus: Optional[CodeableConcept] = None
	subject: Optional[List[Reference]] = None