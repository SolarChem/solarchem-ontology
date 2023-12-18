# SolarChem Ontology

Authors: Oier Beaskoetxea

Contributors: Ana Iglesias, Oscar Corcho, Daniel Garijo, Victor de la Peña O'Shea.

Vocabulary for the representation of photocatalysis processes mentioned in scientific papers. These experiments serve to define how a photocatalysis experiment has been done; under what circumstances, what products were used and what have been the results in order to analyze and reproduce the experiments mentioned in the articles. This vocabulary has been created in collaboration with the [IMDEA Energía](https://www.energia.imdea.org/) institute of Madrid.

This vocabulary is based on data used by the [IMDEA Energy](https://www.energia.imdea.org/) institute as part of its **[Artleafs](http://www.artleafs.eu/)** project. This project is dedicated to storing information regarding scientific articles related to the field of artificial photosynthesis, which is used to report how the photocatalysis experiments are done, to facilitate access to information and reproducibility of the same. The vocabulary also reuses concepts from other ontologies such as *[the Bibliographic Ontology](https://bibliontology.com/)* (BIBO) and [schema.org](https://schema.org/) to represent articles that define the experiments and their authors; *[Chemical Entities of Biological Interest](https://www.ebi.ac.uk/chebi/)* (ChEBI) used to represent chemical elements and *[Quantities, Units, Dimensions, and Types](https://www.qudt.org/)* (QUDT) for quantities and units of measure.

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




## Purpose and scope of the vocabulary

This vocabulary focuses on the representation of photocatalysis processes described in scientific articles. The vocabulary defines several classes and properties that allow describing such experiments, being the class [phcat:MaterialTransformationProcess](#MaterialTransformationProcess) the central axis of it and defining through its properties the context of the complete experiment, such as the input chemicals and output, defined as [phcat:Input](#Input) and [phcat:Output](#Output); the conditions to perform the process, defined by [phcat:Condition](#Condition); and the article that mentions them by an element of the class [bibo:Article](http://bibliontology.com/content/article.html). In addition to these characteristics, material transformation processes have information that characterizes them, such as [phcat:operationMode](#operationMode), [phcat:Eg](#Eg) or energy band, [phcat:BET](#BET) or Surface Area and [phcat:Yield](#Yield).

The elements of [bibo:Article](http://bibliontology.com/content/article.html) refer to the article in which the process is described. Among its properties are informative data about it, as well as relationships with the elements [bibo:Journal](http://gbol.life/ontology/bibo/Journal/) and [schema:Person](https://schema.org/person). The latter also contain information including [schema:Country](https://schema.org/Country) useful for searching by the researchers country of affiliation. The elements of the classes [phcat:Input](#Input) and [phcat:Output](#Output) store a reference of type [phcat:hasChemical](#hasChemical) with the class [chebi:CHEBI_24431](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:24431) (a chemical) but only the input elements fulfill a role of type [phcat:MaterialTransformationProcess](#MaterialTransformationProcess) for the process . On the other hand, the process can have several types of conditions, all of them subclasses of [phcat:Condition](#Condition), which represent an element measurable by some unit of measure and quantities of the QUDT ontology such as [qudt:Unit]( https://qudt.org/schema/qudt/Unit) and [qudt:value](https://qudt.org/schema/qudt/value).


<!-- # Development phases

The material generated in the different activities carried out during the development of the vocabulary, use
cases, user stories, glossary of terms, etc., will be available in the [Vocabulary Wiki](#)

# Project maintenance

To manage those incidents or suggested improvements with respect to the vocabulary, we recommend you to follow
the guides provided in [Issues Management](https://github.com/nombre-repositorio/wiki/issues-management) to
generate an issue (work in progress)

# Examples

Some [queries](https://github.com/repository-name/blob/master/examples/queries.md) will be performed in a
SPARQL endpoint to test and exemplify its operability. -->

