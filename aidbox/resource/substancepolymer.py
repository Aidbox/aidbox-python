from pydantic import *
from typing import Optional, List
from ..base import *

class SubstancePolymer_MonomerSet_StartingMaterial(BackboneElement):
	material: Optional[CodeableConcept] = None
	type: Optional[CodeableConcept] = None
	isDefining: Optional[bool] = None
	amount: Optional[SubstanceAmount] = None

class SubstancePolymer_MonomerSet(BackboneElement):
	ratioType: Optional[CodeableConcept] = None
	startingMaterial: Optional[List[SubstancePolymer_MonomerSet_StartingMaterial]] = None

class SubstancePolymer_Repeat_RepeatUnit_DegreeOfPolymerisation(BackboneElement):
	degree: Optional[CodeableConcept] = None
	amount: Optional[SubstanceAmount] = None

class SubstancePolymer_Repeat_RepeatUnit_StructuralRepresentation(BackboneElement):
	type: Optional[CodeableConcept] = None
	representation: Optional[str] = None
	attachment: Optional[Attachment] = None

class SubstancePolymer_Repeat_RepeatUnit(BackboneElement):
	orientationOfPolymerisation: Optional[CodeableConcept] = None
	repeatUnit: Optional[str] = None
	amount: Optional[SubstanceAmount] = None
	degreeOfPolymerisation: Optional[List[SubstancePolymer_Repeat_RepeatUnit_DegreeOfPolymerisation]] = None
	structuralRepresentation: Optional[List[SubstancePolymer_Repeat_RepeatUnit_StructuralRepresentation]] = None

class SubstancePolymer_Repeat(BackboneElement):
	numberOfUnits: Optional[int] = None
	averageMolecularFormula: Optional[str] = None
	repeatUnitAmountType: Optional[CodeableConcept] = None
	repeatUnit: Optional[List[SubstancePolymer_Repeat_RepeatUnit]] = None

class SubstancePolymer(DomainResource):
	class_: Optional[CodeableConcept] = None
	geometry: Optional[CodeableConcept] = None
	copolymerConnectivity: Optional[List[CodeableConcept]] = None
	modification: Optional[List[str]] = None
	monomerSet: Optional[List[SubstancePolymer_MonomerSet]] = None
	repeat: Optional[List[SubstancePolymer_Repeat]] = None