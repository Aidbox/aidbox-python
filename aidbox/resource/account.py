from pydantic import *
from typing import Optional, List
from ..base import *

class Account_Coverage(BackboneElement):
	coverage: Reference
	priority: Optional[PositiveInt] = None

class Account_Guarantor(BackboneElement):
	party: Reference
	onHold: Optional[bool] = None
	period: Optional[Period] = None

class Account(DomainResource):
	description: Optional[str] = None
	name: Optional[str] = None
	servicePeriod: Optional[Period] = None
	coverage: Optional[List[Account_Coverage]] = None
	type: Optional[CodeableConcept] = None
	guarantor: Optional[List[Account_Guarantor]] = None
	status: str
	identifier: Optional[List[Identifier]] = None
	partOf: Optional[Reference] = None
	subject: Optional[List[Reference]] = None
	owner: Optional[Reference] = None