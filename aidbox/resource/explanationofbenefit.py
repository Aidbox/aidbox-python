from typing import Optional
from ..base import *

class ExplanationOfBenefit_Insurance(BackboneElement):
	coverage: Reference
	focal: bool
	preAuthRef: list[str] = []

class ExplanationOfBenefit_BenefitBalance_Financial(BackboneElement):
	allowedMoney: Optional[Money] = None
	allowedString: Optional[str] = None
	allowedUnsignedInt: Optional[str] = None
	type: CodeableConcept
	usedMoney: Optional[Money] = None
	usedUnsignedInt: Optional[str] = None

class ExplanationOfBenefit_BenefitBalance(BackboneElement):
	category: CodeableConcept
	description: Optional[str] = None
	excluded: Optional[bool] = None
	financial: list[ExplanationOfBenefit_BenefitBalance_Financial] = []
	name: Optional[str] = None
	network: Optional[CodeableConcept] = None
	term: Optional[CodeableConcept] = None
	unit: Optional[CodeableConcept] = None

class ExplanationOfBenefit_ProcessNote(BackboneElement):
	language: Optional[CodeableConcept] = None
	number: Optional[str] = None
	text: Optional[str] = None
	type: Optional[str] = None

class ExplanationOfBenefit_Diagnosis(BackboneElement):
	diagnosisCodeableConcept: Optional[CodeableConcept] = None
	diagnosisReference: Optional[Reference] = None
	onAdmission: Optional[CodeableConcept] = None
	packageCode: Optional[CodeableConcept] = None
	sequence: str
	type: list[CodeableConcept] = []

class ExplanationOfBenefit_SupportingInfo(BackboneElement):
	category: CodeableConcept
	valueReference: Optional[Reference] = None
	valueQuantity: Optional[Quantity] = None
	timingPeriod: Optional[Period] = None
	valueString: Optional[str] = None
	valueBoolean: Optional[bool] = None
	reason: Optional[Coding] = None
	sequence: str
	code: Optional[CodeableConcept] = None
	timingDate: Optional[str] = None
	valueAttachment: Optional[Attachment] = None

class ExplanationOfBenefit_Payment(BackboneElement):
	adjustment: Optional[Money] = None
	adjustmentReason: Optional[CodeableConcept] = None
	amount: Optional[Money] = None
	date: Optional[str] = None
	identifier: Optional[Identifier] = None
	type: Optional[CodeableConcept] = None

class ExplanationOfBenefit_Item_Adjudication(BackboneElement):
	amount: Optional[Money] = None
	category: CodeableConcept
	reason: Optional[CodeableConcept] = None
	value: Optional[str] = None

class ExplanationOfBenefit_Item_Detail_SubDetail(BackboneElement):
	category: Optional[CodeableConcept] = None
	modifier: list[CodeableConcept] = []
	revenue: Optional[CodeableConcept] = None
	adjudication: list[str] = []
	net: Optional[Money] = None
	productOrService: CodeableConcept
	udi: list[Reference] = []
	programCode: list[CodeableConcept] = []
	factor: Optional[str] = None
	sequence: str
	quantity: Optional[Quantity] = None
	noteNumber: list[str] = []
	unitPrice: Optional[Money] = None

class ExplanationOfBenefit_Item_Detail(BackboneElement):
	category: Optional[CodeableConcept] = None
	modifier: list[CodeableConcept] = []
	revenue: Optional[CodeableConcept] = None
	adjudication: list[str] = []
	net: Optional[Money] = None
	productOrService: CodeableConcept
	udi: list[Reference] = []
	programCode: list[CodeableConcept] = []
	factor: Optional[str] = None
	sequence: str
	subDetail: list[ExplanationOfBenefit_Item_Detail_SubDetail] = []
	quantity: Optional[Quantity] = None
	noteNumber: list[str] = []
	unitPrice: Optional[Money] = None

class ExplanationOfBenefit_Item(BackboneElement):
	category: Optional[CodeableConcept] = None
	diagnosisSequence: list[str] = []
	procedureSequence: list[str] = []
	locationAddress: Optional[Address] = None
	modifier: list[CodeableConcept] = []
	revenue: Optional[CodeableConcept] = None
	adjudication: list[ExplanationOfBenefit_Item_Adjudication] = []
	encounter: list[Reference] = []
	locationCodeableConcept: Optional[CodeableConcept] = None
	net: Optional[Money] = None
	subSite: list[CodeableConcept] = []
	careTeamSequence: list[str] = []
	productOrService: CodeableConcept
	locationReference: Optional[Reference] = None
	udi: list[Reference] = []
	informationSequence: list[str] = []
	programCode: list[CodeableConcept] = []
	factor: Optional[str] = None
	servicedDate: Optional[str] = None
	sequence: str
	bodySite: Optional[CodeableConcept] = None
	quantity: Optional[Quantity] = None
	noteNumber: list[str] = []
	unitPrice: Optional[Money] = None
	servicedPeriod: Optional[Period] = None
	detail: list[ExplanationOfBenefit_Item_Detail] = []

