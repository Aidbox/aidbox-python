from typing import Optional

from base import Quantity
from base import BackboneElement
from base import BackboneElement
from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import BackboneElement
from base import BackboneElement
from base import BackboneElement
from base import BackboneElement
from base import Reference
from base import BackboneElement
from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import Reference
from base import BackboneElement
from base import DomainResource


class MedicationKnowledge(DomainResource):
	preparationInstruction: Optional[str] = None
	amount: Optional[Quantity] = None
	monograph: list[BackboneElement] = []
	regulatory: list[BackboneElement] = []
	doseForm: Optional[CodeableConcept] = None
	intendedRoute: list[CodeableConcept] = []
	drugCharacteristic: list[BackboneElement] = []
	packaging: Optional[BackboneElement] = None
	relatedMedicationKnowledge: list[BackboneElement] = []
	medicineClassification: list[BackboneElement] = []
	kinetics: list[BackboneElement] = []
	associatedMedication: list[Reference] = []
	ingredient: list[BackboneElement] = []
	monitoringProgram: list[BackboneElement] = []
	contraindication: list[Reference] = []
	status: Optional[str] = None
	productType: list[CodeableConcept] = []
	synonym: list[str] = []
	code: Optional[CodeableConcept] = None
	administrationGuidelines: list[BackboneElement] = []
	manufacturer: Optional[Reference] = None
	cost: list[BackboneElement] = []

