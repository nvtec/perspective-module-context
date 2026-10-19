# **Agent Instructions: Ignition Perspective SCADA Development**

This repository contains the authoritative JSON schemas, component palettes, binding specifications, and golden project fixtures extracted from the Ignition Perspective module (Perspective-module.modl).  
When generating Perspective views (view.json) or style classes (style.json), act as an expert SCADA frontend engineer. Follow the architecture and serialization rules defined below.

## ---

**1\. Repository Layout & File Mapping**

Inspect files in this repository before generating or altering any resource:

> * **Component Palettes & Defaults**:  
  * Core containers, inputs, displays, and symbols: perspective-common-3.3.9/ia.components.json  
  * Time Series charts: perspective-common-3.3.9/perspective-timeseries.components.json  
  * XY, Pie, and Gauge charts: perspective-common-3.3.9/perspective-amcharts.components.json  
  * Maps: perspective-common-3.3.9/perspective-map.components.json  
> * **Structural Schemas & Bindings**:  
  * Root view contract: perspective-common-3.3.9/descriptors/view.json  
  * Component node contract: perspective-common-3.3.9/descriptors/component.json  
  * Bindings (Tag, Property, Expression, Query): perspective-common-3.3.9/schemas/binding-\*.json  
  * Transforms (Format, Map, Expression): perspective-common-3.3.9/schemas/transform-\*.json  
  * Style classes: perspective-common-3.3.9/schemas/style-class-schema.json  
  * Supported CSS properties: perspective-common-3.3.9/schemas/style-properties.schema.json  
> * **Icons & Events**:  
  * Material/Vector Icon paths: perspective-designer-3.3.9/images/perspective-vector-icons.json  
  * Supported DOM events: perspective-designer-3.3.9/dom\_events.json  
> * **Golden Reference Examples**:  
  * Working view implementations: golden_examples/*/view.json  
> * **Scripting & Gateway Rules**:  
  * Jython 2.7 execution, system.perspective.\* API, and tag I/O: SCRIPTS.md  
> * **Project Filesystem & Manifests**:  
  * On-disk folder hierarchy and resource.json manifests: PROJECT\_STRUCTURE.md  
> * **Automated Validation**:  
  * Schema & position contract verification script: validate\_view.py

## ---

**2\. Core Serialization Constraints**

### **Rule A: Delta Serialization Only (Sparse JSON)**

> * Ignition injects default properties automatically at runtime.  
> * Inspect the default field inside the target component's schema in ia.components.json.  
> * **NEVER output properties that match default values.** Only emit properties explicitly required for layout, data bindings, or user specifications.  
> * Do not emit empty objects or placeholder data arrays unless required by component structure.

### **Rule B: Container Position Contract (Strict Hierarchy)**

The position block of every child component is dictated strictly by the type of its immediate **PARENT** container. Never mix positioning models:

> 1. **Parent is Flex Container (ia.container.flex)**:  
>    "position": {  
>      "basis": "auto",  
>      "grow": 0,  
>      "shrink": 1  
>    }

> 2. **Parent is Coordinate Container (ia.container.coord)**:  
>    "position": {  
>      "x": 0,  
>      "y": 0,  
>      "width": 100,  
>      "height": 50  
>    }

> 3. **Parent is Column Container (ia.container.column)**:  
>    "position": {  
>      "column": 1,  
>      "span": 6  
>    }

> 4. **Parent is Breakpoint Container (ia.container.breakpt)**:  
>    "position": {  
>      "size": "small"  
>    }

### **Rule C: Design Tokens Over Hardcoded Hex Values**

> * Never use hardcoded colors in props.style or style classes (e.g., avoid \#1E88E5).  
> * Reference Ignition CSS theme variables: "var(--call-to-action)", "var(--neutral-20)", "var(--error)". See THEMES.md.

### **Rule D: Gateway Jython Scripting Standard**

> * When writing script transforms, change scripts, or action handlers, adhere strictly to SCRIPTS.md.  
> * Never use Vision APIs (system.gui.\*, system.nav.\*) or browser DOM globals.  
> * For tag operations, use system.tag.readBlocking and system.tag.writeBlocking.

## ---

**3\. Root View Envelope Templates**

When asked to generate a full view.json, select the appropriate envelope:

### **Standard Flex Root (Default for dashboards, forms, responsive screens)**

{  
  "custom": {},  
  "params": {},  
  "props": {},  
  "root": {  
    "type": "ia.container.flex",  
    "meta": { "name": "root" },  
    "props": {  
      "direction": "column",  
      "justify": "flex-start",  
      "alignItems": "stretch"  
    },  
    "children": \[\]  
  }  
}

### **Coordinate Root (P\&ID mimics, fixed spatial layouts)**

{  
  "custom": {},  
  "params": {},  
  "props": {},  
  "root": {  
    "type": "ia.container.coord",  
    "meta": { "name": "root" },  
    "props": {  
      "mode": "percent"  
    },  
    "children": \[\]  
  }  
}

## ---

**4\. Bindings & Transforms Pattern (propConfig)**

Dynamic behavior is configured in the component's propConfig object using schema-compliant paths:  
{  
  "type": "ia.display.label",  
  "meta": { "name": "PressureReadout" },  
  "position": { "basis": "32px", "grow": 0, "shrink": 0 },  
  "props": { "text": "0.0 PSI" },  
  "propConfig": {  
    "props.text": {  
      "binding": {  
        "type": "tag",  
        "config": {  
          "mode": "direct",  
          "tagPath": "{view.params.tagPath}/Pressure",  
          "fallbackDelay": 2.5  
        },  
        "transforms": \[  
          {  
            "type": "format",  
            "format": "0.0 'PSI'"  
          }  
        \]  
      }  
    }  
  }  
}

## ---


## ---

**5\. Events & Actions (events Object)**

Component events and scripts are configured under the `events` object on the component. Use the `dom` or `custom` event keys.
{  
  "type": "ia.input.button",  
  "meta": { "name": "SubmitButton" },  
  "position": { "basis": "32px" },  
  "events": {  
    "dom": {  
      "onClick": {  
        "type": "script",  
        "scope": "G",  
        "config": {  
          "script": "\tsystem.perspective.print(\"Clicked!\")"  
        }  
      }  
    }  
  }  
}

## ---

**6\. View Validation Workflow**


When operating in an environment with terminal or execution access:

> 1. After generating or updating any view.json, run:  
>    python validate\_view.py \<path\_to\_view.json\>  
> 2. If validate\_view.py reports any envelope missing keys or container position mismatches, correct the JSON before finalizing your output.