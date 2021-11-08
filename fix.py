import pandas as pd
from io import StringIO
print(pd.__version__)
style = '''
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match = "corpus">
<reviews> 
<xsl:for-each select="review">
<review>
        <rid><xsl:value-of select="@rid"/></rid>
        <text><xsl:value-of select="text"/></text>  
        <xsl:for-each select="aspects">
                <xsl:if test = "@id = 0">
                <food><xsl:value-of select="//aspect[@category='FOOD']/@polarity"/></food>
                <ambience><xsl:value-of select="//aspect[@category='AMBIENCE']/@polarity"/></ambience>
                <service><xsl:value-of select="//aspect[@category='SERVICE']/@polarity"/></service>
                <price><xsl:value-of select="//aspect[@category='PRICE']/@polarity"/></price>
                
                </xsl:if>
        </xsl:for-each>
</review>
    </xsl:for-each>
</reviews>
</xsl:template > 
</xsl:stylesheet>
'''
labelled_data = pd.read_xml("labelled_data_fixed.xml", stylesheet=StringIO(style))
print(labelled_data)