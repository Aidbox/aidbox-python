from pydantic import *
from typing import Optional, List
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
	status: Optional[CodeableConcept] = None
	date: Optional[str] = None

class SubstanceSpecification_Name(BackboneElement):
	official: Optional[List[SubstanceSpecification_Name_Official]] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	name: str
	type: Optional[CodeableConcept] = None
	source: Optional[List[Reference]] = None
	status: Optional[CodeableConcept] = None
	language: Optional[List[CodeableConcept]] = None
	synonym: Optional[List[str]] = None
	translation: Optional[List[str]] = None
	preferred: Optional[bool] = None
	domain: Optional[List[CodeableConcept]] = None

class SubstanceSpecification_Relationship(BackboneElement):
	substanceCodeableConcept: Optional[CodeableConcept] = None
	amountRatioLowLimit: Optional[Ratio] = None
	amountType: Optional[CodeableConcept] = None
	relationship: Optional[CodeableConcept] = None
	source: Optional[List[Reference]] = None
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
	method: Optional[CodeableConcept] = None
	type: Optional[CodeableConcept] = None
	amount: Optional[Quantity] = None

class SubstanceSpecification_Structure_Isotope(BackboneElement):
	identifier: Optional[Identifier] = None
	name: Optional[CodeableConcept] = None
	substitution: Optional[CodeableConcept] = None
	halfLife: Optional[Quantity] = None
	molecularWeight: Optional[SubstanceSpecification_Structure_Isotope_MolecularWeight] = None

class SubstanceSpecification_Structure_Representation(BackboneElement):
	type: Optional[CodeableConcept] = None
	representation: Optional[str] = None
	attachment: Optional[Attachment] = None

class SubstanceSpecification_Structure(BackboneElement):
	stereochemistry: Optional[CodeableConcept] = None
	opticalActivity: Optional[CodeableConcept] = None
	molecularFormula: Optional[str] = None
	molecularFormulaByMoiety: Optional[str] = None
	isotope: Optional[List[SubstanceSpecification_Structure_Isotope]] = None
	molecularWeight: Optional[str] = None
	source: Optional[List[Reference]] = None
	representation: Optional[List[SubstanceSpecification_Structure_Representation]] = None

class SubstanceSpecification_Code(BackboneElement):
	code: Optional[CodeableConcept] = None
	status: Optional[CodeableConcept] = None
	statusDate: Optional[str] = None
	comment: Optional[str] = None
	source: Optional[List[Reference]] = None

class SubstanceSpecification(DomainResource):
	description: Optional[str] = None
	property: Optional[List[SubstanceSpecification_Property]] = None
	name: Optional[List[SubstanceSpecification_Name]] = None
	referenceInformation: Optional[Reference] = None
	relationship: Optional[List[SubstanceSpecification_Relationship]] = None
	type: Optional[CodeableConcept] = None
	moiety: Optional[List[SubstanceSpecification_Moiety]] = None
	source: Optional[List[Reference]] = None
	nucleicAcid: Optional[Reference] = None
	structure: Optional[SubstanceSpecification_Structure] = None
	status: Optional[CodeableConcept] = None
	comment: Optional[str] = None
	code: Optional[List[SubstanceSpecification_Code]] = None
	identifier: Optional[Identifier] = None
	molecularWeight: Optional[List[str]] = None
	polymer: Optional[Reference] = None
	protein: Optional[Reference] = None
	domain: Optional[CodeableConcept] = None
	sourceMaterial: Optional[Reference] = None