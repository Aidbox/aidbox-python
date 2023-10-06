from typing import Optional

from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import CodeableConcept
from base import BackboneElement
from base import BackboneElement
from base import CodeableConcept
from base import Reference
from base import DomainResource


class VerificationResult(DomainResource):
	failureAction: Optional[CodeableConcept] = None
	validationType: Optional[CodeableConcept] = None
	targetLocation: list[str] = []
	validator: list[BackboneElement] = []
	need: Optional[CodeableConcept] = None
	frequency: Optional[str] = None
	nextScheduled: Optional[str] = None
	primarySource: list[BackboneElement] = []
	attestation: Optional[BackboneElement] = None
	status: str
	validationProcess: list[CodeableConcept] = []
	statusDate: Optional[str] = None
	target: list[Reference] = []
	lastPerformed: Optional[str] = None

