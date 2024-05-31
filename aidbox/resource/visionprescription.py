from pydantic import *
from typing import Optional, List
from ..base import *

class VisionPrescription_LensSpecification_Prism(BackboneElement):
	amount: float
	base: str

class VisionPrescription_LensSpecification(BackboneElement):
	sphere: Optional[float] = None
	color: Optional[str] = None
	eye: str
	diameter: Optional[float] = None
	duration: Optional[Quantity] = None
	brand: Optional[str] = None
	note: Optional[List[Annotation]] = None
	power: Optional[float] = None
	product: CodeableConcept
	cylinder: Optional[float] = None
	prism: Optional[List[VisionPrescription_LensSpecification_Prism]] = None
	axis: Optional[int] = None
	add: Optional[float] = None
	backCurve: Optional[float] = None

class VisionPrescription(DomainResource):
	identifier: Optional[List[Identifier]] = None
	status: str
	created: str
	patient: Reference
	encounter: Optional[Reference] = None
	dateWritten: str
	prescriber: Reference
	lensSpecification: List[VisionPrescription_LensSpecification]