from pydantic import *
from typing import Optional, List
from ..base import *

class StructureMap_Group_Input(BackboneElement):
	name: str
	type: Optional[str] = None
	mode: str
	documentation: Optional[str] = None

class StructureMap_Group_Rule_Source(BackboneElement):
	defaultValueTime: Optional[str] = None
	defaultValueDataRequirement: Optional[DataRequirement] = None
	min: Optional[int] = None
	defaultValueMoney: Optional[Money] = None
	defaultValueContactPoint: Optional[ContactPoint] = None
	defaultValueMeta: Optional[Meta] = None
	defaultValueCoding: Optional[Coding] = None
	variable: Optional[str] = None
	defaultValueCode: Optional[str] = None
	element: Optional[str] = None
	defaultValueSampledData: Optional[SampledData] = None
	defaultValueMarkdown: Optional[str] = None
	defaultValueHumanName: Optional[HumanName] = None
	defaultValueDuration: Optional[Duration] = None
	defaultValueDecimal: Optional[float] = None
	defaultValueUri: Optional[str] = None
	check: Optional[str] = None
	defaultValueQuantity: Optional[Quantity] = None
	defaultValueCount: Optional[Count] = None
	defaultValueId: Optional[str] = None
	defaultValueBase64Binary: Optional[str] = None
	defaultValueContactDetail: Optional[ContactDetail] = None
	type: Optional[str] = None
	defaultValueBoolean: Optional[bool] = None
	defaultValuePeriod: Optional[Period] = None
	defaultValueTriggerDefinition: Optional[TriggerDefinition] = None
	logMessage: Optional[str] = None
	defaultValueDate: Optional[str] = None
	defaultValueReference: Optional[Reference] = None
	defaultValueDosage: Optional[Dosage] = None
	defaultValueRange: Optional[Range] = None
	defaultValueInstant: Optional[str] = None
	defaultValueAttachment: Optional[Attachment] = None
	defaultValueUnsignedInt: Optional[NonNegativeInt] = None
	defaultValueDistance: Optional[Distance] = None
	max: Optional[str] = None
	defaultValueContributor: Optional[Contributor] = None
	condition: Optional[str] = None
	defaultValueRatio: Optional[Ratio] = None
	defaultValueCanonical: Optional[str] = None
	defaultValueExpression: Optional[Expression] = None
	defaultValueSignature: Optional[Signature] = None
	defaultValueUrl: Optional[str] = None
	context: str
	defaultValueAnnotation: Optional[Annotation] = None
	defaultValueUuid: Optional[str] = None
	defaultValueAddress: Optional[Address] = None
	defaultValueString: Optional[str] = None
	defaultValueAge: Optional[Age] = None
	defaultValueOid: Optional[str] = None
	defaultValueUsageContext: Optional[UsageContext] = None
	listMode: Optional[str] = None
	defaultValueParameterDefinition: Optional[ParameterDefinition] = None
	defaultValueDateTime: Optional[str] = None
	defaultValuePositiveInt: Optional[PositiveInt] = None
	defaultValueInteger: Optional[int] = None
	defaultValueTiming: Optional[Timing] = None
	defaultValueRelatedArtifact: Optional[RelatedArtifact] = None
	defaultValueIdentifier: Optional[Identifier] = None
	defaultValueCodeableConcept: Optional[CodeableConcept] = None

class StructureMap_Group_Rule_Target_Parameter(BackboneElement):
	valueId: Optional[str] = None
	valueString: Optional[str] = None
	valueBoolean: Optional[bool] = None
	valueInteger: Optional[int] = None
	valueDecimal: Optional[float] = None

class StructureMap_Group_Rule_Target(BackboneElement):
	context: Optional[str] = None
	contextType: Optional[str] = None
	element: Optional[str] = None
	variable: Optional[str] = None
	listMode: Optional[List[str]] = None
	listRuleId: Optional[str] = None
	transform: Optional[str] = None
	parameter: Optional[List[StructureMap_Group_Rule_Target_Parameter]] = None

class StructureMap_Group_Rule_Dependent(BackboneElement):
	name: str
	variable: List[str]

class StructureMap_Group_Rule(BackboneElement):
	name: str
	source: List[StructureMap_Group_Rule_Source]
	target: Optional[List[StructureMap_Group_Rule_Target]] = None
	rule: Optional[List[str]] = None
	dependent: Optional[List[StructureMap_Group_Rule_Dependent]] = None
	documentation: Optional[str] = None

class StructureMap_Group(BackboneElement):
	name: str
	extends: Optional[str] = None
	typeMode: str
	documentation: Optional[str] = None
	input: List[StructureMap_Group_Input]
	rule: List[StructureMap_Group_Rule]

class StructureMap_Structure(BackboneElement):
	url: str
	mode: str
	alias: Optional[str] = None
	documentation: Optional[str] = None

class StructureMap(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	group: List[StructureMap_Group]
	publisher: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	name: str
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	structure: Optional[List[StructureMap_Structure]] = None
	status: str
	url: str
	identifier: Optional[List[Identifier]] = None
	version: Optional[str] = None
	import_: Optional[List[str]] = None
	contact: Optional[List[ContactDetail]] = None