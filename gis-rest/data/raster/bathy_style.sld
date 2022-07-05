<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld" version="1.0.0" xmlns:gml="http://www.opengis.net/gml">
  <UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>Clipped (mask)</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:ChannelSelection>
              <sld:GrayChannel>
                <sld:SourceChannelName>1</sld:SourceChannelName>
              </sld:GrayChannel>
            </sld:ChannelSelection>
            <sld:ColorMap type="ramp">
              <sld:ColorMapEntry label="-21.1972" color="#08306b" quantity="-21.197154999999999"/>
              <sld:ColorMapEntry label="-16.1467" color="#2979b9" quantity="-16.146704324999998"/>
              <sld:ColorMapEntry label="-11.0963" color="#73b2d8" quantity="-11.09625365"/>
              <sld:ColorMapEntry label="-6.0458" color="#c8dcf0" quantity="-6.0458029750000009"/>
              <sld:ColorMapEntry label="-0.9954" color="#f7fbff" quantity="-0.99535230000000041"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>
