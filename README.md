# Mass noredirect admin

A Python script to scan URLs for potential admin dashboards using concurrent requests.

## Features
- Scans multiple URLs for admin dashboard access
- Checks for common dashboard keywords
- Uses concurrent requests for faster scanning
- Color-coded output for easy result interpretation
- Handles redirects and connection errors

## Requirements
- Python 3.x
- Required packages:
  - `requests`
  - `colorama`

## Installation
1. Clone the repository:
```bash
git clone https://github.com/InMyMine7/mass-noredirect-admin.git
```
2. Install dependencies:
```bash
pip install requests colorama
```

## Usage
1. Prepare two text files:
   - `list.txt`: Contains URLs to scan (one per line)
   - `path.txt`: Contains paths to check for admin dashboards (one per line)
2. Run the script:
```bash
python main.py
```
3. Enter the name of the URL file when prompted (e.g., `list.txt`)

## Example
**list.txt**:
```
https://example.com
https://test.com
```

**path.txt**:
```
admin
dashboard
control-panel
```

**Output**:
```
[VULNERABLE] https://example.com/admin - Status: 200 - Likely dashboard (Time: 0.45s)
[CHECK MANUAL] https://example.com/dashboard - Status: 200 - No dashboard keywords (Time: 0.38s)
[REDIRECT] https://test.com/admin - Status: 301 - Redirects to https://test.com/login (Time: 0.22s)
```

## Notes
- The script uses a thread pool with 10 workers for concurrent scanning
- Timeout for each request is set to 5 seconds
- Dashboard detection is based on keywords: 'dashboard', 'admin', 'control panel', 'overview', 'home', 'Gallery'
- Results are color-coded:
  - Green: Vulnerable (likely dashboard)
  - Yellow: Manual check needed
  - White: Not vulnerable or error

## Author
- GitHub: [InMyMine7](https://github.com/InMyMine7)

## License
This project is licensed under the MIT License.

Note: This tool is for educational and testing purposes only. Always ensure you have permission before testing any website.
