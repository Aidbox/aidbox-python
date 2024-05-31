from pydantic import *
from typing import Optional, List
from ..base import *

class EpisodeOfCare_Diagnosis(BackboneElement):
	condition: Reference
	role: Optional[CodeableConcept] = None
	rank: Optional[PositiveInt] = None

class EpisodeOfCare_StatusHistory(BackboneElement):
	status: str
	period: Period

class EpisodeOfCare(DomainResource):
	patient: Reference
	diagnosis: Optional[List[EpisodeOfCare_Diagnosis]] = None
	managingOrganization: Optional[Reference] = None
	type: Optional[List[CodeableConcept]] = None
	account: Optional[List[Reference]] = None
	referralRequest: Optional[List[Reference]] = None
	team: Optional[List[Reference]] = None
	status: str
	identifier: Optional[List[Identifier]] = None
	period: Optional[Period] = None
	careManager: Optional[Reference] = None
	statusHistory: Optional[List[EpisodeOfCare_StatusHistory]] = None