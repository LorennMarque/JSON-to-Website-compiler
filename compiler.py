import json

def load_section_templates(config):
    html_sections = {}
    for section_config in config['sections']:
        section_name = section_config['name']
        template_path = f'section_templates/{section_name}.html'
        with open(template_path, 'r') as f:
            html_sections[section_name] = f.read()
    return html_sections

def load_html_structure():
    with open('html_structure.html', 'r') as f:
        return f.read()

def generate_html(config_file, section_templates, html_structure):
    with open(config_file, 'r') as f:
        config = json.load(f)

    selected_sections = []
    for section_config in config['sections']:
        section_name = section_config['name']
        section_content = section_templates[section_name]

        for key, value in section_config.items():
            if key in section_content:
                section_content = section_content.replace('{{' + key + '}}', value)

        selected_sections.append(section_content)

    html_content = html_structure.replace('{{content}}', ''.join(selected_sections))
    html_content = html_content.replace('{{page_title}}', config.get('page_title', 'My Website'))

    with open('output.html', 'w') as output_file:
        output_file.write(html_content)

if __name__ == "__main__":
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    section_templates = load_section_templates(config)
    html_structure = load_html_structure()
    generate_html('config.json', section_templates, html_structure)
