from pydantic import *
from typing import Optional, List
from ..base import *

class Basic(DomainResource):
	identifier: Optional[List[Identifier]] = None
	code: CodeableConcept
	subject: Optional[Reference] = None
	created: Optional[str] = None
	author: Optional[Reference] = None