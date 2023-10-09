from typing import Optional
from ..base import *

class Basic(DomainResource):
	author: Optional[Reference] = None
	code: CodeableConcept
	created: Optional[str] = None
	identifier: list[Identifier] = []
	subject: Optional[Reference] = None

