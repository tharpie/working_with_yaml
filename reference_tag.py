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
