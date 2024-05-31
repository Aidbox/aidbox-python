from pydantic import *
from typing import Optional, List
from ..base import *

class SubstanceSourceMaterial_Organism_Author(BackboneElement):
	authorType: Optional[CodeableConcept] = None
	authorDescription: Optional[str] = None

class SubstanceSourceMaterial_Organism_Hybrid(BackboneElement):
	maternalOrganismId: Optional[str] = None
	maternalOrganismName: Optional[str] = None
	paternalOrganismId: Optional[str] = None
	paternalOrganismName: Optional[str] = None
	hybridType: Optional[CodeableConcept] = None

class SubstanceSourceMaterial_Organism_OrganismGeneral(BackboneElement):
	kingdom: Optional[CodeableConcept] = None
	phylum: Optional[CodeableConcept] = None
	class_: Optional[CodeableConcept] = None
	order: Optional[CodeableConcept] = None

class SubstanceSourceMaterial_Organism(BackboneElement):
	family: Optional[CodeableConcept] = None
	genus: Optional[CodeableConcept] = None
	species: Optional[CodeableConcept] = None
	intraspecificType: Optional[CodeableConcept] = None
	intraspecificDescription: Optional[str] = None
	author: Optional[List[SubstanceSourceMaterial_Organism_Author]] = None
	hybrid: Optional[SubstanceSourceMaterial_Organism_Hybrid] = None
	organismGeneral: Optional[SubstanceSourceMaterial_Organism_OrganismGeneral] = None

class SubstanceSourceMaterial_PartDescription(BackboneElement):
	part: Optional[CodeableConcept] = None
	partLocation: Optional[CodeableConcept] = None

class SubstanceSourceMaterial_FractionDescription(BackboneElement):
	fraction: Optional[str] = None
	materialType: Optional[CodeableConcept] = None

class SubstanceSourceMaterial(DomainResource):
	parentSubstanceName: Optional[List[str]] = None
	organism: Optional[SubstanceSourceMaterial_Organism] = None
	partDescription: Optional[List[SubstanceSourceMaterial_PartDescription]] = None
	developmentStage: Optional[CodeableConcept] = None
	fractionDescription: Optional[List[SubstanceSourceMaterial_FractionDescription]] = None
	sourceMaterialState: Optional[CodeableConcept] = None
	countryOfOrigin: Optional[List[CodeableConcept]] = None
	sourceMaterialType: Optional[CodeableConcept] = None
	organismId: Optional[Identifier] = None
	organismName: Optional[str] = None
	parentSubstanceId: Optional[List[Identifier]] = None
	geographicalLocation: Optional[List[str]] = None
	sourceMaterialClass: Optional[CodeableConcept] = None