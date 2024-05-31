from pydantic import *
from typing import Optional, List
from ..base import *

class ClaimResponse_Insurance(BackboneElement):
	sequence: PositiveInt
	focal: bool
	coverage: Reference
	businessArrangement: Optional[str] = None
	claimResponse: Optional[Reference] = None

class ClaimResponse_ProcessNote(BackboneElement):
	number: Optional[PositiveInt] = None
	type: Optional[str] = None
	text: str
	language: Optional[CodeableConcept] = None

class ClaimResponse_Payment(BackboneElement):
	type: CodeableConcept
	adjustment: Optional[Money] = None
	adjustmentReason: Optional[CodeableConcept] = None
	date: Optional[str] = None
	amount: Money
	identifier: Optional[Identifier] = None

class ClaimResponse_Item_Adjudication(BackboneElement):
	category: CodeableConcept
	reason: Optional[CodeableConcept] = None
	amount: Optional[Money] = None
	value: Optional[float] = None

class ClaimResponse_Item_Detail_SubDetail(BackboneElement):
	subDetailSequence: PositiveInt
	noteNumber: Optional[List[PositiveInt]] = None
	adjudication: Optional[List[str]] = None

class ClaimResponse_Item_Detail(BackboneElement):
	detailSequence: PositiveInt
	noteNumber: Optional[List[PositiveInt]] = None
	adjudication: List[str]
	subDetail: Optional[List[ClaimResponse_Item_Detail_SubDetail]] = None

class ClaimResponse_Item(BackboneElement):
	itemSequence: PositiveInt
	noteNumber: Optional[List[PositiveInt]] = None
	adjudication: List[ClaimResponse_Item_Adjudication]
	detail: Optional[List[ClaimResponse_Item_Detail]] = None

class ClaimResponse_Total(BackboneElement):
	category: CodeableConcept
	amount: Money

class ClaimResponse_Error(BackboneElement):
	itemSequence: Optional[PositiveInt] = None
	detailSequence: Optional[PositiveInt] = None
	subDetailSequence: Optional[PositiveInt] = None
	code: CodeableConcept

class ClaimResponse_AddItem_Detail_SubDetail(BackboneElement):
	productOrService: CodeableConcept
	modifier: Optional[List[CodeableConcept]] = None
	quantity: Optional[Quantity] = None
	unitPrice: Optional[Money] = None
	factor: Optional[float] = None
	net: Optional[Money] = None
	noteNumber: Optional[List[PositiveInt]] = None
	adjudication: List[str]

class ClaimResponse_AddItem_Detail(BackboneElement):
	modifier: Optional[List[CodeableConcept]] = None
	adjudication: List[str]
	net: Optional[Money] = None
	productOrService: CodeableConcept
	factor: Optional[float] = None
	subDetail: Optional[List[ClaimResponse_AddItem_Detail_SubDetail]] = None
	quantity: Optional[Quantity] = None
	noteNumber: Optional[List[PositiveInt]] = None
	unitPrice: Optional[Money] = None

class ClaimResponse_AddItem(BackboneElement):
	locationAddress: Optional[Address] = None
	modifier: Optional[List[CodeableConcept]] = None
	adjudication: List[str]
	subdetailSequence: Optional[List[PositiveInt]] = None
	locationCodeableConcept: Optional[CodeableConcept] = None
	itemSequence: Optional[List[PositiveInt]] = None
	net: Optional[Money] = None
	detailSequence: Optional[List[PositiveInt]] = None
	subSite: Optional[List[CodeableConcept]] = None
	productOrService: CodeableConcept
	locationReference: Optional[Reference] = None
	programCode: Optional[List[CodeableConcept]] = None
	factor: Optional[float] = None
	servicedDate: Optional[str] = None
	bodySite: Optional[CodeableConcept] = None
	quantity: Optional[Quantity] = None
	provider: Optional[List[Reference]] = None
	noteNumber: Optional[List[PositiveInt]] = None
	unitPrice: Optional[Money] = None
	servicedPeriod: Optional[Period] = None
	detail: Optional[List[ClaimResponse_AddItem_Detail]] = None

class ClaimResponse(DomainResource):
	patient: Reference
	requestor: Optional[Reference] = None
	payeeType: Optional[CodeableConcept] = None
	insurance: Optional[List[ClaimResponse_Insurance]] = None
	request: Optional[Reference] = None
	processNote: Optional[List[ClaimResponse_ProcessNote]] = None
	preAuthRef: Optional[str] = None
	adjudication: Optional[List[str]] = None
	use: str
	payment: Optional[ClaimResponse_Payment] = None
	item: Optional[List[ClaimResponse_Item]] = None
	type: CodeableConcept
	created: str
	preAuthPeriod: Optional[Period] = None
	outcome: str
	disposition: Optional[str] = None
	communicationRequest: Optional[List[Reference]] = None
	total: Optional[List[ClaimResponse_Total]] = None
	insurer: Reference
	fundsReserve: Optional[CodeableConcept] = None
	status: str
	identifier: Optional[List[Identifier]] = None
	error: Optional[List[ClaimResponse_Error]] = None
	form: Optional[Attachment] = None
	subType: Optional[CodeableConcept] = None
	formCode: Optional[CodeableConcept] = None
	addItem: Optional[List[ClaimResponse_AddItem]] = None