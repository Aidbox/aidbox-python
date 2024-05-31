from pydantic import *
from typing import Optional, List
from ..base import *

class SubstanceReferenceInformation_Gene(BackboneElement):
	geneSequenceOrigin: Optional[CodeableConcept] = None
	gene: Optional[CodeableConcept] = None
	source: Optional[List[Reference]] = None

class SubstanceReferenceInformation_GeneElement(BackboneElement):
	type: Optional[CodeableConcept] = None
	element: Optional[Identifier] = None
	source: Optional[List[Reference]] = None

class SubstanceReferenceInformation_Classification(BackboneElement):
	domain: Optional[CodeableConcept] = None
	classification: Optional[CodeableConcept] = None
	subtype: Optional[List[CodeableConcept]] = None
	source: Optional[List[Reference]] = None

class SubstanceReferenceInformation_Target(BackboneElement):
	organism: Optional[CodeableConcept] = None
	organismType: Optional[CodeableConcept] = None
	amountType: Optional[CodeableConcept] = None
	type: Optional[CodeableConcept] = None
	interaction: Optional[CodeableConcept] = None
	source: Optional[List[Reference]] = None
	amountQuantity: Optional[Quantity] = None
	amountString: Optional[str] = None
	target: Optional[Identifier] = None
	amountRange: Optional[Range] = None

class SubstanceReferenceInformation(DomainResource):
	comment: Optional[str] = None
	gene: Optional[List[SubstanceReferenceInformation_Gene]] = None
	geneElement: Optional[List[SubstanceReferenceInformation_GeneElement]] = None
	classification: Optional[List[SubstanceReferenceInformation_Classification]] = None
	target: Optional[List[SubstanceReferenceInformation_Target]] = None