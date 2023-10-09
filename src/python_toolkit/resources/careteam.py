from typing import Optional
from base import *

class CareTeam_Participant(BackboneElement):
	member: Optional[Reference] = None
	onBehalfOf: Optional[Reference] = None
	period: Optional[Period] = None
	role: list[CodeableConcept] = []

class CareTeam(DomainResource):
	category: list[CodeableConcept] = []
	managingOrganization: list[Reference] = []
	encounter: Optional[Reference] = None
	name: Optional[str] = None
	reasonCode: list[CodeableConcept] = []
	participant: list[CareTeam_Participant] = []
	note: list[Annotation] = []
	status: Optional[str] = None
	identifier: list[Identifier] = []
	telecom: list[ContactPoint] = []
	period: Optional[Period] = None
	subject: Optional[Reference] = None
	reasonReference: list[Reference] = []

