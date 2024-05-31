from __future__ import annotations
from typing_extensions import TypeAlias

IncEx: TypeAlias = "set[int] | set[str] | dict[int, Any] | dict[str, Any] | None"
from typing import Literal, Union, Literal, Mapping, Optional, List, Any, overload
from pydantic import BaseModel, EmailStr, Field, PositiveInt, NonNegativeInt

import os

import requests
from requests.auth import HTTPBasicAuth


@overload
def Where(
    attribute: Literal[
    "address-city",
    "address",
    "address-country",
    "address-postalcode",
    "address-state",
    "family",
    "name",
    "given",
],
    value: str,
    ):
    ...


@overload
def Where(attribute: Literal["active"], value: bool):
    ...


@overload
def Where(attribute: Literal["gender"], value: Literal["male", "female", "other"]):
    ...


def Where(attribute: str, value: Any):
    return {attribute: str(value).lower() if type(value) is bool else value}


def Count(value: int):
    return {"_count": value}


def Page(value: int):
    return {"_page": value}


def Sort(
    value: Union[Literal["last_updated", "created_at"], str],
    order: Literal["asc", "desc"],
    ):
    if value == "last_updated":
        return {"_sort": "-lastUpdated" if order == "desc" else "lastUpdated"}
    if value == "created_at":
        return {"_sort": "-createdAt" if order == "desc" else "createdAt"}
    return {"_sort": "-" + value if order == "desc" else value}


username = os.environ.get("AIDBOX_CLIENT_USERNAME")
password = os.environ.get("AIDBOX_CLIENT_PASSWORD")

if username is None:
    raise Exception("AIDBOX_CLIENT_USERNAME environment variable is missing")
if password is None:
    raise Exception("AIDBOX_CLIENT_PASSWORD environment variable is missing")

base = os.environ.get("AIDBOX_URL")
basic = HTTPBasicAuth(username, password)


class API(BaseModel):
    @classmethod
    def from_id(cls, id: str):
        response = requests.get(url=f"{base}/fhir/{cls.__name__}/{id}", auth=basic)
        response.raise_for_status()  # TODO: handle and type HTTP codes except 200+
        return cls(**response.json())

    @classmethod
    def bundle(cls, entry: list[Any], type: Literal["transaction"]):
        data = {"resourceType": "Bundle", "type": type, "entry": entry}
        response = requests.post(url=f"{base}/fhir", json=data, auth=basic)
        response.raise_for_status()  # TODO: handle and type HTTP codes except 200+

    @classmethod
    def get(cls, *args: dict[str, Any]):
        search_params: dict[str, Any] = {}
        [search_params.update(d) for d in args]
        response = requests.get(
            url=f"{base}/fhir/{cls.__name__}", params=search_params, auth=basic
        )
        response.raise_for_status()  # TODO: handle and type HTTP codes except 200+
        data = response.json()  # TODO: handle HTTP response bodies
        return (
            list(map(lambda patient: cls(**patient["resource"]), data["entry"]))
            if "entry" in data
            else []
        )

    def delete(self):
        assert self.id is not None
        resource_type = self.__class__.__name__
        response = requests.delete(
            url=f"{base}/fhir/{resource_type}/{self.id}", auth=basic
        )
        response.raise_for_status()  # TODO: handle and type HTTP codes except 200+

    def save(self):  # create | persist | save
        resource_type = self.__class__.__name__
        response = requests.put(
            url=f"{base}/fhir/{resource_type}/{self.id or ''}",
            json=self.dumps(exclude_unset=True),
            auth=basic,
        )
        response.raise_for_status()  # TODO: handle and type HTTP codes except 200+
        data = response.json()
        self.id = data["id"]
        self.meta = Meta(**data["meta"])

    def dumps(
        self,
        *,
        mode: Literal["json", "python"] | str = "python",
        include: IncEx = None,
        exclude: IncEx = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        round_trip: bool = False,
        warnings: bool = True,
        ):
        data = self.model_dump(
            mode=mode,
            by_alias=by_alias,
            include=include,
            exclude=exclude,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            round_trip=round_trip,
            warnings=warnings,
        )

        for item in ["class", "global", "for", "import"]:
            if (item + "_") in data:
                data[item] = data[item + "_"]
                del data[item + "_"]

        return data

    @classmethod
    def make_request(cls, endpoint, method="GET", **kwargs):
        url = f"{base}{endpoint}"
        return requests.request(method, url, auth=basic, **kwargs)


