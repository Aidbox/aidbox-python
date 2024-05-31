from pydantic import *
from typing import Optional, List
from ..base import *

class ExplanationOfBenefit_Insurance(BackboneElement):
	focal: bool
	coverage: Reference
	preAuthRef: Optional[List[str]] = None

class ExplanationOfBenefit_BenefitBalance_Financial(BackboneElement):
	type: CodeableConcept
	allowedUnsignedInt: Optional[NonNegativeInt] = None
	allowedString: Optional[str] = None
	allowedMoney: Optional[Money] = None
	usedUnsignedInt: Optional[NonNegativeInt] = None
	usedMoney: Optional[Money] = None

class ExplanationOfBenefit_BenefitBalance(BackboneElement):
	category: CodeableConcept
	excluded: Optional[bool] = None
	name: Optional[str] = None
	description: Optional[str] = None
	network: Optional[CodeableConcept] = None
	unit: Optional[CodeableConcept] = None
	term: Optional[CodeableConcept] = None
	financial: Optional[List[ExplanationOfBenefit_BenefitBalance_Financial]] = None

class ExplanationOfBenefit_ProcessNote(BackboneElement):
	number: Optional[PositiveInt] = None
	type: Optional[str] = None
	text: Optional[str] = None
	language: Optional[CodeableConcept] = None

class ExplanationOfBenefit_Diagnosis(BackboneElement):
	sequence: PositiveInt
	diagnosisCodeableConcept: Optional[CodeableConcept] = None
	diagnosisReference: Optional[Reference] = None
	type: Optional[List[CodeableConcept]] = None
	onAdmission: Optional[CodeableConcept] = None
	packageCode: Optional[CodeableConcept] = None

class ExplanationOfBenefit_SupportingInfo(BackboneElement):
	category: CodeableConcept
	valueReference: Optional[Reference] = None
	valueQuantity: Optional[Quantity] = None
	timingPeriod: Optional[Period] = None
	valueString: Optional[str] = None
	valueBoolean: Optional[bool] = None
	reason: Optional[Coding] = None
	sequence: PositiveInt
	code: Optional[CodeableConcept] = None
	timingDate: Optional[str] = None
	valueAttachment: Optional[Attachment] = None

class ExplanationOfBenefit_Payment(BackboneElement):
	type: Optional[CodeableConcept] = None
	adjustment: Optional[Money] = None
	adjustmentReason: Optional[CodeableConcept] = None
	date: Optional[str] = None
	amount: Optional[Money] = None
	identifier: Optional[Identifier] = None

class ExplanationOfBenefit_Item_Adjudication(BackboneElement):
	category: CodeableConcept
	reason: Optional[CodeableConcept] = None
	amount: Optional[Money] = None
	value: Optional[float] = None

class ExplanationOfBenefit_Item_Detail_SubDetail(BackboneElement):
	category: Optional[CodeableConcept] = None
	modifier: Optional[List[CodeableConcept]] = None
	revenue: Optional[CodeableConcept] = None
	adjudication: Optional[List[str]] = None
	net: Optional[Money] = None
	productOrService: CodeableConcept
	udi: Optional[List[Reference]] = None
	programCode: Optional[List[CodeableConcept]] = None
	factor: Optional[float] = None
	sequence: PositiveInt
	quantity: Optional[Quantity] = None
	noteNumber: Optional[List[PositiveInt]] = None
	unitPrice: Optional[Money] = None

class ExplanationOfBenefit_Item_Detail(BackboneElement):
	category: Optional[CodeableConcept] = None
	modifier: Optional[List[CodeableConcept]] = None
	revenue: Optional[CodeableConcept] = None
	adjudication: Optional[List[str]] = None
	net: Optional[Money] = None
	productOrService: CodeableConcept
	udi: Optional[List[Reference]] = None
	programCode: Optional[List[CodeableConcept]] = None
	factor: Optional[float] = None
	sequence: PositiveInt
	subDetail: Optional[List[ExplanationOfBenefit_Item_Detail_SubDetail]] = None
	quantity: Optional[Quantity] = None
	noteNumber: Optional[List[PositiveInt]] = None
	unitPrice: Optional[Money] = None

class ExplanationOfBenefit_Item(BackboneElement):
	category: Optional[CodeableConcept] = None
	diagnosisSequence: Optional[List[PositiveInt]] = None
	procedureSequence: Optional[List[PositiveInt]] = None
	locationAddress: Optional[Address] = None
	modifier: Optional[List[CodeableConcept]] = None
	revenue: Optional[CodeableConcept] = None
	adjudication: Optional[List[ExplanationOfBenefit_Item_Adjudication]] = None
	encounter: Optional[List[Reference]] = None
	locationCodeableConcept: Optional[CodeableConcept] = None
	net: Optional[Money] = None
	subSite: Optional[List[CodeableConcept]] = None
	careTeamSequence: Optional[List[PositiveInt]] = None
	productOrService: CodeableConcept
	locationReference: Optional[Reference] = None
	udi: Optional[List[Reference]] = None
	informationSequence: Optional[List[PositiveInt]] = None
	programCode: Optional[List[CodeableConcept]] = None
	factor: Optional[float] = None
	servicedDate: Optional[str] = None
	sequence: PositiveInt
	bodySite: Optional[CodeableConcept] = None
	quantity: Optional[Quantity] = None
	noteNumber: Optional[List[PositiveInt]] = None
	unitPrice: Optional[Money] = None
	servicedPeriod: Optional[Period] = None
	detail: Optional[List[ExplanationOfBenefit_Item_Detail]] = None

