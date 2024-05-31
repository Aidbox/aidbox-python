from pydantic import *
from typing import Optional, List
from ..base import *

class MedicinalProductPharmaceutical_Characteristics(BackboneElement):
	code: CodeableConcept
	status: Optional[CodeableConcept] = None

class MedicinalProductPharmaceutical_RouteOfAdministration_TargetSpecies_WithdrawalPeriod(BackboneElement):
	tissue: CodeableConcept
	value: Quantity
	supportingInformation: Optional[str] = None

class MedicinalProductPharmaceutical_RouteOfAdministration_TargetSpecies(BackboneElement):
	code: CodeableConcept
	withdrawalPeriod: Optional[List[MedicinalProductPharmaceutical_RouteOfAdministration_TargetSpecies_WithdrawalPeriod]] = None

class MedicinalProductPharmaceutical_RouteOfAdministration(BackboneElement):
	code: CodeableConcept
	firstDose: Optional[Quantity] = None
	maxSingleDose: Optional[Quantity] = None
	maxDosePerDay: Optional[Quantity] = None
	maxDosePerTreatmentPeriod: Optional[Ratio] = None
	maxTreatmentPeriod: Optional[Duration] = None
	targetSpecies: Optional[List[MedicinalProductPharmaceutical_RouteOfAdministration_TargetSpecies]] = None

class MedicinalProductPharmaceutical(DomainResource):
	identifier: Optional[List[Identifier]] = None
	administrableDoseForm: CodeableConcept
	unitOfPresentation: Optional[CodeableConcept] = None
	ingredient: Optional[List[Reference]] = None
	device: Optional[List[Reference]] = None
	characteristics: Optional[List[MedicinalProductPharmaceutical_Characteristics]] = None
	routeOfAdministration: List[MedicinalProductPharmaceutical_RouteOfAdministration]