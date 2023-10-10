from typing import Optional
from ..base import *

class OrganizationAffiliation(DomainResource):
	specialty: list[CodeableConcept] = []
	organization: Optional[Reference] = None
	participatingOrganization: Optional[Reference] = None
	active: Optional[bool] = None
	code: list[CodeableConcept] = []
	identifier: list[Identifier] = []
	telecom: list[ContactPoint] = []
	network: list[Reference] = []
	period: Optional[Period] = None
	location: list[Reference] = []
	endpoint: list[Reference] = []
	healthcareService: list[Reference] = []

