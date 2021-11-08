# Necessary Import
# import numpy as np
import pandas as pd
# import nltk
import io
from googletrans import Translator
from langdetect import detect, LangDetectException

style_string = '''
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
'''

xsl_style = io.StringIO(style_string)

labelled_df = pd.read_xml("labelled_data_fixed.xml", stylesheet=xsl_style)
unlabelled_df = pd.read_xml("unlabelled_data.xml")
testing_df = pd.read_xml("testing_data.xml")

print(labelled_df)
print(unlabelled_df)
print(testing_df)

from langdetect import detect

detect(testing_df['review'][0])

# Translate english reviews to indonesian for consistency
translator = Translator()
translated_rows = []

for index, row in labelled_df.iterrows():
  try:
    if detect(row['text']) == 'en':
      translated = translator.translate(row["text"], src='en', dest='id')
      row['text'] = translated.text
      print(translated.text)
      translated_rows.append(row)
    else:
      translated_rows.append(row)

  except LangDetectException:
    continue

labelled_translated_df = pd.DataFrame(translated_rows)