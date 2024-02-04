import os
import json
import re

def extract_parameters_from_template(template_path):
    with open(template_path, 'r') as f:
        content = f.read()

    # Using regular expression to find placeholders in the template
    placeholders = re.findall(r'\{\{([^}]+)\}\}', content)

    return placeholders

def generate_guide(template_folder):
    guide = {'sections': []}

    for filename in os.listdir(template_folder):
        if filename.endswith(".html"):
            section_name = os.path.splitext(filename)[0]
            template_path = os.path.join(template_folder, filename)
            parameters = extract_parameters_from_template(template_path)

            section_info = {'name': section_name, 'parameters': parameters}
            guide['sections'].append(section_info)

    guide_json = json.dumps(guide, indent=2)

    with open('guide.json', 'w') as guide_file:
        guide_file.write(guide_json)

if __name__ == "__main__":
    generate_guide('section_templates')
