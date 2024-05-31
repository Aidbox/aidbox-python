from pydantic import *
from typing import Optional, List
from ..base import *

class Invoice_Participant(BackboneElement):
	role: Optional[CodeableConcept] = None
	actor: Reference

class Invoice_LineItem_PriceComponent(BackboneElement):
	type: str
	code: Optional[CodeableConcept] = None
	factor: Optional[float] = None
	amount: Optional[Money] = None

class Invoice_LineItem(BackboneElement):
	sequence: Optional[PositiveInt] = None
	chargeItemReference: Optional[Reference] = None
	chargeItemCodeableConcept: Optional[CodeableConcept] = None
	priceComponent: Optional[List[Invoice_LineItem_PriceComponent]] = None

class Invoice(DomainResource):
	date: Optional[str] = None
	totalNet: Optional[Money] = None
	recipient: Optional[Reference] = None
	totalPriceComponent: Optional[List[str]] = None
	type: Optional[CodeableConcept] = None
	totalGross: Optional[Money] = None
	participant: Optional[List[Invoice_Participant]] = None
	note: Optional[List[Annotation]] = None
	account: Optional[Reference] = None
	status: str
	lineItem: Optional[List[Invoice_LineItem]] = None
	identifier: Optional[List[Identifier]] = None
	issuer: Optional[Reference] = None
	cancelledReason: Optional[str] = None
	paymentTerms: Optional[str] = None
	subject: Optional[Reference] = None