class ExplanationOfBenefit_Procedure(BackboneElement):
	sequence: PositiveInt
	type: Optional[List[CodeableConcept]] = None
	date: Optional[str] = None
	procedureCodeableConcept: Optional[CodeableConcept] = None
	procedureReference: Optional[Reference] = None
	udi: Optional[List[Reference]] = None

class ExplanationOfBenefit_Related(BackboneElement):
	claim: Optional[Reference] = None
	relationship: Optional[CodeableConcept] = None
	reference: Optional[Identifier] = None

class ExplanationOfBenefit_Total(BackboneElement):
	category: CodeableConcept
	amount: Money

class ExplanationOfBenefit_Accident(BackboneElement):
	date: Optional[str] = None
	type: Optional[CodeableConcept] = None
	locationAddress: Optional[Address] = None
	locationReference: Optional[Reference] = None

class ExplanationOfBenefit_Payee(BackboneElement):
	type: Optional[CodeableConcept] = None
	party: Optional[Reference] = None

class ExplanationOfBenefit_AddItem_Detail_SubDetail(BackboneElement):
	productOrService: CodeableConcept
	modifier: Optional[List[CodeableConcept]] = None
	quantity: Optional[Quantity] = None
	unitPrice: Optional[Money] = None
	factor: Optional[float] = None
	net: Optional[Money] = None
	noteNumber: Optional[List[PositiveInt]] = None
	adjudication: Optional[List[str]] = None

class ExplanationOfBenefit_AddItem_Detail(BackboneElement):
	modifier: Optional[List[CodeableConcept]] = None
	adjudication: Optional[List[str]] = None
	net: Optional[Money] = None
	productOrService: CodeableConcept
	factor: Optional[float] = None
	subDetail: Optional[List[ExplanationOfBenefit_AddItem_Detail_SubDetail]] = None
	quantity: Optional[Quantity] = None
	noteNumber: Optional[List[PositiveInt]] = None
	unitPrice: Optional[Money] = None

class ExplanationOfBenefit_AddItem(BackboneElement):
	locationAddress: Optional[Address] = None
	modifier: Optional[List[CodeableConcept]] = None
	adjudication: Optional[List[str]] = None
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
	subDetailSequence: Optional[List[PositiveInt]] = None
	bodySite: Optional[CodeableConcept] = None
	quantity: Optional[Quantity] = None
	provider: Optional[List[Reference]] = None
	noteNumber: Optional[List[PositiveInt]] = None
	unitPrice: Optional[Money] = None
	servicedPeriod: Optional[Period] = None
	detail: Optional[List[ExplanationOfBenefit_AddItem_Detail]] = None

class ExplanationOfBenefit_CareTeam(BackboneElement):
	sequence: PositiveInt
	provider: Reference
	responsible: Optional[bool] = None
	role: Optional[CodeableConcept] = None
	qualification: Optional[CodeableConcept] = None

class ExplanationOfBenefit(DomainResource):
	patient: Reference
	claimResponse: Optional[Reference] = None
	insurance: List[ExplanationOfBenefit_Insurance]
	benefitBalance: Optional[List[ExplanationOfBenefit_BenefitBalance]] = None
	facility: Optional[Reference] = None
	processNote: Optional[List[ExplanationOfBenefit_ProcessNote]] = None
	diagnosis: Optional[List[ExplanationOfBenefit_Diagnosis]] = None
	preAuthRef: Optional[List[str]] = None
	adjudication: Optional[List[str]] = None
	enterer: Optional[Reference] = None
	supportingInfo: Optional[List[ExplanationOfBenefit_SupportingInfo]] = None
	use: str
	payment: Optional[ExplanationOfBenefit_Payment] = None
	item: Optional[List[ExplanationOfBenefit_Item]] = None
	type: CodeableConcept
	created: str
	procedure: Optional[List[ExplanationOfBenefit_Procedure]] = None
	outcome: str
	related: Optional[List[ExplanationOfBenefit_Related]] = None
	disposition: Optional[str] = None
	referral: Optional[Reference] = None
	preAuthRefPeriod: Optional[List[Period]] = None
	total: Optional[List[ExplanationOfBenefit_Total]] = None
	insurer: Reference
	fundsReserve: Optional[CodeableConcept] = None
	priority: Optional[CodeableConcept] = None
	accident: Optional[ExplanationOfBenefit_Accident] = None
	status: str
	payee: Optional[ExplanationOfBenefit_Payee] = None
	prescription: Optional[Reference] = None
	billablePeriod: Optional[Period] = None
	identifier: Optional[List[Identifier]] = None
	form: Optional[Attachment] = None
	subType: Optional[CodeableConcept] = None
	fundsReserveRequested: Optional[CodeableConcept] = None
	benefitPeriod: Optional[Period] = None
	precedence: Optional[PositiveInt] = None
	formCode: Optional[CodeableConcept] = None
	provider: Reference
	addItem: Optional[List[ExplanationOfBenefit_AddItem]] = None
	originalPrescription: Optional[Reference] = None
	careTeam: Optional[List[ExplanationOfBenefit_CareTeam]] = None
	claim: Optional[Reference] = None