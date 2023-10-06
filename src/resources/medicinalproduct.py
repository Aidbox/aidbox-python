from typing import Optional

from base import CodeableConcept
from base import BackboneElement
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import BackboneElement
from base import Reference
from base import Reference
from base import CodeableConcept
from base import BackboneElement
from base import Reference
from base import Identifier
from base import Identifier
from base import Reference
from base import Coding
from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import MarketingStatus
from base import DomainResource


class MedicinalProduct(DomainResource):
	additionalMonitoringIndicator: Optional[CodeableConcept] = None
	manufacturingBusinessOperation: list[BackboneElement] = []
	combinedPharmaceuticalDoseForm: Optional[CodeableConcept] = None
	clinicalTrial: list[Reference] = []
	productClassification: list[CodeableConcept] = []
	name: list[BackboneElement]
	masterFile: list[Reference] = []
	pharmaceuticalProduct: list[Reference] = []
	type: Optional[CodeableConcept] = None
	marketingStatus: list[MarketingStatus] = []
	specialMeasures: list[str] = []
	specialDesignation: list[BackboneElement] = []
	packagedMedicinalProduct: list[Reference] = []
	identifier: list[Identifier] = []
	crossReference: list[Identifier] = []
	attachedDocument: list[Reference] = []
	domain: Optional[Coding] = None
	legalStatusOfSupply: Optional[CodeableConcept] = None
	paediatricUseIndicator: Optional[CodeableConcept] = None
	contact: list[Reference] = []

