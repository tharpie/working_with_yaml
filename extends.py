import ruamel.yaml
import json


def merge_dicts(base, extend):
    merged = dict()
    merged.update(base)
    for key, value in extend.items():
        merged[key] = value
    return(merged)


def process_extends(data, extends_map):
   processed = dict()
   for k,v in data.items():
       e = dict()
       p = dict()
       if k == 'extends':
           e.update(extends_map[data['extends']])

       if isinstance(v, dict):
          p[k] = process_extends(v, extends_map)
          if 'extends' in p[k]:
              del(p[k]['extends'])
       else:
          p[k] = v

       if 'extends' in p:
           del(p['extends'])

       m = merge_dicts(p, e)
       processed.update(m)

   return(processed)


def search_dict(data, extends_map):
    p = dict()
    for k,v in data.items():
        if isinstance(v, str):
            p[k] = v
        elif isinstance(v, list):
            l = list()
            for item in v:
                if isinstance(item, dict):
                   _v = process_extends(item, extends_map)
                   l.append(_v)
                else:
                   l.append(item)
            p[k] = l
        elif isinstance(v, dict):
            p[k] = process_extends(v, extends_map)

    return(p)


with open('extends.yaml', 'r') as f:
    extends_map = ruamel.yaml.load(f, Loader=ruamel.yaml.Loader)

with open('main.yaml', 'r') as f:
    data = ruamel.yaml.load(f, Loader=ruamel.yaml.Loader)

merged = search_dict(data, extends_map)

print(json.dumps(merged, indent=2))
