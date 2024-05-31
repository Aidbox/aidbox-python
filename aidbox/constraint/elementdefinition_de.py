from pydantic import *
from typing import Optional, List, Literal
from ..base import *

class ElementDefinition_Constraint(Element):
	key: str
	requirements: Optional[str] = None
	severity: str
	human: str
	expression: Optional[str] = None
	xpath: Optional[str] = None
	source: Optional[str] = None

class ElementDefinition_Mapping(Element):
	identity: str
	language: Optional[str] = None
	map: str
	comment: Optional[str] = None

class ElementDefinition_Slicing_Discriminator(Element):
	type: str
	path: str

class ElementDefinition_Slicing(Element):
	discriminator: Optional[List[ElementDefinition_Slicing_Discriminator]] = None
	description: Optional[str] = None
	ordered: Optional[bool] = None
	rules: str

class ElementDefinition_Type(Element):
	code: str
	profile: Optional[List[str]] = None
	targetProfile: Optional[List[str]] = None
	aggregation: Optional[List[str]] = None
	versioning: Optional[str] = None

class ElementDefinition_Binding(Element):
	strength: str
	description: Optional[str] = None
	valueSet: Optional[str] = None

class ElementDefinition_Example(Element):
	valueBase64Binary: Optional[str] = None
	valueAge: Optional[Age] = None
	valueParameterDefinition: Optional[ParameterDefinition] = None
	valueTiming: Optional[Timing] = None
	valueCode: Optional[str] = None
	valueReference: Optional[Reference] = None
	valueContributor: Optional[Contributor] = None
	valueContactDetail: Optional[ContactDetail] = None
	valueUri: Optional[str] = None
	valueUsageContext: Optional[UsageContext] = None
	valueTime: Optional[str] = None
	valueDecimal: Optional[float] = None
	valueCanonical: Optional[str] = None
	valueMarkdown: Optional[str] = None
	valueIdentifier: Optional[Identifier] = None
	valueTriggerDefinition: Optional[TriggerDefinition] = None
	valueQuantity: Optional[Quantity] = None
	valueCount: Optional[Count] = None
	valueString: Optional[str] = None
	valueRatio: Optional[Ratio] = None
	valueBoolean: Optional[bool] = None
	valueInstant: Optional[str] = None
	valueDateTime: Optional[str] = None
	valueDate: Optional[str] = None
	valueDuration: Optional[Duration] = None
	valueDataRequirement: Optional[DataRequirement] = None
	valueMeta: Optional[Meta] = None
	valueMoney: Optional[Money] = None
	valueCoding: Optional[Coding] = None
	valueExpression: Optional[Expression] = None
	valueSampledData: Optional[SampledData] = None
	label: str
	valueDosage: Optional[Dosage] = None
	valueContactPoint: Optional[ContactPoint] = None
	valueCodeableConcept: Optional[CodeableConcept] = None
	valueAnnotation: Optional[Annotation] = None
	valuePeriod: Optional[Period] = None
	valueDistance: Optional[Distance] = None
	valueRange: Optional[Range] = None
	valueSignature: Optional[Signature] = None
	valueUuid: Optional[str] = None
	valueInteger: Optional[int] = None
	valueHumanName: Optional[HumanName] = None
	valueUnsignedInt: Optional[NonNegativeInt] = None
	valueAttachment: Optional[Attachment] = None
	valueOid: Optional[str] = None
	valueAddress: Optional[Address] = None
	valueRelatedArtifact: Optional[RelatedArtifact] = None
	valuePositiveInt: Optional[PositiveInt] = None
	valueId: Optional[str] = None
	valueUrl: Optional[str] = None

class ElementDefinition_Base(Element):
	path: str
	min: NonNegativeInt
	max: str

