"""Whitelist of Taipei AI event sources.

Each source is a KKTIX subdomain. Flag ``ai_only=True`` means every event from
that community is treated as AI-related and kept as-is. ``ai_only=False`` means
the community is general-purpose (e.g. DevOps, Python) so individual events go
through the AI keyword filter.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Source:
    name: str
    subdomain: str
    ai_only: bool
    tags: tuple[str, ...] = field(default_factory=tuple)

    @property
    def atom_url(self) -> str:
        return f"https://{self.subdomain}.kktix.cc/events.atom"


# Curated whitelist. Start narrow; expand as we discover more.
SOURCES: list[Source] = [
    # --- Communities where every event is AI-related ---
    Source("Generative AI 年會 / 小聚", "blindegg", ai_only=True, tags=("genai", "llm")),
    Source("Chatbot Developers Taiwan", "chatbots", ai_only=True, tags=("chatbot", "llm")),
    # --- General tech communities, AI-filtered ---
    Source("DevOps Taiwan", "devops", ai_only=False, tags=("devops",)),
    Source("HITCON", "hitcon", ai_only=False, tags=("security",)),
    Source("Taipei.py", "taipei-py", ai_only=False, tags=("python",)),
    Source("MOPCON", "mopcon", ai_only=False, tags=("mobile",)),
    Source("PyCon Taiwan", "pycontw", ai_only=False, tags=("python",)),
    Source("JSDC Taiwan", "jsdc", ai_only=False, tags=("javascript",)),
    Source("SITCON", "sitcon", ai_only=False, tags=("students",)),
    Source("COSCUP", "coscup", ai_only=False, tags=("opensource",)),
]
