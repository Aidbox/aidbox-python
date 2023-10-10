from typing import Optional
from ..base import *

class StructureMap_Group_Input(BackboneElement):
	documentation: Optional[str] = None
	mode: str
	name: str
	type: Optional[str] = None

class StructureMap_Group_Rule_Dependent(BackboneElement):
	name: str
	variable: list[str]

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
	defaultValueDuration: Optional[str] = None
	defaultValueDecimal: Optional[str] = None
	defaultValueUri: Optional[str] = None
	check: Optional[str] = None
	defaultValueQuantity: Optional[Quantity] = None
	defaultValueCount: Optional[str] = None
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
	defaultValueDosage: Optional[str] = None
	defaultValueRange: Optional[Range] = None
	defaultValueInstant: Optional[str] = None
	defaultValueAttachment: Optional[Attachment] = None
	defaultValueUnsignedInt: Optional[str] = None
	defaultValueDistance: Optional[str] = None
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
	defaultValueAge: Optional[str] = None
	defaultValueOid: Optional[str] = None
	defaultValueUsageContext: Optional[UsageContext] = None
	listMode: Optional[str] = None
	defaultValueParameterDefinition: Optional[ParameterDefinition] = None
	defaultValueDateTime: Optional[str] = None
	defaultValuePositiveInt: Optional[str] = None
	defaultValueInteger: Optional[int] = None
	defaultValueTiming: Optional[str] = None
	defaultValueRelatedArtifact: Optional[RelatedArtifact] = None
	defaultValueIdentifier: Optional[Identifier] = None
	defaultValueCodeableConcept: Optional[CodeableConcept] = None

class StructureMap_Group_Rule_Target_Parameter(BackboneElement):
	valueBoolean: Optional[bool] = None
	valueDecimal: Optional[str] = None
	valueId: Optional[str] = None
	valueInteger: Optional[int] = None
	valueString: Optional[str] = None

class StructureMap_Group_Rule_Target(BackboneElement):
	context: Optional[str] = None
	contextType: Optional[str] = None
	element: Optional[str] = None
	listMode: list[str] = []
	listRuleId: Optional[str] = None
	parameter: list[StructureMap_Group_Rule_Target_Parameter] = []
	transform: Optional[str] = None
	variable: Optional[str] = None

class StructureMap_Group_Rule(BackboneElement):
	dependent: list[StructureMap_Group_Rule_Dependent] = []
	documentation: Optional[str] = None
	name: str
	rule: list[str] = []
	source: list[StructureMap_Group_Rule_Source]
	target: list[StructureMap_Group_Rule_Target] = []

class StructureMap_Group(BackboneElement):
	documentation: Optional[str] = None
	extends: Optional[str] = None
	input: list[StructureMap_Group_Input]
	name: str
	rule: list[StructureMap_Group_Rule]
	typeMode: str

class StructureMap_Structure(BackboneElement):
	alias: Optional[str] = None
	documentation: Optional[str] = None
	mode: str
	url: str

class StructureMap(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	group: list[StructureMap_Group]
	publisher: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: str
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	structure: list[StructureMap_Structure] = []
	status: str
	url: str
	identifier: list[Identifier] = []
	version: Optional[str] = None
	import_: list[str] = []
	contact: list[ContactDetail] = []

