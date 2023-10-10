from typing import Optional
from ..base import *

class Invoice_Participant(BackboneElement):
	actor: Reference
	role: Optional[CodeableConcept] = None

class Invoice_LineItem_PriceComponent(BackboneElement):
	amount: Optional[Money] = None
	code: Optional[CodeableConcept] = None
	factor: Optional[str] = None
	type: str

class Invoice_LineItem(BackboneElement):
	chargeItemCodeableConcept: Optional[CodeableConcept] = None
	chargeItemReference: Optional[Reference] = None
	priceComponent: list[Invoice_LineItem_PriceComponent] = []
	sequence: Optional[str] = None

class Invoice(DomainResource):
	date: Optional[str] = None
	totalNet: Optional[Money] = None
	recipient: Optional[Reference] = None
	totalPriceComponent: list[str] = []
	type: Optional[CodeableConcept] = None
	totalGross: Optional[Money] = None
	participant: list[Invoice_Participant] = []
	note: list[Annotation] = []
	account: Optional[Reference] = None
	status: str
	lineItem: list[Invoice_LineItem] = []
	identifier: list[Identifier] = []
	issuer: Optional[Reference] = None
	cancelledReason: Optional[str] = None
	paymentTerms: Optional[str] = None
	subject: Optional[Reference] = None

