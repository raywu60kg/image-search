from typing import Any, Callable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import RedirectResponse


class RedirectTailingSlashMiddleware(BaseHTTPMiddleware):
    def dispatch(self, request: Request, call_next: Callable[[Any], Any]) -> Any:
        if request.url.path.endswith("/") and request.url.path != "/":
            url = request.url.replace(path=request.url.path.rstrip("/"))
            return RedirectResponse(url=str(url))
        return call_next(request)
