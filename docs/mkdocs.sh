#/bin/bash
pydoc-markdown
cd build/docs
mkdocs gh-deploy -b mkdocs -m "Deploy docs v{version}"
