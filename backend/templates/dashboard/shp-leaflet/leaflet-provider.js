(function (root, factory) {
  if (typeof define === "function" && define.amd) {
    // AMD. Register as an anonymous module.
    define(["leaflet"], factory);
  } else if (typeof modules === "object" && module.exports) {
    // define a Common JS module that relies on 'leaflet'
    module.exports = factory(require("leaflet"));
  } else {
    // Assume Leaflet is loaded into global object L already
    factory(L);
  }
})(this, function (L) {
  "use strict";

  L.TileLayer.Provider = L.TileLayer.extend({
    initialize: function (arg, options) {
      var providers = L.TileLayer.Provider.providers;

      var parts = arg.split(".");

      var providerName = parts[0];
      var variantName = parts[1];

      if (!providers[providerName]) {
        throw "No such provider (" + providerName + ")";
      }

      var provider = {
        url: providers[providerName].url,
        options: providers[providerName].options
      };

      // overwrite values in provider from variant.
      if (variantName && "variants" in providers[providerName]) {
        if (!(variantName in providers[providerName].variants)) {
          throw "No such variant of " + providerName + " (" + variantName + ")";
        }
        var variant = providers[providerName].variants[variantName];
        var variantOptions;
        if (typeof variant === "string") {
          variantOptions = {
            variant: variant
          };
        } else {
          variantOptions = variant.options;
        }
        provider = {
          url: variant.url || provider.url,
          options: L.Util.extend({}, provider.options, variantOptions)
        };
      }

      // replace attribution placeholders with their values from toplevel provider attribution,
      // recursively
      var attributionReplacer = function (attr) {
        if (attr.indexOf("{attribution.") === -1) {
          return attr;
        }
        return attr.replace(/\{attribution.(\w*)\}/g, function (
          match,
          attributionName
        ) {
          return attributionReplacer(
            providers[attributionName].options.attribution
          );
        });
      };
      provider.options.attribution = attributionReplacer(
        provider.options.attribution
      );

      // Compute final options combining provider options with any user overrides
      var layerOpts = L.Util.extend({}, provider.options, options);
      L.TileLayer.prototype.initialize.call(this, provider.url, layerOpts);
    }
  });

  /**
   * Definition of providers.
   * see http://leafletjs.com/reference.html#tilelayer for options in the options map.
   */

  L.TileLayer.Provider.providers = {
    OpenStreetMap: {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      options: {
        maxZoom: 19,
        attribution:
          '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      },
      variants: {
        Mapnik: {},
        DE: {
          url: "https://{s}.tile.openstreetmap.de/tiles/osmde/{z}/{x}/{y}.png",
          options: {
            maxZoom: 18
          }
        },
        CH: {
          url: "https://tile.osm.ch/switzerland/{z}/{x}/{y}.png",
          options: {
            maxZoom: 18,
            bounds: [
              [45, 5],
              [48, 11]
            ]
          }
        },
        France: {
          url: "https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png",
          options: {
            maxZoom: 20,
            attribution:
              "&copy; OpenStreetMap France | {attribution.OpenStreetMap}"
          }
        },
        HOT: {
          url: "https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png",
          options: {
            attribution:
              "{attribution.OpenStreetMap}, " +
              'Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> ' +
              'hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>'
          }
        },
        BZH: {
          url: "https://tile.openstreetmap.bzh/br/{z}/{x}/{y}.png",
          options: {
            attribution:
              '{attribution.OpenStreetMap}, Tiles courtesy of <a href="http://www.openstreetmap.bzh/" target="_blank">Breton OpenStreetMap Team</a>',
            bounds: [
              [46.2, -5.5],
              [50, 0.7]
            ]
          }
        }
      }
    }
  };

  L.tileLayer.provider = function (provider, options) {
    return new L.TileLayer.Provider(provider, options);
  };

  return L;
});
