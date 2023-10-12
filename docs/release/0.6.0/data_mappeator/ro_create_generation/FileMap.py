class FileMap:

    def __init__(self, doi, pdf_file = None, rdf_file = None):
        self.__doi = doi
        self.__pdf = pdf_file
        self.__rdf = rdf_file

    @property
    def doi(self):
        return self.__doi
    
    @property
    def pdf(self):
        return self.__pdf

    @property
    def rdf(self):
        return self.__rdf

    @pdf.setter
    def pdf(self, pdf):
        self.__pdf = pdf

    @rdf.setter
    def rdf(self, rdf):
        self.__rdf = rdf