from typing import Optional

from base import Reference
from base import BackboneElement
from base import Reference
from base import Reference
from base import Identifier
from base import Reference
from base import Reference
from base import Reference
from base import DomainResource


class QuestionnaireResponse(DomainResource):
	questionnaire: Optional[str] = None
	encounter: Optional[Reference] = None
	item: list[BackboneElement] = []
	source: Optional[Reference] = None
	author: Optional[Reference] = None
	status: str
	identifier: Optional[Identifier] = None
	basedOn: list[Reference] = []
	authored: Optional[str] = None
	partOf: list[Reference] = []
	subject: Optional[Reference] = None

