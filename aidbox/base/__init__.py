from __future__ import annotations
from typing_extensions import TypeAlias

IncEx: TypeAlias = "set[int] | set[str] | dict[int, Any] | dict[str, Any] | None"
from typing import Literal, Union, Literal, Mapping, Optional, Any, overload
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
    def request(cls, endpoint, method="GET", **kwargs):
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
    family: Optional[str] = None
    given: list[str] = []
    period: Optional[Period] = None
    prefix: list[str] = []
    suffix: list[str] = []
    text: Optional[str] = None
    use: Optional[str] = None


class Signature(Element):
    data: Optional[str] = None
    onBehalfOf: Optional[Reference] = None
    sigFormat: Optional[str] = None
    targetFormat: Optional[str] = None
    type: list[Coding]
    when: str
    who: Reference


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
    creation: Optional[str] = None
    data: Optional[str] = None
    hash: Optional[str] = None
    language: Optional[str] = None
    size: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None


class BackboneElement(Element):
    modifierExtension: list[Extension] = []


class Address(Element):
    use: Optional[str] = None
    city: Optional[str] = None
    type: Optional[str] = None
    state: Optional[str] = None
    line: list[str] = []
    postalCode: Optional[str] = None
    period: Optional[Period] = None
    country: Optional[str] = None
    district: Optional[str] = None
    text: Optional[str] = None


class Money(Element):
    currency: Optional[str] = None
    value: Optional[str] = None


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
    timingTiming: Optional[str] = None
    condition: Optional[Expression] = None
    timingDate: Optional[str] = None
    data: list[DataRequirement] = []


class Contributor(Element):
    contact: list[ContactDetail] = []
    name: str
    type: str


class Identifier(Element):
    assigner: Optional[Reference] = None
    period: Optional[Period] = None
    system: Optional[str] = None
    type: Optional[CodeableConcept] = None
    use: Optional[str] = None
    value: Optional[str] = None


class Extension(Element):
    valueBase64Binary: Optional[str] = None
    valueAge: Optional[str] = None
    valueParameterDefinition: Optional[ParameterDefinition] = None
    valueTiming: Optional[str] = None
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
    valueCount: Optional[str] = None
    valueString: Optional[str] = None
    valueRatio: Optional[Ratio] = None
    valueBoolean: Optional[bool] = None
    valueInstant: Optional[str] = None
    valueDateTime: Optional[str] = None
    valueDate: Optional[str] = None
    valueDuration: Optional[str] = None
    valueDataRequirement: Optional[DataRequirement] = None
    valueMeta: Optional[Meta] = None
    valueMoney: Optional[Money] = None
    valueCoding: Optional[Coding] = None
    valueExpression: Optional[Expression] = None
    valueSampledData: Optional[SampledData] = None
    valueDosage: Optional[str] = None
    valueContactPoint: Optional[ContactPoint] = None
    url: str
    valueCodeableConcept: Optional[CodeableConcept] = None
    valueAnnotation: Optional[Annotation] = None
    valuePeriod: Optional[Period] = None
    valueDistance: Optional[str] = None
    valueRange: Optional[Range] = None
    valueSignature: Optional[Signature] = None
    valueUuid: Optional[str] = None
    valueInteger: Optional[int] = None
    valueHumanName: Optional[HumanName] = None
    valueUnsignedInt: Optional[str] = None
    valueAttachment: Optional[Attachment] = None
    valueOid: Optional[str] = None
    valueAddress: Optional[Address] = None
    valueRelatedArtifact: Optional[RelatedArtifact] = None
    valuePositiveInt: Optional[str] = None
    valueId: Optional[str] = None
    valueUrl: Optional[str] = None


class Quantity(Element):
    code: Optional[str] = None
    comparator: Optional[str] = None
    system: Optional[str] = None
    unit: Optional[str] = None
    value: Optional[float] = None


