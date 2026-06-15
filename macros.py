"""mkdocs-macros module for the ISO TC204 site.

Automatically inject a
standard-metadata box (name + Published/Edition/Pages + annotation) at the top
of every extract page. Extract pages are identified by a ``standard`` key in
their YAML front matter.

It also appends a "See also" block at the very end of an extract page when a
``see-also.yaml`` file sits next to the page's ``index.md``.
"""

import os

import yaml


def on_pre_page_macros(env):
    """Inject the metadata box (top) and See-also block (bottom) for extracts."""
    if "standard" in env.page.meta:
        if "render_standard_metadata" not in env.markdown:
            env.markdown = "{{ render_standard_metadata() }}\n\n" + env.markdown
        if "render_see_also" not in env.markdown:
            env.markdown = env.markdown + "\n\n{{ render_see_also() }}"


def define_env(env):
    @env.macro
    def render_standard_metadata(meta=None):
        """Render a metadata box for a standard extract from page front matter."""
        if meta is None:
            meta = env.page.meta
        if not meta:
            return ""

        html = f'<p><strong><em>{meta.get("name", "")}</em></strong></p>\n'
        html += (
            '<div class="standard-metadata" style="'
            "background-color: #f8f9fa; "
            "padding: 0.75em 1.1em; "
            "margin-top: 0.3em; "
            "margin-bottom: 1em; "
            "border-left: 4px solid #3f51b5; "
            'border-radius: 4px;"><small>\n'
        )

        for label, value in (
            ("Published", meta.get("published")),
            ("Edition", meta.get("edition")),
            ("Pages", meta.get("pages")),
        ):
            if value:
                html += f"  <strong>{label}:</strong> {value}<br>\n"

        if meta.get("annotation"):
            html += f'  {meta.get("annotation")}\n'

        html += "</small></div>"
        return html

    @env.macro
    def render_see_also(path=None):
        """Render a "See also" block from a sibling ``see-also.yaml`` file.

        The YAML file is a mapping of ``label -> url``. It is looked up next to
        the current page's source file. Returns an empty string when the file
        is absent or empty, so pages without one render nothing extra.
        """
        if path is None:
            try:
                src = env.page.file.abs_src_path
            except AttributeError:
                return ""
            path = os.path.join(os.path.dirname(src), "see-also.yaml")

        if not os.path.isfile(path):
            return ""

        with open(path, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)

        if not isinstance(data, dict) or not data:
            return ""

        lines = ["## See also", ""]
        for label, url in data.items():
            lines.append(f"- [{label}]({url})")
        return "\n".join(lines)