class Resource(API):
    id: Optional[str] = None
    implicitRules: Optional[str] = None
    language: Optional[str] = None
    meta: Optional[Meta] = None


class Element(BaseModel):
    extension: list[Extension] = []
    id: Optional[str] = None


class HumanName(Element):
    use: Optional[str] = None
    text: Optional[str] = None
    family: Optional[str] = None
    given: Optional[List[str]] = None
    prefix: Optional[List[str]] = None
    suffix: Optional[List[str]] = None
    period: Optional[Period] = None


class Signature(Element):
    type: List[Coding]
    when: str
    who: Reference
    onBehalfOf: Optional[Reference] = None
    targetFormat: Optional[str] = None
    sigFormat: Optional[str] = None
    data: Optional[str] = None


class Range(Element):
    high: Optional[Quantity] = None
    low: Optional[Quantity] = None


class Coding(Element):
    code: Optional[str] = None
    display: Optional[str] = None
    system: Optional[str] = None
    userSelected: Optional[bool] = None
    version: Optional[str] = None


class Attachment(Element):
    contentType: Optional[str] = None
    language: Optional[str] = None
    data: Optional[str] = None
    url: Optional[str] = None
    size: Optional[NonNegativeInt] = None
    hash: Optional[str] = None
    title: Optional[str] = None
    creation: Optional[str] = None


class BackboneElement(Element):
    modifierExtension: Optional[List[Extension]] = None


class Address(Element):
    use: Optional[str] = None
    city: Optional[str] = None
    type: Optional[str] = None
    state: Optional[str] = None
    line: Optional[List[str]] = None
    postalCode: Optional[str] = None
    period: Optional[Period] = None
    country: Optional[str] = None
    district: Optional[str] = None
    text: Optional[str] = None


class Money(Element):
    value: Optional[float] = None
    currency: Optional[str] = None


class Period(Element):
    end: Optional[str] = None
    start: Optional[str] = None


class Expression(Element):
    description: Optional[str] = None
    expression: Optional[str] = None
    language: str
    name: Optional[str] = None
    reference: Optional[str] = None


class TriggerDefinition(Element):
    timingReference: Optional[Reference] = None
    name: Optional[str] = None
    type: str
    timingDateTime: Optional[str] = None
    timingTiming: Optional[Timing] = None
    condition: Optional[Expression] = None
    timingDate: Optional[str] = None
    data: Optional[List[DataRequirement]] = None


class Contributor(Element):
    contact: Optional[List[ContactDetail]] = None
    name: str
    type: str


class Identifier(Element):
    use: Optional[str] = None
    type: Optional[CodeableConcept] = None
    system: Optional[str] = None
    value: Optional[str] = None
    period: Optional[Period] = None
    assigner: Optional[Reference] = None


class Extension(Element):
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
    valueDosage: Optional[Dosage] = None
    valueContactPoint: Optional[ContactPoint] = None
    url: str
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


class Quantity(Element):
    value: Optional[float] = None
    comparator: Optional[str] = None
    unit: Optional[str] = None
    system: Optional[str] = None
    code: Optional[str] = None


class Count(Quantity):
    pass


class Age(Quantity):
    pass


class Distance(Quantity):
    pass


class RelatedArtifact(Element):
    type: str
    label: Optional[str] = None
    display: Optional[str] = None
    citation: Optional[str] = None
    url: Optional[str] = None
    document: Optional[Attachment] = None
    resource: Optional[str] = None


class Ratio(Element):
    denominator: Optional[Quantity] = None
    numerator: Optional[Quantity] = None


class UsageContext(Element):
    code: Coding
    valueCodeableConcept: Optional[CodeableConcept] = None
    valueQuantity: Optional[Quantity] = None
    valueRange: Optional[Range] = None
    valueReference: Optional[Reference] = None


class ContactPoint(Element):
    system: Optional[str] = None
    value: Optional[str] = None
    use: Optional[str] = None
    rank: Optional[PositiveInt] = None
    period: Optional[Period] = None


class ContactPointEmail(ContactPoint):
    system: Literal["email"] = "email"
    value: EmailStr

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system = "email"


class Narrative(Element):
    div: str
    status: str


