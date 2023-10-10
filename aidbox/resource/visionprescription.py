from typing import Optional
from ..base import *

class VisionPrescription_LensSpecification_Prism(BackboneElement):
	amount: str
	base: str

class VisionPrescription_LensSpecification(BackboneElement):
	sphere: Optional[str] = None
	color: Optional[str] = None
	eye: str
	diameter: Optional[str] = None
	duration: Optional[Quantity] = None
	brand: Optional[str] = None
	note: list[Annotation] = []
	power: Optional[str] = None
	product: CodeableConcept
	cylinder: Optional[str] = None
	prism: list[VisionPrescription_LensSpecification_Prism] = []
	axis: Optional[int] = None
	add: Optional[str] = None
	backCurve: Optional[str] = None

class VisionPrescription(DomainResource):
	created: str
	dateWritten: str
	encounter: Optional[Reference] = None
	identifier: list[Identifier] = []
	lensSpecification: list[VisionPrescription_LensSpecification]
	patient: Reference
	prescriber: Reference
	status: str

