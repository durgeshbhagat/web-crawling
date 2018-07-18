import urllib2
import cookielib
import zlib

op_dir = 'saved_html'
class Browser:
    """Initializes the Browser class, handler the cookies,set User-Agent
    Function :- get_html , get_link
    It uses the Package urllib2 and cookielib
    exception :- URLError and HTTPError
    for more details  go to     /usr/lib/python2.6/urllib2.py or    /usr/share/doc/python2.6/html/library/urllib2.html
    """

    def __init__(self, newbrowser=None):
        """
        It initializes the Cookies  and modify user agent
        """
        # Initialize Cookies
        CHandler = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
        self.newbrowser = urllib2.build_opener(CHandler)
        self.newbrowser.addheaders = [
            ('User-agent', 'Mozilla/5.0 (X11; Debian; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0')] # Mozilla/5.0 (X11; Debian; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
        urllib2.install_opener(self.newbrowser)
        self.error_dict={} # to be returned by get_html if any thing goes wrong



    def get_html(self,link):
        """ Get html of the link  """
        print 'opening  ' + link
        try :
            res = self.newbrowser.open(link)
            if res.headers.getheader('Content-Encoding') == 'gzip':
                data=zlib.decompress(res.read(), 16+zlib.MAX_WBITS) #decompress to normal html if server returns content in 'gziped' form 
            else:
                data=res.read()
            return data
            
        except urllib2.HTTPError as e:
            self.error_dict['e_code'] = e.code
            self.error_dict['e_reason']=e.reason
            print('HTTPError in link=%s' %(link))
            print('error code:: ' , e.code)
            print('reason ::' , e.reason) 
            return(self.error_dict)

        except urllib2.URLError as e: 
            
            self.error_dict['e_code'] = 12 # general  URLError code assigned by me
            self.error_dict['e_reason'] = 'URLError' # 
            print('UrlError in link=%s' %(link))
            return(self.error_dict)

        except socket.timeout :
            time.sleep(60*5) # wait for 5 min after socket timeout  Error occured
            self.error_dict['e_code'] = 678 # assigned bY me 
            self.error_dict['e_reason']= 'SocketTimeOut'
            print('SocketTimeout Error in link=%s' %(link))
            return(self.error_dict)

        except KeyboardInterrupt: 
            self.error_dict['e_code'] = 789 # assigned bY me
            self.error_dict['e_reason']='KeyboardInterrupt'
            print('Keyboard Interrupt in link=%s' %(link))
            return(self.error_dict)


    def get_link(self, html, patt=None):
        """ Get link of story for each day from html page of the day, takes html page and special pattern for the story link if any """
        print('scrapping:::: \n')
        soup = bs4.BeautifulSoup(html)        
        pat = r'http://www.thehindu.com/todays-paper/.*/article(\d)+.ece' # link pattern of the story for 2006-2013
        patt = re.compile(pat)
        link_total = soup.findAll('a', href=patt)
        link_n = []
        '''for link in link_total:
            t=link.get('href')
            print 't:::', t
            t=link.getText()
            print 'text::',t
            #link_n= link_n+ [t]
            #return link_n'''
        return link_total


def test(link, fname):
    b = Browser()
    html = b.get_html(link)
    try:
        os.mkdir(op_dir)
    except:
        print '%s dir already exists' %(op_dir))
        pass
    fname = ''
    fname_total = '%s/%s' %( op_dir,. fname)
    fout = open(fname_total, 'w')
    fout.write(html)
    fout.close()
   

def main():
    #test('http://timesofindia.indiatimes.com/archive/year-2001,month-2.cms')
    test('https://trends24.in/india/', trends24)
    
if __name__ =='__main__':
    main()
    
                                                                                                                              
