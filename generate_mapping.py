import json
import yaml

# Orignial mappings can be found here https://raw.githubusercontent.com/leanprover/vscode-lean4/c7efb256743d3a5e35ffda21f09f6c32900ba69c/vscode-lean4/src/abbreviation/abbreviations.json

# TODO right now we generate many 'matches' entries, but there can only be one
# top level matches entry!

def json_to_espanso(json_file, espanso_file):
    with open(json_file, 'r') as f:
        mappings = json.load(f)
    print(mappings)

    espanso_mappings = {"matches": []}
    for key, value in mappings.items():
        espanso_mappings["matches"].append(
            {
                "triggers": [f"\\{key}\\", f"\\{key} ", f"\\{key}\t"],
                "replace": value
            }
        )

    with open(espanso_file, 'w', encoding='utf-8') as out_file:
        yaml.dump(espanso_mappings, out_file, sort_keys=False, allow_unicode=True)

    with open(espanso_file, 'w', encoding='utf-8') as out_file:
        yaml.dump(espanso_mappings, out_file, sort_keys=False, allow_unicode=True)

# Example usage:
json_to_espanso('abbreviations.json', 'package.yml')
