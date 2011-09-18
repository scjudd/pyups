pyups
=====

A UPS package tracking library

Example
-------

```python
import sys
from scrapers.UPSScraper import UPSScraper

package = UPSScraper('1Z9999999999999999')

print('[Tracking info for: %s]\n' % package.trackingNo)

for update in package.get_items():
    print('%s %s %s %s' % (update.location.ljust(20), update.date.ljust(10),
                             update.time.ljust(10), update.description))
```