class Meta(Element):
    versionId: Optional[str] = None
    lastUpdated: Optional[str] = None
    source: Optional[str] = None
    profile: Optional[List[str]] = None
    security: Optional[List[Coding]] = None
    tag: Optional[List[Coding]] = None


class SampledData(Element):
    origin: Quantity
    period: float
    factor: Optional[float] = None
    lowerLimit: Optional[float] = None
    upperLimit: Optional[float] = None
    dimensions: PositiveInt
    data: Optional[str] = None


class Annotation(Element):
    authorReference: Optional[Reference] = None
    authorString: Optional[str] = None
    text: str
    time: Optional[str] = None


class Reference(Element):
    reference: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[Identifier] = None
    display: Optional[str] = None


class CodeableConcept(Element):
    coding: Optional[List[Coding]] = None
    text: Optional[str] = None


class ContactDetail(Element):
    name: Optional[str] = None
    telecom: Optional[List[ContactPoint]] = None


class ParameterDefinition(Element):
    name: Optional[str] = None
    use: str
    min: Optional[int] = None
    max: Optional[str] = None
    documentation: Optional[str] = None
    type: str
    profile: Optional[str] = None


class DataRequirement_CodeFilter(Element):
    path: Optional[str] = None
    searchParam: Optional[str] = None
    valueSet: Optional[str] = None
    code: Optional[List[Coding]] = None


class DataRequirement_DateFilter(Element):
    path: Optional[str] = None
    searchParam: Optional[str] = None
    valueDateTime: Optional[str] = None
    valuePeriod: Optional[Period] = None
    valueDuration: Optional[Duration] = None


class DataRequirement_Sort(Element):
    path: str
    direction: str


class DataRequirement(Element):
    limit: Optional[PositiveInt] = None
    subjectCodeableConcept: Optional[CodeableConcept] = None
    type: str
    mustSupport: Optional[List[str]] = None
    codeFilter: Optional[List[DataRequirement_CodeFilter]] = None
    subjectReference: Optional[Reference] = None
    dateFilter: Optional[List[DataRequirement_DateFilter]] = None
    sort: Optional[List[DataRequirement_Sort]] = None
    profile: Optional[List[str]] = None


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


class ElementDefinition(BackboneElement):
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
    isModifier: Optional[bool] = None
    patternRatio: Optional[Ratio] = None
    patternContactDetail: Optional[ContactDetail] = None
    short: Optional[str] = None
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
    contentReference: Optional[str] = None
    fixedOid: Optional[str] = None
    defaultValueId: Optional[str] = None
    fixedIdentifier: Optional[Identifier] = None
    defaultValueBase64Binary: Optional[str] = None
    slicing: Optional[ElementDefinition_Slicing] = None
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
    representation: Optional[List[str]] = None
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
    isSummary: Optional[bool] = None
    fixedMeta: Optional[Meta] = None
    fixedInstant: Optional[str] = None
    patternExpression: Optional[Expression] = None
    fixedInteger: Optional[int] = None


class Population(BackboneElement):
    ageRange: Optional[Range] = None
    ageCodeableConcept: Optional[CodeableConcept] = None
    gender: Optional[CodeableConcept] = None
    race: Optional[CodeableConcept] = None
    physiologicalCondition: Optional[CodeableConcept] = None


class Dosage_DoseAndRate(Element):
    type: Optional[CodeableConcept] = None
    doseRange: Optional[Range] = None
    doseQuantity: Optional[Quantity] = None
    rateRatio: Optional[Ratio] = None
    rateRange: Optional[Range] = None
    rateQuantity: Optional[Quantity] = None

class Dosage(BackboneElement):
    site: Optional[CodeableConcept] = None
    method: Optional[CodeableConcept] = None
    patientInstruction: Optional[str] = None
    maxDosePerLifetime: Optional[Quantity] = None
    maxDosePerAdministration: Optional[Quantity] = None
    route: Optional[CodeableConcept] = None
    asNeededBoolean: Optional[bool] = None
    timing: Optional[Timing] = None
    additionalInstruction: Optional[List[CodeableConcept]] = None
    sequence: Optional[int] = None
    maxDosePerPeriod: Optional[Ratio] = None
    doseAndRate: Optional[List[Dosage_DoseAndRate]] = None
    asNeededCodeableConcept: Optional[CodeableConcept] = None
    text: Optional[str] = None


class Duration(Quantity):
    pass


