---
description: "Scaffold a new technical blog post"
---
# Workflow: New Blog Post

1.  **Check Context**:
    -   Are we in a "Sprint" phase? (If Coasting, ensure this is maintenance/cleanup only).
    -   Does the topic fit "Hardware Bridge" (Problem -> Solution -> Hardware)?

2.  **Scaffold**:
    ```bash
    hugo new content/blog/YYYY-MM-DD-slug.md
    ```

3.  **Frontmatter Setup**:
    -   Ensure `title`, `date`, `tags` are populated.
    -   Set `draft: true` initially.

4.  **Content Structure**:
    -   **Introduction**: State the problem clearly.
    -   **Solution**: The technical fix/tutorial (numbered steps).
    -   **Hardware Bridge**: Link to the specific hardware used using `{{< affiliate-link >}}`.

5.  **Review**:
    -   Run `hugo server -D` to preview.
    -   Verify no raw Amazon links.
