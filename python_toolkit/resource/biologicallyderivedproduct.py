from typing import Optional
from base import *

class BiologicallyDerivedProduct_Processing(BackboneElement):
	additive: Optional[Reference] = None
	description: Optional[str] = None
	procedure: Optional[CodeableConcept] = None
	timeDateTime: Optional[str] = None
	timePeriod: Optional[Period] = None

class BiologicallyDerivedProduct_Storage(BackboneElement):
	description: Optional[str] = None
	duration: Optional[Period] = None
	scale: Optional[str] = None
	temperature: Optional[str] = None

class BiologicallyDerivedProduct_Manipulation(BackboneElement):
	description: Optional[str] = None
	timeDateTime: Optional[str] = None
	timePeriod: Optional[Period] = None

class BiologicallyDerivedProduct_Collection(BackboneElement):
	collectedDateTime: Optional[str] = None
	collectedPeriod: Optional[Period] = None
	collector: Optional[Reference] = None
	source: Optional[Reference] = None

class BiologicallyDerivedProduct(DomainResource):
	request: list[Reference] = []
	processing: list[BiologicallyDerivedProduct_Processing] = []
	parent: list[Reference] = []
	status: Optional[str] = None
	identifier: list[Identifier] = []
	productCode: Optional[CodeableConcept] = None
	storage: list[BiologicallyDerivedProduct_Storage] = []
	quantity: Optional[int] = None
	productCategory: Optional[str] = None
	manipulation: Optional[BiologicallyDerivedProduct_Manipulation] = None
	collection: Optional[BiologicallyDerivedProduct_Collection] = None

