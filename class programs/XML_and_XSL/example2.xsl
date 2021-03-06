<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html"/>
  <xsl:template match="/">
    <html>
      <head>
        <title>Wonders of the World</title>
      </head>
      <body>
       <h1>Seven Wonders of the Ancient World</h1>

        <xsl:for-each select="ancient_wonders/wonder">

          <p>The <xsl:value-of select="name"/> is one of the wonders.</p>
        </xsl:for-each>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
