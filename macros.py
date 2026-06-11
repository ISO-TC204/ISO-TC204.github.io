def define_env(env):
    """Define macros and variables for MkDocs."""

    @env.macro
    def render_standard_metadata(meta=None):
        """
        Renders a nice metadata box for EN ISO standards extracts.
        Uses page.meta by default if no meta dict is passed.
        """
        if meta is None:
            meta = env.page.meta  # Access current page's front matter

        if not meta:
            return ""

        html = f'<p><strong><em>{meta.get("name")}</em></strong></p>\n'
        html += '<div class="standard-metadata" style="'
        html += 'background-color: #f8f9fa; '
        html += 'padding: 0.75em 1.1em; '          # Reduced vertical padding
        html += 'margin-top: 0.3em; '
        html += 'margin-bottom: 1em; '
        html += 'border-left: 4px solid #3f51b5; '
        html += 'border-radius: 4px;"><small>\n'

        fields = [
            ("Published", meta.get("published")),
            ("Edition", meta.get("edition")),
            ("Pages", meta.get("pages")),
        ]

        for label, value in fields:
            if value:
                html += f'  <strong>{label}:</strong> {value}<br>\n'

        if meta.get("annotation"):
            html += f'  {meta.get("annotation")}\n'

        html += '</small></div>'
        return html