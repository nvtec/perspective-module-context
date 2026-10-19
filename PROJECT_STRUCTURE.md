# **Ignition Perspective Project Filesystem Specification**

This document details the on-disk directory structure and manifest requirements for Ignition Gateway projects. When generating files intended to be written directly to a project repository or filesystem (data/projects/\<projectName\>/), each resource must follow these naming and manifest contracts to be recognized by the Ignition Gateway scanner.

## ---

**1\. Directory Hierarchy**

Perspective resources are located under the module namespace directory com.inductiveautomation.perspective/ inside each project:  
data/projects/\<projectName\>/  
├── project.json                                        \<-- Root project manifest  
└── com.inductiveautomation.perspective/  
    ├── views/  
    │   └── \<FolderPath\>/  
    │       └── \<ViewName\>/  
    │           ├── view.json                           \<-- The Perspective view serialization  
    │           ├── resource.json                       \<-- Ignition resource manifest (REQUIRED)  
    │           └── thumbnail.png                       \<-- View thumbnail preview (optional)  
    ├── style-classes/  
    │   └── \<FolderPath\>/  
    │       └── \<StyleClassName\>/  
    │           ├── style.json                          \<-- Style class definition  
    │           └── resource.json                       \<-- Ignition resource manifest (REQUIRED)  
    ├── session-props/  
    │   ├── props.json                                  \<-- Session properties definition  
    │   └── resource.json                               \<-- Ignition resource manifest  
    └── page-config/  
        ├── config.json                                 \<-- Page URLs, titles, and docked views  
        └── resource.json                               \<-- Ignition resource manifest

## ---

**2\. The resource.json Manifest Contract**

Every view, style class, or page configuration directory **must** contain a resource.json file. If resource.json is missing, Ignition will ignore the directory entirely.

### **Manifest Schema Fields**

| Field | Type | Description   |
| :---- | :---- | :---- |
| scope | String | Identifies execution context: "A" (All / Gateway & Client), "G" (Gateway), "C" (Client). Perspective views use "A". |
| version | Integer | Resource parsing schema version. Default is 1\. |
| restricted | Boolean | If true, restricts resource visibility based on role permissions. Default is false. |
| overridable | Boolean | Enables inheritance overrides from parent projects. Default is true. |
| files | Array of Strings | Exact manifest list of content files present in this resource directory. |
| attributes | Object | Arbitrary user and runtime metadata (e.g., documentation strings, modification signatures). |

## ---

**3\. Canonical resource.json Templates**

### **For a Perspective View (views/.../resource.json)**

{  
  "scope": "A",  
  "version": 1,  
  "restricted": false,  
  "overridable": true,  
  "files": \[  
    "view.json"  
  \],  
  "attributes": {}  
}

### **For a Style Class (style-classes/.../resource.json)**

{  
  "scope": "A",  
  "version": 1,  
  "restricted": false,  
  "overridable": true,  
  "files": \[  
    "style.json"  
  \],  
  "attributes": {}  
}

## ---

**4\. View Pathing Translation Rules**

> * **Filesystem to Designer Path:** The directory path beneath com.inductiveautomation.perspective/views/ maps directly to the view path referenced in Designer and navigation scripts.  
>   Example: .../views/PlantA/Boilers/Boiler1/view.json is addressed in Perspective scripts as "PlantA/Boilers/Boiler1".  
> * **Case Sensitivity:** Ignition paths are case-sensitive. Maintain consistent PascalCase or camelCase across filesystem directory names and script references.  
> * **Folder Creation:** Intermediate directories between views/ and the leaf view folder act as Designer organization folders. Intermediate folders do not require a resource.json file; only the leaf folder containing view.json requires it.