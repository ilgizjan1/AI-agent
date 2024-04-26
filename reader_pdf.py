
####v1
from pypdf import PdfReader 

def read_file_pdf(path_pdf):

    # creating a pdf reader object 
    reader = PdfReader(path_pdf) 
    
    # printing number of pages in pdf file 
    print(len(reader.pages)) 

    page = reader.pages[0] 

    pages = []
    # getting a specific page from the pdf file 
    for page in reader.pages:

        # extracting text from page 
        text = page.extract_text() 
        pages.append(text)
        #print(text)
    return pages
    



if __name__ == "__main__":
    read_file_pdf('deep-0.pdf')