import json
from fastapi.responses import JSONResponse

class PrettyJSONResponse(JSONResponse):
    def render(self, content: any) -> bytes:
        return json.dumps(content, indent=4, ensure_ascii=False).encode("utf-8")