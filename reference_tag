import ruamel.yaml
import os

class ReferenceTag(ruamel.yaml.nodes.Node):
    def __init__(self, value):
        super(ReferenceTag, self).__init__()
        self.value = value

def represent_reference(dumper, data):
    return dumper.represent_scalar('!reference', str(data.value))

def construct_reference(loader, node):
    value = loader.construct_scalar(node)
    # Assuming the referenced file contains YAML with anchors
    with open(value, 'r') as file:
        referenced_data = ruamel.yaml.load(file, Loader=ruamel.yaml.Loader)
    return ReferenceTag(referenced_data)

ruamel.yaml.add_constructor('!reference', construct_reference)
ruamel.yaml.add_representer(ReferenceTag, represent_reference)

# Example usage
data = ReferenceTag('path/to/your/reference_file.yaml')

yaml_str = ruamel.yaml.dump(data, default_flow_style=False)
print(yaml_str)


import ruamel.yaml

class ReferenceTag(ruamel.yaml.nodes.Node):
    def __init__(self, value):
        super(ReferenceTag, self).__init__()
        self.value = value

def represent_reference(dumper, data):
    return dumper.represent_scalar('!reference', str(data.value))

def construct_reference(loader, node):
    value = loader.construct_scalar(node)
    with open(value, 'r') as file:
        referenced_data = ruamel.yaml.load(file, Loader=ruamel.yaml.Loader)
    return ReferenceTag(referenced_data)

ruamel.yaml.add_constructor('!reference', construct_reference)
ruamel.yaml.add_representer(ReferenceTag, represent_reference)

# Load and process example.yaml
with open('path/to/example.yaml', 'r') as file:
    data = ruamel.yaml.load(file, Loader=ruamel.yaml.Loader)

# Output the processed data
print(ruamel.yaml.dump(data, default_flow_style=False))
