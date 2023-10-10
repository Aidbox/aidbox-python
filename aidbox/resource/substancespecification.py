from typing import Optional
from ..base import *

class SubstanceSpecification_Property(BackboneElement):
	category: Optional[CodeableConcept] = None
	definingSubstanceCodeableConcept: Optional[CodeableConcept] = None
	definingSubstanceReference: Optional[Reference] = None
	amountQuantity: Optional[Quantity] = None
	amountString: Optional[str] = None
	code: Optional[CodeableConcept] = None
	parameters: Optional[str] = None

class SubstanceSpecification_Name_Official(BackboneElement):
	authority: Optional[CodeableConcept] = None
	date: Optional[str] = None
	status: Optional[CodeableConcept] = None

class SubstanceSpecification_Name(BackboneElement):
	official: list[SubstanceSpecification_Name_Official] = []
	jurisdiction: list[CodeableConcept] = []
	name: str
	type: Optional[CodeableConcept] = None
	source: list[Reference] = []
	status: Optional[CodeableConcept] = None
	language: list[CodeableConcept] = []
	synonym: list[str] = []
	translation: list[str] = []
	preferred: Optional[bool] = None
	domain: list[CodeableConcept] = []

class SubstanceSpecification_Relationship(BackboneElement):
	substanceCodeableConcept: Optional[CodeableConcept] = None
	amountRatioLowLimit: Optional[Ratio] = None
	amountType: Optional[CodeableConcept] = None
	relationship: Optional[CodeableConcept] = None
	source: list[Reference] = []
	substanceReference: Optional[Reference] = None
	amountRatio: Optional[Ratio] = None
	amountQuantity: Optional[Quantity] = None
	amountString: Optional[str] = None
	isDefining: Optional[bool] = None
	amountRange: Optional[Range] = None

class SubstanceSpecification_Moiety(BackboneElement):
	role: Optional[CodeableConcept] = None
	name: Optional[str] = None
	molecularFormula: Optional[str] = None
	amountQuantity: Optional[Quantity] = None
	amountString: Optional[str] = None
	opticalActivity: Optional[CodeableConcept] = None
	identifier: Optional[Identifier] = None
	stereochemistry: Optional[CodeableConcept] = None

class SubstanceSpecification_Structure_Isotope_MolecularWeight(BackboneElement):
	amount: Optional[Quantity] = None
	method: Optional[CodeableConcept] = None
	type: Optional[CodeableConcept] = None

class SubstanceSpecification_Structure_Isotope(BackboneElement):
	halfLife: Optional[Quantity] = None
	identifier: Optional[Identifier] = None
	molecularWeight: Optional[SubstanceSpecification_Structure_Isotope_MolecularWeight] = None
	name: Optional[CodeableConcept] = None
	substitution: Optional[CodeableConcept] = None

class SubstanceSpecification_Structure_Representation(BackboneElement):
	attachment: Optional[Attachment] = None
	representation: Optional[str] = None
	type: Optional[CodeableConcept] = None

class SubstanceSpecification_Structure(BackboneElement):
	isotope: list[SubstanceSpecification_Structure_Isotope] = []
	molecularFormula: Optional[str] = None
	molecularFormulaByMoiety: Optional[str] = None
	molecularWeight: Optional[str] = None
	opticalActivity: Optional[CodeableConcept] = None
	representation: list[SubstanceSpecification_Structure_Representation] = []
	source: list[Reference] = []
	stereochemistry: Optional[CodeableConcept] = None

class SubstanceSpecification_Code(BackboneElement):
	code: Optional[CodeableConcept] = None
	comment: Optional[str] = None
	source: list[Reference] = []
	status: Optional[CodeableConcept] = None
	statusDate: Optional[str] = None

class SubstanceSpecification(DomainResource):
	description: Optional[str] = None
	property: list[SubstanceSpecification_Property] = []
	name: list[SubstanceSpecification_Name] = []
	referenceInformation: Optional[Reference] = None
	relationship: list[SubstanceSpecification_Relationship] = []
	type: Optional[CodeableConcept] = None
	moiety: list[SubstanceSpecification_Moiety] = []
	source: list[Reference] = []
	nucleicAcid: Optional[Reference] = None
	structure: Optional[SubstanceSpecification_Structure] = None
	status: Optional[CodeableConcept] = None
	comment: Optional[str] = None
	code: list[SubstanceSpecification_Code] = []
	identifier: Optional[Identifier] = None
	molecularWeight: list[str] = []
	polymer: Optional[Reference] = None
	protein: Optional[Reference] = None
	domain: Optional[CodeableConcept] = None
	sourceMaterial: Optional[Reference] = None

