from typing import Optional
from base import *

class SubstancePolymer_MonomerSet_StartingMaterial(BackboneElement):
	amount: Optional[SubstanceAmount] = None
	isDefining: Optional[bool] = None
	material: Optional[CodeableConcept] = None
	type: Optional[CodeableConcept] = None

class SubstancePolymer_MonomerSet(BackboneElement):
	ratioType: Optional[CodeableConcept] = None
	startingMaterial: list[SubstancePolymer_MonomerSet_StartingMaterial] = []

class SubstancePolymer_Repeat_RepeatUnit_DegreeOfPolymerisation(BackboneElement):
	amount: Optional[SubstanceAmount] = None
	degree: Optional[CodeableConcept] = None

class SubstancePolymer_Repeat_RepeatUnit_StructuralRepresentation(BackboneElement):
	attachment: Optional[Attachment] = None
	representation: Optional[str] = None
	type: Optional[CodeableConcept] = None

class SubstancePolymer_Repeat_RepeatUnit(BackboneElement):
	amount: Optional[SubstanceAmount] = None
	degreeOfPolymerisation: list[SubstancePolymer_Repeat_RepeatUnit_DegreeOfPolymerisation] = []
	orientationOfPolymerisation: Optional[CodeableConcept] = None
	repeatUnit: Optional[str] = None
	structuralRepresentation: list[SubstancePolymer_Repeat_RepeatUnit_StructuralRepresentation] = []

class SubstancePolymer_Repeat(BackboneElement):
	averageMolecularFormula: Optional[str] = None
	numberOfUnits: Optional[int] = None
	repeatUnit: list[SubstancePolymer_Repeat_RepeatUnit] = []
	repeatUnitAmountType: Optional[CodeableConcept] = None

class SubstancePolymer(DomainResource):
	class_: Optional[CodeableConcept] = None
	copolymerConnectivity: list[CodeableConcept] = []
	geometry: Optional[CodeableConcept] = None
	modification: list[str] = []
	monomerSet: list[SubstancePolymer_MonomerSet] = []
	repeat: list[SubstancePolymer_Repeat] = []

