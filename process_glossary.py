import re

# Define file paths
glossary_file = 'glossary/glossary.md'
vocab_file = 'docs/vocab.md'

# Read the scope content
with open(glossary_file, 'r') as f:
    glossary_content = f.read()
    
# Extract terms and definitions
glossary_entries = []
for line in glossary_content:
    match = re.match(r'\*\[(.+?)\]:\s*(.+)', line)
    if match:
        term = match.group(1)
        definition = match.group(2)
        glossary_entries.append(f'**{term}**: {definition}\n\n')

# Write to the vocab file
with open(vocab_file, 'w') as f:
    f.write('## Glossary \n\n')
    f.writelines(glossary_entries)

print(f'Generated general.md with {len(glossary_entries)} glossary entries.')