"""Jury subagent for the judicial module."""

from typing import List, Dict, Any, Optional
from google.adk.agents import Agent, SequentialAgent

from justice_system.judicial.subagents.jury.prompt import JURY_PROMPT


class JuryAgent:
    """Jury agent that creates dynamic agents based on a list of jurors."""

    def __init__(self, name: str = "jury_agent", description: str = "Agent representing the jury in a court case."):
        """Initialize the jury agent.
        
        Args:
            name: Name of the jury agent
            description: Description of the jury agent
        """
        self.name = name
        self.description = description
        self.jurors = []
        self.agent = None

    def create_agent(self, jurors: List[Dict[str, Any]]) -> SequentialAgent:
        """Create a jury agent with subagents for each juror.
        
        Args:
            jurors: List of juror information dictionaries
                Each juror should have at least 'id' and 'name' fields
                
        Returns:
            SequentialAgent: The jury agent with juror subagents
        """
        if not jurors:
            raise ValueError("No jurors provided to create jury agent")
        
        self.jurors = jurors
        
        # Create the main jury agent
        jury_agent = SequentialAgent(
            name=self.name,
            description=self.description
        )
        
        # Create a subagent for each juror
        for i, juror in enumerate(jurors):
            juror_name = juror.get('name', f"Juror {i+1}")
            juror_id = juror.get('id', f"juror_{i+1}")
            
            # Create a unique name for each juror agent
            agent_name = f"juror_{juror_id}"
            
            # Create the juror agent
            juror_agent = Agent(
                name=agent_name,
                description=f"Agent representing juror {juror_name}",
                llm_config={
                    "prompt": JURY_PROMPT
                }
            )
            
            # Add the juror agent to the jury agent
            jury_agent.add_agent(juror_agent)
        
        self.agent = jury_agent
        return jury_agent

    def get_agent(self) -> Optional[SequentialAgent]:
        """Get the jury agent.
        
        Returns:
            Optional[SequentialAgent]: The jury agent if created, None otherwise
        """
        return self.agent