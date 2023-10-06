from typing import Optional

from base import DataRequirement
from base import Reference
from base import CodeableConcept
from base import Reference
from base import Reference
from base import Identifier
from base import Annotation
from base import Reference
from base import Identifier
from base import CodeableConcept
from base import Reference
from base import Reference
from base import Reference
from base import DomainResource


class GuidanceResponse(DomainResource):
	dataRequirement: list[DataRequirement] = []
	moduleCanonical: Optional[str] = None
	encounter: Optional[Reference] = None
	reasonCode: list[CodeableConcept] = []
	outputParameters: Optional[Reference] = None
	evaluationMessage: list[Reference] = []
	requestIdentifier: Optional[Identifier] = None
	note: list[Annotation] = []
	status: str
	result: Optional[Reference] = None
	identifier: list[Identifier] = []
	moduleCodeableConcept: Optional[CodeableConcept] = None
	moduleUri: Optional[str] = None
	occurrenceDateTime: Optional[str] = None
	subject: Optional[Reference] = None
	performer: Optional[Reference] = None
	reasonReference: list[Reference] = []

