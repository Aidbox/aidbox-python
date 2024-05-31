from pydantic import *
from typing import Optional, List
from ..base import *

class SubstanceNucleicAcid_Subunit_Linkage(BackboneElement):
	connectivity: Optional[str] = None
	identifier: Optional[Identifier] = None
	name: Optional[str] = None
	residueSite: Optional[str] = None

class SubstanceNucleicAcid_Subunit_Sugar(BackboneElement):
	identifier: Optional[Identifier] = None
	name: Optional[str] = None
	residueSite: Optional[str] = None

class SubstanceNucleicAcid_Subunit(BackboneElement):
	subunit: Optional[int] = None
	sequence: Optional[str] = None
	length: Optional[int] = None
	sequenceAttachment: Optional[Attachment] = None
	fivePrime: Optional[CodeableConcept] = None
	threePrime: Optional[CodeableConcept] = None
	linkage: Optional[List[SubstanceNucleicAcid_Subunit_Linkage]] = None
	sugar: Optional[List[SubstanceNucleicAcid_Subunit_Sugar]] = None

class SubstanceNucleicAcid(DomainResource):
	sequenceType: Optional[CodeableConcept] = None
	numberOfSubunits: Optional[int] = None
	areaOfHybridisation: Optional[str] = None
	oligoNucleotideType: Optional[CodeableConcept] = None
	subunit: Optional[List[SubstanceNucleicAcid_Subunit]] = None