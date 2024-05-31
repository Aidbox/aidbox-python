from pydantic import *
from typing import Optional, List, Literal
from ..base import *
class Coding812479(Coding):
	system: Literal["http://loinc.org"] = "http://loinc.org"
	code: Literal["81247-9"] = "81247-9"

class McodeGenomicsReportCode(CodeableConcept):
	coding: List[Coding812479] = [Coding812479()]


class DiagnosticReport_Media(BackboneElement):
	comment: Optional[str] = None
	link: Reference

class McodeGenomicsReport(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-genomics-report"])
	category: List[CodeableConcept]
	conclusionCode: Optional[List[CodeableConcept]] = None
	conclusion: Optional[str] = None
	encounter: Optional[Reference] = None
	specimen: Optional[List[Reference]] = None
	effectiveDateTime: Optional[str] = None
	resultsInterpreter: Optional[List[Reference]] = None
	status: str
	result: Optional[List[Reference]] = None
	code: McodeGenomicsReportCode = McodeGenomicsReportCode()
	identifier: Optional[List[Identifier]] = None
	issued: str
	presentedForm: Optional[List[Attachment]] = None
	basedOn: Optional[List[Reference]] = None
	imagingStudy: Optional[List[Reference]] = None
	media: Optional[List[DiagnosticReport_Media]] = None
	subject: Reference
	performer: Optional[List[Reference]] = None
	effectivePeriod: Optional[Period] = None