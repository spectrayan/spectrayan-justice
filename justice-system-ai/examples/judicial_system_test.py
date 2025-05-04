"""Test script for the judicial system."""

from justice_system.judicial import (
    setup_judicial_system,
    create_jury_agent,
    create_lawyers_agent
)

def main():
    """Test the judicial system."""
    # Create sample jurors
    jurors = [
        {"id": "juror1", "name": "John Doe"},
        {"id": "juror2", "name": "Jane Smith"},
        {"id": "juror3", "name": "Bob Johnson"},
    ]
    
    # Create sample prosecutors
    prosecutors = [
        {"id": "prosecutor1", "name": "Alice Williams"},
        {"id": "prosecutor2", "name": "David Brown"},
    ]
    
    # Create sample defense attorneys
    defense_attorneys = [
        {"id": "defense1", "name": "Michael Davis"},
        {"id": "defense2", "name": "Sarah Miller"},
    ]
    
    # Test creating jury agent
    print("Creating jury agent...")
    jury_agent = create_jury_agent(jurors)
    print(f"Jury agent created: {jury_agent.name}")
    print(f"Number of juror subagents: {len(jury_agent.agents)}")
    
    # Test creating lawyers agent
    print("\nCreating lawyers agent...")
    lawyers_agent = create_lawyers_agent(prosecutors, defense_attorneys)
    print(f"Lawyers agent created: {lawyers_agent.name}")
    print(f"Number of lawyer subagents: {len(lawyers_agent.agents)}")
    
    # Test setting up the judicial system
    print("\nSetting up judicial system...")
    judicial_system = setup_judicial_system(jurors, prosecutors, defense_attorneys)
    print(f"Judicial system set up: {judicial_system.name}")
    print(f"Number of subagents: {len(judicial_system.agents)}")
    
    # Print the structure of the judicial system
    print("\nJudicial system structure:")
    print(f"Root agent: {judicial_system.name}")
    for agent in judicial_system.agents:
        print(f"  Subagent: {agent.name}")
        if hasattr(agent, 'agents'):
            for subagent in agent.agents:
                print(f"    Subagent: {subagent.name}")
    
    print("\nTest completed successfully!")

if __name__ == "__main__":
    main()