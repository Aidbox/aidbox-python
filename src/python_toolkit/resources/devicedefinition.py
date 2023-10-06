from typing import Optional

from base import BackboneElement
from base import BackboneElement
from base import BackboneElement
from base import CodeableConcept
from base import Reference
from base import BackboneElement
from base import BackboneElement
from base import Reference
from base import Annotation
from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import Identifier
from base import Quantity
from base import ContactPoint
from base import Reference
from base import ProductShelfLife
from base import ProdCharacteristic
from base import DomainResource


class DeviceDefinition(DomainResource):
	deviceName: list[BackboneElement] = []
	shelfLifeStorage: list[ProductShelfLife] = []
	property: list[BackboneElement] = []
	manufacturerString: Optional[str] = None
	modelNumber: Optional[str] = None
	udiDeviceIdentifier: list[BackboneElement] = []
	type: Optional[CodeableConcept] = None
	manufacturerReference: Optional[Reference] = None
	capability: list[BackboneElement] = []
	specialization: list[BackboneElement] = []
	parentDevice: Optional[Reference] = None
	note: list[Annotation] = []
	languageCode: list[CodeableConcept] = []
	safety: list[CodeableConcept] = []
	material: list[BackboneElement] = []
	url: Optional[str] = None
	identifier: list[Identifier] = []
	quantity: Optional[Quantity] = None
	version: list[str] = []
	contact: list[ContactPoint] = []
	owner: Optional[Reference] = None
	onlineInformation: Optional[str] = None
	physicalCharacteristics: Optional[ProdCharacteristic] = None

