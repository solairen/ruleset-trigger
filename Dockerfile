FROM python:3.13.5-slim-bookworm

LABEL org.opencontainers.image.source="https://github.com/solairen/ruleset-trigger"
LABEL org.opencontainers.image.description="Change ruleset on GitHub"
LABEL org.opencontainers.image.authors="Michał Oleszek michal@michaloleszek.com"
LABEL org.opencontainers.image.licenses=MIT
LABEL release=production

RUN pip install requests

COPY github_ruleset.py /action/github_ruleset.py

ENTRYPOINT ["python", "/action/github_ruleset.py"]