from typing import Optional
from base import *

class MedicinalProductPharmaceutical_Characteristics(BackboneElement):
	code: CodeableConcept
	status: Optional[CodeableConcept] = None

class MedicinalProductPharmaceutical_RouteOfAdministration_TargetSpecies_WithdrawalPeriod(BackboneElement):
	supportingInformation: Optional[str] = None
	tissue: CodeableConcept
	value: Quantity

class MedicinalProductPharmaceutical_RouteOfAdministration_TargetSpecies(BackboneElement):
	code: CodeableConcept
	withdrawalPeriod: list[MedicinalProductPharmaceutical_RouteOfAdministration_TargetSpecies_WithdrawalPeriod] = []

class MedicinalProductPharmaceutical_RouteOfAdministration(BackboneElement):
	code: CodeableConcept
	firstDose: Optional[Quantity] = None
	maxDosePerDay: Optional[Quantity] = None
	maxDosePerTreatmentPeriod: Optional[Ratio] = None
	maxSingleDose: Optional[Quantity] = None
	maxTreatmentPeriod: Optional[str] = None
	targetSpecies: list[MedicinalProductPharmaceutical_RouteOfAdministration_TargetSpecies] = []

class MedicinalProductPharmaceutical(DomainResource):
	administrableDoseForm: CodeableConcept
	characteristics: list[MedicinalProductPharmaceutical_Characteristics] = []
	device: list[Reference] = []
	identifier: list[Identifier] = []
	ingredient: list[Reference] = []
	routeOfAdministration: list[MedicinalProductPharmaceutical_RouteOfAdministration]
	unitOfPresentation: Optional[CodeableConcept] = None

