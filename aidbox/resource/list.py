from typing import Optional
from ..base import *

class List_Entry(BackboneElement):
	date: Optional[str] = None
	deleted: Optional[bool] = None
	flag: Optional[CodeableConcept] = None
	item: Reference

class List(DomainResource):
	date: Optional[str] = None
	encounter: Optional[Reference] = None
	orderedBy: Optional[CodeableConcept] = None
	mode: str
	source: Optional[Reference] = None
	title: Optional[str] = None
	note: list[Annotation] = []
	emptyReason: Optional[CodeableConcept] = None
	status: str
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	entry: list[List_Entry] = []
	subject: Optional[Reference] = None