class Timing_Repeat(Element):
    boundsRange: Optional[Range] = None
    frequencyMax: Optional[PositiveInt] = None
    boundsPeriod: Optional[Period] = None
    when: Optional[List[str]] = None
    offset: Optional[NonNegativeInt] = None
    periodUnit: Optional[str] = None
    frequency: Optional[PositiveInt] = None
    durationMax: Optional[float] = None
    duration: Optional[float] = None
    boundsDuration: Optional[Duration] = None
    durationUnit: Optional[str] = None
    dayOfWeek: Optional[List[str]] = None
    count: Optional[PositiveInt] = None
    periodMax: Optional[float] = None
    period: Optional[float] = None
    countMax: Optional[PositiveInt] = None
    timeOfDay: Optional[List[str]] = None


class Timing(BackboneElement):
    event: Optional[List[str]] = None
    repeat: Optional[Timing_Repeat] = None
    code: Optional[CodeableConcept] = None


class MarketingStatus(BackboneElement):
    country: CodeableConcept
    jurisdiction: Optional[CodeableConcept] = None
    status: CodeableConcept
    dateRange: Period
    restoreDate: Optional[str] = None


class SubstanceAmount_ReferenceRange(Element):
    lowLimit: Optional[Quantity] = None
    highLimit: Optional[Quantity] = None


class SubstanceAmount(BackboneElement):
    amountQuantity: Optional[Quantity] = None
    amountRange: Optional[Range] = None
    amountString: Optional[str] = None
    amountType: Optional[CodeableConcept] = None
    amountText: Optional[str] = None
    referenceRange: Optional[SubstanceAmount_ReferenceRange] = None


class ProductShelfLife(BackboneElement):
    identifier: Optional[Identifier] = None
    type: CodeableConcept
    period: Quantity
    specialPrecautionsForStorage: Optional[List[CodeableConcept]] = None


class ProdCharacteristic(BackboneElement):
    imprint: Optional[List[str]] = None
    color: Optional[List[str]] = None
    width: Optional[Quantity] = None
    nominalVolume: Optional[Quantity] = None
    weight: Optional[Quantity] = None
    shape: Optional[str] = None
    scoring: Optional[CodeableConcept] = None
    image: Optional[List[Attachment]] = None
    depth: Optional[Quantity] = None
    externalDiameter: Optional[Quantity] = None
    height: Optional[Quantity] = None


class Parameters_Parameter(BackboneElement):
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
    name: str
    valueMarkdown: Optional[str] = None
    valueIdentifier: Optional[Identifier] = None
    valueTriggerDefinition: Optional[TriggerDefinition] = None
    valueQuantity: Optional[Quantity] = None
    part: Optional[List[str]] = None
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
    resource: Optional[Resource] = None
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

class Parameters(Resource):
    parameter: Optional[List[Parameters_Parameter]] = None


class Binary(Resource):
    contentType: str
    data: Optional[str] = None
    securityContext: Optional[Reference] = None


class Bundle_Link(BackboneElement):
    relation: str
    url: str


class Bundle_Entry_Search(BackboneElement):
    mode: Optional[str] = None
    score: Optional[float] = None


class Bundle_Entry_Request(BackboneElement):
    method: str
    url: str
    ifNoneMatch: Optional[str] = None
    ifModifiedSince: Optional[str] = None
    ifMatch: Optional[str] = None
    ifNoneExist: Optional[str] = None


class Bundle_Entry_Response(BackboneElement):
    status: str
    location: Optional[str] = None
    etag: Optional[str] = None
    lastModified: Optional[str] = None
    outcome: Optional[Resource] = None


class Bundle_Entry(BackboneElement):
    link: Optional[List[str]] = None
    fullUrl: Optional[str] = None
    resource: Optional[Resource] = None
    search: Optional[Bundle_Entry_Search] = None
    request: Optional[Bundle_Entry_Request] = None
    response: Optional[Bundle_Entry_Response] = None


class Bundle(Resource):
    identifier: Optional[Identifier] = None
    type: str
    timestamp: Optional[str] = None
    total: Optional[NonNegativeInt] = None
    link: Optional[List[Bundle_Link]] = None
    entry: Optional[List[Bundle_Entry]] = None
    signature: Optional[Signature] = None


class DomainResource(Resource):
    text: Optional[Narrative] = None
    contained: Optional[List[Resource]] = None
    extension: Optional[List[Extension]] = None
    modifierExtension: Optional[List[Extension]] = None
