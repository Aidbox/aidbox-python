from typing import Optional
from base import *

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
	fivePrime: Optional[CodeableConcept] = None
	length: Optional[int] = None
	linkage: list[SubstanceNucleicAcid_Subunit_Linkage] = []
	sequence: Optional[str] = None
	sequenceAttachment: Optional[Attachment] = None
	subunit: Optional[int] = None
	sugar: list[SubstanceNucleicAcid_Subunit_Sugar] = []
	threePrime: Optional[CodeableConcept] = None

class SubstanceNucleicAcid(DomainResource):
	areaOfHybridisation: Optional[str] = None
	numberOfSubunits: Optional[int] = None
	oligoNucleotideType: Optional[CodeableConcept] = None
	sequenceType: Optional[CodeableConcept] = None
	subunit: list[SubstanceNucleicAcid_Subunit] = []

