from typing import Optional
from ..base import *

class Composition_Section(BackboneElement):
	orderedBy: Optional[CodeableConcept] = None
	section: list[str] = []
	mode: Optional[str] = None
	title: Optional[str] = None
	emptyReason: Optional[CodeableConcept] = None
	author: list[Reference] = []
	code: Optional[CodeableConcept] = None
	focus: Optional[Reference] = None
	entry: list[Reference] = []
	text: Optional[Narrative] = None

class Composition_Attester(BackboneElement):
	mode: str
	party: Optional[Reference] = None
	time: Optional[str] = None

class Composition_Event(BackboneElement):
	code: list[CodeableConcept] = []
	detail: list[Reference] = []
	period: Optional[Period] = None

class Composition_RelatesTo(BackboneElement):
	code: str
	targetIdentifier: Optional[Identifier] = None
	targetReference: Optional[Reference] = None

class Composition(DomainResource):
	category: list[CodeableConcept] = []
	date: str
	encounter: Optional[Reference] = None
	section: list[Composition_Section] = []
	attester: list[Composition_Attester] = []
	type: CodeableConcept
	title: str
	author: list[Reference]
	event: list[Composition_Event] = []
	custodian: Optional[Reference] = None
	status: str
	identifier: Optional[Identifier] = None
	relatesTo: list[Composition_RelatesTo] = []
	subject: Optional[Reference] = None
	confidentiality: Optional[str] = None

