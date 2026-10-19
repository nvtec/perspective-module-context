# **Perspective Jython Scripting Guidelines**

All Perspective scripting executes strictly within the **Gateway scope** running Jython 2.7. There is no client-side Python execution in Perspective. When generating or modifying script transforms, event actions, or message handlers, adhere to the architectural constraints and API signatures detailed below.

## ---

**1\. Scope & Execution Rules**

> * **Gateway Execution:** All scripts run on the Ignition Gateway server. Thread locks, long sleeps (time.sleep), or heavy synchronous loops freeze Gateway threads and degrade session performance.  
> * **Forbidden APIs (Vision / Client-Only):**  
  * system.gui.\* (e.g., system.gui.warningBox) — Does not exist in Perspective.  
  * system.nav.\* (e.g., system.nav.openWindow) — Replaced by system.perspective.navigate.  
  * Browser Globals (e.g., window, document, console.log) — Jython has no direct DOM access.  
> * **Thread-Safe Logging:** Always use system.util.getLogger("LoggerName") to log diagnostic information to the Gateway log console.

## ---

**2\. Script Transforms Contract**

Script transforms accept an incoming bound value and must return the transformed value. The function signature implicitly provided by Perspective is:  
`# Arguments provided by runtime:`  
`# value: The current value from the preceding binding or transform.`  
`# quality: The quality code of the bound value (QualityCode object).`  
`# timestamp: Timestamp of the value change.`

`if quality.isGood():`  
    `return round(float(value), 2)`  
`return 0.0`

> * Always test data quality via quality.isGood() before performing operations on tag values.  
> * A script transform **must** return a value. Returning None sets the property to null.

## ---

**3\. Property Change Scripts**

Configured on a component or custom property under scripts \> propertyChange:  
`# Parameters passed by runtime:`  
`# self: Reference to the component owning the property.`  
`# event: An object containing:`  
`#   event.propertyName (str)`  
`#   event.currentValue (QualifiedValue)`  
`#   event.previousValue (QualifiedValue)`  
`#   event.initialChange (bool)`

`if event.initialChange:`  
    `return`

`new_val = event.currentValue.value`  
`if new_val > 100:`  
    `system.perspective.sendMessage("HighAlarmNotice", payload={"alarmVal": new_val}, scope="page")`

## ---

**4\. Perspective API Method Signatures (system.perspective.\*)**

### **Popup Management**

`# Open a popup view`  
`system.perspective.openPopup(`  
    `id="PumpDetailsPopup",`  
    `view="Popups/PumpDetail",`  
    `params={"pumpId": 101},`  
    `title="Pump 101 Details",`  
    `position={"width": 450, "height": 350},`  
    `showCloseIcon=True,`  
    `resizable=True,`  
    `modal=False,`  
    `overlayDismiss=False`  
`)`

`# Close a popup view`  
`system.perspective.closePopup(id="PumpDetailsPopup")`

`# Toggle a popup view`  
`system.perspective.togglePopup(id="PumpDetailsPopup", view="Popups/PumpDetail", params={"pumpId": 101})`

### **Navigation**

`# Navigate to a mounted page route`  
`system.perspective.navigate(page="/overview")`

`# Navigate directly to a View (swapping the primary view)`  
`system.perspective.navigate(view="Views/Dashboard")`

`# Navigate to an external URL`  
`system.perspective.navigate(url="https://inductiveautomation.com", newTab=True)`

### **Message Handlers (system.perspective.sendMessage)**

`# Send a message across components or sessions`  
`# Scopes: "view" (current view only), "page" (current browser page/tab), "session" (all pages in session)`  
`system.perspective.sendMessage(`  
    `messageType="RefreshDataTable",`  
    `payload={"source": "ManualRefreshButton"},`  
    `scope="page"`  
`)`

### **File Downloads & Workstation**

`# Trigger a file download on the client device`  
`system.perspective.download(`  
    `filename="production_report.csv",`  
    `data=csv_data_string,`  
    `contentType="text/csv"`  
`)`

## ---

**5\. Industrial Tag I/O Best Practices**

Always use the non-deprecated batch blocking methods:  
`# Tag Reading`  
`tag_paths = ["[default]Motors/M101/Speed", "[default]Motors/M101/Status"]`  
`values = system.tag.readBlocking(tag_paths)`  
`speed = values[0].value`  
`status = values[1].value`

`# Tag Writing`  
`write_paths = ["[default]Motors/M101/Setpoint"]`  
`write_values = [75.5]`  
`quality_codes = system.tag.writeBlocking(write_paths, write_values)`  
`if not quality_codes[0].isGood():`  
    `system.util.getLogger("TagIO").warn("Failed to write to Setpoint: " + str(quality_codes[0]))`  
