# whitewater-image-insight

## Initial setup
```
# sync dependencies
uv sync

# source python venv
source .venv/bin/activate
```
## How to run

Dev
```
uv run uvicorn app.main:app --reload
```

Production
```
uv run uvicorn app.main:app
```