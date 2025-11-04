
import os
import re
import json
import sys
import shutil
from pathlib import Path
from typing import Set, List, Dict, Tuple
HTML_TEMPLATE = r"""
<!DOCTYPE html>
    <head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="../styles/styles.css">
        <link rel="icon" href="assets/icon.ico" />
        <meta name="google-site-verification" content="gGsyj98Hmr9mZj0-DQzJIAdOP3eJXZJZnM4_NF8Mai8" />
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0"> 
        <title>Mara Daniels - MIT</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
        <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
        <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
            onload="renderMathInElement(document.body, {
                delimiters: [
                    {left: '$$', right: '$$', display: true},
                    {left: '$', right: '$', display: false},
                ],
                macros: {
                    '\\saeq': '\\{#1\\}',
                    '\\linf': '\\lim_{n \\to \\infty}',
                    '\\Alpha': '\\mathcal{A}',
                    '\\norm': '\\left\\lVert#1\\right\\rVert',
                    '\\ct': 'C^\\infty_c ( #1 )',
                    '\\lloc': 'L^1_{\\mathsf{loc}}( #1 )',
                    '\\Scr': '\\mathscr{S}',
                    '\\tmpr': '\\mathscr{S}',
                    '\\limnf': '\\liminf \\limits_{#1}',
                    '\\limsp': '\\limsup \\limits_{#1}',
                    '\\R': '{\\mathbb R}',
                    '\\C': '{\\mathbb C}',
                    '\\N': '{\\mathbb N}',
                    '\\Q': '{\\mathbb Q}',
                    '\\H': '{\\mathbb H}',
                    '\\S': '{\\mathbb S}',
                    '\\Z': '{\\mathbb Z}',
                    '\\E': '{\\mathbb E}',
                    '\\Var': '\\mathsf{Var}',
                    '\\Cov': '\\mathsf{Cov}',
                    '\\KL': '\\mathsf{KL}',
                    '\\Ent': '\\mathsf{Ent}',
                    '\\F': '{\\mathbb F}',
                    '\\Acl': '\\mathcal{A}',
                    '\\Bcl': '\\mathcal{B}',
                    '\\Ccl': '\\mathcal{C}',
                    '\\Dcl': '\\mathcal{D}',
                    '\\Ecl': '\\mathcal{E}',
                    '\\Fcl': '\\mathcal{F}',
                    '\\Gcl': '\\mathcal{G}',
                    '\\Hcl': '\\mathcal{H}',
                    '\\Jcl': '\\mathcal{J}',
                    '\\Kcl': '\\mathcal{K}',
                    '\\Lcl': '\\mathcal{L}',
                    '\\Mcl': '\\mathcal{M}',
                    '\\Ncl': '\\mathcal{N}',
                    '\\Ocl': '\\mathcal{O}',
                    '\\Pcl': '\\mathcal{P}',
                    '\\Qcl': '\\mathcal{Q}',
                    '\\Rcl': '\\mathcal{R}',
                    '\\Scl': '\\mathcal{S}',
                    '\\Tcl': '\\mathcal{T}',
                    '\\Ucl': '\\mathcal{U}',
                    '\\Vcl': '\\mathcal{V}',
                    '\\Wcl': '\\mathcal{W}',
                    '\\Xcl': '\\mathcal{X}',
                    '\\Ycl': '\\mathcal{Y}',
                    '\\Zcl': '\\mathcal{Z}',
                    '\\diag': '\\mathrm{diag}',
                    '\\supp': '\\mathrm{supp}',
                    '\\diam': '\\mathrm{diam}',
                    '\\sgn': '\\mathrm{sgn}',
                    '\\im': '\\mathrm{Im}',
                    '\\lcm': '\\mathrm{lcm}',
                    '\\aut': '\\mathrm{Aut}',
                    '\\inn': '\\mathrm{Inn}',
                    '\\rg': '\\mathrm{rg}',
                    '\\vol': '\\mathrm{vol}',
                    '\\Pr': '\\mathrm{Pr}',
                    '\\Tr': '\\mathrm{Tr}',
                    '\\eps': '\\varepsilon',
                    '\\charfct': '\\mathds{1}',
                    '\\nullfct': '{\\bf 0}',
                    '\\as': '\\text{a.s.}\\xspace',
                    '\\argmax': '\\mathop{\\mathrm{arg\\,max}}',
                    '\\argmin': '\\mathop{\\mathrm{arg\\,min}}',
                    '\\esssup': '\\mathop{\\mathrm{ess\\,sup}}',
                    '\\th': '\\hat{\\theta}',
                    '\\pto': '\\stackrel{p}{\\longrightarrow}',
                    '\\dto': '\\stackrel{d}{\\longrightarrow}',
                    '\\asto': '\\stackrel{a.s.}{\\longrightarrow}',
                    '\\coloneqq': ':='
                }
            });">
            </script>
    </head>
    <body>
        <div class="row">
            <div class="col-lg-12 col-xl-8 offset-xl-2"> 
            {content}
            </div>
        </div>
        <div class="row">
        <p style="text-align: right; width:100%"><i><a href="../miscellany.html">Back...</a></i></p>
        </div>
    </body>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"
  integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
    crossorigin="anonymous"></script>
</html>
"""

