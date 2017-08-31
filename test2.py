import lxml.html
from lxml.etree import tostring

html = '<p class="slideshowtags">	<strong>This is an example of:</strong>	<ul class="cloud-filter">		<li><a href="/gallery/filter/stratus" rel="366" class="filter366">Stratus</a></li> </ul> </p>'

#html = '<p class="slideshowtags"><strong>This is an example of: </br></strong> 	 </p><ul>		 </ul>'


xhtml = lxml.html.fromstring(html)

print("out {}".format( tostring(xhtml) ))

