from typing import Optional
from base import *

class EpisodeOfCare_Diagnosis(BackboneElement):
	condition: Reference
	rank: Optional[str] = None
	role: Optional[CodeableConcept] = None

class EpisodeOfCare_StatusHistory(BackboneElement):
	period: Period
	status: str

class EpisodeOfCare(DomainResource):
	patient: Reference
	diagnosis: list[EpisodeOfCare_Diagnosis] = []
	managingOrganization: Optional[Reference] = None
	type: list[CodeableConcept] = []
	account: list[Reference] = []
	referralRequest: list[Reference] = []
	team: list[Reference] = []
	status: str
	identifier: list[Identifier] = []
	period: Optional[Period] = None
	careManager: Optional[Reference] = None
	statusHistory: list[EpisodeOfCare_StatusHistory] = []

