Como se ha mencionado anteriormente este vocabulario se centra en la representación de procesos de fotocatálisis descritos en artículos científicos. El vocabulario define varias clases y propiedades que permiten describir dichos dichos experimentos, siendo la clase [phcat:MaterialTransformationProcess](#MaterialTransformationProcess) el eje central de la misma y definiendo mediante sus propiedades el contexto del experimento completo, como por ejemplo los químicos de entrada y de salida, definidos como [phcat:Input](#Input) y [phcat:Output](#Output); las condiciones para realizar el proceso, definidas mediante [phcat:Condition](#Condition); y el artículo que los menciona por un elemento de la clase [bibo:Article](http://bibliontology.com/content/article.html). Además de estas características, los procesos de transformación de materiales cuentan con información que los caracteriza, como el [phcat:operationMode](#operationMode), [phcat:Eg](#Eg) o banda energética, [phcat:BET](#BET) o Superficie específica y [phcat:Yield](#Yield). 

Los elementos de [bibo:Article](http://bibliontology.com/content/article.html) referencian al artículo en el que el proceso es descrito. Entre sus propiedades se encuentran datos informativos sobre el mismo, así como relaciones con los elementos [bibo:Journal](http://gbol.life/ontology/bibo/Journal/) y [schema:Person](https://schema.org/Person). Estos últimos además contienen información entre la que se encuentra el [schema:Country](https://schema.org/Country) útil para hacer búsquedas por país de afiliación de los investigadores. Los elementos de las clases [phcat:Input](#Input) y [phcat:Output](#Output) guardan una referencia del tipo [phcat:hasChemical](#hasChemical) con la clase [chebi:CHEBI_24431](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:24431) (una sustancia química) pero solo los elementos de entrada cumplen con un rol del tipo [phcat:MaterialTransformationProcess](#MaterialTransformationProcess) para el proceso. Por otro lado el proceso puede tener varios tipos de condiciones, todas ellas subclases de [phcat:Condition](#Condition), las cuales representan un elemento medible mediante alguna unidad de medida y cantidades de la ontología QUDT como [qudt:Unit](https://qudt.org/schema/qudt/Unit) y [qudt:value](https://qudt.org/schema/qudt/value).

<!-- SKOS -->
También se han utilizado varios esquemas conceptuales (Tesauros) de SKOS para representar algunas de las clasificaciones de este dominio. <!-- La Figura 1 muestra algunas de estas relaciones con los esquemas conceptuales de SKOS. --> En el caso de esta ontología, estos esquemas se han usado para definir los modos de operación posibles y para controlar la clasificación de varios tipos de condición (propiedad phcat:conditionTypeAsSKOSConcept) como la fuente de luz y medio de reacción.

## 3.1 Ejemplos de uso

Con la finalidad de facilitar la comprensión del uso de algunas clases y propiedades de este vocabulario se proporcionarán a continuación algunos ejemplos.

En primer lugar generamos una instancia de la clase [bibo:Article](http://bibliontology.com/content/article.html) y añadimos las propiedades [bibo:doi](http://gbol.life/ontology/bibo/doi/), [bibo:abstract](http://gbol.life/0.1/abstract/), [bibo:volume](http://gbol.life/ontology/bibo/volume/), [dcterms:title](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/title/), [bibo:issue](http://gbol.life/ontology/bibo/issue/), [dcterms:date](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/date/) y [bibo:pageStart](http://gbol.life/ontology/bibo/pageStart/). Tras esto creamos por un lado un elemento de la clase [bibo:Journal](http://gbol.life/ontology/bibo/Journal/) (con su [dcterms:title](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/title/) como propiedad) y lo asociamos con el artículo mediante la propiedad [dcterms:isPartOf](dublincore.org/specifications/dublin-core/dcmi-terms/terms/isPartOf/); y por el otro instanciamos la clase [schema:Person](https://schema.org/Person) con las propiedades [schema:name](https://schema.org/name) y [schema:email](https://schema.org/email) de los autores de la publicación y los asociamos con un elemento de [schema:Country](https://schema.org/Country) para definir su país de afiliación ([phcat:affiliationCountry](#affiliationCountry)). Los artículos suelen ser identificados mediante la uri de su [DOI](https://www.doi.org/) así como los journal pueden ser identificados por [ISSN](https://www.issn.org/) y los autores mediante sistemas como [ORCID](https://orcid.org/). Más tarde instanciaremos la clase [phcat:MaterialTransformationProcess](#MaterialTransformationProcess) para cada experimento del artículo y las asociaremos con el artículo mediante la propiedad [phcat:hasMaterialTransformationProcess](#hasMaterialTransformationProcess). Para este ejemplo a continuación usaremos el artículo *[Synthesis of Ag@AgBr/AgCl heterostructured nanocashews with enhanced photocatalytic performance via anion exchange](https://doi.org/10.1039/C2JM31736B)*.

    <https://doi.org/10.1039/C2JM31736B> a bibo:Article ;
        bibo:doi "10.1039/C2JM31736B" ;
        bibo:abstract "Heterostructured Ag@AgBr/AgCl nanocashews have been synthesized by an anion-exchange reaction between AgCl nanocubes and Br&minus; ions followed by photoreduction. Compared to polyhedral Ag@AgBr nanoparticles, the obtained nanostructures exhibit enhanced photocatalytic activity towards decomposition of organic pollutants, i.e., rhodamine-B (RhB). For example, only 2 min is taken to completely decompose RhB molecules with the assistance of these novel heterostructured nanoparticles under visible light irradiation. Furthermore, the as-synthesized nanocatalyst can be reused 20 times without losing activity, showing its high stability. Interestingly, the novel heterostructured Ag@AgBr/AgCl nanophotocatalyst also shows efficient visible light conversion of CO2 to energetic fuels, e.g. methanol/ethanol. Therefore, the present route opens an avenue to achieve highly efficient visible-light-driven nanophotocatalysts for applications in environmental remediation and resourceful use of CO2." ;
        bibo:volume 22 ;
        dcterms:title "Synthesis of Ag@AgBr/AgCl heterostructured nanocashews with enhanced photocatalytic performance via anion exchange" ;
        dcterms:date 2012 ;
        bibo:pageStart 13153 ;
        dcterms:isPartOf  <https://portal.issn.org/resource/ISSN/1571-1013> ;
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

A continuación creamos las instancias de la clase [phcat:MaterialTransformationProcess](#MaterialTransformationProcess) y añadimos primero sus [rdfs:label](https://www.w3.org/TR/rdf-schema/#ch_label) (nombre del proceso) y [phcat:operationMode](#operationMode). Después, en caso de tenerla, añadimos la información sobre el [phcat:Eg](#Eg) (Banda Energética), [phcat:BET](#BET) (Superficie específica) y [phcat:Yield] (rendimiento) y las asociamos con las propiedades del mismo nombre comenzando con *has* ([phcat:hasEg](#hasEg), [phcat:hasBET](#hasBET), [phcat:hasYield](#hasYield)). Lo siguiente es añadir los [phcat:Input](#Input), los cuales explicaremos más adelante, y asociarlos ([phcat:hasInput](#hasInput)). Después creamos los [phcat:Output](#Output) y los asociamos con su químico mediante [phcat:hasChemical](#hasChemical) y su [phcat:OutputQuantity](#OutputQuantity) ([phcat:hasOutputQuantity](#hasOutputQuantity)) el cual se puede asociar con unidades ([qudt:unit]) de distintos tipos: [unit:MicroMOL-PER-M2-HR](https://qudt.org/vocab/unit/MicroMOL-PER-M2-HR), [unit:MicroMOL-PER-GM](https://qudt.org/vocab/unit/MicroMOL-PER-GM) o [unit:MicroMOL-PER-GM-HR](https://qudt.org/vocab/unit/MicroMOL-PER-GM-HR) todos ellos instancias de [qudt:Unit](https://qudt.org/schema/qudt/Unit). Para terminar creamos las instancias de [phcat:Condition](#Condition) como propiedades [phcat:hasCondition](#hasCondition) para el proceso de transformación.

<!-- inputs -->
Para generar los elementos de tipo [phcat:Input](#Input) solo hace falta añadir las propiedades de [phcat:percentage](#percentage), [phcat:crystalStructure](#crystalStructure) (este solo si el elemento es un catalizador), [phcat:hasChemical](#hasChemical) (para relacionarlo con la instacia de [chebi:CHEBI_24431](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:24431) correspondiente) y [phcat:hasRole](#hasRole) que es el rol que tiene en la entrada instancias de [phcat:MaterialTransformationRole](#MaterialTransformationRole) de entre las que encontramos [phcat:Catalyst](#Catalyst), [phcat:CoCatalyst](#CoCatalyst), [phcat:Dye](#Dye), [phcat:Support](#Support), [phcat:Dopant](#Dopant) o [phcat:Reductant](#Reductant).

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

<!-- condiciones -->
Para crear las condiciones Basta con ir instanciando las clases hijas de [phcat:Condition](#Condition). Estas clases tienen como propiedad [phcat:conditiontype](#conditionType) (explicación del tipo de condición, cuando se hereda define el tipo de reactor, la configuración, ...) y pueden contener cantidades, si aparecen especificadas, definidas mediante [qudt:value](https://qudt.org/schema/qudt/value) y [qudt:unit](https://qudt.org/schema/qudt/unit).

    <#process4/reaction-medium> a phcat:ReactionMediumCondition ;
        phcat:reactionMediumType "Liquid" ;
        qudt:unit unit:PH ; 
        qudt:numericValue 0 .
    <#process4/reactor-condition> a phcat:ReactorCondition ;
        phcat:reactorType "Slurry" .
    <#process4/lightsource> a phcat:WavelengthCondition ;
        phcat:lightSourceType "Visual" ;
        qudt:unit unit:NanoM ;
        qudt:value "400-780" .
    <#process4/lamppower> a phcat:IrradianceCondition ;
        phcat:lampType "Xenon(Xe)" ;
        qudt:unit unit:W ;
        qudt:numericValue "300"^^xsd:double .
    <#process4/catalyst-set-up> a phcat:CatalystSetUpCondition ;
        phcat:setUpType "Powder(Suspended)" .
    <#process4/reaction-time> a phcat:ReactionTimeCondition ;
        qudt:unit unit:HR ;
        qudt:numericValue 5.00 .

<!-- Añadir, si es posible, algún SPARQL queries que se puedan usar -->