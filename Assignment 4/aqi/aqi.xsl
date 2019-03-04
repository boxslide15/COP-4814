<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" version="5.0" encoding="UTF-8" indent="yes"/>
<xsl:template match="/">
<html><head><title>Air Quality in Miami</title></head>
    <body>
        <table border="1"><tr><th></th><th>City</th><th>State</th><th>Country</th></tr>
            <xsl:for-each select="all/data">
                <tr>
                    <td><strong><xsl:value-of select="name"/></strong> </td>
                    <td><xsl:value-of select="price"/></td>
                    <td><xsl:value-of select="calorie"/></td>
                    <td><xsl:value-of select="description"/></td>
                </tr>
            </xsl:for-each>
        </table>
        <xsl:if test="all/data/current/weather/ic = ’01d’">
            <img src="weather_icons/01d.png" alt="Clear Sky (Day)"></img>
            <figcaption>Clear Sky (Day)</figcaption>
        </xsl:if>
        #Your code for displaying the weather icon continues here
        ...

    </body>
</html>
</xsl:template>
</xsl:stylesheet>