from pydantic import *
from typing import Optional, List
from ..base import *

class SubstanceProtein_Subunit(BackboneElement):
	subunit: Optional[int] = None
	sequence: Optional[str] = None
	length: Optional[int] = None
	sequenceAttachment: Optional[Attachment] = None
	nTerminalModificationId: Optional[Identifier] = None
	nTerminalModification: Optional[str] = None
	cTerminalModificationId: Optional[Identifier] = None
	cTerminalModification: Optional[str] = None

class SubstanceProtein(DomainResource):
	sequenceType: Optional[CodeableConcept] = None
	numberOfSubunits: Optional[int] = None
	disulfideLinkage: Optional[List[str]] = None
	subunit: Optional[List[SubstanceProtein_Subunit]] = None