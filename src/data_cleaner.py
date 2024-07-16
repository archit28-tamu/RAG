import re
import os

def process_content(text):
    # Heading 1
    text = re.sub(r'\n(.+)\n=+', r'# \1', text)
    # Heading 2
    text = re.sub(r'\*+\d+\\. ([^\*]+)\*+\n-+', r'## \1', text)
    # Codeblock
    text = re.sub(r'(\s)*`\[\]\(#__codelineno-\d+-\d+\)(.+)`', r'\n```\n\2\n\1```', text)
    # CodeLine
    text = re.sub(r'\[\]\(#__codelineno-\d+-\d+\)', '\n', text)
    return text


def clean(documents_dir):
    for document in os.listdir(os.path.join(documents_dir, 'raw')):

        if not os.path.exists(os.path.join(documents_dir, 'processed', document)):

            os.makedirs(os.path.join(documents_dir, 'processed'), exist_ok=True)
            with open(os.path.join(documents_dir, 'raw', document), 'r') as f:
                text = f.read()

            text = process_content(text)

            with open(os.path.join(documents_dir, 'processed', document), 'w') as f:
                f.write(text)

            print(f"Processed Content of {os.path.join(documents_dir, 'raw', document)} and Saved to {os.path.join(documents_dir, 'processed', document)}")

        else:
            print(f"{document} already cleaned to {os.path.join(documents_dir, 'processed', document)}")