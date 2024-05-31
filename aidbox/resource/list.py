from pydantic import *
from typing import Optional, List
from ..base import *

class List_Entry(BackboneElement):
	flag: Optional[CodeableConcept] = None
	deleted: Optional[bool] = None
	date: Optional[str] = None
	item: Reference

class List(DomainResource):
	date: Optional[str] = None
	encounter: Optional[Reference] = None
	orderedBy: Optional[CodeableConcept] = None
	mode: str
	source: Optional[Reference] = None
	title: Optional[str] = None
	note: Optional[List[Annotation]] = None
	emptyReason: Optional[CodeableConcept] = None
	status: str
	code: Optional[CodeableConcept] = None
	identifier: Optional[List[Identifier]] = None
	entry: Optional[List[List_Entry]] = None
	subject: Optional[Reference] = None