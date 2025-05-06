"""Lawyer subagents for the judicial module."""

from typing import List, Dict, Any, Optional
from google.adk.agents import Agent, SequentialAgent

from justice_system.agent.subagents.lawyers.prompt import PROSECUTOR_PROMPT, DEFENSE_ATTORNEY_PROMPT


class LawyersAgent:
    """Lawyers agent that creates dynamic agents for prosecutors and defense attorneys."""

    def __init__(self, name: str = "lawyers_agent", description: str = "Agent representing the lawyers in a court case."):
        """Initialize the lawyers agent.
        
        Args:
            name: Name of the lawyers agent
            description: Description of the lawyers agent
        """
        self.name = name
        self.description = description
        self.prosecutors = []
        self.defense_attorneys = []
        self.agent = None

    def create_agent(self, prosecutors: List[Dict[str, Any]], defense_attorneys: List[Dict[str, Any]]) -> SequentialAgent:
        """Create a lawyers agent with subagents for prosecutors and defense attorneys.
        
        Args:
            prosecutors: List of prosecutor information dictionaries
                Each prosecutor should have at least 'id' and 'name' fields
            defense_attorneys: List of defense attorney information dictionaries
                Each defense attorney should have at least 'id' and 'name' fields
                
        Returns:
            SequentialAgent: The lawyers agent with prosecutor and defense attorney subagents
        """
        if not prosecutors and not defense_attorneys:
            raise ValueError("No lawyers provided to create lawyers agent")
        
        self.prosecutors = prosecutors
        self.defense_attorneys = defense_attorneys
        
        # Create the main lawyers agent
        lawyers_agent = SequentialAgent(
            name=self.name,
            description=self.description
        )
        
        # Create a subagent for each prosecutor
        for i, prosecutor in enumerate(prosecutors):
            prosecutor_name = prosecutor.get('name', f"Prosecutor {i+1}")
            prosecutor_id = prosecutor.get('id', f"prosecutor_{i+1}")
            
            # Create a unique name for each prosecutor agent
            agent_name = f"prosecutor_{prosecutor_id}"
            
            # Create the prosecutor agent
            prosecutor_agent = Agent(
                name=agent_name,
                description=f"Agent representing prosecutor {prosecutor_name}",
                llm_config={
                    "prompt": PROSECUTOR_PROMPT
                }
            )
            
            # Add the prosecutor agent to the lawyers agent
            lawyers_agent.add_agent(prosecutor_agent)
        
        # Create a subagent for each defense attorney
        for i, defense_attorney in enumerate(defense_attorneys):
            defense_attorney_name = defense_attorney.get('name', f"Defense Attorney {i+1}")
            defense_attorney_id = defense_attorney.get('id', f"defense_attorney_{i+1}")
            
            # Create a unique name for each defense attorney agent
            agent_name = f"defense_attorney_{defense_attorney_id}"
            
            # Create the defense attorney agent
            defense_attorney_agent = Agent(
                name=agent_name,
                description=f"Agent representing defense attorney {defense_attorney_name}",
                llm_config={
                    "prompt": DEFENSE_ATTORNEY_PROMPT
                }
            )
            
            # Add the defense attorney agent to the lawyers agent
            lawyers_agent.add_agent(defense_attorney_agent)
        
        self.agent = lawyers_agent
        return lawyers_agent

    def get_agent(self) -> Optional[SequentialAgent]:
        """Get the lawyers agent.
        
        Returns:
            Optional[SequentialAgent]: The lawyers agent if created, None otherwise
        """
        return self.agent