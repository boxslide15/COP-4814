<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" version="5.0" encoding="UTF-8" indent="yes"/>
<xsl:template match="/">
<html><head><title>Air Quality</title></head>
    <body>
        <table border="5">
            <tr>
                <th>City</th>
                <th>State</th>
                <th>Country</th>
                <th>Latitude</th>
                <th>Longitute</th>
                <th>Timnestamp</th>
                <th>Temperature (Celsius)</th>
                <th>Humidity</th>
                <th>Atmospheric Pressure</th>
                <th>Wind Direction</th>
                <th>Wind Speed</th>
                <th>AQI Value (US Standard)</th>
                <th>Main Pollutant</th>
            </tr>
            <xsl:for-each select="all/data">
                <tr>
                    <td><xsl:value-of select="city"/></td>
                    <td><xsl:value-of select="state"/></td>
                    <td><xsl:value-of select="country"/></td>
                    <td><xsl:value-of select="location/coordinates[2]"/></td>
                    <td><xsl:value-of select="location/coordinates[1]"/></td>
                    <td><xsl:value-of select="current/weather/ts"/></td>
                    <td><xsl:value-of select="current/weather/tp"/></td>
                    <td><xsl:value-of select="current/weather/hu"/></td>
                    <td><xsl:value-of select="current/weather/pr"/></td>
                    <td><xsl:value-of select="current/weather/wd"/></td>
                    <td><xsl:value-of select="current/weather/ws"/></td>
                    <td><xsl:value-of select="current/pollution/aqius"/></td>
                    <td><xsl:value-of select="current/pollution/mainus"/></td>
                </tr>
            </xsl:for-each>
        </table>
        <xsl:if test="all/data/current/weather/ic = '01d'">
            <img src="weather_icons/01d.png" alt="Clear Sky (Day)"></img>
            <figcaption>Clear Sky (Day)</figcaption>
            </xsl:if>
            <xsl:if test="all/data/current/weather/ic = '01n'">
            <img src="weather_icons/01n.png" alt="Clear Sky (Night)"></img>
            <figcaption>Clear Sky (Night)</figcaption>
            </xsl:if>
            <xsl:if test="all/data/current/weather/ic = '02d'">
            <img src="weather_icons/02d.png" alt="Cloudy (Day)"></img>
            <figcaption>Cloudy (Day)</figcaption>
            </xsl:if>
            <xsl:if test="all/data/current/weather/ic = '02n'">
            <img src="weather_icons/02n.png" alt="Cloudy (Night)"></img>
            <figcaption>Cloudy (Night)</figcaption>
            </xsl:if>
            <xsl:if test="all/data/current/weather/ic = '03d'">
            <img src="weather_icons/03d.png" alt="Cloudy"></img>
            <figcaption>Cloudy</figcaption>
            </xsl:if>
            <xsl:if test="all/data/current/weather/ic = '04d'">
            <img src="weather_icons/04d.png" alt="Very Cloudy"></img>
            <figcaption>Very Cloudy</figcaption>
            </xsl:if>
            <xsl:if test="all/data/current/weather/ic = '09d'">
            <img src="weather_icons/09d.png" alt="Rainy"></img>
            <figcaption>Rainy</figcaption>
            </xsl:if>
            <xsl:if test="all/data/current/weather/ic = '10d'">
            <img src="weather_icons/10d.png" alt="Rainy (Day)"></img>
            <figcaption>Rainy (Day)</figcaption>
            </xsl:if>
            <xsl:if test="all/data/current/weather/ic = '10n'">
            <img src="weather_icons/10n.png" alt="Rainy (Night)"></img>
            <figcaption>Rainy (Night)</figcaption>
            </xsl:if>
            <xsl:if test="all/data/current/weather/ic = '11d'">
            <img src="weather_icons/11d.png" alt="Thunderstorm"></img>
            <figcaption>Thunderstorm</figcaption>
            </xsl:if>
            <xsl:if test="all/data/current/weather/ic = '13d'">
            <img src="weather_icons/13d.png" alt="Snowy"></img>
            <figcaption>Snowy</figcaption>
            </xsl:if>
            <xsl:if test="all/data/current/weather/ic = '50d'">
            <img src="weather_icons/50d.png" alt="Foggy"></img>
            <figcaption>Foggy</figcaption>
        </xsl:if>
        <img src="city.png" alt="City"></img>
    </body>
</html>
</xsl:template>
</xsl:stylesheet>