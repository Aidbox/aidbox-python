from typing import Optional

from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import CodeableConcept
from base import Identifier
from base import Attachment
from base import Reference
from base import Reference
from base import BackboneElement
from base import Reference
from base import Reference
from base import Period
from base import DomainResource


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
	media: list[BackboneElement] = []
	subject: Optional[Reference] = None
	performer: list[Reference] = []
	effectivePeriod: Optional[Period] = None

