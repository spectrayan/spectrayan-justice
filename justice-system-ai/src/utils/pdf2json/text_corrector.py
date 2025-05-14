"""
Text Corrector module.

This module provides a class for correcting spelling and grammar in text and anonymizing names
of individuals and entities using LlamaIndex and Ollama. The anonymization process replaces
names with appropriate role-based terms like defendant, witness, lawyer, organization, etc.
"""

import logging
import re
from typing import Optional, Dict, Any

from llama_index.llms.ollama import Ollama

logger = logging.getLogger(__name__)


class TextCorrector:
    """Class for correcting spelling and grammar in text and anonymizing names using LlamaIndex and Ollama.

    This class provides functionality to correct spelling and grammar errors in text
    and replace names of individuals or entities with appropriate role-based terms
    (like defendant, witness, lawyer, organization, etc.) for anonymization purposes.
    """

    def __init__(self, model_name: str = "llama2", temperature: float = 0.1):
        """
        Initialize the text corrector.

        Args:
            model_name: Name of the Ollama model to use
            temperature: Temperature parameter for text generation (lower values are more deterministic)
        """
        self.model_name = model_name
        self.temperature = temperature
        self.llm = None
        self._initialize_llm()

    def _initialize_llm(self) -> None:
        """Initialize the language model."""
        try:
            self.llm = Ollama(model=self.model_name, temperature=self.temperature)
            logger.info(f"Initialized Ollama with model: {self.model_name}")
        except Exception as e:
            logger.error(f"Failed to initialize Ollama: {str(e)}")
            logger.warning("Text correction will be disabled")
            self.llm = None

    def is_available(self) -> bool:
        """
        Check if the text corrector is available.

        Returns:
            True if the text corrector is available, False otherwise
        """
        return self.llm is not None

    def correct_text(self, text: str) -> str:
        """
        Correct spelling and grammar in text and replace names with appropriate role-based terms.

        This method corrects spelling and grammar errors in the provided text and also
        replaces names of individuals or entities/companies with appropriate role-based terms
        like defendant, witness, lawyer, organization, expert, police, etc.

        Args:
            text: Text to correct and anonymize

        Returns:
            Corrected and anonymized text
        """
        # Check if text is None, empty, contains only whitespace, or doesn't contain any alphabets
        # Only call Ollama if the text contains at least one alphabetic character
        logger.info(f"Correcting text: {text}")
        if not self.is_available() or not text or not text.strip() or not re.search(r'[a-zA-Z]', text):
            logger.info("Skipping text correction: text is empty, whitespace-only, or contains no alphabets")
            return text

        try:
            logger.info("Correcting text with Ollama")

            # Create a prompt for the language model
            prompt = f"""
            Please correct any spelling and grammar errors in the following text.
            Additionally, replace names of individuals or entities/companies with appropriate role-based terms like:
            - defendant, accused, petitioner, appellant, respondent for parties in the case
            - witness, victim, complainant for those giving testimony or affected
            - lawyer, attorney, counsel, advocate for legal representatives
            - organization, company, corporation, institution for business entities
            - expert, specialist, professional for those providing expert opinions
            - police, investigator, officer for law enforcement
            - judge, magistrate, justice for judicial officers

            Maintain the original meaning and structure. Only fix errors and replace names, don't rewrite or summarize or add notes of what was changed.

            Do not respond with any additional information other than the corrected text. If provided text is empty or could not correct, simply return the original text. Do not request for any additional information.

            TEXT: {text}

            CORRECTED TEXT:
            """

            # Generate corrected text
            response = self.llm.complete(prompt)
            corrected_text = response.text.strip()

            # If the model returns the prompt or formatting, extract just the corrected text
            if "CORRECTED TEXT:" in corrected_text:
                corrected_text = corrected_text.split("CORRECTED TEXT:")[1].strip()

            logger.info("Text correction completed")
            return corrected_text
        except Exception as e:
            logger.error(f"Error during text correction: {str(e)}")
            return text

    def correct_fields(self, data: Dict[str, Any], fields_to_correct: Optional[list] = None) -> Dict[str, Any]:
        """
        Correct spelling and grammar in specified fields of a dictionary and anonymize names.

        This method applies the correction and anonymization process to specified fields
        in a dictionary. It corrects spelling and grammar errors and replaces names of
        individuals or entities with appropriate role-based terms.

        Args:
            data: Dictionary containing fields to correct and anonymize
            fields_to_correct: List of field names to correct (if None, corrects all string fields)

        Returns:
            Dictionary with corrected and anonymized fields
        """
        if not self.is_available():
            return data

        # If fields_to_correct is not specified, correct all string fields
        if fields_to_correct is None:
            fields_to_correct = [field for field, value in data.items() if isinstance(value, str) and value]

        # Create a copy of the data to avoid modifying the original
        corrected_data = data.copy()

        # Correct each field
        for field in fields_to_correct:
            if field in data and isinstance(data[field], str) and data[field]:
                logger.info(f"Correcting field: {field}")
                corrected_data[field] = self.correct_text(data[field])

        return corrected_data
