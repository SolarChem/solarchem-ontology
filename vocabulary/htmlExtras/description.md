As mentioned above, the scope of this vocabulary is the representation of photocatalysis processes mentioned in scientific articles. The vocabulary defines several classes and properties that allow describing said experiments, being the class [phcat:MaterialTransformationProcess](#MaterialTransformationProcess) the central axis of it and defining through its properties the context of the complete experiment, such as the input chemicals and output, defined as [phcat:Input](#Input) and [phcat:Output](#Output); the conditions prepared to perform the process, defined by [phcat:Condition](#Condition); and the article that mentions them by an element of the class [bibo:Article](http://bibliontology.com/content/article.html). In addition to these characteristics, material transformation processes have information that characterizes them such as [phcat:operationMode](#operationMode), [phcat:Eg](#Eg) or energy band, [phcat:BET](#BET) or Surface Area and [phcat:Yield](#Yield).

The elements of [bibo:Article](http://bibliontology.com/content/article.html) refer to the article in which the process is described and among its properties are informative data about it, as well as relationships with the [bibo:Journal](http://gbol.life/ontology/bibo/Journal/) and [schema:Person](https://schema.org/Person) elements. The latter also contain information including [schema:Country](https://schema.org/Country), useful later for searching for the country of affiliation. The elements of the classes [phcat:Input](#Input) and [phcat:Output](#Output) both store a reference of the type [phcat:hasChemical](#hasChemical) with the class [chebi:CHEBI_24431](https ://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:24431) (chemical entity) but only the input elements fulfill a role of type [phcat:MaterialTransformationProcess](#MaterialTransformationProcess) for the process. On the other hand, the process can have several types of conditions, all of them subclasses of [phcat:Condition](#Condition), which represent an element measurable by some unit of measure and quantities of the QUDT ontology such as [qudt:Unit]( https://qudt.org/schema/qudt/Unit) and [qudt:value](https://qudt.org/schema/qudt/value).

## 3.1 Examples of use

In order to facilitate the understanding of the use of some classes and properties of this vocabulary, some examples will be provided below.

First we generate an instance of the class [bibo:Article](http://bibliontology.com/content/article.html) and add the properties [bibo:doi](http://gbol.life/ontology/bibo /doi/), [bibo:abstract](http://gbol.life/0.1/abstract/), [bibo:volume](http://gbol.life/ontology/bibo/volume/), [dcterms: title](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/title/), [bibo:issue](http://gbol.life/ontology/bibo/issue/) , [dcterms:date](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/date/) and [bibo:pageStart](http://gbol.life/ontology/bibo /pageStart/). After this we create on the one hand an element of the class [bibo:Journal](http://gbol.life/ontology/bibo/Journal/) (with its [dcterms:title](https://www.dublincore.org /specifications/dublin-core/dcmi-terms/terms/title/) property) and associate it with the part using the property [dcterms:isPartOf](dublincore.org/specifications/dublin-core/dcmi-terms/terms/ isPartOf/); and on the other we instantiate the class [schema:Person](https://schema.org/Person) with the properties [schema:name](https://schema.org/name) and [schema:email](https ://schema.org/email) of the authors and associate them with a [schema:Country](https://schema.org/Country) element to define their country of affiliation ([phcat:affiliationCountry] (#affiliationCountry)). Articles are usually identified by their [DOI](https://www.doi.org/) uri, as well as journals can be identified by [ISSN](https://www.issn.org/) and authors through systems such as [ORCID](https://orcid.org/). Later we will instantiate the [phcat:MaterialTransformationProcess](#MaterialTransformationProcess) class for each experiment referenced and associate them with the node using the [phcat:hasMaterialTransformationProcess](#hasMaterialTransformationProcess) property. For this example below we will use the article *[Synthesis of Ag@AgBr/AgCl heterostructured nanocashews with enhanced photocatalytic performance via anion exchange](https://doi.org/10.1039/C2JM31736B)*.

    <https://doi.org/10.1039/C2JM31736B> a bibo:Article ;
        bibo:doi "10.1039/C2JM31736B" ;
        bibo:abstract "Heterostructured Ag@AgBr/AgCl nanocashews have been synthesized by an anion-exchange reaction between AgCl nanocubes and Br&minus; ions followed by photoreduction. Compared to polyhedral Ag@AgBr nanoparticles, the obtained nanostructures exhibit enhanced photocatalytic activity towards decomposition of organic pollutants, i.e., rhodamine-B (RhB). For example, only 2 min is taken to completely decompose RhB molecules with the assistance of these novel heterostructured nanoparticles under visible light irradiation. Furthermore, the as-synthesized nanocatalyst can be reused 20 times without losing activity, showing its high stability. Interestingly, the novel heterostructured Ag@AgBr/AgCl nanophotocatalyst also shows efficient visible light conversion of CO2 to energetic fuels, e.g. methanol/ethanol. Therefore, the present route opens an avenue to achieve highly efficient visible-light-driven nanophotocatalysts for applications in environmental remediation and resourceful use of CO2." ;
        bibo:volume 22 ;
        dcterms:title "Synthesis of Ag@AgBr/AgCl heterostructured nanocashews with enhanced photocatalytic performance via anion exchange" ;
        dcterms:date 2012 ;
        bibo:pageStart 13153 ;
        dcterms:isPartOf  <https://portal.issn.org/resource/ISSN/1571-1013>;
        #NOTE: no se ha podido encontrar a todos los autores
        dcterms:creator  <https://orcid.org/0000-0003-2227-5008> ;
        dcterms:creator  <https://orcid.org/0000-0002-4106-9093> ;
        dcterms:creator  <https://scholar.google.com/citations?user=GZOJpwYAAAAJ&hl=es&oi=sra> ;
        dcterms:creator  <https://orcid.org/0000-0003-3030-2440> ;
        dcterms:creator	<#WenJiang> ;
        phcat:hasMaterialTransformationProcess <#process4> .
    <https://portal.issn.org/resource/ISSN/0959-9428> a bibo:Journal ;
        dcterms:title "Journal of Materials Chemistry" .
    <https://orcid.org/0000-0003-2227-5008> a schema:Person ;
        schema:email "qhzhang@upc.edu.cn" ;
        phcat:affilitaionCountry <https://en.wikipedia.org/wiki/China>^^schema:Country .
    <https://orcid.org/0000-0002-4106-9093> a schema:Person ;
        schema:email "jizhuang@jnu.edu.cn" ;
        phcat:affilitaionCountry <https://en.wikipedia.org/wiki/China>^^schema:Country .
    <https://scholar.google.com/citations?user=GZOJpwYAAAAJ&hl=es&oi=sra> a schema:Person ;
        phcat:affilitaionCountry <https://en.wikipedia.org/wiki/China>^^schema:Country .
    <https://orcid.org/0000-0003-3030-2440> a schema:Person ;
        phcat:affilitaionCountry <https://en.wikipedia.org/wiki/China>^^schema:Country .
    <#WenJiang> a schema:Person ;
        schema:name "Wen Jiang" .

Next we create the instances of the [phcat:MaterialTransformationProcess](#MaterialTransformationProcess) class. Then we add its [rdfs:label](https://www.w3.org/TR/rdf-schema/#ch_label) (process name) and [phcat:operationMode](#operationMode) properties first. After that, we add the information about the [phcat:Eg](#Eg) (Energy Band), [phcat:BET](#BET) (Specific Surface Area) and [phcat:Yield] (yield) and the we associate with the properties of the same name starting with *has* ([phcat:hasEg](#hasEg), [phcat:hasBET](#hasBET), [phcat:hasYield](#hasYield)) if we have them. The next thing to do is to add the [phcat:Input](#Input), which we will explain later, and associate them ([phcat:hasInput](#hasInput)). We then create the [phcat:Output](#Output) and associate them with their chemical using [phcat:hasChemical](#hasChemical) and their [phcat:OutputQuantity](#OutputQuantity) ([phcat:hasOutputQuantity](#hasOutputQuantity)) which can be associated with units ([qudt:unit]) of different types: [unit:MicroMOL-PER-M2-HR](https://qudt.org/vocab/unit/MicroMOL-PER-M2-HR) , [unit:MicroMOL-PER-GM](https://qudt.org/vocab/unit/MicroMOL-PER-GM) or [unit:MicroMOL-PER-GM-HR](https://qudt.org/ vocab/unit/MicroMOL-PER-GM-HR) all of them instances of [qudt:Unit](https://qudt.org/schema/qudt/Unit). At the end we create the instances of [phcat:Condition](#Condition) as [phcat:hasCondition](#hasCondition) properties for the transformation process.

<!-- inputs -->
To generate the elements of type [phcat:Input](#Input) it is only necessary to add the properties of [phcat:percentage](#percentage), [phcat:crystalStructure](#crystalStructure) (this only if the element is a catalyst), [phcat:hasChemical](#hasChemical) (to link it with the corresponding [chebi:CHEBI_24431](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:24431) instance) and [phcat:hasRole](#hasRole) which is the role that instances of [phcat:MaterialTransformationRole](#MaterialTransformationRole) have in the input, among which we find [phcat:Catalyst](#Catalyst), [phcat:CoCatalyst ](#CoCatalyst), [phcat:Dye](#Dye), [phcat:Support](#Support), [phcat:Dopant](#Dopant) or [phcat:Reductant](#Reductant).

    <#process4> a phcat:MaterialTransformation ;
        rdfs:label "Ag@AgBr/AgCl"xsd:string ;
        phcat:hasInput <#process4/catalyst_AgCl> ;
        phcat:hasInput <#process4/co-catalyst_AgBr> ;
        phcat:hasInput <#process4/co-catalyst_Ag> ;
        phcat:hasInput <#process4/support_NiO2> ;
        phcat:hasInput <#process1/reductant_H20> ;
        phcat:reportedIn <https://doi.org/10.1039/C2JM31736B>
        phcat:operationMode "Continuous"
        phcat:hasCondition <#process4/reaction-medium> ;
        phcat:hasCondition <#process4/reactor-condition> ;
        phcat:hasCondition <#process4/lightsource> ;
        phcat:hasCondition <#process4/lamppower> ;
        phcat:hasCondition <#process4/catalyst-set-up> ;
        phcat:hasCondition <#process4/reaction-time> ;
        phcat:hasOutput <#process4/output1> ;
        phcat:hasOutput <#process4/output2> ;
        phcat:hasOutput <#process4/output3> ;
        phcat:hasOutput <#process4/output4> .
    <#process4/catalyst_AgCl> a phcat:Input ;
        phcat:hasChemical chebi:CHEBI_30341 ;
        phcat:hasRole phcat:Catalyst .
    <#AgBr> a chebi:CHEBI_24431
        chebi:formula "AgBr" .
    <#process4/co-catalyst_AgBr> a phcat:Input ;
        phcat:hasChemical <#AgBr> ;
        phcat:hasRole phcat:Co-catalyst .
    <#process4/co-catalyst_Ag> a phcat:Input ;
        phcat:hasChemical chebi:CHEBI_30512 ;
        phcat:hasRole phcat:Co-catalyst .
    <#process4/support_NiO2/chemical> a chebi:CHEBI_24431
        chebi:formula "NiO2" .
    <#process4/support_NiO2> a phcat:Input ;
        phcat:hasChemical <#process4/support_NiO2/chemical> ;
        phcat:hasRole phcat:Support .
    <#process4/reductant_H20> a phcat:Input ;
        phcat:hasChemical chebi:CHEBI_15377^^chebi:CHEBI_24431 ;
        phcat:hasRole phcat:Reductant .
    <#CH3OH> a chebi:CHEBI_24431
        chebi:formula "CH3OH" ;
        rdfs:label "metanol" .
    <#process4/output1> a phcat:Output ;
        phcat:hasChemical <#CH3OH> ;
        phcat:hasOutputQuantity <#process4/output1/quantity> .
    <#process4/output1/quantity> a phcat:OutputQuantity ;
        qudt:numericValue 220 ;
        qudt:unit unit:MicroMOL-PER-GM .
    <#process4/output2> a phcat:Output ;
        phcat:hasChemical chebi:<#CH3OH> ;
        phcat:hasOutputQuantity <#process4/output2/quantity> .
    <#process4/output2/quantity> a phcat:OutputQuantity ;
        qudt:numericValue 44 ;
        qudt:unit unit:MicroMOL-PER-GM-HR .
    <#process4/output3> a phcat:Output ;
        phcat:hasChemical chebi:CHEBI_16236 ;
        phcat:hasOutputQuantity <#process4/output3/quantity> .
    <#process4/output3/quantity> a phcat:OutputQuantity ;
        qudt:numericValue 310 ;
        qudt:unit unit:MicroMOL-PER-GM-HR .
    <#process4/output4> a phcat:Output ;
        phcat:hasChemical chebi:CHEBI_16236 ;
        phcat:hasOutputQuantity <#process4/output4/quantity> .
    <#process4/output4/quantity> a phcat:OutputQuantity ;
        qudt:numericValue 62 ;
        qudt:unit unit:MicroMOL-PER-GM-HR .

<!-- conditions -->
To create the conditions, simply instantiate the child classes of [phcat:Condition](#Condition). These classes have the property [phcat:conditionType](#conditionType) (explanation of the type of condition, when it is inherited it defines the type of reactor, the configuration, ...) and can contain quantities, if they appear specified, defined by [qudt:value](https://qudt.org/schema/qudt/value) and [qudt:unit](https://qudt.org/schema/qudt/unit).