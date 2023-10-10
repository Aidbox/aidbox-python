from typing import Optional
from ..base import *

class DocumentManifest_Related(BackboneElement):
	identifier: Optional[Identifier] = None
	ref: Optional[Reference] = None

class DocumentManifest(DomainResource):
	description: Optional[str] = None
	content: list[Reference]
	recipient: list[Reference] = []
	type: Optional[CodeableConcept] = None
	created: Optional[str] = None
	related: list[DocumentManifest_Related] = []
	source: Optional[str] = None
	author: list[Reference] = []
	masterIdentifier: Optional[Identifier] = None
	status: str
	identifier: list[Identifier] = []
	subject: Optional[Reference] = None