class RelatedArtifact(Element):
    citation: Optional[str] = None
    display: Optional[str] = None
    document: Optional[Attachment] = None
    label: Optional[str] = None
    resource: Optional[str] = None
    type: str
    url: Optional[str] = None


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
    period: Optional[Period] = None
    rank: Optional[int] = None
    system: Optional[str] = None
    use: Optional[str] = None
    value: Optional[str] = None


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
    lastUpdated: Optional[str] = None
    profile: list[str] = []
    security: list[Coding] = []
    source: Optional[str] = None
    tag: list[Coding] = []
    versionId: Optional[str] = None


class SampledData(Element):
    data: Optional[str] = None
    dimensions: str
    factor: Optional[str] = None
    lowerLimit: Optional[str] = None
    origin: Quantity
    period: str
    upperLimit: Optional[str] = None


class Annotation(Element):
    authorReference: Optional[Reference] = None
    authorString: Optional[str] = None
    text: str
    time: Optional[str] = None


class Reference(Element):
    display: Optional[str] = None
    identifier: Optional[Identifier] = None
    reference: Optional[str] = None
    type: Optional[str] = None


class CodeableConcept(Element):
    coding: list[Coding] = []
    text: Optional[str] = None


class ContactDetail(Element):
    name: Optional[str] = None
    telecom: list[ContactPoint] = []


class ParameterDefinition(Element):
    documentation: Optional[str] = None
    max: Optional[str] = None
    min: Optional[int] = None
    name: Optional[str] = None
    profile: Optional[str] = None
    type: str
    use: str


class DataRequirement(Element):
    limit: Optional[str] = None
    subjectCodeableConcept: Optional[CodeableConcept] = None
    type: str
    mustSupport: list[str] = []
    codeFilter: list[Element] = []
    subjectReference: Optional[Reference] = None
    dateFilter: list[Element] = []
    sort: list[Element] = []
    profile: list[str] = []


