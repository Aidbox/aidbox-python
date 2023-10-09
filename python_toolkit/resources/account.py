from typing import Optional
from base import *

class Account_Coverage(BackboneElement):
	coverage: Reference
	priority: Optional[str] = None

class Account_Guarantor(BackboneElement):
	onHold: Optional[bool] = None
	party: Reference
	period: Optional[Period] = None

class Account(DomainResource):
	description: Optional[str] = None
	name: Optional[str] = None
	servicePeriod: Optional[Period] = None
	coverage: list[Account_Coverage] = []
	type: Optional[CodeableConcept] = None
	guarantor: list[Account_Guarantor] = []
	status: str
	identifier: list[Identifier] = []
	partOf: Optional[Reference] = None
	subject: list[Reference] = []
	owner: Optional[Reference] = None