def expand_path(path: str) -> str:
    """Expand ~ and environment variables in path."""
    return os.path.expanduser(os.path.expandvars(path))

def extract_internal_links(content: str) -> List[str]:
    """Extract Obsidian-style internal links [[Link Text]] from content."""
    # Pattern for [[Link]] or [[Link|Display Text]] or [[Link#Section]]
    pattern = r'\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]'
    links = re.findall(pattern, content)
    return links

def extract_image_links(content: str) -> List[str]:
    """Extract image links from markdown content."""
    # Pattern for ![alt](image.png) or ![[image.png]]
    patterns = [
        r'!\[([^\]]*)\]\(([^\)]+)\)',  # ![alt](image.png)
        r'!\[\[([^\]]+)\]\]'  # ![[image.png]]
    ]
    images = []
    for pattern in patterns:
        matches = re.findall(pattern, content)
        if pattern == patterns[0]:
            images.extend([match[1] for match in matches])
        else:
            images.extend(matches)
    return images

def find_file_in_obsidian(obsidian_dir: str, filename: str) -> str | None:
    """
    Find a file in the obsidian directory by name.
    Returns the relative path from obsidian_dir if found, None otherwise.
    """
    obsidian_path = Path(expand_path(obsidian_dir))
    
    # Try with .md extension
    candidates = [
        f"{filename}.md",
        filename
    ]
    
    for candidate in candidates:
        for filepath in obsidian_path.rglob(candidate):
            if filepath.is_file():
                return str(filepath.relative_to(obsidian_path))
    
    return None

