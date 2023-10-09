from typing import Optional
from ..base import *

class Contract_Rule(BackboneElement):
	contentAttachment: Optional[Attachment] = None
	contentReference: Optional[Reference] = None

class Contract_Legal(BackboneElement):
	contentAttachment: Optional[Attachment] = None
	contentReference: Optional[Reference] = None

class Contract_ContentDefinition(BackboneElement):
	copyright: Optional[str] = None
	publicationDate: Optional[str] = None
	publicationStatus: str
	publisher: Optional[Reference] = None
	subType: Optional[CodeableConcept] = None
	type: CodeableConcept

class Contract_Signer(BackboneElement):
	party: Reference
	signature: list[Signature]
	type: Coding

class Contract_Term_Offer_Party(BackboneElement):
	reference: list[Reference]
	role: CodeableConcept

class Contract_Term_Offer_Answer(BackboneElement):
	valueReference: Optional[Reference] = None
	valueUri: Optional[str] = None
	valueTime: Optional[str] = None
	valueDecimal: Optional[str] = None
	valueQuantity: Optional[Quantity] = None
	valueString: Optional[str] = None
	valueBoolean: Optional[bool] = None
	valueDateTime: Optional[str] = None
	valueDate: Optional[str] = None
	valueCoding: Optional[Coding] = None
	valueInteger: Optional[int] = None
	valueAttachment: Optional[Attachment] = None

class Contract_Term_Offer(BackboneElement):
	party: list[Contract_Term_Offer_Party] = []
	linkId: list[str] = []
	decisionMode: list[CodeableConcept] = []
	type: Optional[CodeableConcept] = None
	topic: Optional[Reference] = None
	securityLabelNumber: list[str] = []
	answer: list[Contract_Term_Offer_Answer] = []
	identifier: list[Identifier] = []
	decision: Optional[CodeableConcept] = None
	text: Optional[str] = None

class Contract_Term_Action_Subject(BackboneElement):
	reference: list[Reference]
	role: Optional[CodeableConcept] = None

class Contract_Term_Action(BackboneElement):
	requesterLinkId: list[str] = []
	performerType: list[CodeableConcept] = []
	linkId: list[str] = []
	performerRole: Optional[CodeableConcept] = None
	reasonLinkId: list[str] = []
	reasonCode: list[CodeableConcept] = []
	type: CodeableConcept
	occurrenceTiming: Optional[str] = None
	note: list[Annotation] = []
	reason: list[str] = []
	requester: list[Reference] = []
	securityLabelNumber: list[str] = []
	occurrencePeriod: Optional[Period] = None
	status: CodeableConcept
	doNotPerform: Optional[bool] = None
	context: Optional[Reference] = None
	intent: CodeableConcept
	performerLinkId: list[str] = []
	occurrenceDateTime: Optional[str] = None
	subject: list[Contract_Term_Action_Subject] = []
	performer: Optional[Reference] = None
	contextLinkId: list[str] = []
	reasonReference: list[Reference] = []

class Contract_Term_SecurityLabel(BackboneElement):
	category: list[Coding] = []
	classification: Coding
	control: list[Coding] = []
	number: list[str] = []

class Contract_Term_Asset_Context(BackboneElement):
	code: list[CodeableConcept] = []
	reference: Optional[Reference] = None
	text: Optional[str] = None

class Contract_Term_Asset_ValuedItem(BackboneElement):
	linkId: list[str] = []
	payment: Optional[str] = None
	recipient: Optional[Reference] = None
	net: Optional[Money] = None
	points: Optional[str] = None
	responsible: Optional[Reference] = None
	securityLabelNumber: list[str] = []
	factor: Optional[str] = None
	paymentDate: Optional[str] = None
	entityCodeableConcept: Optional[CodeableConcept] = None
	identifier: Optional[Identifier] = None
	effectiveTime: Optional[str] = None
	quantity: Optional[Quantity] = None
	unitPrice: Optional[Money] = None
	entityReference: Optional[Reference] = None

class Contract_Term_Asset(BackboneElement):
	periodType: list[CodeableConcept] = []
	usePeriod: list[Period] = []
	linkId: list[str] = []
	relationship: Optional[Coding] = None
	type: list[CodeableConcept] = []
	scope: Optional[CodeableConcept] = None
	securityLabelNumber: list[str] = []
	typeReference: list[Reference] = []
	condition: Optional[str] = None
	answer: list[str] = []
	context: list[Contract_Term_Asset_Context] = []
	period: list[Period] = []
	valuedItem: list[Contract_Term_Asset_ValuedItem] = []
	subtype: list[CodeableConcept] = []
	text: Optional[str] = None

class Contract_Term(BackboneElement):
	group: list[str] = []
	applies: Optional[Period] = None
	offer: Contract_Term_Offer
	type: Optional[CodeableConcept] = None
	topicCodeableConcept: Optional[CodeableConcept] = None
	topicReference: Optional[Reference] = None
	identifier: Optional[Identifier] = None
	action: list[Contract_Term_Action] = []
	issued: Optional[str] = None
	subType: Optional[CodeableConcept] = None
	securityLabel: list[Contract_Term_SecurityLabel] = []
	asset: list[Contract_Term_Asset] = []
	text: Optional[str] = None

class Contract_Friendly(BackboneElement):
	contentAttachment: Optional[Attachment] = None
	contentReference: Optional[Reference] = None

class Contract(DomainResource):
	legallyBindingAttachment: Optional[Attachment] = None
	instantiatesCanonical: Optional[Reference] = None
	instantiatesUri: Optional[str] = None
	legallyBindingReference: Optional[Reference] = None
	site: list[Reference] = []
	relevantHistory: list[Reference] = []
	supportingInfo: list[Reference] = []
	applies: Optional[Period] = None
	name: Optional[str] = None
	authority: list[Reference] = []
	rule: list[Contract_Rule] = []
	type: Optional[CodeableConcept] = None
	legal: list[Contract_Legal] = []
	contentDerivative: Optional[CodeableConcept] = None
	topicCodeableConcept: Optional[CodeableConcept] = None
	legalState: Optional[CodeableConcept] = None
	contentDefinition: Optional[Contract_ContentDefinition] = None
	scope: Optional[CodeableConcept] = None
	title: Optional[str] = None
	signer: list[Contract_Signer] = []
	author: Optional[Reference] = None
	term: list[Contract_Term] = []
	friendly: list[Contract_Friendly] = []
	alias: list[str] = []
	status: Optional[str] = None
	subtitle: Optional[str] = None
	topicReference: Optional[Reference] = None
	url: Optional[str] = None
	identifier: list[Identifier] = []
	expirationType: Optional[CodeableConcept] = None
	issued: Optional[str] = None
	domain: list[Reference] = []
	subType: list[CodeableConcept] = []
	version: Optional[str] = None
	subject: list[Reference] = []

