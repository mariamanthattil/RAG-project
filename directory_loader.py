#New file is DirectoryLoader.py

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
loader = DirectoryLoader(
path='Books',
glob= '*.pdf',
loader_cls=PyPDFLoader
)
docs = loader.load()
print(len(docs))
#pprint(docs[5].page_content)
