from typing import Optional
from ..base import *

class MolecularSequence_StructureVariant_Inner(BackboneElement):
	end: Optional[int] = None
	start: Optional[int] = None

class MolecularSequence_StructureVariant_Outer(BackboneElement):
	end: Optional[int] = None
	start: Optional[int] = None

class MolecularSequence_StructureVariant(BackboneElement):
	exact: Optional[bool] = None
	inner: Optional[MolecularSequence_StructureVariant_Inner] = None
	length: Optional[int] = None
	outer: Optional[MolecularSequence_StructureVariant_Outer] = None
	variantType: Optional[CodeableConcept] = None

class MolecularSequence_Repository(BackboneElement):
	datasetId: Optional[str] = None
	name: Optional[str] = None
	readsetId: Optional[str] = None
	type: str
	url: Optional[str] = None
	variantsetId: Optional[str] = None

class MolecularSequence_Variant(BackboneElement):
	cigar: Optional[str] = None
	end: Optional[int] = None
	observedAllele: Optional[str] = None
	referenceAllele: Optional[str] = None
	start: Optional[int] = None
	variantPointer: Optional[Reference] = None

class MolecularSequence_Quality_Roc(BackboneElement):
	fMeasure: list[str] = []
	numFN: list[int] = []
	numFP: list[int] = []
	numTP: list[int] = []
	precision: list[str] = []
	score: list[int] = []
	sensitivity: list[str] = []

class MolecularSequence_Quality(BackboneElement):
	truthTP: Optional[str] = None
	fScore: Optional[str] = None
	truthFN: Optional[str] = None
	queryFP: Optional[str] = None
	method: Optional[CodeableConcept] = None
	precision: Optional[str] = None
	start: Optional[int] = None
	queryTP: Optional[str] = None
	type: str
	recall: Optional[str] = None
	roc: Optional[MolecularSequence_Quality_Roc] = None
	score: Optional[Quantity] = None
	end: Optional[int] = None
	standardSequence: Optional[CodeableConcept] = None
	gtFP: Optional[str] = None

class MolecularSequence_ReferenceSeq(BackboneElement):
	chromosome: Optional[CodeableConcept] = None
	referenceSeqId: Optional[CodeableConcept] = None
	windowEnd: Optional[int] = None
	strand: Optional[str] = None
	genomeBuild: Optional[str] = None
	orientation: Optional[str] = None
	referenceSeqPointer: Optional[Reference] = None
	referenceSeqString: Optional[str] = None
	windowStart: Optional[int] = None

class MolecularSequence(DomainResource):
	patient: Optional[Reference] = None
	structureVariant: list[MolecularSequence_StructureVariant] = []
	repository: list[MolecularSequence_Repository] = []
	variant: list[MolecularSequence_Variant] = []
	specimen: Optional[Reference] = None
	type: Optional[str] = None
	pointer: list[Reference] = []
	observedSeq: Optional[str] = None
	identifier: list[Identifier] = []
	quality: list[MolecularSequence_Quality] = []
	device: Optional[Reference] = None
	quantity: Optional[Quantity] = None
	coordinateSystem: int
	referenceSeq: Optional[MolecularSequence_ReferenceSeq] = None
	performer: Optional[Reference] = None
	readCoverage: Optional[int] = None

