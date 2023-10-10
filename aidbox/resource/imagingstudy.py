from typing import Optional
from ..base import *

class ImagingStudy_Series_Instance(BackboneElement):
	number: Optional[str] = None
	sopClass: Coding
	title: Optional[str] = None
	uid: str

class ImagingStudy_Series_Performer(BackboneElement):
	actor: Reference
	function: Optional[CodeableConcept] = None

class ImagingStudy_Series(BackboneElement):
	description: Optional[str] = None
	started: Optional[str] = None
	laterality: Optional[Coding] = None
	instance: list[ImagingStudy_Series_Instance] = []
	number: Optional[str] = None
	uid: str
	specimen: list[Reference] = []
	modality: Coding
	bodySite: Optional[Coding] = None
	endpoint: list[Reference] = []
	numberOfInstances: Optional[str] = None
	performer: list[ImagingStudy_Series_Performer] = []

class ImagingStudy(DomainResource):
	description: Optional[str] = None
	started: Optional[str] = None
	numberOfSeries: Optional[str] = None
	interpreter: list[Reference] = []
	series: list[ImagingStudy_Series] = []
	procedureReference: Optional[Reference] = None
	encounter: Optional[Reference] = None
	reasonCode: list[CodeableConcept] = []
	modality: list[Coding] = []
	note: list[Annotation] = []
	referrer: Optional[Reference] = None
	status: str
	identifier: list[Identifier] = []
	basedOn: list[Reference] = []
	location: Optional[Reference] = None
	endpoint: list[Reference] = []
	subject: Reference
	numberOfInstances: Optional[str] = None
	reasonReference: list[Reference] = []
	procedureCode: list[CodeableConcept] = []

