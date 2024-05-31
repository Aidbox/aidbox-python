from pydantic import *
from typing import Optional, List
from ..base import *

class Claim_Insurance(BackboneElement):
	sequence: PositiveInt
	focal: bool
	identifier: Optional[Identifier] = None
	coverage: Reference
	businessArrangement: Optional[str] = None
	preAuthRef: Optional[List[str]] = None
	claimResponse: Optional[Reference] = None

class Claim_Diagnosis(BackboneElement):
	sequence: PositiveInt
	diagnosisCodeableConcept: Optional[CodeableConcept] = None
	diagnosisReference: Optional[Reference] = None
	type: Optional[List[CodeableConcept]] = None
	onAdmission: Optional[CodeableConcept] = None
	packageCode: Optional[CodeableConcept] = None

class Claim_SupportingInfo(BackboneElement):
	category: CodeableConcept
	valueReference: Optional[Reference] = None
	valueQuantity: Optional[Quantity] = None
	timingPeriod: Optional[Period] = None
	valueString: Optional[str] = None
	valueBoolean: Optional[bool] = None
	reason: Optional[CodeableConcept] = None
	sequence: PositiveInt
	code: Optional[CodeableConcept] = None
	timingDate: Optional[str] = None
	valueAttachment: Optional[Attachment] = None

class Claim_Item_Detail_SubDetail(BackboneElement):
	category: Optional[CodeableConcept] = None
	modifier: Optional[List[CodeableConcept]] = None
	revenue: Optional[CodeableConcept] = None
	net: Optional[Money] = None
	productOrService: CodeableConcept
	udi: Optional[List[Reference]] = None
	programCode: Optional[List[CodeableConcept]] = None
	factor: Optional[float] = None
	sequence: PositiveInt
	quantity: Optional[Quantity] = None
	unitPrice: Optional[Money] = None

class Claim_Item_Detail(BackboneElement):
	category: Optional[CodeableConcept] = None
	modifier: Optional[List[CodeableConcept]] = None
	revenue: Optional[CodeableConcept] = None
	net: Optional[Money] = None
	productOrService: CodeableConcept
	udi: Optional[List[Reference]] = None
	programCode: Optional[List[CodeableConcept]] = None
	factor: Optional[float] = None
	sequence: PositiveInt
	subDetail: Optional[List[Claim_Item_Detail_SubDetail]] = None
	quantity: Optional[Quantity] = None
	unitPrice: Optional[Money] = None

class Claim_Item(BackboneElement):
	category: Optional[CodeableConcept] = None
	diagnosisSequence: Optional[List[PositiveInt]] = None
	procedureSequence: Optional[List[PositiveInt]] = None
	locationAddress: Optional[Address] = None
	modifier: Optional[List[CodeableConcept]] = None
	revenue: Optional[CodeableConcept] = None
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
	unitPrice: Optional[Money] = None
	servicedPeriod: Optional[Period] = None
	detail: Optional[List[Claim_Item_Detail]] = None

class Claim_Procedure(BackboneElement):
	sequence: PositiveInt
	type: Optional[List[CodeableConcept]] = None
	date: Optional[str] = None
	procedureCodeableConcept: Optional[CodeableConcept] = None
	procedureReference: Optional[Reference] = None
	udi: Optional[List[Reference]] = None

class Claim_Related(BackboneElement):
	claim: Optional[Reference] = None
	relationship: Optional[CodeableConcept] = None
	reference: Optional[Identifier] = None

class Claim_Accident(BackboneElement):
	date: str
	type: Optional[CodeableConcept] = None
	locationAddress: Optional[Address] = None
	locationReference: Optional[Reference] = None

class Claim_Payee(BackboneElement):
	type: CodeableConcept
	party: Optional[Reference] = None

class Claim_CareTeam(BackboneElement):
	sequence: PositiveInt
	provider: Reference
	responsible: Optional[bool] = None
	role: Optional[CodeableConcept] = None
	qualification: Optional[CodeableConcept] = None

class Claim(DomainResource):
	patient: Reference
	insurance: List[Claim_Insurance]
	facility: Optional[Reference] = None
	diagnosis: Optional[List[Claim_Diagnosis]] = None
	enterer: Optional[Reference] = None
	supportingInfo: Optional[List[Claim_SupportingInfo]] = None
	use: str
	item: Optional[List[Claim_Item]] = None
	type: CodeableConcept
	created: str
	procedure: Optional[List[Claim_Procedure]] = None
	related: Optional[List[Claim_Related]] = None
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
	identifier: Optional[List[Identifier]] = None
	subType: Optional[CodeableConcept] = None
	provider: Reference
	originalPrescription: Optional[Reference] = None
	careTeam: Optional[List[Claim_CareTeam]] = None