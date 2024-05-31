from pydantic import *
from typing import Optional, List
from ..base import *

class DocumentManifest_Related(BackboneElement):
	identifier: Optional[Identifier] = None
	ref: Optional[Reference] = None

class DocumentManifest(DomainResource):
	description: Optional[str] = None
	content: List[Reference]
	recipient: Optional[List[Reference]] = None
	type: Optional[CodeableConcept] = None
	created: Optional[str] = None
	related: Optional[List[DocumentManifest_Related]] = None
	source: Optional[str] = None
	author: Optional[List[Reference]] = None
	masterIdentifier: Optional[Identifier] = None
	status: str
	identifier: Optional[List[Identifier]] = None
	subject: Optional[Reference] = None