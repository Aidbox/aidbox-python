from typing import Optional
from base import *

class SubstanceReferenceInformation_Classification(BackboneElement):
	classification: Optional[CodeableConcept] = None
	domain: Optional[CodeableConcept] = None
	source: list[Reference] = []
	subtype: list[CodeableConcept] = []

class SubstanceReferenceInformation_Gene(BackboneElement):
	gene: Optional[CodeableConcept] = None
	geneSequenceOrigin: Optional[CodeableConcept] = None
	source: list[Reference] = []

class SubstanceReferenceInformation_GeneElement(BackboneElement):
	element: Optional[Identifier] = None
	source: list[Reference] = []
	type: Optional[CodeableConcept] = None

class SubstanceReferenceInformation_Target(BackboneElement):
	organism: Optional[CodeableConcept] = None
	organismType: Optional[CodeableConcept] = None
	amountType: Optional[CodeableConcept] = None
	type: Optional[CodeableConcept] = None
	interaction: Optional[CodeableConcept] = None
	source: list[Reference] = []
	amountQuantity: Optional[Quantity] = None
	amountString: Optional[str] = None
	target: Optional[Identifier] = None
	amountRange: Optional[Range] = None

class SubstanceReferenceInformation(DomainResource):
	classification: list[SubstanceReferenceInformation_Classification] = []
	comment: Optional[str] = None
	gene: list[SubstanceReferenceInformation_Gene] = []
	geneElement: list[SubstanceReferenceInformation_GeneElement] = []
	target: list[SubstanceReferenceInformation_Target] = []