class ElementDefinition(BackboneElement):
    constraint: list[Element] = []
    fixedMarkdown: Optional[str] = None
    path: str
    patternRange: Optional[Range] = None
    patternMeta: Optional[Meta] = None
    defaultValueTime: Optional[str] = None
    fixedCode: Optional[str] = None
    maxValueDecimal: Optional[str] = None
    requirements: Optional[str] = None
    patternDosage: Optional[str] = None
    defaultValueDataRequirement: Optional[DataRequirement] = None
    min: Optional[str] = None
    defaultValueMoney: Optional[Money] = None
    fixedPositiveInt: Optional[str] = None
    patternTiming: Optional[str] = None
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
    fixedAge: Optional[str] = None
    patternDataRequirement: Optional[DataRequirement] = None
    minValueDate: Optional[str] = None
    maxValuePositiveInt: Optional[str] = None
    fixedRelatedArtifact: Optional[RelatedArtifact] = None
    fixedAddress: Optional[Address] = None
    defaultValueCode: Optional[str] = None
    fixedUri: Optional[str] = None
    defaultValueSampledData: Optional[SampledData] = None
    fixedDistance: Optional[str] = None
    patternUnsignedInt: Optional[str] = None
    defaultValueMarkdown: Optional[str] = None
    defaultValueHumanName: Optional[HumanName] = None
    minValueInstant: Optional[str] = None
    defaultValueDuration: Optional[str] = None
    defaultValueDecimal: Optional[str] = None
    defaultValueUri: Optional[str] = None
    fixedDosage: Optional[str] = None
    fixedRatio: Optional[Ratio] = None
    fixedContactDetail: Optional[ContactDetail] = None
    patternSampledData: Optional[SampledData] = None
    fixedParameterDefinition: Optional[ParameterDefinition] = None
    defaultValueQuantity: Optional[Quantity] = None
    patternAttachment: Optional[Attachment] = None
    defaultValueCount: Optional[str] = None
    fixedExpression: Optional[Expression] = None
    minValueDecimal: Optional[str] = None
    fixedUnsignedInt: Optional[str] = None
    fixedDuration: Optional[str] = None
    patternTriggerDefinition: Optional[TriggerDefinition] = None
    mapping: list[Element] = []
    contentReference: Optional[str] = None
    fixedOid: Optional[str] = None
    defaultValueId: Optional[str] = None
    fixedIdentifier: Optional[Identifier] = None
    defaultValueBase64Binary: Optional[str] = None
    slicing: Optional[Element] = None
    fixedDateTime: Optional[str] = None
    defaultValueContactDetail: Optional[ContactDetail] = None
    type: list[Element] = []
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
    patternDecimal: Optional[str] = None
    defaultValueDosage: Optional[str] = None
    fixedDataRequirement: Optional[DataRequirement] = None
    defaultValueRange: Optional[Range] = None
    patternString: Optional[str] = None
    minValueTime: Optional[str] = None
    patternTime: Optional[str] = None
    meaningWhenMissing: Optional[str] = None
    maxValueQuantity: Optional[Quantity] = None
    fixedDecimal: Optional[str] = None
    fixedCoding: Optional[Coding] = None
    patternAnnotation: Optional[Annotation] = None
    fixedSampledData: Optional[SampledData] = None
    patternUuid: Optional[str] = None
    patternDuration: Optional[str] = None
    patternCode: Optional[str] = None
    fixedCount: Optional[str] = None
    patternSignature: Optional[Signature] = None
    minValueUnsignedInt: Optional[str] = None
    fixedCodeableConcept: Optional[CodeableConcept] = None
    patternReference: Optional[Reference] = None
    defaultValueInstant: Optional[str] = None
    binding: Optional[Element] = None
    patternCount: Optional[str] = None
    maxValueDate: Optional[str] = None
    alias: list[str] = []
    defaultValueAttachment: Optional[Attachment] = None
    defaultValueUnsignedInt: Optional[str] = None
    patternAge: Optional[str] = None
    fixedSignature: Optional[Signature] = None
    representation: list[str] = []
    patternParameterDefinition: Optional[ParameterDefinition] = None
    fixedId: Optional[str] = None
    fixedUrl: Optional[str] = None
    defaultValueDistance: Optional[str] = None
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
    condition: list[str] = []
    defaultValueRatio: Optional[Ratio] = None
    patternInstant: Optional[str] = None
    defaultValueCanonical: Optional[str] = None
    defaultValueExpression: Optional[Expression] = None
    comment: Optional[str] = None
    defaultValueSignature: Optional[Signature] = None
    patternDate: Optional[str] = None
    code: list[Coding] = []
    fixedTime: Optional[str] = None
    defaultValueUrl: Optional[str] = None
    fixedContributor: Optional[Contributor] = None
    maxValueInstant: Optional[str] = None
    patternCoding: Optional[Coding] = None
    patternHumanName: Optional[HumanName] = None
    patternMarkdown: Optional[str] = None
    fixedBase64Binary: Optional[str] = None
    patternDistance: Optional[str] = None
    patternRelatedArtifact: Optional[RelatedArtifact] = None
    fixedTiming: Optional[str] = None
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
    example: list[Element] = []
    defaultValueAge: Optional[str] = None
    patternPositiveInt: Optional[str] = None
    patternMoney: Optional[Money] = None
    patternId: Optional[str] = None
    patternQuantity: Optional[Quantity] = None
    minValuePositiveInt: Optional[str] = None
    fixedPeriod: Optional[Period] = None
    defaultValueOid: Optional[str] = None
    orderMeaning: Optional[str] = None
    defaultValueUsageContext: Optional[UsageContext] = None
    fixedAttachment: Optional[Attachment] = None
    patternCodeableConcept: Optional[CodeableConcept] = None
    minValueQuantity: Optional[Quantity] = None
    base: Optional[Element] = None
    patternInteger: Optional[int] = None
    defaultValueParameterDefinition: Optional[ParameterDefinition] = None
    defaultValueDateTime: Optional[str] = None
    defaultValuePositiveInt: Optional[str] = None
    maxValueUnsignedInt: Optional[str] = None
    defaultValueInteger: Optional[int] = None
    isModifierReason: Optional[str] = None
    patternAddress: Optional[Address] = None
    patternBase64Binary: Optional[str] = None
    patternUrl: Optional[str] = None
    patternDateTime: Optional[str] = None
    defaultValueTiming: Optional[str] = None
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
    ageCodeableConcept: Optional[CodeableConcept] = None
    ageRange: Optional[Range] = None
    gender: Optional[CodeableConcept] = None
    physiologicalCondition: Optional[CodeableConcept] = None
    race: Optional[CodeableConcept] = None