class ElementdefinitionDe(BackboneElement):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/elementdefinition-de"])
	constraint: Optional[List[ElementDefinition_Constraint]] = None
	fixedMarkdown: Optional[str] = None
	path: str
	patternRange: Optional[Range] = None
	patternMeta: Optional[Meta] = None
	defaultValueTime: Optional[str] = None
	fixedCode: Optional[str] = None
	maxValueDecimal: Optional[float] = None
	requirements: Optional[str] = None
	patternDosage: Optional[Dosage] = None
	defaultValueDataRequirement: Optional[DataRequirement] = None
	min: Optional[NonNegativeInt] = None
	defaultValueMoney: Optional[Money] = None
	fixedPositiveInt: Optional[PositiveInt] = None
	patternTiming: Optional[Timing] = None
	definition: Optional[str] = None
	patternContributor: Optional[Contributor] = None
	patternContactPoint: Optional[ContactPoint] = None
	defaultValueContactPoint: Optional[ContactPoint] = None
	minValueInteger: Optional[int] = None
	defaultValueMeta: Optional[Meta] = None
	patternRatio: Optional[Ratio] = None
	patternContactDetail: Optional[ContactDetail] = None
	fixedUsageContext: Optional[UsageContext] = None
	defaultValueCoding: Optional[Coding] = None
	fixedAge: Optional[Age] = None
	patternDataRequirement: Optional[DataRequirement] = None
	minValueDate: Optional[str] = None
	maxValuePositiveInt: Optional[PositiveInt] = None
	fixedRelatedArtifact: Optional[RelatedArtifact] = None
	fixedAddress: Optional[Address] = None
	defaultValueCode: Optional[str] = None
	fixedUri: Optional[str] = None
	defaultValueSampledData: Optional[SampledData] = None
	fixedDistance: Optional[Distance] = None
	patternUnsignedInt: Optional[NonNegativeInt] = None
	defaultValueMarkdown: Optional[str] = None
	defaultValueHumanName: Optional[HumanName] = None
	minValueInstant: Optional[str] = None
	defaultValueDuration: Optional[Duration] = None
	defaultValueDecimal: Optional[float] = None
	defaultValueUri: Optional[str] = None
	fixedDosage: Optional[Dosage] = None
	fixedRatio: Optional[Ratio] = None
	fixedContactDetail: Optional[ContactDetail] = None
	patternSampledData: Optional[SampledData] = None
	fixedParameterDefinition: Optional[ParameterDefinition] = None
	defaultValueQuantity: Optional[Quantity] = None
	patternAttachment: Optional[Attachment] = None
	defaultValueCount: Optional[Count] = None
	fixedExpression: Optional[Expression] = None
	minValueDecimal: Optional[float] = None
	fixedUnsignedInt: Optional[NonNegativeInt] = None
	fixedDuration: Optional[Duration] = None
	patternTriggerDefinition: Optional[TriggerDefinition] = None
	mapping: Optional[List[ElementDefinition_Mapping]] = None
	fixedOid: Optional[str] = None
	defaultValueId: Optional[str] = None
	fixedIdentifier: Optional[Identifier] = None
	defaultValueBase64Binary: Optional[str] = None
	fixedDateTime: Optional[str] = None
	defaultValueContactDetail: Optional[ContactDetail] = None
	type: Optional[List[ElementDefinition_Type]] = None
	defaultValueBoolean: Optional[bool] = None
	defaultValuePeriod: Optional[Period] = None
	patternBoolean: Optional[bool] = None
	defaultValueTriggerDefinition: Optional[TriggerDefinition] = None
	mustSupport: Optional[bool] = None
	defaultValueDate: Optional[str] = None
	fixedMoney: Optional[Money] = None
	sliceName: Optional[str] = None
	fixedUuid: Optional[str] = None
	fixedDate: Optional[str] = None
	fixedReference: Optional[Reference] = None
	fixedHumanName: Optional[HumanName] = None
	fixedTriggerDefinition: Optional[TriggerDefinition] = None
	defaultValueReference: Optional[Reference] = None
	patternDecimal: Optional[float] = None
	defaultValueDosage: Optional[Dosage] = None
	fixedDataRequirement: Optional[DataRequirement] = None
	defaultValueRange: Optional[Range] = None
	patternString: Optional[str] = None
	minValueTime: Optional[str] = None
	patternTime: Optional[str] = None
	meaningWhenMissing: Optional[str] = None
	maxValueQuantity: Optional[Quantity] = None
	fixedDecimal: Optional[float] = None
	fixedCoding: Optional[Coding] = None
	patternAnnotation: Optional[Annotation] = None
	fixedSampledData: Optional[SampledData] = None
	patternUuid: Optional[str] = None
	patternDuration: Optional[Duration] = None
	patternCode: Optional[str] = None
	fixedCount: Optional[Count] = None
	patternSignature: Optional[Signature] = None
	minValueUnsignedInt: Optional[NonNegativeInt] = None
	fixedCodeableConcept: Optional[CodeableConcept] = None
	patternReference: Optional[Reference] = None
	defaultValueInstant: Optional[str] = None
	binding: Optional[ElementDefinition_Binding] = None
	patternCount: Optional[Count] = None
	maxValueDate: Optional[str] = None
	alias: Optional[List[str]] = None
	defaultValueAttachment: Optional[Attachment] = None
	defaultValueUnsignedInt: Optional[NonNegativeInt] = None
	patternAge: Optional[Age] = None
	fixedSignature: Optional[Signature] = None
	patternParameterDefinition: Optional[ParameterDefinition] = None
	fixedId: Optional[str] = None
	fixedUrl: Optional[str] = None
	defaultValueDistance: Optional[Distance] = None
	patternIdentifier: Optional[Identifier] = None
	maxValueDateTime: Optional[str] = None
	fixedContactPoint: Optional[ContactPoint] = None
	fixedQuantity: Optional[Quantity] = None
	fixedAnnotation: Optional[Annotation] = None
	patternCanonical: Optional[str] = None
	max: Optional[str] = None
	minValueDateTime: Optional[str] = None
	fixedString: Optional[str] = None
	label: Optional[str] = None
	defaultValueContributor: Optional[Contributor] = None
	condition: Optional[List[str]] = None
	defaultValueRatio: Optional[Ratio] = None
	patternInstant: Optional[str] = None
	defaultValueCanonical: Optional[str] = None
	defaultValueExpression: Optional[Expression] = None
	comment: Optional[str] = None
	defaultValueSignature: Optional[Signature] = None
	patternDate: Optional[str] = None
	code: Optional[List[Coding]] = None
	fixedTime: Optional[str] = None
	defaultValueUrl: Optional[str] = None
	fixedContributor: Optional[Contributor] = None
	maxValueInstant: Optional[str] = None
	patternCoding: Optional[Coding] = None
	patternHumanName: Optional[HumanName] = None
	patternMarkdown: Optional[str] = None
	fixedBase64Binary: Optional[str] = None
	patternDistance: Optional[Distance] = None
	patternRelatedArtifact: Optional[RelatedArtifact] = None
	fixedTiming: Optional[Timing] = None
	maxLength: Optional[int] = None
	defaultValueAnnotation: Optional[Annotation] = None
	defaultValueUuid: Optional[str] = None
	fixedCanonical: Optional[str] = None
	patternUsageContext: Optional[UsageContext] = None
	patternPeriod: Optional[Period] = None
	defaultValueAddress: Optional[Address] = None
	maxValueInteger: Optional[int] = None
	patternOid: Optional[str] = None
	sliceIsConstraining: Optional[bool] = None
	defaultValueString: Optional[str] = None
	example: Optional[List[ElementDefinition_Example]] = None
	defaultValueAge: Optional[Age] = None
	patternPositiveInt: Optional[PositiveInt] = None
	patternMoney: Optional[Money] = None
	patternId: Optional[str] = None
	patternQuantity: Optional[Quantity] = None
	minValuePositiveInt: Optional[PositiveInt] = None
	fixedPeriod: Optional[Period] = None
	defaultValueOid: Optional[str] = None
	orderMeaning: Optional[str] = None
	defaultValueUsageContext: Optional[UsageContext] = None
	fixedAttachment: Optional[Attachment] = None
	patternCodeableConcept: Optional[CodeableConcept] = None
	minValueQuantity: Optional[Quantity] = None
	base: Optional[ElementDefinition_Base] = None
	patternInteger: Optional[int] = None
	defaultValueParameterDefinition: Optional[ParameterDefinition] = None
	defaultValueDateTime: Optional[str] = None
	defaultValuePositiveInt: Optional[PositiveInt] = None
	maxValueUnsignedInt: Optional[NonNegativeInt] = None
	defaultValueInteger: Optional[int] = None
	isModifierReason: Optional[str] = None
	patternAddress: Optional[Address] = None
	patternBase64Binary: Optional[str] = None
	patternUrl: Optional[str] = None
	patternDateTime: Optional[str] = None
	defaultValueTiming: Optional[Timing] = None
	patternUri: Optional[str] = None
	fixedRange: Optional[Range] = None
	defaultValueRelatedArtifact: Optional[RelatedArtifact] = None
	maxValueTime: Optional[str] = None
	defaultValueIdentifier: Optional[Identifier] = None
	defaultValueCodeableConcept: Optional[CodeableConcept] = None
	fixedBoolean: Optional[bool] = None
	fixedMeta: Optional[Meta] = None
	fixedInstant: Optional[str] = None
	patternExpression: Optional[Expression] = None
	fixedInteger: Optional[int] = None