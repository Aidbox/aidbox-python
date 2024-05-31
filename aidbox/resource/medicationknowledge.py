from pydantic import *
from typing import Optional, List
from ..base import *

class MedicationKnowledge_Monograph(BackboneElement):
	type: Optional[CodeableConcept] = None
	source: Optional[Reference] = None

class MedicationKnowledge_Regulatory_Substitution(BackboneElement):
	type: CodeableConcept
	allowed: bool

class MedicationKnowledge_Regulatory_Schedule(BackboneElement):
	schedule: CodeableConcept

class MedicationKnowledge_Regulatory_MaxDispense(BackboneElement):
	quantity: Quantity
	period: Optional[Duration] = None

class MedicationKnowledge_Regulatory(BackboneElement):
	regulatoryAuthority: Reference
	substitution: Optional[List[MedicationKnowledge_Regulatory_Substitution]] = None
	schedule: Optional[List[MedicationKnowledge_Regulatory_Schedule]] = None
	maxDispense: Optional[MedicationKnowledge_Regulatory_MaxDispense] = None

class MedicationKnowledge_DrugCharacteristic(BackboneElement):
	type: Optional[CodeableConcept] = None
	valueCodeableConcept: Optional[CodeableConcept] = None
	valueString: Optional[str] = None
	valueQuantity: Optional[Quantity] = None
	valueBase64Binary: Optional[str] = None

class MedicationKnowledge_Packaging(BackboneElement):
	type: Optional[CodeableConcept] = None
	quantity: Optional[Quantity] = None

class MedicationKnowledge_RelatedMedicationKnowledge(BackboneElement):
	type: CodeableConcept
	reference: List[Reference]

class MedicationKnowledge_MedicineClassification(BackboneElement):
	type: CodeableConcept
	classification: Optional[List[CodeableConcept]] = None

class MedicationKnowledge_Kinetics(BackboneElement):
	areaUnderCurve: Optional[List[Quantity]] = None
	lethalDose50: Optional[List[Quantity]] = None
	halfLifePeriod: Optional[Duration] = None

class MedicationKnowledge_Ingredient(BackboneElement):
	itemCodeableConcept: Optional[CodeableConcept] = None
	itemReference: Optional[Reference] = None
	isActive: Optional[bool] = None
	strength: Optional[Ratio] = None

class MedicationKnowledge_MonitoringProgram(BackboneElement):
	type: Optional[CodeableConcept] = None
	name: Optional[str] = None

class MedicationKnowledge_AdministrationGuidelines_Dosage(BackboneElement):
	type: CodeableConcept
	dosage: List[Dosage]

class MedicationKnowledge_AdministrationGuidelines_PatientCharacteristics(BackboneElement):
	characteristicCodeableConcept: Optional[CodeableConcept] = None
	characteristicQuantity: Optional[Quantity] = None
	value: Optional[List[str]] = None

class MedicationKnowledge_AdministrationGuidelines(BackboneElement):
	dosage: Optional[List[MedicationKnowledge_AdministrationGuidelines_Dosage]] = None
	indicationCodeableConcept: Optional[CodeableConcept] = None
	indicationReference: Optional[Reference] = None
	patientCharacteristics: Optional[List[MedicationKnowledge_AdministrationGuidelines_PatientCharacteristics]] = None

class MedicationKnowledge_Cost(BackboneElement):
	type: CodeableConcept
	source: Optional[str] = None
	cost: Money

class MedicationKnowledge(DomainResource):
	preparationInstruction: Optional[str] = None
	amount: Optional[Quantity] = None
	monograph: Optional[List[MedicationKnowledge_Monograph]] = None
	regulatory: Optional[List[MedicationKnowledge_Regulatory]] = None
	doseForm: Optional[CodeableConcept] = None
	intendedRoute: Optional[List[CodeableConcept]] = None
	drugCharacteristic: Optional[List[MedicationKnowledge_DrugCharacteristic]] = None
	packaging: Optional[MedicationKnowledge_Packaging] = None
	relatedMedicationKnowledge: Optional[List[MedicationKnowledge_RelatedMedicationKnowledge]] = None
	medicineClassification: Optional[List[MedicationKnowledge_MedicineClassification]] = None
	kinetics: Optional[List[MedicationKnowledge_Kinetics]] = None
	associatedMedication: Optional[List[Reference]] = None
	ingredient: Optional[List[MedicationKnowledge_Ingredient]] = None
	monitoringProgram: Optional[List[MedicationKnowledge_MonitoringProgram]] = None
	contraindication: Optional[List[Reference]] = None
	status: Optional[str] = None
	productType: Optional[List[CodeableConcept]] = None
	synonym: Optional[List[str]] = None
	code: Optional[CodeableConcept] = None
	administrationGuidelines: Optional[List[MedicationKnowledge_AdministrationGuidelines]] = None
	manufacturer: Optional[Reference] = None
	cost: Optional[List[MedicationKnowledge_Cost]] = None