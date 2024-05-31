from pydantic import *
from typing import Optional, List
from ..base import *

class CareTeam_Participant(BackboneElement):
	role: Optional[List[CodeableConcept]] = None
	member: Optional[Reference] = None
	onBehalfOf: Optional[Reference] = None
	period: Optional[Period] = None

class CareTeam(DomainResource):
	category: Optional[List[CodeableConcept]] = None
	managingOrganization: Optional[List[Reference]] = None
	encounter: Optional[Reference] = None
	name: Optional[str] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	participant: Optional[List[CareTeam_Participant]] = None
	note: Optional[List[Annotation]] = None
	status: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	telecom: Optional[List[ContactPoint]] = None
	period: Optional[Period] = None
	subject: Optional[Reference] = None
	reasonReference: Optional[List[Reference]] = None