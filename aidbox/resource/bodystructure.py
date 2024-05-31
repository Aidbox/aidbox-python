from pydantic import *
from typing import Optional, List
from ..base import *

class BodyStructure(DomainResource):
	identifier: Optional[List[Identifier]] = None
	active: Optional[bool] = None
	morphology: Optional[CodeableConcept] = None
	location: Optional[CodeableConcept] = None
	locationQualifier: Optional[List[CodeableConcept]] = None
	description: Optional[str] = None
	image: Optional[List[Attachment]] = None
	patient: Reference