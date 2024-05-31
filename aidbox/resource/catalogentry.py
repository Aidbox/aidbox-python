from pydantic import *
from typing import Optional, List
from ..base import *

class CatalogEntry_RelatedEntry(BackboneElement):
	relationtype: str
	item: Reference

class CatalogEntry(DomainResource):
	additionalCharacteristic: Optional[List[CodeableConcept]] = None
	additionalClassification: Optional[List[CodeableConcept]] = None
	referencedItem: Reference
	type: Optional[CodeableConcept] = None
	classification: Optional[List[CodeableConcept]] = None
	validityPeriod: Optional[Period] = None
	orderable: bool
	status: Optional[str] = None
	validTo: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	additionalIdentifier: Optional[List[Identifier]] = None
	lastUpdated: Optional[str] = None
	relatedEntry: Optional[List[CatalogEntry_RelatedEntry]] = None