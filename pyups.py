#!/usr/bin/env python
"""
Print UPS Package Tracking info to the console
"""

import sys
from scrapers.UPSScraper import UPSScraper

package = UPSScraper(sys.argv[1])

print('[Tracking info for: %s]\n' % package.trackingNo)

for update in package.get_items():
    print('%s %s %s %s' % (update.location.ljust(40), update.date.ljust(10),
                             update.time.ljust(10), update.description))