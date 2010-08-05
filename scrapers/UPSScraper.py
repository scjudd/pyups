import lxml.html
import re

class Item(object):
    pass

class UPSScraper(object):
    def __init__(self, trackingNo):
        self.trackingNo = trackingNo
        self.items = []
    
    def get_items(self):
        tree = lxml.html.parse('http://wwwapps.ups.com/WebTracking/processInputRequest?sort_by=status&tracknums_displayed=1&TypeOfInquiryNumber=T&loc=en_US&InquiryNumber1='+self.trackingNo+'&track.x=0&track.y=0')
        
        table = tree.xpath('//table[@class="dataTable"][1]/tr')[1:]
        for row in table:
            item = Item()
            
            item.location = re.sub(',\s+', ', ', row.xpath('td[1]/text()')[0].strip())
            if item.location is '':
                item.location = '--------------------'
            item.date = row.xpath('td[2]/text()')[0]
            item.time = row.xpath('td[3]/text()')[0]
            item.description = row.xpath('td[4]/text()')[0].strip()
            
            self.items.append(item)
        
        return self.items

