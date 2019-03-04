<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html"/>
<xsl:template match="/">
 <html><head><title>Gregory's Bakery - Menu</title></head>
  <body>
   <h1>Gregory's Bakery - Menu</h1>
   <table border="1"><tr><th>Item</th><th>Price</th><th>Calorie</th><th>Description</th></tr>
    <xsl:for-each select="breakfast_menu/food">
     <tr>
     <td><strong><xsl:value-of select="name"/></strong> </td>
     <td><xsl:value-of select="price"/></td>
     <td><xsl:value-of select="calorie"/></td>
     <td><xsl:value-of select="description"/></td>
     </tr>
     </xsl:for-each>
   </table>
 </body></html>
</xsl:template>
</xsl:stylesheet>
