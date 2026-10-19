# **Ignition Perspective Component & Schema Index**

Direct index connecting Ignition Perspective component types (type: "ia.\*") to their exact schema definitions, palettes, and reference files in this repository.

## **Containers**

| Component Type | Palette / Schema Path | Description   |
| :---- | :---- | :---- |
| ia.container.flex | perspective-common-3.3.9/ia.components.json | 1D responsive flow container (row or column) |
| ia.container.coord | perspective-common-3.3.9/ia.components.json | Absolute or percentage-based coordinate layout |
| ia.container.breakpt | perspective-common-3.3.9/ia.components.json | Dual-view container switching on screen width |
| ia.container.column | perspective-common-3.3.9/ia.components.json | 12-column responsive grid container |
| ia.container.split | perspective-common-3.3.9/ia.components.json | Resizable split-pane container (vertical/horizontal) |
| ia.container.tab | perspective-common-3.3.9/ia.components.json | Multi-tab container interface |

## **Displays & Visuals**

| Component Type | Palette / Schema Path | Description   |
| :---- | :---- | :---- |
| ia.display.label | perspective-common-3.3.9/ia.components.json | Text and numerical display |
| ia.display.table | perspective-common-3.3.9/ia.components.json | Data grid with column renderers and sorting |
| ia.display.icon | perspective-common-3.3.9/ia.components.json | Material and SVG icon display |
| ia.display.image | perspective-common-3.3.9/ia.components.json | Raster image loader |
| ia.display.progress | perspective-common-3.3.9/ia.components.json | Linear progress bar indicator |
| ia.display.sparkline | perspective-common-3.3.9/ia.components.json | Compact trend line without axes |
| ia.display.cylindrical-tank | perspective-common-3.3.9/ia.components.json | Vessel/tank level visualization |
| ia.display.linear-scale | perspective-common-3.3.9/ia.components.json | Vertical or horizontal level indicator |
| ia.display.moving-analog-indicator | perspective-common-3.3.9/ia.components.json | ISA-101 process bar indicator with alarms |
| ia.display.thermometer | perspective-common-3.3.9/ia.components.json | Temperature indicator with setpoint ranges |
| ia.display.view | perspective-common-3.3.9/ia.components.json | Embedded sub-view container |
| ia.display.flex-repeater | perspective-common-3.3.9/ia.components.json | Dynamic instance repeater for embedded views |
| ia.display.viewcanvas | perspective-common-3.3.9/ia.components.json | Dynamic multi-view absolute positioning canvas |
| ia.display.alarmjournaltable | perspective-common-3.3.9/ia.components.json | Historic alarm log grid |
| ia.display.alarmstatustable | perspective-common-3.3.9/ia.components.json | Active and unacknowledged alarm table |
| ia.display.markdown | perspective-common-3.3.9/ia.components.json | Markdown and rich text renderer |
| ia.display.pdf-viewer | perspective-common-3.3.9/pdf-viewer.components.json | PDF document viewer |
| ia.display.map | perspective-common-3.3.9/perspective-map.components.json | OpenStreetMap / Leaflet tile mapping |
| ia.display.google-map | perspective-common-3.3.9/perspective-googlemap.components.json | Google Maps API mapping |
| ia.display.barcode | perspective-common-3.3.9/barcode.component.json | Barcode and 2D matrix renderer |

## **Inputs**

