"""HTML report helpers used by the UP rainfall prediction notebook."""

from html import escape


def badge(value):
    return f"<span class='badge'>{escape(str(value))}</span>"


def dataframe_html(df, rows=200):
    return df.head(rows).to_html(index=False, border=0)


def gx_doc_page(kind, title, suite_name, columns, overview_html, column_rules, notes):
    toc = ["<a class='toc-active' href='#overview'>Overview</a>"]
    toc += [f"<a href='#{escape(str(col))}'>{escape(str(col))}</a>" for col in columns]

    sections = []
    for col in columns:
        rules = column_rules.get(col, ["column is documented in this validation suite."])
        rules_html = "".join(f"<li>{rule}</li>" for rule in rules)
        sections.append(
            f"<section id='{escape(str(col))}' class='column-section'>"
            f"<h2>{escape(str(col))}</h2>"
            f"<ul class='rules'>{rules_html}</ul>"
            f"</section>"
        )

    subtitle = (
        "A collection of Expectations defined for batches of data."
        if "Suite" in kind
        else "Validation results for the UP rainfall prediction dataset."
    )

    return f"""<!doctype html>
<html>
<head>
<meta charset='utf-8'>
<title>{escape(str(title))}</title>
<style>
:root {{
  --bg:#161b20; --panel:#252b31; --line:#343c45;
  --text:#f3f4f6; --muted:#b8c0ca;
  --header:#e4e7eb; --accent:#ffc107; --badge:#7c8793;
}}
body {{
  margin:0; background:var(--bg); color:var(--text);
  font-family:Arial, Helvetica, sans-serif;
  font-size:20px; line-height:1.42;
}}
.layout {{
  display:grid; grid-template-columns:360px minmax(0,1fr);
  gap:34px; padding:30px 40px 70px;
}}
.sidebar {{ position:sticky; top:24px; }}
.card {{
  background:var(--panel); border:1px solid var(--line);
  border-radius:5px; margin-bottom:20px;
}}
.badge {{
  display:inline-block; background:var(--badge);
  color:#fff; border-radius:5px;
  padding:1px 7px; font-size:14px; font-weight:700;
}}
.table-wrap {{ overflow-x:auto; }}
</style>
</head>
<body>

<div class='layout'>
<aside class='sidebar'>
  <div class='card'>
    <h3>{escape(kind)}</h3>
    <p>{escape(subtitle)}</p>
  </div>
  <div class='card'>
    <h3>Table of Contents</h3>
    {''.join(toc)}
  </div>
</aside>

<main>
<section id='overview'>
<h1>Overview</h1>
{overview_html}
<p><b>Notes:</b> {escape(str(notes))}</p>
</section>
{''.join(sections)}
</main>

</div>
</body>
</html>"""