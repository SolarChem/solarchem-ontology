# SolarChem Ontology

**Contributors**: Ana Iglesias-Molina, Daniel Garijo, Victor de la Peña O'Shea, Laura Collado, Miguel Tecedor.

**Past Contributors**: Oier Beaskoetxea, Oscar Corcho.

Ontology for the representation of execution of experiments of three kinds, photocatalysis, electrocatalysis and photoelectrocatalysis, mentioned in scientific papers. It enables describing how experiments has been conducted; under what conditions, using which inputs and the outputs obtained and measured, in order to analyze and reproduce the experiments mentioned in scientific articles. It reuses concepts from other ontologies such as [the Bibliographic Ontology](https://bibliontology.com/) (BIBO) and [schema.org](https://schema.org/) to represent articles that define the experiments and their authors; [Chemical Entities of Biological Interest](https://www.ebi.ac.uk/chebi/) (ChEBI) used to represent chemical elements, [Ontology for Biomedical Investigations](https://obofoundry.org/ontology/obi.html) (OBI) for conditions in the experiments and [Quantities, Units, Dimensions, and Types](https://www.qudt.org/) (QUDT) for quantities and units of measurement. 

We include in this repository the resources related to the ontology development and publication, along with a corresponding knowledge graph instantiating the ontology with photocatalysis experiments:
* `./docs`: Releases of the documentation of the ontology.
* `./knowledge-graph`: Resources related to the creation of the knowledge graph with photocatalysis experiments data extracted from scientific literature. It includes Jupyter notebooks used for data cleaning, processing and enrichment, configurations for the tools used and the mappings that establish the relationships between the source data and the ontology.
* `./ontology`: OWL code for the four modules comprising the SolarChem ontology
* `./requirements`: Requirements and competency questions that the ontology must satisfy written in natural language. 



<p align="center">
 <img src="./docs/vocab/images/solarchem-diagram.svg/" alt="workflow" width="100%"/>
</p>

## Availability

The landing page of the ontology is accessible at `https://w3id.org/solar/`. Solarchem is divided in 4 modules:
- The solarchem core module: `https://w3id.org/solar/o/core`
- The SolarChem Photocatalysis module: `https://w3id.org/solar/o/pc`
- The SolarChem Electrocatalysis module: `http://w3id.org/solar/o/ec`
- The SolarChem Photoelectrocatalysis: `http://w3id.org/solar/o/pec`

All modules are available in a machine-readable manner with content negotiation. For example, to download a module in turtle, just issue the following command:
```
curl -sH "Accept:text/turtle"  -L https://w3id.org/solar/o/core
```

## Acknowledgements

This resource has been created in collaboration with the [IMDEA Energía](https://www.energia.imdea.org/) institute of Madrid, as part of the research project _[SOLARCHEM 5.0](https://energia.imdea.org/en/porfolio/solarchem-5-0-towards-digital-transition-in-solar-chemistry-solarchem-5-0-ai-assisted-robotized-platform-for-the-development-of-efficient-photoelectrodes/): Towards Digital Transition in Solar Chemistry: AI-assisted robotized platform for the development of efficient photoelectrodes_, corresponding to the call 2021 and reference: TED2021-130173B-C41, within the State Program to Promote Scientific-Technical Research and its Transfer (Strategic Projects Oriented to Ecological Transition and Digital Transition).
