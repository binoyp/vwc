# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import os
import pdb

ROOT_PAGE    = 0
CONTENT_PAGE = 1

STR_PAREND = u"\\\\\n\n"

import re
# regex = re.compile(r"^<!---->", re.IGNORECASE)
# for line in some_file:
#     line = regex.sub("interfaceOpDataFile %s" % fileIn, line)


class LatexGen:

    def __init__(self, htmlPath, pagetype = ROOT_PAGE):
        """
        """
        filedata =""
        self.pagetype = pagetype
        self.latexcontent = u""
        self.header =""
        self.filepath = htmlPath
        self.fname = os.path.basename(htmlPath)


        regex = re.compile(r"<!--'.*'-->", re.IGNORECASE)
        regex_istart = re.compile(r"<i>",  re.IGNORECASE)
        regex_iend = re.compile(r"</i>",  re.IGNORECASE)
        regex_br = re.compile("<br>")
        regex_brend= re.compile("<br/>")
        with open(htmlPath, 'r') as f:
            filedata = f.read()
            filedata = regex.sub("",filedata)
            filedata = regex_istart.sub(r" \\textit{",filedata)
            filedata = regex_iend.sub("}", filedata)
            filedata =regex_br.sub("", filedata)
            filedata= regex_brend.sub("", filedata)

            # print filedata
        self.soup = BeautifulSoup(filedata,"lxml")


    def __str__(self):
        """
        """
        return self.soup.prettify().encode('utf-8')

    def getHeader(self):
        """
        """
        if self.pagetype == ROOT_PAGE:
            self.header = self.soup.h2.string
            return self.header

    def genLatex(self):
        """
        """
        self.latexcontent = ""
        if self.pagetype == ROOT_PAGE:
            self.latexcontent += "\\section{%s}\n"%self.getHeader()

        for tg in self.soup.find_all('p'):
            atts = tg.attrs

            if atts:
                if atts['class'][0] == 'center':
                    try:
                        self.latexcontent += u"\\begin{center}\\textit{%s}\\end{center}\n\n"%tg.string.encode('utf-8')
                    except UnicodeError:
                        print tg
                        print "Unicode Error", Exception.message
                    except AttributeError:
                        if not tg:
                            print "None Type encountered"
                        else:
                            print "Attribute error in <p>:", tg
                        # pdb.set_trace()
                if atts['class'][0] == 'sa':

                    self.latexcontent +="\\begin{center}\n\\begin{sanskrit}\n%s\n\\end{sanskrit}\n\\end{center}\n"%unicode(tg.string)
                if atts['class'][0] == 'right':
                    self.latexcontent += u"\\begin{flushright}\\textit{%s}\\end{flushright}"%tg.string.encode('utf-8') + STR_PAREND
            else:
                try:
                    if tg.string:
                        self.latexcontent += unicode(tg.string) + STR_PAREND
                    else:
                        pdb.set_trace()
                except UnicodeError:
                    print "Error \n\n"


    def writeLatex(self, latexPath= None):
        """

        """
        dirname =  os.path.dirname(self.filepath)
        if not latexPath:
            latexPath = os.path.join(dirname,self.fname[:-4]+".tex")
        self.genLatex()
        with open(latexPath, 'w') as f:
            f.write(self.latexcontent.encode('utf8'))





if __name__ == "__main__":

    pth = r'F:\PyProjects\Vivekananda_WordCloud\swami_texts\volume_1\raja-yoga\concentration_its_spiritual_uses.htm'

    paths = ['v1_c1_response_to_welcome.htm',
 'v1_c1_why_we_disagreee.htm',
 'v1_c1_final_session.htm',
 'v1_c1_buddhism.htm',
 'v1_c1_crying_need.htm',
 'v1_c1_paper_on_hinduism.htm']

    dirpath = r'F:\PyProjects\Vivekananda_WordCloud\swami_texts\volume_1\addresses_at_the_parliament'

    for pth in paths:
        print pth
        l1 = LatexGen(os.path.join(dirpath, pth))

        l1.genLatex()
        l1.writeLatex()