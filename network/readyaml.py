import yaml
with open("data.yml", "r") as f:
    y_data=yaml.safe_load(f)
print(y_data)
