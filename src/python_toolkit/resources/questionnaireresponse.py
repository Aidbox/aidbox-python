from typing import Optional
from base import *

class QuestionnaireResponse_Item_Answer(BackboneElement):
	valueReference: Optional[Reference] = None
	valueUri: Optional[str] = None
	valueTime: Optional[str] = None
	valueDecimal: Optional[str] = None
	valueQuantity: Optional[Quantity] = None
	item: list[str] = []
	valueString: Optional[str] = None
	valueBoolean: Optional[bool] = None
	valueDateTime: Optional[str] = None
	valueDate: Optional[str] = None
	valueCoding: Optional[Coding] = None
	valueInteger: Optional[int] = None
	valueAttachment: Optional[Attachment] = None

class QuestionnaireResponse_Item(BackboneElement):
	answer: list[QuestionnaireResponse_Item_Answer] = []
	definition: Optional[str] = None
	item: list[str] = []
	linkId: str
	text: Optional[str] = None

class QuestionnaireResponse(DomainResource):
	questionnaire: Optional[str] = None
	encounter: Optional[Reference] = None
	item: list[QuestionnaireResponse_Item] = []
	source: Optional[Reference] = None
	author: Optional[Reference] = None
	status: str
	identifier: Optional[Identifier] = None
	basedOn: list[Reference] = []
	authored: Optional[str] = None
	partOf: list[Reference] = []
	subject: Optional[Reference] = None

