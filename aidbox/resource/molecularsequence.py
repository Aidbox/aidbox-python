from pydantic import *
from typing import Optional, List
from ..base import *

class MolecularSequence_StructureVariant_Outer(BackboneElement):
	start: Optional[int] = None
	end: Optional[int] = None

class MolecularSequence_StructureVariant_Inner(BackboneElement):
	start: Optional[int] = None
	end: Optional[int] = None

class MolecularSequence_StructureVariant(BackboneElement):
	variantType: Optional[CodeableConcept] = None
	exact: Optional[bool] = None
	length: Optional[int] = None
	outer: Optional[MolecularSequence_StructureVariant_Outer] = None
	inner: Optional[MolecularSequence_StructureVariant_Inner] = None

class MolecularSequence_Repository(BackboneElement):
	type: str
	url: Optional[str] = None
	name: Optional[str] = None
	datasetId: Optional[str] = None
	variantsetId: Optional[str] = None
	readsetId: Optional[str] = None

class MolecularSequence_Variant(BackboneElement):
	start: Optional[int] = None
	end: Optional[int] = None
	observedAllele: Optional[str] = None
	referenceAllele: Optional[str] = None
	cigar: Optional[str] = None
	variantPointer: Optional[Reference] = None

class MolecularSequence_Quality_Roc(BackboneElement):
	score: Optional[List[int]] = None
	numTP: Optional[List[int]] = None
	numFP: Optional[List[int]] = None
	numFN: Optional[List[int]] = None
	precision: Optional[List[float]] = None
	sensitivity: Optional[List[float]] = None
	fMeasure: Optional[List[float]] = None

class MolecularSequence_Quality(BackboneElement):
	truthTP: Optional[float] = None
	fScore: Optional[float] = None
	truthFN: Optional[float] = None
	queryFP: Optional[float] = None
	method: Optional[CodeableConcept] = None
	precision: Optional[float] = None
	start: Optional[int] = None
	queryTP: Optional[float] = None
	type: str
	recall: Optional[float] = None
	roc: Optional[MolecularSequence_Quality_Roc] = None
	score: Optional[Quantity] = None
	end: Optional[int] = None
	standardSequence: Optional[CodeableConcept] = None
	gtFP: Optional[float] = None

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
	structureVariant: Optional[List[MolecularSequence_StructureVariant]] = None
	repository: Optional[List[MolecularSequence_Repository]] = None
	variant: Optional[List[MolecularSequence_Variant]] = None
	specimen: Optional[Reference] = None
	type: Optional[str] = None
	pointer: Optional[List[Reference]] = None
	observedSeq: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	quality: Optional[List[MolecularSequence_Quality]] = None
	device: Optional[Reference] = None
	quantity: Optional[Quantity] = None
	coordinateSystem: int
	referenceSeq: Optional[MolecularSequence_ReferenceSeq] = None
	performer: Optional[Reference] = None
	readCoverage: Optional[int] = None