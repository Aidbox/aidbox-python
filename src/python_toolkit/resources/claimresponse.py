from typing import Optional
from base import *

class ClaimResponse_Insurance(BackboneElement):
	businessArrangement: Optional[str] = None
	claimResponse: Optional[Reference] = None
	coverage: Reference
	focal: bool
	sequence: str

class ClaimResponse_ProcessNote(BackboneElement):
	language: Optional[CodeableConcept] = None
	number: Optional[str] = None
	text: str
	type: Optional[str] = None

class ClaimResponse_Payment(BackboneElement):
	adjustment: Optional[Money] = None
	adjustmentReason: Optional[CodeableConcept] = None
	amount: Money
	date: Optional[str] = None
	identifier: Optional[Identifier] = None
	type: CodeableConcept

class ClaimResponse_Item_Adjudication(BackboneElement):
	amount: Optional[Money] = None
	category: CodeableConcept
	reason: Optional[CodeableConcept] = None
	value: Optional[str] = None

class ClaimResponse_Item_Detail_SubDetail(BackboneElement):
	adjudication: list[str] = []
	noteNumber: list[str] = []
	subDetailSequence: str

class ClaimResponse_Item_Detail(BackboneElement):
	adjudication: list[str]
	detailSequence: str
	noteNumber: list[str] = []
	subDetail: list[ClaimResponse_Item_Detail_SubDetail] = []

class ClaimResponse_Item(BackboneElement):
	adjudication: list[ClaimResponse_Item_Adjudication]
	detail: list[ClaimResponse_Item_Detail] = []
	itemSequence: str
	noteNumber: list[str] = []

class ClaimResponse_Total(BackboneElement):
	amount: Money
	category: CodeableConcept

class ClaimResponse_Error(BackboneElement):
	code: CodeableConcept
	detailSequence: Optional[str] = None
	itemSequence: Optional[str] = None
	subDetailSequence: Optional[str] = None

class ClaimResponse_AddItem_Detail_SubDetail(BackboneElement):
	adjudication: list[str]
	factor: Optional[str] = None
	modifier: list[CodeableConcept] = []
	net: Optional[Money] = None
	noteNumber: list[str] = []
	productOrService: CodeableConcept
	quantity: Optional[Quantity] = None
	unitPrice: Optional[Money] = None

class ClaimResponse_AddItem_Detail(BackboneElement):
	modifier: list[CodeableConcept] = []
	adjudication: list[str]
	net: Optional[Money] = None
	productOrService: CodeableConcept
	factor: Optional[str] = None
	subDetail: list[ClaimResponse_AddItem_Detail_SubDetail] = []
	quantity: Optional[Quantity] = None
	noteNumber: list[str] = []
	unitPrice: Optional[Money] = None

class ClaimResponse_AddItem(BackboneElement):
	locationAddress: Optional[Address] = None
	modifier: list[CodeableConcept] = []
	adjudication: list[str]
	subdetailSequence: list[str] = []
	locationCodeableConcept: Optional[CodeableConcept] = None
	itemSequence: list[str] = []
	net: Optional[Money] = None
	detailSequence: list[str] = []
	subSite: list[CodeableConcept] = []
	productOrService: CodeableConcept
	locationReference: Optional[Reference] = None
	programCode: list[CodeableConcept] = []
	factor: Optional[str] = None
	servicedDate: Optional[str] = None
	bodySite: Optional[CodeableConcept] = None
	quantity: Optional[Quantity] = None
	provider: list[Reference] = []
	noteNumber: list[str] = []
	unitPrice: Optional[Money] = None
	servicedPeriod: Optional[Period] = None
	detail: list[ClaimResponse_AddItem_Detail] = []

class ClaimResponse(DomainResource):
	patient: Reference
	requestor: Optional[Reference] = None
	payeeType: Optional[CodeableConcept] = None
	insurance: list[ClaimResponse_Insurance] = []
	request: Optional[Reference] = None
	processNote: list[ClaimResponse_ProcessNote] = []
	preAuthRef: Optional[str] = None
	adjudication: list[str] = []
	use: str
	payment: Optional[ClaimResponse_Payment] = None
	item: list[ClaimResponse_Item] = []
	type: CodeableConcept
	created: str
	preAuthPeriod: Optional[Period] = None
	outcome: str
	disposition: Optional[str] = None
	communicationRequest: list[Reference] = []
	total: list[ClaimResponse_Total] = []
	insurer: Reference
	fundsReserve: Optional[CodeableConcept] = None
	status: str
	identifier: list[Identifier] = []
	error: list[ClaimResponse_Error] = []
	form: Optional[Attachment] = None
	subType: Optional[CodeableConcept] = None
	formCode: Optional[CodeableConcept] = None
	addItem: list[ClaimResponse_AddItem] = []
