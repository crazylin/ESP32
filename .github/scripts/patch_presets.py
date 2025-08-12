import json
import os


def _strip_invalid_inherits(preset: dict, invalid_presets: set[str]) -> bool:
    changed = False
    inherits = preset.get("inherits")
    if isinstance(inherits, str):
        if inherits in invalid_presets:
            del preset["inherits"]
            changed = True
    elif isinstance(inherits, list):
        new_inherits = [x for x in inherits if x not in invalid_presets]
        if len(new_inherits) != len(inherits):
            changed = True
            if new_inherits:
                preset["inherits"] = new_inherits
            else:
                del preset["inherits"]
    return changed


def _process_file(file_path: str, invalid_presets: set[str]) -> bool:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return False

    changed = False

    if isinstance(data, dict) and isinstance(data.get("configurePresets"), list):
        original_count = len(data["configurePresets"])
        data["configurePresets"] = [
            p for p in data["configurePresets"] if p.get("name") not in invalid_presets
        ]
        if len(data["configurePresets"]) != original_count:
            changed = True
        for preset in data["configurePresets"]:
            if _strip_invalid_inherits(preset, invalid_presets):
                changed = True

    for key in ("buildPresets", "testPresets"):
        if isinstance(data, dict) and isinstance(data.get(key), list):
            for preset in data[key]:
                if _strip_invalid_inherits(preset, invalid_presets):
                    changed = True

    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            f.write("\n")
    return changed


def main() -> None:
    root = "nf-interpreter"
    # Allow override via environment variable, e.g.: INVALID_PRESETS="AtomS3,BrainPad2"
    env_invalid = os.environ.get("INVALID_PRESETS", "").strip()
    if env_invalid:
        invalid_presets = {p.strip() for p in env_invalid.split(",") if p.strip()}
    else:
        invalid_presets = {"AtomS3", "BrainPad2"}

    removed_any = False
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".json") and "Presets" in filename:
                full_path = os.path.join(dirpath, filename)
                if _process_file(full_path, invalid_presets):
                    removed_any = True
                    print(f"Updated {full_path}")

    if not removed_any:
        print("No AtomS3 presets changed")
    else:
        print("Patched preset files to remove/strip AtomS3")


if __name__ == "__main__":
    main()