class Dosage(BackboneElement):
    site: Optional[CodeableConcept] = None
    method: Optional[CodeableConcept] = None
    patientInstruction: Optional[str] = None
    maxDosePerLifetime: Optional[Quantity] = None
    maxDosePerAdministration: Optional[Quantity] = None
    route: Optional[CodeableConcept] = None
    asNeededBoolean: Optional[bool] = None
    timing: Optional[str] = None
    additionalInstruction: list[CodeableConcept] = []
    sequence: Optional[int] = None
    maxDosePerPeriod: Optional[Ratio] = None
    doseAndRate: list[Element] = []
    asNeededCodeableConcept: Optional[CodeableConcept] = None
    text: Optional[str] = None


class TimingRepeat(Element):
    boundsDuration: Optional[Duration] = None
    boundsRange: Optional[Range] = None
    boundsPeriod: Optional[Period] = None
    count: Optional[PositiveInt] = None
    countMax: Optional[PositiveInt] = None
    duration: Optional[float] = None
    durationMax: Optional[float] = None
    frequency: Optional[PositiveInt] = None
    frequencyMax: Optional[PositiveInt] = None
    period: Optional[float] = None
    periodMax: Optional[float] = None
    durationUnit: Optional[str] = None
    periodUnit: Optional[str] = None
    dayOfWeek: Optional[str] = None
    timeOfDay: Optional[str] = None
    when: Optional[str] = None
    offset: Optional[NonNegativeInt] = None


class Timing(BackboneElement):
    code: Optional[CodeableConcept] = None
    event: list[str] = []
    repeat: Optional[TimingRepeat] = None


class MarketingStatus(BackboneElement):
    country: CodeableConcept
    dateRange: Period
    jurisdiction: Optional[CodeableConcept] = None
    restoreDate: Optional[str] = None
    status: CodeableConcept


class SubstanceAmount(BackboneElement):
    amountQuantity: Optional[Quantity] = None
    amountRange: Optional[Range] = None
    amountString: Optional[str] = None
    amountText: Optional[str] = None
    amountType: Optional[CodeableConcept] = None
    referenceRange: Optional[Element] = None


class ProductShelfLife(BackboneElement):
    identifier: Optional[Identifier] = None
    period: Quantity
    specialPrecautionsForStorage: list[CodeableConcept] = []
    type: CodeableConcept


class ProdCharacteristic(BackboneElement):
    imprint: list[str] = []
    color: list[str] = []
    width: Optional[Quantity] = None
    nominalVolume: Optional[Quantity] = None
    weight: Optional[Quantity] = None
    shape: Optional[str] = None
    scoring: Optional[CodeableConcept] = None
    image: list[Attachment] = []
    depth: Optional[Quantity] = None
    externalDiameter: Optional[Quantity] = None
    height: Optional[Quantity] = None


class Parameters(Resource):
    parameter: list[BackboneElement] = []


class Binary(Resource):
    contentType: str
    data: Optional[str] = None
    securityContext: Optional[Reference] = None


class Bundle(Resource):
    entry: list[BackboneElement] = []
    identifier: Optional[Identifier] = None
    link: list[BackboneElement] = []
    signature: Optional[Signature] = None
    timestamp: Optional[str] = None
    total: Optional[str] = None
    type: str


class DomainResource(Resource):
    contained: list[Resource] = []
    extension: list[Extension] = []
    modifierExtension: list[Extension] = []
    text: Optional[Narrative] = None
