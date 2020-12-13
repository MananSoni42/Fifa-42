#/bin/bash
pydoc-markdown
cd build/docs
mkdocs gh-deploy -m "Deploy docs v{version}" --force
