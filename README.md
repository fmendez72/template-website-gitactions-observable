# Quarto Observable Template with gitactions

A minimal Quarto website template using Observable JavaScript for interactive data tables. No R or Python runtime required.

## Features

- Static website rendered with Quarto
- Interactive data table using Observable
- GitHub Actions workflow for automatic deployment
- Ready for GitHub Pages hosting

## Local Setup

1. Install [Quarto](https://quarto.org/docs/get-started/)
2. Clone this repository
3. Run `quarto render` to build the site
4. Open `docs/index.html` in your browser

## GitHub Pages Deployment

1. Push this repository to GitHub
2. Go to Settings → Pages
3. Set Source to "GitHub Actions"
4. Push to `main` branch to trigger automatic deployment

## Customization

- Edit `.qmd` files to modify content
- Replace `data/table.csv` with your own data
- Update `_quarto.yml` to change site title and navigation
- Replace `images/banner.jpg` with your own banner

## Structure

```
├─ _quarto.yml              # Site configuration
├─ index.qmd                # Landing page
├─ about.qmd                # About page
├─ data.qmd                 # Data table page
├─ data/
│   └─ table.csv            # Sample dataset
├─ images/
│   └─ banner.jpg           # Banner image
└─ .github/
    └─ workflows/
        └─ quarto-publish.yml  # Deployment workflow
```

## License

Use freely for any purpose.
