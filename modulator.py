 ###############
##  MODULATOR  ##
 ###############
  
#Import Modules
################
# from applicator import Applicator
# from extractor import Extractor
# from generator import Generator
# from splitter import Splitter
# from stripper import Stripper



 #######################
## Applicator Functions##
 #######################

##Build Applicator
#applicator = Applicator()

##Pass in text
#text = """ Here is a test string """
#applicator.set_text(text)

##Return text and print
#my_text = applicator.get_text()
#print(my_text)

##Paste text into document
#applicator.apply_text("mydoc.txt")


 
 ######################
# Extractor Functions ##
 ######################

##Set source file
#source = "/home/lux/Downloads/test/test.txt"
#source2 = "/home/lux/Downloads/test/test2.docx"

##Get extensions from splitter
#splitter = Splitter()

#splitter.split_source(source)
#ext = splitter.get_ext()

#splitter.split_source(source2)
#ext2 = splitter.get_ext()

##Build extractor
#extractor = Extractor()

##Pass in extension
#extractor.set_ext(ext)

##Call extract function
#extractor.extract_text(source)

##Print extracted text
#text = extractor.get_text()
#print(text)

##Do it again
#extractor.set_ext(ext2)
#extractor.extract_text(source2)
#text = extractor.get_text()
#print(text)

##Discard collected text
#extractor.discard_text()



 ######################
# Generator Functions ##
 ######################

##Build generator object
#generator = Generator()

##Set source and epochs
#source = "/home/lux/Downloads/test/test.txt"
#epochs=1

##Generate a new weight
#generator.gen_weight(source, epochs)

##Set weight
#weight = "textgenrnn_weights.hdf5"
#generator.set_weight(weight)

##Generate text from weight
#generator.gen_text(num_lines=1, temp=0.5)

##Get the generated text and print
#text = generator.get_text()
#print(text)

 

 #####################
# Splitter Functions ##
 #####################

##Build splitter object
#splitter = Splitter()

##Set source file
#source = "mysource"

##Split source path
#splitter.split_source(source)

##Return source path, filename, name with ext, and extension
#path = splitter.get_path()
#flname = splitter.get_flname()
#name = splitter.get_name()
#ext = splitter.get_ext()
#print(path)
#print(flname)
#print(name)
#print(ext)



 #####################
# Stripper Functions ##
 #####################

##scrape text to string
#extractor = Extractor()
#source = "/home/lux/Downloads/test/test.txt"
#ext = ".txt"
#extractor.set_ext(ext)
#extractor.extract_text(source)
#text = extractor.get_text()

##Construct object
#stripper = Stripper()

##Pass collected text into object
#stripper.set_text(text)
#text1 = stripper.get_text()
#print("This is the text that was passed in: ")
#print(text1)

##strip string from text
#string = "This is a test"
#stripper.strip_string(string)

##strip slice from string
#slc1 = '"'
#slc2 = '"'
#stripper.strip_slice(slc1, slc2)

#slc1 = '!!'
#slc2 = '!!'
#stripper.strip_slice(slc1, slc2)

##strip page following string
#stripper.strip_page("End page here")

##Return collected text
#new_text = stripper.get_text()
#print("This is the text after being stripped: ")
#print(new_text)

