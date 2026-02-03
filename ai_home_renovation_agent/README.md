# AI Home Renovation Agent

A multi-agent Google ADK project that analyzes room photos, proposes renovation plans, and generates photorealistic renderings. It uses a coordinator/dispatcher to route requests to specialized agents and a sequential planning pipeline for full renovation workflows.

## What This Project Does
- Analyze current room photos and optional inspiration images
- Produce a detailed renovation plan with materials, colors, fixtures, and budget guidance
- Generate photorealistic renderings while preserving the exact room layout
- Support iterative edits to renderings based on user feedback

## Architecture Overview
The system follows a Coordinator/Dispatcher pattern with a sequential pipeline:

1. InfoAgent: Handles general questions
2. RenderingEditor: Applies changes to an existing rendering
3. PlanningPipeline (Sequential):
   - VisualAssessor: Vision-based room and inspiration analysis
   - DesignPlanner: Detailed finish/material plan (layout preserved)
   - ProjectCoordinator: Roadmap, budget, timeline, and rendering generation

## Requirements
- Python 3.10+ (recommended)
- Google ADK
- Gemini API key

Dependencies are listed in `requirements.txt`.

## Setup
1. Create and activate a virtual environment
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your API key:

Option A: Environment variable
```bash
export GOOGLE_API_KEY="your_api_key"
```

Option B: `.env` file (project root)
```env
GOOGLE_API_KEY=your_api_key
```

Note: The code accepts either `GOOGLE_API_KEY` or `GEMINI_API_KEY`.

## Run (ADK Web)
From the parent directory that contains this folder, run:

```bash
adk web
```

Then open the ADK Web UI and select `ai_home_renovation_agent`.

## Usage Examples
Text-only:
```
Renovate my 10x12 kitchen with a modern farmhouse style. Budget: $25k.
```

Room + inspiration:
```
[Upload current room photo]
[Upload inspiration photo]
Transform my kitchen to match this style. What's the cost?
```

Iterative refinement (after initial rendering):
```
Make the cabinets cream instead of white.
Add pendant lights over the island.
```

## Artifacts and Versioning
- Each rendering is saved as a versioned artifact: `asset_name_v1.png`, `asset_name_v2.png`, etc.
- The latest rendering is stored in session state for easy editing.
- Reference images can be stored and reused during generation or edits.

## Project Structure
- `agent.py`: Agent definitions and routing logic
- `tools.py`: Rendering and asset management tools
- `requirements.txt`: Python dependencies
- `.env`: Local environment variables (do not commit real keys)

## Troubleshooting
- Missing API key: Ensure `GOOGLE_API_KEY` or `GEMINI_API_KEY` is set.
- No rendering generated: Provide a more detailed prompt, and ensure reference images are valid.
- Edit fails to find a rendering: Use `list_renovation_renderings` to see available artifacts.

## Security Notes
- Never commit real API keys to source control.
- If a key is exposed, rotate it immediately in the Google Cloud Console.
