from pydantic import *
from typing import Optional, List
from ..base import *

class PaymentReconciliation_ProcessNote(BackboneElement):
	type: Optional[str] = None
	text: Optional[str] = None

class PaymentReconciliation_Detail(BackboneElement):
	response: Optional[Reference] = None
	amount: Optional[Money] = None
	date: Optional[str] = None
	request: Optional[Reference] = None
	type: CodeableConcept
	responsible: Optional[Reference] = None
	payee: Optional[Reference] = None
	predecessor: Optional[Identifier] = None
	identifier: Optional[Identifier] = None
	submitter: Optional[Reference] = None

class PaymentReconciliation(DomainResource):
	requestor: Optional[Reference] = None
	request: Optional[Reference] = None
	paymentAmount: Money
	processNote: Optional[List[PaymentReconciliation_ProcessNote]] = None
	created: str
	outcome: Optional[str] = None
	disposition: Optional[str] = None
	paymentIdentifier: Optional[Identifier] = None
	status: str
	paymentDate: str
	identifier: Optional[List[Identifier]] = None
	period: Optional[Period] = None
	paymentIssuer: Optional[Reference] = None
	formCode: Optional[CodeableConcept] = None
	detail: Optional[List[PaymentReconciliation_Detail]] = None