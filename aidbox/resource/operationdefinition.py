from pydantic import *
from typing import Optional, List
from ..base import *

class OperationDefinition_Overload(BackboneElement):
	parameterName: Optional[List[str]] = None
	comment: Optional[str] = None

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
	part: Optional[List[str]] = None
	type: Optional[str] = None
	referencedFrom: Optional[List[OperationDefinition_Parameter_ReferencedFrom]] = None
	documentation: Optional[str] = None
	binding: Optional[OperationDefinition_Parameter_Binding] = None
	max: str
	targetProfile: Optional[List[str]] = None

class OperationDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	system: bool
	publisher: Optional[str] = None
	instance: bool
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	name: str
	useContext: Optional[List[UsageContext]] = None
	type: bool
	overload: Optional[List[OperationDefinition_Overload]] = None
	experimental: Optional[bool] = None
	outputProfile: Optional[str] = None
	title: Optional[str] = None
	status: str
	resource: Optional[List[str]] = None
	affectsState: Optional[bool] = None
	kind: str
	comment: Optional[str] = None
	url: Optional[str] = None
	code: str
	base: Optional[str] = None
	version: Optional[str] = None
	contact: Optional[List[ContactDetail]] = None
	inputProfile: Optional[str] = None
	parameter: Optional[List[OperationDefinition_Parameter]] = None