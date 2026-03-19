# Offline Package Builder

Bundle TMs, exercises, syllabi, and PDFs for disconnected/DDIL environments.

## Quick Start

```bash
streamlit run apps/offline_packager/dashboard.py --server.port 8508
```

## Features

- Select content by category or preset bundle
- Auto-resolves prerequisite dependencies
- Includes manifest and offline README in every package
- Estimates package size before building
- Session-based package history in sidebar
