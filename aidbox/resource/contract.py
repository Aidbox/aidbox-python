from pydantic import *
from typing import Optional, List
from ..base import *

class Contract_Rule(BackboneElement):
	contentAttachment: Optional[Attachment] = None
	contentReference: Optional[Reference] = None

class Contract_Legal(BackboneElement):
	contentAttachment: Optional[Attachment] = None
	contentReference: Optional[Reference] = None

class Contract_ContentDefinition(BackboneElement):
	type: CodeableConcept
	subType: Optional[CodeableConcept] = None
	publisher: Optional[Reference] = None
	publicationDate: Optional[str] = None
	publicationStatus: str
	copyright: Optional[str] = None

class Contract_Signer(BackboneElement):
	type: Coding
	party: Reference
	signature: List[Signature]

class Contract_Term_Offer_Party(BackboneElement):
	reference: List[Reference]
	role: CodeableConcept

class Contract_Term_Offer_Answer(BackboneElement):
	valueReference: Optional[Reference] = None
	valueUri: Optional[str] = None
	valueTime: Optional[str] = None
	valueDecimal: Optional[float] = None
	valueQuantity: Optional[Quantity] = None
	valueString: Optional[str] = None
	valueBoolean: Optional[bool] = None
	valueDateTime: Optional[str] = None
	valueDate: Optional[str] = None
	valueCoding: Optional[Coding] = None
	valueInteger: Optional[int] = None
	valueAttachment: Optional[Attachment] = None

class Contract_Term_Offer(BackboneElement):
	party: Optional[List[Contract_Term_Offer_Party]] = None
	linkId: Optional[List[str]] = None
	decisionMode: Optional[List[CodeableConcept]] = None
	type: Optional[CodeableConcept] = None
	topic: Optional[Reference] = None
	securityLabelNumber: Optional[List[NonNegativeInt]] = None
	answer: Optional[List[Contract_Term_Offer_Answer]] = None
	identifier: Optional[List[Identifier]] = None
	decision: Optional[CodeableConcept] = None
	text: Optional[str] = None

class Contract_Term_Action_Subject(BackboneElement):
	reference: List[Reference]
	role: Optional[CodeableConcept] = None

class Contract_Term_Action(BackboneElement):
	requesterLinkId: Optional[List[str]] = None
	performerType: Optional[List[CodeableConcept]] = None
	linkId: Optional[List[str]] = None
	performerRole: Optional[CodeableConcept] = None
	reasonLinkId: Optional[List[str]] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	type: CodeableConcept
	occurrenceTiming: Optional[Timing] = None
	note: Optional[List[Annotation]] = None
	reason: Optional[List[str]] = None
	requester: Optional[List[Reference]] = None
	securityLabelNumber: Optional[List[NonNegativeInt]] = None
	occurrencePeriod: Optional[Period] = None
	status: CodeableConcept
	doNotPerform: Optional[bool] = None
	context: Optional[Reference] = None
	intent: CodeableConcept
	performerLinkId: Optional[List[str]] = None
	occurrenceDateTime: Optional[str] = None
	subject: Optional[List[Contract_Term_Action_Subject]] = None
	performer: Optional[Reference] = None
	contextLinkId: Optional[List[str]] = None
	reasonReference: Optional[List[Reference]] = None

class Contract_Term_SecurityLabel(BackboneElement):
	number: Optional[List[NonNegativeInt]] = None
	classification: Coding
	category: Optional[List[Coding]] = None
	control: Optional[List[Coding]] = None

class Contract_Term_Asset_Context(BackboneElement):
	reference: Optional[Reference] = None
	code: Optional[List[CodeableConcept]] = None
	text: Optional[str] = None

class Contract_Term_Asset_ValuedItem(BackboneElement):
	linkId: Optional[List[str]] = None
	payment: Optional[str] = None
	recipient: Optional[Reference] = None
	net: Optional[Money] = None
	points: Optional[float] = None
	responsible: Optional[Reference] = None
	securityLabelNumber: Optional[List[NonNegativeInt]] = None
	factor: Optional[float] = None
	paymentDate: Optional[str] = None
	entityCodeableConcept: Optional[CodeableConcept] = None
	identifier: Optional[Identifier] = None
	effectiveTime: Optional[str] = None
	quantity: Optional[Quantity] = None
	unitPrice: Optional[Money] = None
	entityReference: Optional[Reference] = None

class Contract_Term_Asset(BackboneElement):
	periodType: Optional[List[CodeableConcept]] = None
	usePeriod: Optional[List[Period]] = None
	linkId: Optional[List[str]] = None
	relationship: Optional[Coding] = None
	type: Optional[List[CodeableConcept]] = None
	scope: Optional[CodeableConcept] = None
	securityLabelNumber: Optional[List[NonNegativeInt]] = None
	typeReference: Optional[List[Reference]] = None
	condition: Optional[str] = None
	answer: Optional[List[str]] = None
	context: Optional[List[Contract_Term_Asset_Context]] = None
	period: Optional[List[Period]] = None
	valuedItem: Optional[List[Contract_Term_Asset_ValuedItem]] = None
	subtype: Optional[List[CodeableConcept]] = None
	text: Optional[str] = None

class Contract_Term(BackboneElement):
	group: Optional[List[str]] = None
	applies: Optional[Period] = None
	offer: Contract_Term_Offer
	type: Optional[CodeableConcept] = None
	topicCodeableConcept: Optional[CodeableConcept] = None
	topicReference: Optional[Reference] = None
	identifier: Optional[Identifier] = None
	action: Optional[List[Contract_Term_Action]] = None
	issued: Optional[str] = None
	subType: Optional[CodeableConcept] = None
	securityLabel: Optional[List[Contract_Term_SecurityLabel]] = None
	asset: Optional[List[Contract_Term_Asset]] = None
	text: Optional[str] = None

class Contract_Friendly(BackboneElement):
	contentAttachment: Optional[Attachment] = None
	contentReference: Optional[Reference] = None

class Contract(DomainResource):
	legallyBindingAttachment: Optional[Attachment] = None
	instantiatesCanonical: Optional[Reference] = None
	instantiatesUri: Optional[str] = None
	legallyBindingReference: Optional[Reference] = None
	site: Optional[List[Reference]] = None
	relevantHistory: Optional[List[Reference]] = None
	supportingInfo: Optional[List[Reference]] = None
	applies: Optional[Period] = None
	name: Optional[str] = None
	authority: Optional[List[Reference]] = None
	rule: Optional[List[Contract_Rule]] = None
	type: Optional[CodeableConcept] = None
	legal: Optional[List[Contract_Legal]] = None
	contentDerivative: Optional[CodeableConcept] = None
	topicCodeableConcept: Optional[CodeableConcept] = None
	legalState: Optional[CodeableConcept] = None
	contentDefinition: Optional[Contract_ContentDefinition] = None
	scope: Optional[CodeableConcept] = None
	title: Optional[str] = None
	signer: Optional[List[Contract_Signer]] = None
	author: Optional[Reference] = None
	term: Optional[List[Contract_Term]] = None
	friendly: Optional[List[Contract_Friendly]] = None
	alias: Optional[List[str]] = None
	status: Optional[str] = None
	subtitle: Optional[str] = None
	topicReference: Optional[Reference] = None
	url: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	expirationType: Optional[CodeableConcept] = None
	issued: Optional[str] = None
	domain: Optional[List[Reference]] = None
	subType: Optional[List[CodeableConcept]] = None
	version: Optional[str] = None
	subject: Optional[List[Reference]] = None