| Component Type | Palette / Schema Path | Description   |
| :---- | :---- | :---- |
| ia.input.button | perspective-common-3.3.9/ia.components.json | Standard action button |
| ia.input.text-field | perspective-common-3.3.9/ia.components.json | Single-line alphanumeric input |
| ia.input.numeric-entry-field | perspective-common-3.3.9/ia.components.json | Number input with min/max clamps |
| ia.input.dropdown | perspective-common-3.3.9/ia.components.json | Selection menu with search and multi-select |
| ia.input.checkbox | perspective-common-3.3.9/ia.components.json | Boolean toggle box |
| ia.input.toggle-switch | perspective-common-3.3.9/ia.components.json | Sliding binary toggle switch |
| ia.input.slider | perspective-common-3.3.9/ia.components.json | Linear range slider input |
| ia.input.multi-state-button | perspective-common-3.3.9/ia.components.json | Segmented state selector (Hand/Off/Auto) |
| ia.input.oneshotbutton | perspective-common-3.3.9/ia.components.json | Self-resetting pulse write button |
| ia.input.date-time-picker | perspective-common-3.3.9/ia.components.json | Calendar and clock picker modal |
| ia.input.form | perspective-common-3.3.9/ia.components.json | Schema-driven responsive input form |
| ia.input.signature-pad | perspective-common-3.3.9/ia.components.json | Freehand digital signature canvas |

## **Charts**

| Component Type | Palette / Schema Path | Description   |
| :---- | :---- | :---- |
| ia.chart.timeseries | perspective-common-3.3.9/perspective-timeseries.components.json | Standard historical time series trend chart |
| ia.chart.xy | perspective-common-3.3.9/perspective-amcharts.components.json | Multi-axis bar, line, and scatter chart |
| ia.chart.pie | perspective-common-3.3.9/perspective-amcharts.components.json | Donut and pie distribution chart |
| ia.chart.gauge | perspective-common-3.3.9/perspective-amcharts.components.json | Multi-range radial gauge |
| ia.chart.simple-gauge | perspective-common-3.3.9/ia.components.json | Lightweight SVG radial gauge |
| ia.chart.chartrangeselector | perspective-common-3.3.9/ia.components.json | Timeline zoom/scrub controller |
| ia.chart.powerchart | perspective-common-3.3.9/ia.components.json | Runtime user-configurable pen historian chart |

## **Symbols & Shapes**

| Component Type | Palette / Schema Path | Description   |
| :---- | :---- | :---- |
| ia.symbol.motor | perspective-common-3.3.9/ia.components.json | Dynamic process motor symbol |
| ia.symbol.pump | perspective-common-3.3.9/ia.components.json | Dynamic process pump symbol |
| ia.symbol.valve | perspective-common-3.3.9/ia.components.json | Discrete/analog valve symbol |
| ia.symbol.sensor | perspective-common-3.3.9/ia.components.json | Process instrument bubble symbol |
| ia.symbol.vessel | perspective-common-3.3.9/ia.components.json | Vessel symbol with level dynamics |
| ia.shapes.svg | perspective-common-3.3.9/ia.components.json | Raw SVG path and vector group canvas |

## **Navigation & Menus**

| Component Type | Palette / Schema Path | Description   |
| :---- | :---- | :---- |
| ia.navigation.horizontalmenu | perspective-common-3.3.9/ia.components.json | Top-bar menu navigation |
| ia.navigation.menutree | perspective-common-3.3.9/ia.components.json | Multi-level side navigation tree |
| ia.navigation.link | perspective-common-3.3.9/ia.components.json | Direct URL / View redirect link |

## **Bindings & Transforms (schemas/)**

| Concept | Schema Path   |
| :---- | :---- |
| Tag Binding | perspective-common-3.3.9/schemas/binding-tag.json |
| Tag History Binding | perspective-common-3.3.9/schemas/binding-tag-history.json |
| Property Binding | perspective-common-3.3.9/schemas/binding-property.json |
| Expression Binding | perspective-common-3.3.9/schemas/binding-expr.json |
| Named Query Binding | perspective-common-3.3.9/schemas/binding-query.json |
| Format Transform | perspective-common-3.3.9/schemas/transform-format.json |
| Map Transform | perspective-common-3.3.9/schemas/transform-map.json |
| Expression Transform | perspective-common-3.3.9/schemas/transform-expr.json |
| Style Class Envelope | perspective-common-3.3.9/schemas/style-class-schema.json |

