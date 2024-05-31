from pydantic import *
from typing import Optional, List
from ..base import *

class QuestionnaireResponse_Item_Answer(BackboneElement):
	valueReference: Optional[Reference] = None
	valueUri: Optional[str] = None
	valueTime: Optional[str] = None
	valueDecimal: Optional[float] = None
	valueQuantity: Optional[Quantity] = None
	item: Optional[List[str]] = None
	valueString: Optional[str] = None
	valueBoolean: Optional[bool] = None
	valueDateTime: Optional[str] = None
	valueDate: Optional[str] = None
	valueCoding: Optional[Coding] = None
	valueInteger: Optional[int] = None
	valueAttachment: Optional[Attachment] = None

class QuestionnaireResponse_Item(BackboneElement):
	linkId: str
	definition: Optional[str] = None
	text: Optional[str] = None
	answer: Optional[List[QuestionnaireResponse_Item_Answer]] = None
	item: Optional[List[str]] = None

class QuestionnaireResponse(DomainResource):
	questionnaire: Optional[str] = None
	encounter: Optional[Reference] = None
	item: Optional[List[QuestionnaireResponse_Item]] = None
	source: Optional[Reference] = None
	author: Optional[Reference] = None
	status: str
	identifier: Optional[Identifier] = None
	basedOn: Optional[List[Reference]] = None
	authored: Optional[str] = None
	partOf: Optional[List[Reference]] = None
	subject: Optional[Reference] = None