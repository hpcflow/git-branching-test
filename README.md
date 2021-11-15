Test repository for exploring continuous integration/delivery workflow.

Notes:
- Use conventional commits
- Pre-commit hooks to ensure (local) commits are all "conventional"

More:
- Use git-chglog to generate the changelog when "releasing"
- On GitHub actions, when merging develop -> main, we can delete all the pre-release tags (somehow), then generate the changelog (so it is combined across all pre-releases for that version)
