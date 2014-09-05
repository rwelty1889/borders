<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" >
    <xsl:template match="tag[@k]">
      <xsl:choose>
	<xsl:when test='@k="LSAD"'>
	  <xsl:value-of select='@v'/>
	</xsl:when>
      </xsl:choose>
    </xsl:template>
</xsl:stylesheet>