def extract_title_from_frontmatter(content: str) -> str | None:
    """Extract title from YAML frontmatter if it exists."""
    frontmatter_pattern = r'^---\s*\n(.*?)\n---'
    match = re.match(frontmatter_pattern, content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        title_match = re.search(r'^title:\s*(.+)$', frontmatter, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()
    return None

def collate_files(obsidian_dir: str, top_level: List[str]) -> Tuple[List[str], List[str]]:
    """
    Step 1: Recursively collate all markdown files linked from top_level.
    Returns (manifest, missing) where manifest contains existing files and missing contains broken links.
    """
    obsidian_path = Path(expand_path(obsidian_dir))
    manifest: Set[str] = set()
    missing: Set[str] = set()
    to_process: List[str] = []
    
    # Initialize with top-level files
    for filename in top_level:
        if not filename:
            continue
        filepath = find_file_in_obsidian(obsidian_dir, filename)
        if filepath:
            to_process.append(filepath)
        else:
            missing.add(filename)
    
    # Process files recursively
    while to_process:
        current_file = to_process.pop(0)
        
        if current_file in manifest:
            continue
        
        manifest.add(current_file)
        
        # Skip processing non-text files (images, etc.)
        full_path = obsidian_path / current_file
        if full_path.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp', '.webp']:
            continue
        
        # Read the file
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {current_file}: {e}")
            continue
        
        # Extract internal links
        links = extract_internal_links(content)
        for link in links:
            link = link.strip()
            if not link:
                continue
            
            # Try to find the linked file
            linked_path = find_file_in_obsidian(obsidian_dir, link)
            if linked_path:
                if linked_path not in manifest:
                    to_process.append(linked_path)
            else:
                missing.add(link)
        
        # Extract image links
        images = extract_image_links(content)
        for image in images:
            image = image.strip()
            if not image:
                continue
            
            # Try to find the image file
            image_path = find_file_in_obsidian(obsidian_dir, image)
            if image_path:
                if image_path not in manifest:
                    manifest.add(image_path)
            else:
                missing.add(image)
    
    return sorted(list(manifest)), sorted(list(missing))

def create_header_id(text: str) -> str:
    """
    Create a URL-safe ID from header text.
    Removes HTML tags, converts to lowercase, replaces spaces with hyphens.
    """
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Convert to lowercase and replace spaces/special chars with hyphens
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = text.strip('-')
    return text

def markdown_to_html(content: str, filename: str, manifest: Set[str], obsidian_dir: str, tld_prefix: str = None) -> str:
    """
    Convert markdown content to HTML with proper nested list support.
    """
    # Remove frontmatter
    content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
    
    # Replace horizontal rules before inline processing (so *** doesn't get converted to bold+italic)
    content = re.sub(r'^(\*{3,}|-{3,}|_{3,})$', '<hr />', content, flags=re.MULTILINE)
    
    # Process inline elements (LaTeX, links, images, formatting) on the ENTIRE content first
    # This ensures multiline blocks like $$ ... $$ are protected before line-by-line processing
    content = process_inline_elements(content, manifest, obsidian_dir)
    
    lines = content.split('\n')
    html_lines = []
    in_paragraph = False
    list_stack = []  # Stack: [(type, indent_level), ...]
    prev_indent = -1
    
    def close_all_lists():
        """Close all open lists and list items."""
        nonlocal list_stack, prev_indent
        while list_stack:
            html_lines.append('</li>')
            list_type, _ = list_stack.pop()
            html_lines.append('</ul>' if list_type == 'ul' else '</ol>')
        prev_indent = -1
    
    for line in lines:
        stripped = line.strip()
        
        # Calculate indentation
        indent = len(line) - len(line.lstrip())
        
        # Skip empty lines
        if not stripped:
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False
            close_all_lists()
            continue
        
        # Handle headers
        header_match = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if header_match:
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False
            close_all_lists()
            level = len(header_match.group(1)) + 1
            text = header_match.group(2)
            header_id = create_header_id(text)
            html_lines.append(f'<h{level} id="{header_id}">{text}</h{level}>')
            continue
        
        # Handle horizontal rules (already converted to <hr /> before inline processing)
        if stripped == '<hr />':
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False
            close_all_lists()
            html_lines.append('<hr />')
            continue
        
        # Handle unordered lists
        ul_match = re.match(r'^[-*+]\s+(.+)$', stripped)
        if ul_match:
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False
            
            # Handle indentation changes
            if indent > prev_indent:
                # Going deeper - open new nested list
                html_lines.append('<ul>')
                list_stack.append(('ul', indent))
            elif indent < prev_indent:
                # Going back - close lists until we match indent
                while list_stack and list_stack[-1][1] > indent:
                    html_lines.append('</li>')
                    list_type, _ = list_stack.pop()
                    html_lines.append('</ul>' if list_type == 'ul' else '</ol>')
                
                # Close the previous li at current level
                if list_stack:
                    html_lines.append('</li>')
            else:
                # Same level - close previous li
                if list_stack:
                    html_lines.append('</li>')
            
            # If no list at this level, open one
            if not list_stack or list_stack[-1][1] != indent:
                html_lines.append('<ul>')
                list_stack.append(('ul', indent))
            
            # Handle list type switching at same indent
            if list_stack and list_stack[-1][1] == indent and list_stack[-1][0] == 'ol':
                html_lines.append('</ol>')
                list_stack.pop()
                html_lines.append('<ul>')
                list_stack.append(('ul', indent))
            
            text = ul_match.group(1)
            html_lines.append(f'<li>{text}')
            prev_indent = indent
            continue
        
        # Handle ordered lists
        ol_match = re.match(r'^(\d+)\.\s+(.+)$', stripped)
        if ol_match:
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False
            
            # Handle indentation changes
            if indent > prev_indent:
                # Going deeper - open new nested list
                html_lines.append('<ol>')
                list_stack.append(('ol', indent))
            elif indent < prev_indent:
                # Going back - close lists until we match indent
                while list_stack and list_stack[-1][1] > indent:
                    html_lines.append('</li>')
                    list_type, _ = list_stack.pop()
                    html_lines.append('</ul>' if list_type == 'ul' else '</ol>')
                
                # Close the previous li at current level
                if list_stack:
                    html_lines.append('</li>')
            else:
                # Same level - close previous li
                if list_stack:
                    html_lines.append('</li>')
            
            # If no list at this level, open one
            if not list_stack or list_stack[-1][1] != indent:
                html_lines.append('<ol>')
                list_stack.append(('ol', indent))
            
            # Handle list type switching at same indent
            if list_stack and list_stack[-1][1] == indent and list_stack[-1][0] == 'ul':
                html_lines.append('</ul>')
                list_stack.pop()
                html_lines.append('<ol>')
                list_stack.append(('ol', indent))
            
            text = ol_match.group(2)
            html_lines.append(f'<li>{text}')
            prev_indent = indent
            continue
        
        # Regular paragraph line
        close_all_lists()
        if not in_paragraph:
            html_lines.append('<p>')
            in_paragraph = True
        
        html_lines.append(stripped)
    
    if in_paragraph:
        html_lines.append('</p>')
    close_all_lists()
    
    return '\n'.join(html_lines)

def process_inline_elements(text: str, manifest: Set[str], obsidian_dir: str) -> str:
    """
    Process inline elements: internal links, images, and preserve LaTeX.
    """
    # First, protect LaTeX by temporarily replacing it with placeholders
    latex_blocks = []
    latex_counter = [0]
    
    def store_latex(match):
        latex_blocks.append(match.group(0))
        placeholder = f"LATEXBLOCK{latex_counter[0]}ENDLATEX"
        latex_counter[0] += 1
        return placeholder
    
    # Protect display math $$...$$ (must come before inline math)
    # Handle both inline and block-style display math
    text = re.sub(r'\$\$\s*(.+?)\s*\$\$', store_latex, text, flags=re.DOTALL)
    
    # Protect inline math $...$
    text = re.sub(r'\$(.+?)\$', store_latex, text)
    
    # Protect LaTeX \(...\) inline math
    text = re.sub(r'\\\((.+?)\\\)', store_latex, text)
    
    # Protect LaTeX \[...\] display math
    text = re.sub(r'\\\[(.+?)\\\]', store_latex, text, flags=re.DOTALL)
    
    # Process image links first
    # ![[image.png]] or ![[image.png|width]] format
    def replace_obsidian_image(match):
        full_content = match.group(1)
        
        # Check if there's a width specification
        if '|' in full_content:
            image_name, width = full_content.split('|', 1)
            image_name = image_name.strip()
            width = width.strip()
            
            # Check if width is numeric (pixel value)
            if width.isdigit():
                width_style = f"width: {width}px; height: auto;"
            else:
                # Default to 100% if width format is not recognized
                width_style = "width: 100%; height: auto;"
        else:
            image_name = full_content.strip()
            width_style = "width: 100%; height: auto;"
        
        image_path = find_file_in_obsidian(obsidian_dir, image_name)
        if image_path and image_path in manifest:
            # Convert to web path
            web_path = f"assets/{Path(image_path).name}"
            return f'<img src="{web_path}" alt="{image_name}" style="{width_style}">'
        return match.group(0)
    
    text = re.sub(r'!\[\[([^\]]+)\]\]', replace_obsidian_image, text)
    
    # ![alt](image.png) format
    def replace_markdown_image(match):
        alt_text = match.group(1)
        image_name = match.group(2)
        image_path = find_file_in_obsidian(obsidian_dir, image_name)
        if image_path and image_path in manifest:
            web_path = f"assets/{Path(image_path).name}"
            return f'<img src="{web_path}" alt="{alt_text}" style="width: 100%; height: auto;">'
        return match.group(0)
    
    text = re.sub(r'!\[([^\]]*)\]\(([^\)]+)\)', replace_markdown_image, text)
    
    # Process internal links [[Link]] or [[Link|Display]] or [[Link#Section]] or [[Link#Section|Display]]
    # Also handle [[image.png|width]] for images without ! prefix
    def replace_internal_link(match):
        full_link = match.group(1)
        
        # Parse link components: [[Page#Section|Display Text]]
        # First, check for custom display text (after |)
        if '|' in full_link:
            link_part, display_text = full_link.split('|', 1)
        else:
            link_part = full_link
            display_text = None
        
        link_part = link_part.strip()
        display_text = display_text.strip() if display_text else None
        
        # Check if this is an image reference (check file extension)
        if link_part.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp', '.webp')):
            # This is an image, not a page link
            image_path = find_file_in_obsidian(obsidian_dir, link_part)
            if image_path and image_path in manifest:
                web_path = f"assets/{Path(image_path).name}"
                
                # Check if display_text is a width specification
                if display_text and display_text.isdigit():
                    width_style = f"width: {display_text}px; height: auto;"
                else:
                    width_style = "width: 100%; height: auto;"
                
                return f'<img src="{web_path}" alt="{link_part}" style="{width_style}">'
            return match.group(0)
        
        # Now parse the link part for page and section (before |)
        if '#' in link_part:
            page_name, section = link_part.split('#', 1)
        else:
            page_name = link_part
            section = None
        
        page_name = page_name.strip()
        section = section.strip() if section else None
        
        # If no custom display text, use the full link part as display
        if display_text is None:
            if section:
                display_text = f"{page_name}#{section}" if page_name else section
            else:
                display_text = page_name
        
        # Check if link exists in manifest
        linked_path = find_file_in_obsidian(obsidian_dir, page_name) if page_name else None
        
        if linked_path and linked_path in manifest:
            # Convert to HTML filename
            html_name = Path(linked_path).stem + '.html'
            
            # Add section anchor if present
            if section:
                section_id = create_header_id(section)
                html_name += f'#{section_id}'
            
            # Internal links are relative (same directory), no prefix needed
            return f'<a href="{html_name}">{display_text}</a>'
        elif not page_name and section:
            # Link to section in current page (e.g., [[#Section]])
            section_id = create_header_id(section)
            return f'<a href="#{section_id}">{display_text}</a>'
        else:
            # Broken link
            return f'<a class="broken" href="#">{display_text}</a>'
    
    text = re.sub(r'\[\[([^\]]+)\]\]', replace_internal_link, text)
    
    # Process markdown hyperlinks [text](url) - but not images which start with !
    # This needs to come after image processing but before other formatting
    def replace_markdown_link(match):
        link_text = match.group(1)
        url = match.group(2)
        return f'<a href="{url}">{link_text}</a>'
    
    text = re.sub(r'(?<!!)\[([^\]]+)\]\(([^\)]+)\)', replace_markdown_link, text)
    
    # Process bold and italic (LaTeX is already protected with placeholders at this point)
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    
    # Process underscore emphasis
    text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)
    text = re.sub(r'_(.+?)_', r'<em>\1</em>', text)
    
    # Process strikethrough
    text = re.sub(r'<del>(.+?)</del>', r'<del>\1</del>', text)
    text = re.sub(r'~~(.+?)~~', r'<del>\1</del>', text)
    
    # Restore LaTeX from placeholders
    for i, latex_block in enumerate(latex_blocks):
        placeholder = f"LATEXBLOCK{i}ENDLATEX"
        # Convert align/align* to aligned in LaTeX blocks
        latex_block = re.sub(r'\\begin\{align\*?\}', r'\\begin{aligned}', latex_block)
        latex_block = re.sub(r'\\end\{align\*?\}', r'\\end{aligned}', latex_block)
        text = text.replace(placeholder, latex_block)
    
    return text

def process_html_includes(html: str, parts_dir: str = "parts") -> str:
    """
    Process {{include}} directives in HTML, replacing them with content from parts/ directory.
    Mimics the behavior of build.py.
    """
    include_identifier = re.compile(r'{{.+?}}')
    
    for include_fmt in include_identifier.findall(html):
        include_name = include_fmt.strip("{{").strip("}}") + ".html"
        include_path = os.path.join(parts_dir, include_name)
        
        try:
            with open(include_path, 'r', encoding='utf-8') as include_fobj:
                include = include_fobj.read()
        except FileNotFoundError:
            print(f"Warning: Include file {include_path} not found, skipping.")
            continue
        
        html = html.replace(include_fmt, "\n" + include + "\n")
    
    return html

def generate_html(manifest_path: str, output_dir: str, tld_prefix: str = None):
    """
    Step 2: Generate HTML files from manifest.
    """
    # Load manifest
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest_data = json.load(f)
    
    manifest = set(manifest_data['manifest'])
    obsidian_dir = manifest_data.get('obsidian_dir', '~/Obsidian/maradan-archive')
    obsidian_path = Path(expand_path(obsidian_dir))
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    
    # Create assets directory for images
    assets_dir = output_path / 'assets'
    assets_dir.mkdir(exist_ok=True)
    
    # Process each file in manifest
    for rel_path in manifest:
        full_path = obsidian_path / rel_path
        
        # Skip if it's an image file
        if full_path.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.svg']:
            # Copy image to assets
            dest_path = assets_dir / full_path.name
            try:
                shutil.copy2(full_path, dest_path)
                print(f"Copied image: {full_path.name}")
            except Exception as e:
                print(f"Error copying image {full_path}: {e}")
            continue
        
        # Process markdown files
        if full_path.suffix != '.md':
            continue
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {rel_path}: {e}")
            continue
        
        # Extract title
        title = extract_title_from_frontmatter(content)
        if not title:
            title = full_path.stem
        
        # Convert to HTML
        html_content = markdown_to_html(content, rel_path, manifest, obsidian_dir, tld_prefix)
        
        # Add title as h1
        full_content = f'<h1>{title}</h1>\n{html_content}'
        
        # Generate full HTML
        html_output = HTML_TEMPLATE.replace("{content}", full_content)
        
        # Process {{include}} directives
        #html_output = process_html_includes(html_output)
         
        # Write output file
        output_file = output_path / (full_path.stem + '.html')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_output)
        
        print(f"Generated: {output_file.name}")

