from typing import Optional
from base import *

class PaymentReconciliation_ProcessNote(BackboneElement):
	text: Optional[str] = None
	type: Optional[str] = None

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
	processNote: list[PaymentReconciliation_ProcessNote] = []
	created: str
	outcome: Optional[str] = None
	disposition: Optional[str] = None
	paymentIdentifier: Optional[Identifier] = None
	status: str
	paymentDate: str
	identifier: list[Identifier] = []
	period: Optional[Period] = None
	paymentIssuer: Optional[Reference] = None
	formCode: Optional[CodeableConcept] = None
	detail: list[PaymentReconciliation_Detail] = []

