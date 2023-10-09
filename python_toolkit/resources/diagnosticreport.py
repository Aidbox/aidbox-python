from typing import Optional
from base import *

class DiagnosticReport_Media(BackboneElement):
	comment: Optional[str] = None
	link: Reference

class DiagnosticReport(DomainResource):
	category: list[CodeableConcept] = []
	conclusionCode: list[CodeableConcept] = []
	conclusion: Optional[str] = None
	encounter: Optional[Reference] = None
	specimen: list[Reference] = []
	effectiveDateTime: Optional[str] = None
	resultsInterpreter: list[Reference] = []
	status: str
	result: list[Reference] = []
	code: CodeableConcept
	identifier: list[Identifier] = []
	issued: Optional[str] = None
	presentedForm: list[Attachment] = []
	basedOn: list[Reference] = []
	imagingStudy: list[Reference] = []
	media: list[DiagnosticReport_Media] = []
	subject: Optional[Reference] = None
	performer: list[Reference] = []
	effectivePeriod: Optional[Period] = None

