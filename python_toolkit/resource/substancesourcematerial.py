from typing import Optional
from base import *

class SubstanceSourceMaterial_Organism_Author(BackboneElement):
	authorDescription: Optional[str] = None
	authorType: Optional[CodeableConcept] = None

class SubstanceSourceMaterial_Organism_Hybrid(BackboneElement):
	hybridType: Optional[CodeableConcept] = None
	maternalOrganismId: Optional[str] = None
	maternalOrganismName: Optional[str] = None
	paternalOrganismId: Optional[str] = None
	paternalOrganismName: Optional[str] = None

class SubstanceSourceMaterial_Organism_OrganismGeneral(BackboneElement):
	class_: Optional[CodeableConcept] = None
	kingdom: Optional[CodeableConcept] = None
	order: Optional[CodeableConcept] = None
	phylum: Optional[CodeableConcept] = None

class SubstanceSourceMaterial_Organism(BackboneElement):
	author: list[SubstanceSourceMaterial_Organism_Author] = []
	family: Optional[CodeableConcept] = None
	genus: Optional[CodeableConcept] = None
	hybrid: Optional[SubstanceSourceMaterial_Organism_Hybrid] = None
	intraspecificDescription: Optional[str] = None
	intraspecificType: Optional[CodeableConcept] = None
	organismGeneral: Optional[SubstanceSourceMaterial_Organism_OrganismGeneral] = None
	species: Optional[CodeableConcept] = None

class SubstanceSourceMaterial_PartDescription(BackboneElement):
	part: Optional[CodeableConcept] = None
	partLocation: Optional[CodeableConcept] = None

class SubstanceSourceMaterial_FractionDescription(BackboneElement):
	fraction: Optional[str] = None
	materialType: Optional[CodeableConcept] = None

class SubstanceSourceMaterial(DomainResource):
	parentSubstanceName: list[str] = []
	organism: Optional[SubstanceSourceMaterial_Organism] = None
	partDescription: list[SubstanceSourceMaterial_PartDescription] = []
	developmentStage: Optional[CodeableConcept] = None
	fractionDescription: list[SubstanceSourceMaterial_FractionDescription] = []
	sourceMaterialState: Optional[CodeableConcept] = None
	countryOfOrigin: list[CodeableConcept] = []
	sourceMaterialType: Optional[CodeableConcept] = None
	organismId: Optional[Identifier] = None
	organismName: Optional[str] = None
	parentSubstanceId: list[Identifier] = []
	geographicalLocation: list[str] = []
	sourceMaterialClass: Optional[CodeableConcept] = None

