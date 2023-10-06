from typing import Optional

from base import Reference
from base import CodeableConcept
from base import Identifier
from base import Reference
from base import DomainResource


class Basic(DomainResource):
	author: Optional[Reference] = None
	code: CodeableConcept
	created: Optional[str] = None
	identifier: list[Identifier] = []
	subject: Optional[Reference] = None

