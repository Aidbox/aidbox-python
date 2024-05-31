from pydantic import *
from typing import Optional, List
from ..base import *

class BiologicallyDerivedProduct_Processing(BackboneElement):
	description: Optional[str] = None
	procedure: Optional[CodeableConcept] = None
	additive: Optional[Reference] = None
	timeDateTime: Optional[str] = None
	timePeriod: Optional[Period] = None

class BiologicallyDerivedProduct_Storage(BackboneElement):
	description: Optional[str] = None
	temperature: Optional[float] = None
	scale: Optional[str] = None
	duration: Optional[Period] = None

class BiologicallyDerivedProduct_Manipulation(BackboneElement):
	description: Optional[str] = None
	timeDateTime: Optional[str] = None
	timePeriod: Optional[Period] = None

class BiologicallyDerivedProduct_Collection(BackboneElement):
	collector: Optional[Reference] = None
	source: Optional[Reference] = None
	collectedDateTime: Optional[str] = None
	collectedPeriod: Optional[Period] = None

class BiologicallyDerivedProduct(DomainResource):
	request: Optional[List[Reference]] = None
	processing: Optional[List[BiologicallyDerivedProduct_Processing]] = None
	parent: Optional[List[Reference]] = None
	status: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	productCode: Optional[CodeableConcept] = None
	storage: Optional[List[BiologicallyDerivedProduct_Storage]] = None
	quantity: Optional[int] = None
	productCategory: Optional[str] = None
	manipulation: Optional[BiologicallyDerivedProduct_Manipulation] = None
	collection: Optional[BiologicallyDerivedProduct_Collection] = None