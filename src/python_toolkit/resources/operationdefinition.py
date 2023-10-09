from typing import Optional
from base import *

class OperationDefinition_Overload(BackboneElement):
	comment: Optional[str] = None
	parameterName: list[str] = []

class OperationDefinition_Parameter_ReferencedFrom(BackboneElement):
	source: str
	sourceId: Optional[str] = None

class OperationDefinition_Parameter_Binding(BackboneElement):
	strength: str
	valueSet: str

class OperationDefinition_Parameter(BackboneElement):
	min: int
	searchType: Optional[str] = None
	use: str
	name: str
	part: list[str] = []
	type: Optional[str] = None
	referencedFrom: list[OperationDefinition_Parameter_ReferencedFrom] = []
	documentation: Optional[str] = None
	binding: Optional[OperationDefinition_Parameter_Binding] = None
	max: str
	targetProfile: list[str] = []

class OperationDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	system: bool
	publisher: Optional[str] = None
	instance: bool
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: str
	useContext: list[UsageContext] = []
	type: bool
	overload: list[OperationDefinition_Overload] = []
	experimental: Optional[bool] = None
	outputProfile: Optional[str] = None
	title: Optional[str] = None
	status: str
	resource: list[str] = []
	affectsState: Optional[bool] = None
	kind: str
	comment: Optional[str] = None
	url: Optional[str] = None
	code: str
	base: Optional[str] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []
	inputProfile: Optional[str] = None
	parameter: list[OperationDefinition_Parameter] = []

