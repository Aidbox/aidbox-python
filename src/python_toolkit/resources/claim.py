from typing import Optional
from base import *

class Claim_Insurance(BackboneElement):
	businessArrangement: Optional[str] = None
	claimResponse: Optional[Reference] = None
	coverage: Reference
	focal: bool
	identifier: Optional[Identifier] = None
	preAuthRef: list[str] = []
	sequence: str

class Claim_Diagnosis(BackboneElement):
	diagnosisCodeableConcept: Optional[CodeableConcept] = None
	diagnosisReference: Optional[Reference] = None
	onAdmission: Optional[CodeableConcept] = None
	packageCode: Optional[CodeableConcept] = None
	sequence: str
	type: list[CodeableConcept] = []

class Claim_SupportingInfo(BackboneElement):
	category: CodeableConcept
	valueReference: Optional[Reference] = None
	valueQuantity: Optional[Quantity] = None
	timingPeriod: Optional[Period] = None
	valueString: Optional[str] = None
	valueBoolean: Optional[bool] = None
	reason: Optional[CodeableConcept] = None
	sequence: str
	code: Optional[CodeableConcept] = None
	timingDate: Optional[str] = None
	valueAttachment: Optional[Attachment] = None

class Claim_Item_Detail_SubDetail(BackboneElement):
	category: Optional[CodeableConcept] = None
	modifier: list[CodeableConcept] = []
	revenue: Optional[CodeableConcept] = None
	net: Optional[Money] = None
	productOrService: CodeableConcept
	udi: list[Reference] = []
	programCode: list[CodeableConcept] = []
	factor: Optional[str] = None
	sequence: str
	quantity: Optional[Quantity] = None
	unitPrice: Optional[Money] = None

class Claim_Item_Detail(BackboneElement):
	category: Optional[CodeableConcept] = None
	modifier: list[CodeableConcept] = []
	revenue: Optional[CodeableConcept] = None
	net: Optional[Money] = None
	productOrService: CodeableConcept
	udi: list[Reference] = []
	programCode: list[CodeableConcept] = []
	factor: Optional[str] = None
	sequence: str
	subDetail: list[Claim_Item_Detail_SubDetail] = []
	quantity: Optional[Quantity] = None
	unitPrice: Optional[Money] = None

class Claim_Item(BackboneElement):
	category: Optional[CodeableConcept] = None
	diagnosisSequence: list[str] = []
	procedureSequence: list[str] = []
	locationAddress: Optional[Address] = None
	modifier: list[CodeableConcept] = []
	revenue: Optional[CodeableConcept] = None
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
	unitPrice: Optional[Money] = None
	servicedPeriod: Optional[Period] = None
	detail: list[Claim_Item_Detail] = []

class Claim_Procedure(BackboneElement):
	date: Optional[str] = None
	procedureCodeableConcept: Optional[CodeableConcept] = None
	procedureReference: Optional[Reference] = None
	sequence: str
	type: list[CodeableConcept] = []
	udi: list[Reference] = []

class Claim_Related(BackboneElement):
	claim: Optional[Reference] = None
	reference: Optional[Identifier] = None
	relationship: Optional[CodeableConcept] = None

class Claim_Accident(BackboneElement):
	date: str
	locationAddress: Optional[Address] = None
	locationReference: Optional[Reference] = None
	type: Optional[CodeableConcept] = None

class Claim_Payee(BackboneElement):
	party: Optional[Reference] = None
	type: CodeableConcept

class Claim_CareTeam(BackboneElement):
	provider: Reference
	qualification: Optional[CodeableConcept] = None
	responsible: Optional[bool] = None
	role: Optional[CodeableConcept] = None
	sequence: str

class Claim(DomainResource):
	patient: Reference
	insurance: list[Claim_Insurance]
	facility: Optional[Reference] = None
	diagnosis: list[Claim_Diagnosis] = []
	enterer: Optional[Reference] = None
	supportingInfo: list[Claim_SupportingInfo] = []
	use: str
	item: list[Claim_Item] = []
	type: CodeableConcept
	created: str
	procedure: list[Claim_Procedure] = []
	related: list[Claim_Related] = []
	referral: Optional[Reference] = None
	total: Optional[Money] = None
	insurer: Optional[Reference] = None
	fundsReserve: Optional[CodeableConcept] = None
	priority: CodeableConcept
	accident: Optional[Claim_Accident] = None
	status: str
	payee: Optional[Claim_Payee] = None
	prescription: Optional[Reference] = None
	billablePeriod: Optional[Period] = None
	identifier: list[Identifier] = []
	subType: Optional[CodeableConcept] = None
	provider: Reference
	originalPrescription: Optional[Reference] = None
	careTeam: list[Claim_CareTeam] = []

