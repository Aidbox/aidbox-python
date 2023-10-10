from typing import Optional
from ..base import *

class MedicationKnowledge_Monograph(BackboneElement):
	source: Optional[Reference] = None
	type: Optional[CodeableConcept] = None

class MedicationKnowledge_Regulatory_MaxDispense(BackboneElement):
	period: Optional[str] = None
	quantity: Quantity

class MedicationKnowledge_Regulatory_Schedule(BackboneElement):
	schedule: CodeableConcept

class MedicationKnowledge_Regulatory_Substitution(BackboneElement):
	allowed: bool
	type: CodeableConcept

class MedicationKnowledge_Regulatory(BackboneElement):
	maxDispense: Optional[MedicationKnowledge_Regulatory_MaxDispense] = None
	regulatoryAuthority: Reference
	schedule: list[MedicationKnowledge_Regulatory_Schedule] = []
	substitution: list[MedicationKnowledge_Regulatory_Substitution] = []

class MedicationKnowledge_DrugCharacteristic(BackboneElement):
	type: Optional[CodeableConcept] = None
	valueBase64Binary: Optional[str] = None
	valueCodeableConcept: Optional[CodeableConcept] = None
	valueQuantity: Optional[Quantity] = None
	valueString: Optional[str] = None

class MedicationKnowledge_Packaging(BackboneElement):
	quantity: Optional[Quantity] = None
	type: Optional[CodeableConcept] = None

class MedicationKnowledge_RelatedMedicationKnowledge(BackboneElement):
	reference: list[Reference]
	type: CodeableConcept

class MedicationKnowledge_MedicineClassification(BackboneElement):
	classification: list[CodeableConcept] = []
	type: CodeableConcept

class MedicationKnowledge_Kinetics(BackboneElement):
	areaUnderCurve: list[Quantity] = []
	halfLifePeriod: Optional[str] = None
	lethalDose50: list[Quantity] = []

class MedicationKnowledge_Ingredient(BackboneElement):
	isActive: Optional[bool] = None
	itemCodeableConcept: Optional[CodeableConcept] = None
	itemReference: Optional[Reference] = None
	strength: Optional[Ratio] = None

class MedicationKnowledge_MonitoringProgram(BackboneElement):
	name: Optional[str] = None
	type: Optional[CodeableConcept] = None

class MedicationKnowledge_AdministrationGuidelines_Dosage(BackboneElement):
	dosage: list[str]
	type: CodeableConcept

class MedicationKnowledge_AdministrationGuidelines_PatientCharacteristics(BackboneElement):
	characteristicCodeableConcept: Optional[CodeableConcept] = None
	characteristicQuantity: Optional[Quantity] = None
	value: list[str] = []

class MedicationKnowledge_AdministrationGuidelines(BackboneElement):
	dosage: list[MedicationKnowledge_AdministrationGuidelines_Dosage] = []
	indicationCodeableConcept: Optional[CodeableConcept] = None
	indicationReference: Optional[Reference] = None
	patientCharacteristics: list[MedicationKnowledge_AdministrationGuidelines_PatientCharacteristics] = []

class MedicationKnowledge_Cost(BackboneElement):
	cost: Money
	source: Optional[str] = None
	type: CodeableConcept

class MedicationKnowledge(DomainResource):
	preparationInstruction: Optional[str] = None
	amount: Optional[Quantity] = None
	monograph: list[MedicationKnowledge_Monograph] = []
	regulatory: list[MedicationKnowledge_Regulatory] = []
	doseForm: Optional[CodeableConcept] = None
	intendedRoute: list[CodeableConcept] = []
	drugCharacteristic: list[MedicationKnowledge_DrugCharacteristic] = []
	packaging: Optional[MedicationKnowledge_Packaging] = None
	relatedMedicationKnowledge: list[MedicationKnowledge_RelatedMedicationKnowledge] = []
	medicineClassification: list[MedicationKnowledge_MedicineClassification] = []
	kinetics: list[MedicationKnowledge_Kinetics] = []
	associatedMedication: list[Reference] = []
	ingredient: list[MedicationKnowledge_Ingredient] = []
	monitoringProgram: list[MedicationKnowledge_MonitoringProgram] = []
	contraindication: list[Reference] = []
	status: Optional[str] = None
	productType: list[CodeableConcept] = []
	synonym: list[str] = []
	code: Optional[CodeableConcept] = None
	administrationGuidelines: list[MedicationKnowledge_AdministrationGuidelines] = []
	manufacturer: Optional[Reference] = None
	cost: list[MedicationKnowledge_Cost] = []

