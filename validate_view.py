#!/usr/bin/env python3
"""
Ignition Perspective View Offline Validator
Verifies root envelope, JSON Schema compliance, and parent-child position contracts.
Usage: python validate_view.py <path_to_view.json> [--schema <path_to_schema>]
"""

import sys
import os
import json

try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False

def validate_position_contract(parent_type, child_node, path="root"):
    """
    Enforces the Container Position Contract:
    Ensures child position keys match the parent container's layout requirements.
    """
    errors = []
    position = child_node.get("position", {})

    if parent_type == "ia.container.flex":
        coord_keys = {"x", "y", "width", "height"}.intersection(position.keys())
        if coord_keys:
            errors.append(
                f"[POSITION ERROR] At {path}: Parent is 'ia.container.flex', but child has "
                f"coordinate keys {list(coord_keys)}. Must use 'basis', 'grow', 'shrink'."
            )
    elif parent_type == "ia.container.coord":
        flex_keys = {"basis", "grow", "shrink"}.intersection(position.keys())
        if flex_keys:
            errors.append(
                f"[POSITION ERROR] At {path}: Parent is 'ia.container.coord', but child has "
                f"flex keys {list(flex_keys)}. Must use 'x', 'y', 'width', 'height'."
            )
    elif parent_type == "ia.container.column":
        if "column" not in position and "span" not in position:
            errors.append(
                f"[POSITION WARNING] At {path}: Parent is 'ia.container.column'. "
                f"Expected 'column' and 'span' keys in position."
            )
    elif parent_type == "ia.container.breakpt":
        if "size" not in position:
            errors.append(
                f"[POSITION ERROR] At {path}: Parent is 'ia.container.breakpt'. "
                f"Expected 'size' ('small' or 'large') in position."
            )

    return errors

def traverse_and_validate_children(node, current_path="root"):
    """
    Recursively audits every child component in the tree.
    """
    errors = []
    node_type = node.get("type", "")
    children = node.get("children", [])

    for idx, child in enumerate(children):
        child_name = child.get("meta", {}).get("name", f"child_{idx}")
        child_path = f"{current_path} -> {child_name}"

        # 1. Check position contract against parent container type
        errors.extend(validate_position_contract(node_type, child, child_path))

        # 2. Recurse down into children
        errors.extend(traverse_and_validate_children(child, child_path))

    return errors

def validate_perspective_view(view_path, schema_path=None):
    """
    Runs full suite of validations on target view.json.
    """
    if not os.path.isfile(view_path):
        print(f"[ERROR] Target view file not found: {view_path}")
        return 1

    # 1. Parse JSON
    try:
        with open(view_path, "r", encoding="utf-8") as f:
            view_data = json.load(f)
    except json.JSONDecodeError as err:
        print(f"[FATAL] Invalid JSON syntax in '{view_path}': {err}")
        return 1

    all_errors = []

    # 2. Verify Root Envelope
    required_root_keys = ["custom", "params", "props", "root"]
    missing_keys = [k for k in required_root_keys if k not in view_data]
    if missing_keys:
        all_errors.append(f"[ROOT ERROR] Missing required envelope keys: {missing_keys}")

    root_node = view_data.get("root", {})
    if not isinstance(root_node, dict) or "type" not in root_node:
        all_errors.append("[ROOT ERROR] 'root' must be an object containing a 'type' property.")

    # 3. Validate against official view.json schema if provided or found
    if not schema_path:
        default_schema = os.path.join(
            os.path.dirname(__file__),
            "perspective-common-3.3.9",
            "descriptors",
            "view.json"
        )
        if os.path.isfile(default_schema):
            schema_path = default_schema

    if schema_path and os.path.isfile(schema_path):
        if HAS_JSONSCHEMA:
            try:
                with open(schema_path, "r", encoding="utf-8") as sf:
                    schema_data = json.load(sf)
                jsonschema.validate(instance=view_data, schema=schema_data)
                print(f"[PASS] JSON Schema validated against '{os.path.basename(schema_path)}'.")
            except jsonschema.exceptions.SchemaError as err:
                print(f"[WARN] Schema '{os.path.basename(schema_path)}' is not a valid JSON schema (Likely an IDE descriptor). Skipping schema validation.")
            except jsonschema.ValidationError as err:
                path_str = " -> ".join([str(p) for p in err.absolute_path])
                all_errors.append(f"[SCHEMA ERROR] {err.message} (At: {path_str})")
        else:
            print("[INFO] 'jsonschema' package not installed. Skipping descriptor schema validation.")

    # 4. Enforce Hierarchy & Position Contracts
    if "root" in view_data and isinstance(view_data["root"], dict):
        all_errors.extend(traverse_and_validate_children(view_data["root"], "root"))

    # Report results
    if all_errors:
        print(f"\n[FAILED] Found {len(all_errors)} validation issue(s) in '{view_path}':")
        for err in all_errors:
            print(f"  * {err}")
        return 1

    print(f"\n[SUCCESS] '{view_path}' is completely valid and follows all Perspective contracts.")
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_view.py <path_to_view.json> [--schema <path_to_schema.json>]")
        sys.exit(1)

    target_view = sys.argv[1]
    target_schema = None
    if len(sys.argv) >= 4 and sys.argv[2] == "--schema":
        target_schema = sys.argv[3]

    sys.exit(validate_perspective_view(target_view, target_schema))
