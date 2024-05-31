from pydantic import *
from typing import Optional, List
from ..base import *

class Composition_Section(BackboneElement):
	orderedBy: Optional[CodeableConcept] = None
	section: Optional[List[str]] = None
	mode: Optional[str] = None
	title: Optional[str] = None
	emptyReason: Optional[CodeableConcept] = None
	author: Optional[List[Reference]] = None
	code: Optional[CodeableConcept] = None
	focus: Optional[Reference] = None
	entry: Optional[List[Reference]] = None
	text: Optional[Narrative] = None

class Composition_Attester(BackboneElement):
	mode: str
	time: Optional[str] = None
	party: Optional[Reference] = None

class Composition_Event(BackboneElement):
	code: Optional[List[CodeableConcept]] = None
	period: Optional[Period] = None
	detail: Optional[List[Reference]] = None

class Composition_RelatesTo(BackboneElement):
	code: str
	targetIdentifier: Optional[Identifier] = None
	targetReference: Optional[Reference] = None

class Composition(DomainResource):
	category: Optional[List[CodeableConcept]] = None
	date: str
	encounter: Optional[Reference] = None
	section: Optional[List[Composition_Section]] = None
	attester: Optional[List[Composition_Attester]] = None
	type: CodeableConcept
	title: str
	author: List[Reference]
	event: Optional[List[Composition_Event]] = None
	custodian: Optional[Reference] = None
	status: str
	identifier: Optional[Identifier] = None
	relatesTo: Optional[List[Composition_RelatesTo]] = None
	subject: Optional[Reference] = None
	confidentiality: Optional[str] = None