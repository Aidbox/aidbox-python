from typing import Optional
from base import *

class Questionnaire_Item_EnableWhen(BackboneElement):
	answerQuantity: Optional[Quantity] = None
	answerDecimal: Optional[str] = None
	answerDate: Optional[str] = None
	answerReference: Optional[Reference] = None
	answerInteger: Optional[int] = None
	question: str
	answerDateTime: Optional[str] = None
	answerString: Optional[str] = None
	operator: str
	answerBoolean: Optional[bool] = None
	answerCoding: Optional[Coding] = None
	answerTime: Optional[str] = None

class Questionnaire_Item_AnswerOption(BackboneElement):
	initialSelected: Optional[bool] = None
	valueCoding: Optional[Coding] = None
	valueDate: Optional[str] = None
	valueInteger: Optional[int] = None
	valueReference: Optional[Reference] = None
	valueString: Optional[str] = None
	valueTime: Optional[str] = None

class Questionnaire_Item_Initial(BackboneElement):
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

class Questionnaire_Item(BackboneElement):
	enableBehavior: Optional[str] = None
	definition: Optional[str] = None
	linkId: str
	repeats: Optional[bool] = None
	item: list[str] = []
	type: str
	enableWhen: list[Questionnaire_Item_EnableWhen] = []
	answerOption: list[Questionnaire_Item_AnswerOption] = []
	prefix: Optional[str] = None
	readOnly: Optional[bool] = None
	answerValueSet: Optional[str] = None
	code: list[Coding] = []
	initial: list[Questionnaire_Item_Initial] = []
	maxLength: Optional[int] = None
	required: Optional[bool] = None
	text: Optional[str] = None

class Questionnaire(DomainResource):
	description: Optional[str] = None
	subjectType: list[str] = []
	date: Optional[str] = None
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	derivedFrom: list[str] = []
	purpose: Optional[str] = None
	name: Optional[str] = None
	item: list[Questionnaire_Item] = []
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	status: str
	url: Optional[str] = None
	code: list[Coding] = []
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []
	effectivePeriod: Optional[Period] = None

