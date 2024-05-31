from pydantic import *
from typing import Optional, List
from ..base import *

class ImagingStudy_Series_Instance(BackboneElement):
	uid: str
	sopClass: Coding
	number: Optional[NonNegativeInt] = None
	title: Optional[str] = None

class ImagingStudy_Series_Performer(BackboneElement):
	function: Optional[CodeableConcept] = None
	actor: Reference

class ImagingStudy_Series(BackboneElement):
	description: Optional[str] = None
	started: Optional[str] = None
	laterality: Optional[Coding] = None
	instance: Optional[List[ImagingStudy_Series_Instance]] = None
	number: Optional[NonNegativeInt] = None
	uid: str
	specimen: Optional[List[Reference]] = None
	modality: Coding
	bodySite: Optional[Coding] = None
	endpoint: Optional[List[Reference]] = None
	numberOfInstances: Optional[NonNegativeInt] = None
	performer: Optional[List[ImagingStudy_Series_Performer]] = None

class ImagingStudy(DomainResource):
	description: Optional[str] = None
	started: Optional[str] = None
	numberOfSeries: Optional[NonNegativeInt] = None
	interpreter: Optional[List[Reference]] = None
	series: Optional[List[ImagingStudy_Series]] = None
	procedureReference: Optional[Reference] = None
	encounter: Optional[Reference] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	modality: Optional[List[Coding]] = None
	note: Optional[List[Annotation]] = None
	referrer: Optional[Reference] = None
	status: str
	identifier: Optional[List[Identifier]] = None
	basedOn: Optional[List[Reference]] = None
	location: Optional[Reference] = None
	endpoint: Optional[List[Reference]] = None
	subject: Reference
	numberOfInstances: Optional[NonNegativeInt] = None
	reasonReference: Optional[List[Reference]] = None
	procedureCode: Optional[List[CodeableConcept]] = None