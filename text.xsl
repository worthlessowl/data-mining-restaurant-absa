<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match = "corpus">
  <reviews> 
  <xsl:for-each select="review">
    <review>
        <rid><xsl:value-of select="@rid"/></rid>
        <text><xsl:value-of select="text"/></text>  
        <xsl:for-each select="aspects[@id=0]">
          <food><xsl:value-of select="aspect[@category='FOOD']/@polarity"/></food>
          <ambience><xsl:value-of select="aspect[@category='AMBIENCE']/@polarity"/></ambience>
          <service><xsl:value-of select="aspect[@category='SERVICE']/@polarity"/></service>
          <price><xsl:value-of select="aspect[@category='PRICE']/@polarity"/></price>     
        </xsl:for-each>
    </review>
  </xsl:for-each>
</reviews>
</xsl:template > 
</xsl:stylesheet>