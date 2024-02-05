from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class DiagnosticReport_Media(BackboneElement):
	comment: Optional[str] = None
	link: Reference

class Lipidprofile(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/lipidprofile"])
	category: Optional[List[CodeableConcept]] = None
	conclusion: Optional[str] = None
	encounter: Optional[Reference] = None
	specimen: Optional[List[Reference]] = None
	effectiveDateTime: Optional[str] = None
	resultsInterpreter: Optional[List[Reference]] = None
	status: str
	result: Optional[List[Reference]] = None
	code: CodeableConcept
	identifier: Optional[List[Identifier]] = None
	issued: Optional[str] = None
	presentedForm: Optional[List[Attachment]] = None
	basedOn: Optional[List[Reference]] = None
	imagingStudy: Optional[List[Reference]] = None
	media: Optional[List[DiagnosticReport_Media]] = None
	subject: Optional[Reference] = None
	performer: Optional[List[Reference]] = None
	effectivePeriod: Optional[Period] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None