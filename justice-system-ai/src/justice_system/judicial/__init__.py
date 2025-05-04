"""
Judicial submodule for the Justice System AI.

This submodule provides functionality related to judicial processes and decisions.
"""

from justice_system.judicial.agent import (
    get_judge_verdict,
    create_jury_agent,
    create_lawyers_agent,
    setup_judicial_system,
    root_agent
)

__all__ = [
    "get_judge_verdict",
    "create_jury_agent",
    "create_lawyers_agent",
    "setup_judicial_system",
    "root_agent"
]
