from typing import Optional
from base import *

class SubstanceProtein_Subunit(BackboneElement):
	cTerminalModification: Optional[str] = None
	cTerminalModificationId: Optional[Identifier] = None
	length: Optional[int] = None
	nTerminalModification: Optional[str] = None
	nTerminalModificationId: Optional[Identifier] = None
	sequence: Optional[str] = None
	sequenceAttachment: Optional[Attachment] = None
	subunit: Optional[int] = None

class SubstanceProtein(DomainResource):
	disulfideLinkage: list[str] = []
	numberOfSubunits: Optional[int] = None
	sequenceType: Optional[CodeableConcept] = None
	subunit: list[SubstanceProtein_Subunit] = []

