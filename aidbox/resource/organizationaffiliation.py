from pydantic import *
from typing import Optional, List
from ..base import *

class OrganizationAffiliation(DomainResource):
	specialty: Optional[List[CodeableConcept]] = None
	organization: Optional[Reference] = None
	participatingOrganization: Optional[Reference] = None
	active: Optional[bool] = None
	code: Optional[List[CodeableConcept]] = None
	identifier: Optional[List[Identifier]] = None
	telecom: Optional[List[ContactPoint]] = None
	network: Optional[List[Reference]] = None
	period: Optional[Period] = None
	location: Optional[List[Reference]] = None
	endpoint: Optional[List[Reference]] = None
	healthcareService: Optional[List[Reference]] = None