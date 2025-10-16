# AI Agent Error Analysis - Open Coding Tool

A PyScript-based web application for performing open coding analysis on AI agent test results. This tool enables systematic error analysis and pattern identification in agent responses.

## Features

### 📊 Data Management
- **CSV Import**: Load test results from CSV files (compatible with files in `../../../results` directory)
- **SQLite Database**: Automatically creates an in-memory database with enhanced schema:
  - `open_coding` (TEXT): Free-text field for descriptive labels and notes
  - `passed` (BOOLEAN): Test result status (passed/failed/unreviewed)

### 📋 List View
- **Overview Dashboard**: Display all test cases with statistics
- **Real-time Stats**: Shows total, passed, failed, and unreviewed counts
- **Status Indicators**: Color-coded badges for quick status identification
  - 🟢 **Passed**: Green
  - 🔴 **Failed**: Red  
  - 🟡 **Unreviewed**: Yellow
- **Click-to-Detail**: Click any row to view detailed information

### 🔍 Detail View
- **Split-Panel Interface**:
  - **Right Panel**: 
    - Query display at the top
    - Response with markdown formatting below
    - Scrollable content area
  - **Left Panel**:
    - **Passed Toggle**: Visual switch to mark test as passed/failed
    - **Open Coding Text Area**: Free-text input for:
      - Pattern identification
      - Error categorization
      - Descriptive labels
      - Observational notes
      - Hypothesis generation

### ⚡ Auto-Save
- **Real-time Updates**: All changes automatically saved to SQLite database
- **No Manual Save**: Changes persist immediately upon interaction
- **Database Sync**: Toggle and text changes instantly update the database

### 📥 Export Functionality
- **Export to CSV**: Download all coded data with a single click
- **Includes All Columns**: Exports ID, query, response, passed status, and open coding notes
- **Timestamped Files**: Automatic filename with timestamp (e.g., `coded_analysis_20251016_143022.csv`)
- **Preserves Work**: Save your analysis for later review or sharing

## Usage

### Getting Started

1. **Open the Application**
   ```bash
   # Simply open index.html in a modern web browser
   open homeworks/hw2/app/index.html
   ```
   Or use a local server:
   ```bash
   python -m http.server 8000
   # Then navigate to http://localhost:8000/homeworks/hw2/app/
   ```

2. **Load Test Results**
   - Click "Choose File" button
   - Select a CSV file (e.g., from `../../../results/results_*.csv`)
   - Click "Load CSV" button
   - The app will parse the CSV and display all rows

### Performing Open Coding

1. **Review the List**
   - Browse all test cases in the dashboard
   - Check statistics to understand overall performance
   - Click on any row to analyze in detail

2. **Analyze Each Case**
   - Read the query and response carefully
   - Toggle "Passed" switch based on your evaluation
   - Write observations in the "Open Coding Notes" field:
     - Identify patterns (e.g., "hallucination", "incorrect format")
     - Note error types (e.g., "missing ingredient", "wrong cooking time")
     - Describe behaviors (e.g., "overly verbose", "missing dietary restrictions")
     - Add any relevant labels or categories

3. **Navigate Between Cases**
   - Click "← Back to List" to return to overview
   - Select another row to continue coding
   - All your changes are automatically saved

4. **Export Your Work**
   - When finished coding, click "📥 Export Coded Data" button
   - File downloads automatically as `coded_analysis_TIMESTAMP.csv`
   - Contains all original data plus your `passed` and `open_coding` columns
   - Safe to share or archive for later analysis

### CSV Format Requirements

Your CSV file should have at least these columns:
- `query`: The input query/question
- `response`: The agent's response

Example:
```csv
id,query,response
1,"Recipe for pasta","Here's a simple pasta recipe..."
2,"Quick breakfast ideas","Try these quick options..."
```

## Open Coding Best Practices

Open coding is a qualitative analysis technique where you:

1. **Avoid Preconceived Categories**: Let patterns emerge from the data naturally
2. **Be Descriptive**: Use clear, specific labels
3. **Note Everything**: Include observations even if their significance isn't immediately clear
4. **Look for Patterns**: As you code more cases, recurring themes will emerge
5. **Iterate**: You can refine your coding as you progress

### Example Open Coding Notes

```
Pattern: Recipe incompleteness
- Missing ingredient quantities
- No cooking temperature specified
- Vague time estimates ("cook until done")

Possible cause: Training data lacks structured recipes
```

## Technical Details

### Technologies Used
- **PyScript 2024.9.2**: Python in the browser
- **SQLite3**: In-memory database for data management
- **markdown2**: Markdown rendering for responses
- **Vanilla JavaScript**: Event handling and DOM manipulation

### Browser Compatibility
- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support  
- Safari: ✅ Full support
- Mobile browsers: ⚠️ Limited (better on tablets)

### Database Schema
```sql
CREATE TABLE analyses (
    id INTEGER PRIMARY KEY,
    query TEXT NOT NULL,
    response TEXT NOT NULL,
    passed BOOLEAN DEFAULT NULL,
    open_coding TEXT DEFAULT ''
)
```

### Performance
- **Load Time**: ~2-3 seconds for initial PyScript load
- **CSV Processing**: ~0.1s per 100 rows
- **Database Updates**: Instant (in-memory)
- **Recommended Size**: Up to 1000 rows for optimal performance

## Keyboard Shortcuts

(Future enhancement - not yet implemented)
- `←` / `→`: Navigate between rows in detail view
- `Ctrl/Cmd + S`: Manually trigger save
- `Esc`: Return to list view

## Troubleshooting

### CSV Won't Load
- Ensure file has `query` and `response` columns
- Check for proper CSV formatting (commas, quotes)
- Try with a smaller file first

### Changes Not Saving
- Check browser console for errors (F12)
- Ensure JavaScript is enabled
- Try refreshing the page and reloading the CSV

### Slow Performance
- Large files (>1000 rows) may be slow
- Consider splitting into smaller batches
- Close other browser tabs to free memory

## Future Enhancements

- [x] Export coded data to CSV ✅ **IMPLEMENTED**
- [ ] Import previously exported CSV to continue coding
- [ ] Search and filter functionality
- [ ] Keyboard navigation
- [ ] Multiple coders support
- [ ] Inter-rater reliability metrics
- [ ] Tag suggestions based on existing codes
- [ ] Persistent storage (local storage/IndexedDB)
- [ ] Batch operations (mark multiple as passed/failed)

## Credits

Built with PyScript for the AI Agent Error Analysis course homework assignment.

