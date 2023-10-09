from typing import Optional
from base import *

class BodyStructure(DomainResource):
	active: Optional[bool] = None
	description: Optional[str] = None
	identifier: list[Identifier] = []
	image: list[Attachment] = []
	location: Optional[CodeableConcept] = None
	locationQualifier: list[CodeableConcept] = []
	morphology: Optional[CodeableConcept] = None
	patient: Reference

