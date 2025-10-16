# AI Agent Error Analysis - Open Coding App

A PyScript-based web application for performing open coding analysis on AI agent query-response traces.

## Features

- 📂 **CSV File Loading**: Upload and parse results CSV files
- 📋 **List View**: Display all query-response pairs in an organized list
- 🔍 **Detail View**: Examine individual traces with full query and markdown-rendered response
- 📝 **Open Coding**: Add free-text notes to identify patterns and errors
- 💾 **Export**: Save open coding notes to a CSV file with corresponding IDs

## How to Use

### 1. Open the Application

Simply open `index.html` in a modern web browser (Chrome, Firefox, Safari, or Edge).

```bash
# From the app directory
open index.html

# Or navigate to:
file:///path/to/recipe-chatbot/homeworks/hw2/app/index.html
```

### 2. Load a Results CSV File

1. Click on the file input field
2. Select a results CSV file (e.g., from `../../results/`)
3. The app expects CSV files with columns: `id`, `query`, `response`

### 3. Browse Traces

- View the complete list of query-response pairs
- Click on any row to view its details
- Each row shows the ID and a preview of the query

### 4. Perform Open Coding

In the detail view:

**Left Panel - Open Coding Notes:**
- Enter descriptive labels, patterns, or error observations
- Notes are saved in memory as you work
- No predefined categories - use your own classification system

**Right Panel - Trace Display:**
- Top section shows the original query
- Bottom section shows the response (rendered as markdown)
- Scroll to read full responses

### 5. Save Your Analysis

1. Click the "💾 Save Open Coding" button after adding notes
2. A CSV file named `open_coding.csv` will download automatically
3. The CSV contains two columns: `id` and `open_coding`
4. You can continue coding and save again to update the file

### 6. Navigate

- Use the "← Back to List" button to return to the overview
- Click on different rows to analyze multiple traces
- Previous notes are preserved in the session

## CSV Format

### Input Format (Results CSV)

```csv
id,query,response
1,"What is...","# Recipe Name\n\nIngredients:\n* Item 1"
2,"How do I...","# Another Recipe..."
```

### Output Format (Open Coding CSV)

```csv
id,open_coding
1,"Pattern: Missing ingredient quantities. Error type: Incomplete response."
2,"Pattern: Correct format. No errors detected."
```

## Technical Details

- **Built with**: PyScript (Python in the browser)
- **Markdown Rendering**: markdown2 library for rich text display
- **CSV Processing**: Python csv module via Pyodide
- **No Server Required**: Runs entirely in the browser
- **Privacy**: All data processing happens locally

## Tips for Open Coding

Open coding is a qualitative research method where you:

1. **Read carefully**: Understand both the query intent and the response
2. **Identify patterns**: Look for recurring issues or behaviors
3. **Label descriptively**: Use meaningful labels that capture the essence
4. **Stay open**: Don't force data into predefined categories
5. **Be specific**: Note exact errors, missing elements, or quality issues
6. **Track themes**: As patterns emerge, note them for later analysis

Example notes:
- "Missing dietary restrictions handling"
- "Incorrect serving size calculation"
- "Hallucinated ingredient"
- "Good format, accurate content"
- "Query ambiguity not addressed"

## Browser Compatibility

- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari
- ⚠️ Internet Explorer (not supported)

## Troubleshooting

**App won't load:**
- Ensure JavaScript is enabled
- Check browser console for errors
- Try a different browser

**CSV won't parse:**
- Verify the CSV has `id`, `query`, and `response` columns
- Check for malformed CSV (missing quotes, etc.)

**Markdown not rendering:**
- The app includes markdown2 for rendering
- If unavailable, text will display with basic formatting

## File Structure

```
homeworks/hw2/app/
├── index.html          # Main application file
└── README.md          # This file
```

## Related Files

- Input data: `../../results/results_*.csv`
- Generated queries: `../generated_queries.csv`
- Dimensions: `../dimensions.py`

## License

Part of the recipe-chatbot course materials.

