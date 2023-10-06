from typing import Optional

from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import Identifier
from base import Period
from base import Reference
from base import DomainResource


class Flag(DomainResource):
	author: Optional[Reference] = None
	category: list[CodeableConcept] = []
	code: CodeableConcept
	encounter: Optional[Reference] = None
	identifier: list[Identifier] = []
	period: Optional[Period] = None
	status: str
	subject: Reference

