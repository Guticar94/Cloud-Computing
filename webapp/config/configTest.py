import yaml

with open('queryConfig.yaml', 'r') as f:
    config = yaml.safe_load(f)

servers = config['servers']
print(servers)