class ExplanationOfBenefit_Procedure(BackboneElement):
	date: Optional[str] = None
	procedureCodeableConcept: Optional[CodeableConcept] = None
	procedureReference: Optional[Reference] = None
	sequence: str
	type: list[CodeableConcept] = []
	udi: list[Reference] = []

class ExplanationOfBenefit_Related(BackboneElement):
	claim: Optional[Reference] = None
	reference: Optional[Identifier] = None
	relationship: Optional[CodeableConcept] = None

class ExplanationOfBenefit_Total(BackboneElement):
	amount: Money
	category: CodeableConcept

class ExplanationOfBenefit_Accident(BackboneElement):
	date: Optional[str] = None
	locationAddress: Optional[Address] = None
	locationReference: Optional[Reference] = None
	type: Optional[CodeableConcept] = None

class ExplanationOfBenefit_Payee(BackboneElement):
	party: Optional[Reference] = None
	type: Optional[CodeableConcept] = None

class ExplanationOfBenefit_AddItem_Detail_SubDetail(BackboneElement):
	adjudication: list[str] = []
	factor: Optional[str] = None
	modifier: list[CodeableConcept] = []
	net: Optional[Money] = None
	noteNumber: list[str] = []
	productOrService: CodeableConcept
	quantity: Optional[Quantity] = None
	unitPrice: Optional[Money] = None

class ExplanationOfBenefit_AddItem_Detail(BackboneElement):
	modifier: list[CodeableConcept] = []
	adjudication: list[str] = []
	net: Optional[Money] = None
	productOrService: CodeableConcept
	factor: Optional[str] = None
	subDetail: list[ExplanationOfBenefit_AddItem_Detail_SubDetail] = []
	quantity: Optional[Quantity] = None
	noteNumber: list[str] = []
	unitPrice: Optional[Money] = None

class ExplanationOfBenefit_AddItem(BackboneElement):
	locationAddress: Optional[Address] = None
	modifier: list[CodeableConcept] = []
	adjudication: list[str] = []
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
	subDetailSequence: list[str] = []
	bodySite: Optional[CodeableConcept] = None
	quantity: Optional[Quantity] = None
	provider: list[Reference] = []
	noteNumber: list[str] = []
	unitPrice: Optional[Money] = None
	servicedPeriod: Optional[Period] = None
	detail: list[ExplanationOfBenefit_AddItem_Detail] = []

class ExplanationOfBenefit_CareTeam(BackboneElement):
	provider: Reference
	qualification: Optional[CodeableConcept] = None
	responsible: Optional[bool] = None
	role: Optional[CodeableConcept] = None
	sequence: str

class ExplanationOfBenefit(DomainResource):
	patient: Reference
	claimResponse: Optional[Reference] = None
	insurance: list[ExplanationOfBenefit_Insurance]
	benefitBalance: list[ExplanationOfBenefit_BenefitBalance] = []
	facility: Optional[Reference] = None
	processNote: list[ExplanationOfBenefit_ProcessNote] = []
	diagnosis: list[ExplanationOfBenefit_Diagnosis] = []
	preAuthRef: list[str] = []
	adjudication: list[str] = []
	enterer: Optional[Reference] = None
	supportingInfo: list[ExplanationOfBenefit_SupportingInfo] = []
	use: str
	payment: Optional[ExplanationOfBenefit_Payment] = None
	item: list[ExplanationOfBenefit_Item] = []
	type: CodeableConcept
	created: str
	procedure: list[ExplanationOfBenefit_Procedure] = []
	outcome: str
	related: list[ExplanationOfBenefit_Related] = []
	disposition: Optional[str] = None
	referral: Optional[Reference] = None
	preAuthRefPeriod: list[Period] = []
	total: list[ExplanationOfBenefit_Total] = []
	insurer: Reference
	fundsReserve: Optional[CodeableConcept] = None
	priority: Optional[CodeableConcept] = None
	accident: Optional[ExplanationOfBenefit_Accident] = None
	status: str
	payee: Optional[ExplanationOfBenefit_Payee] = None
	prescription: Optional[Reference] = None
	billablePeriod: Optional[Period] = None
	identifier: list[Identifier] = []
	form: Optional[Attachment] = None
	subType: Optional[CodeableConcept] = None
	fundsReserveRequested: Optional[CodeableConcept] = None
	benefitPeriod: Optional[Period] = None
	precedence: Optional[str] = None
	formCode: Optional[CodeableConcept] = None
	provider: Reference
	addItem: list[ExplanationOfBenefit_AddItem] = []
	originalPrescription: Optional[Reference] = None
	careTeam: list[ExplanationOfBenefit_CareTeam] = []
	claim: Optional[Reference] = None

