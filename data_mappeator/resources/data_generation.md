# README

## Generating the RO-Crates

To generate the RO-Crate for each yo must have both mapping files, one for the PDF ***map_file_pdf.csv***, and the other for the RDF ***map_file_rdf.csv***. It is also recommended to download the PDF from Artleafs and generate the RDF from data also. If you don't do that, the RO-Crate will have the pointer to the file but no file will be added to the object. 

## Downloading the PDF files

In order to download all the PDF files to do the mapping, please execute the python file found in: *{your_proyect_dir}/data_mappeator/pdf_extraction*

It generates a ***articles_pdf*** folder in *{your_proyect_dir}/data_mappeator/resources* and all the PDF files from the articles found in *{your_proyect_dir}/data_mappeator/data/paper_refences.csv* will be placed here.

Finally, it will generate a new ***map_file_pdf.csv*** file in *{your_proyect_dir}/data_mappeator/resources*.

## Generating articles RDF from data

In order to generate all the RDF files to do the mapping, please execute the python file found in: *{your_proyect_dir}/data_mappeator/rdf_extraction*

It generates a ***articles_rdf*** folder in *{your_proyect_dir}/data_mappeator/resources* and all the RDF files from the data found in *{your_proyect_dir}/data_mappeator/data* will be placed here.

Finally, it will generate a new ***map_file_rdf.csv*** file in *{your_proyect_dir}/data_mappeator/resources*.