if __name__ == "__main__":
    obsidian_dir = "~/Documents/Obsidian/maradan-archive"
    top_level = [
        'Academic Webpage Resources.md',
    ]
    
    if len(sys.argv) > 1 and sys.argv[1] == '--generate':
        # Step 2: Generate HTML from manifest
        manifest_path = sys.argv[2] if len(sys.argv) > 2 else 'manifest.json'
        output_dir = sys.argv[3] if len(sys.argv) > 3 else 'docs'
        print(f"Generating HTML from {manifest_path} to {output_dir}/")
        generate_html(manifest_path, output_dir)
    else:
        # Step 1: Collate files and create manifest
        print(f"Collating files from {obsidian_dir}")
        print(f"Top-level files: {top_level}")
        manifest, missing = collate_files(obsidian_dir, top_level)
        
        manifest_data = {
            'obsidian_dir': obsidian_dir,
            'manifest': manifest,
            'missing': missing
        }
        
        with open('manifest.json', 'w', encoding='utf-8') as f:
            json.dump(manifest_data, f, indent=2)
        
        print(f"\nManifest created: manifest.json")
        print(f"Files found: {len(manifest)}")
        print(f"Broken links: {len(missing)}")
        if missing:
            print(f"\nMissing files:")
            for m in missing[:10]:  # Show first 10
                print(f"  - {m}")
            if len(missing) > 10:
                print(f"  ... and {len(missing) - 10} more")