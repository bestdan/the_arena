# Enabling GitHub Pages

Quick guide to enable GitHub Pages for The Arena documentation site.

## Steps

1. **Go to Repository Settings**
   - Navigate to https://github.com/bestdan/the_arena
   - Click on **Settings** tab

2. **Navigate to Pages**
   - In the left sidebar, click **Pages** (under "Code and automation")

3. **Configure Source**
   - Under "Build and deployment"
   - Source: Select **GitHub Actions**
   - Click **Save**

4. **Verify Workflow**
   - Go to **Actions** tab
   - You should see "Deploy Public Documentation" workflow
   - It will run automatically on the next push to main

5. **Access Your Site**
   - After the workflow completes (usually 1-2 minutes)
   - Site will be available at: `https://bestdan.github.io/the_arena/`
   - Look for the deployment URL in the Pages settings

## Custom Domain (Optional)

If you want to use a custom domain:

1. In Pages settings, add your custom domain
2. Configure your DNS provider with:
   - CNAME record pointing to `bestdan.github.io`
3. GitHub will automatically provision SSL certificate

## Troubleshooting

### Workflow fails
- Check Actions tab for error logs
- Ensure `requirements.txt` dependencies can install
- Verify Python syntax in `scripts/build_docs.py`

### Site doesn't update
- Check that workflow completed successfully
- Clear browser cache
- Wait a few minutes for CDN propagation

### 404 errors
- Ensure at least one file has `visibility: public` in frontmatter
- Verify `docs/index.md` exists after build
- Check that MkDocs build succeeded

### Links broken
- Ensure linked files are also marked as public
- Check wiki link conversion in build script output
- Verify relative paths are correct

## Maintenance

The site auto-updates on every push to `main` branch:
1. Edit markdown files
2. Add `visibility: public` to frontmatter
3. Commit and push
4. GitHub Actions builds and deploys automatically

No manual deployment needed!
