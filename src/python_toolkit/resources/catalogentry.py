from typing import Optional
from base import *

class CatalogEntry_RelatedEntry(BackboneElement):
	item: Reference
	relationtype: str

class CatalogEntry(DomainResource):
	additionalCharacteristic: list[CodeableConcept] = []
	additionalClassification: list[CodeableConcept] = []
	referencedItem: Reference
	type: Optional[CodeableConcept] = None
	classification: list[CodeableConcept] = []
	validityPeriod: Optional[Period] = None
	orderable: bool
	status: Optional[str] = None
	validTo: Optional[str] = None
	identifier: list[Identifier] = []
	additionalIdentifier: list[Identifier] = []
	lastUpdated: Optional[str] = None
	relatedEntry: list[CatalogEntry_RelatedEntry] = []

