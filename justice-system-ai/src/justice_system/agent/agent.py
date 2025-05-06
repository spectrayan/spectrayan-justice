import datetime
from typing import List, Dict, Any, Optional
from google.adk.agents import SequentialAgent

from justice_system.agent.subagents import JuryAgent, LawyersAgent


def get_judge_verdict(case_details: dict) -> dict:
    """Evaluate case details and deliver a verdict.

    Args:
        case_details: Dictionary containing case information including:
            - jury_verdict: Jury's decision
            - legal_arguments: Arguments from prosecution and defense
            - defendant_plea: Nature of the plea
            - witness_testimonies: List of witness statements
            - expert_testimonies: List of expert witness reports 
            - evidence: Physical and documentary evidence details

    Returns:
        dict: Verdict details with status and reasoning
    """
    if not case_details:
        return {
            "status": "error",
            "error_message": "No case details provided for evaluation"
        }

    try:
        # Validate required case information
        required_fields = ["jury_verdict", "legal_arguments", "defendant_plea"]
        missing_fields = [field for field in required_fields if field not in case_details]

        if missing_fields:
            return {
                "status": "error",
                "error_message": f"Missing required case information: {', '.join(missing_fields)}"
            }

        return {
            "status": "success",
            "verdict": {
                "decision": "Pending detailed implementation",
                "reasoning": "Case evaluation logic to be implemented",
                "timestamp": datetime.datetime.now(datetime.UTC).isoformat()
            }
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error evaluating case: {str(e)}"
        }

def create_jury_agent(jurors: List[Dict[str, Any]]) -> Optional[SequentialAgent]:
    """Create a jury agent with subagents for each juror.

    Args:
        jurors: List of juror information dictionaries
            Each juror should have at least 'id' and 'name' fields

    Returns:
        Optional[SequentialAgent]: The jury agent with juror subagents
    """
    jury_agent = JuryAgent()
    return jury_agent.create_agent(jurors)


def create_lawyers_agent(prosecutors: List[Dict[str, Any]], defense_attorneys: List[Dict[str, Any]]) -> Optional[SequentialAgent]:
    """Create a lawyers agent with subagents for prosecutors and defense attorneys.

    Args:
        prosecutors: List of prosecutor information dictionaries
            Each prosecutor should have at least 'id' and 'name' fields
        defense_attorneys: List of defense attorney information dictionaries
            Each defense attorney should have at least 'id' and 'name' fields

    Returns:
        Optional[SequentialAgent]: The lawyers agent with prosecutor and defense attorney subagents
    """
    lawyers_agent = LawyersAgent()
    return lawyers_agent.create_agent(prosecutors, defense_attorneys)


# Create the root agent
root_agent = SequentialAgent(
    name="justice_agent",
    description=(
        "Agent to deliver the verdict of a case to the court."
    ),
)


def setup_judicial_system(jurors: List[Dict[str, Any]], prosecutors: List[Dict[str, Any]], defense_attorneys: List[Dict[str, Any]]) -> SequentialAgent:
    """Set up the judicial system with all necessary agents.

    Args:
        jurors: List of juror information dictionaries
        prosecutors: List of prosecutor information dictionaries
        defense_attorneys: List of defense attorney information dictionaries

    Returns:
        SequentialAgent: The root agent with all subagents
    """
    # Create the jury agent
    jury_agent = create_jury_agent(jurors)

    # Create the lawyers agent
    lawyers_agent = create_lawyers_agent(prosecutors, defense_attorneys)

    # Add the subagents to the root agent
    root_agent.add_agent(jury_agent)
    root_agent.add_agent(lawyers_agent)

    return root_agent