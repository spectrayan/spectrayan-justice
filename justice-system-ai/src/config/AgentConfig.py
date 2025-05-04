from pydantic import BaseModel, Field


class BaseAgent(BaseModel):
    name: str = Field(description="justice_agent")
    model: str = Field(description="gemini-2.0-flash")
    description: str = Field(description="Agent to deliver the verdict of a case to the court.")