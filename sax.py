import urllib
import urllib2
import feed
from xml.sax import handler, make_parser 

url = feed.feed

class  TestHandler(handler.ContentHandler):  
    img_src=[]                     
    def  __init__(self):                                                                
        pass
                 
    def  startDocument(self):            
        pass
                
    def  endDocument(self):                 
        pass
                
    def  startElement(self, name, attrs):
        if name == "link" and "href" in attrs.keys():
            if "type" in attrs.keys() and attrs["type"] == "image/jpeg":
                self.img_src.append(attrs["href"])

            elif "rel" in attrs.keys() and attrs["rel"] == "enclosure":
                self.img_src.append(attrs["href"])
               
    def  endElement(self, name): 
        pass
    def  characters(self, chrs):                                                     
        pass 
                
     
def  Test(query): 
    handler = TestHandler()
    handler.img_src=[]     
    parser = make_parser()     
    parser.setContentHandler(handler)
    parser.parse(urllib2.urlopen(url+query))
    return handler.img_src   
