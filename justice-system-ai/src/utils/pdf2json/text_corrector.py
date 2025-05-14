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

        The text is processed in chunks of approximately 500 characters, with chunk boundaries
        at natural text breaks like periods or end of lines.

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
            logger.info("Correcting text with Ollama in chunks")

            # Split text into chunks of approximately 500 characters
            # Break at natural boundaries (periods or end of lines)
            chunks = self._split_text_into_chunks(text)
            corrected_chunks = []

            for i, chunk in enumerate(chunks):
                logger.info(f"Processing chunk {i+1}/{len(chunks)}")

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

                TEXT: {chunk}

                CORRECTED TEXT:
                """

                # Generate corrected text for this chunk
                response = self.llm.complete(prompt)
                corrected_chunk = response.text.strip()

                # If the model returns the prompt or formatting, extract just the corrected text
                if "CORRECTED TEXT:" in corrected_chunk:
                    corrected_chunk = corrected_chunk.split("CORRECTED TEXT:")[1].strip()

                corrected_chunks.append(corrected_chunk)

            # Combine all corrected chunks
            corrected_text = " ".join(corrected_chunks)
            logger.info("Text correction completed")
            return corrected_text
        except Exception as e:
            logger.error(f"Error during text correction: {str(e)}")
            return text

    def _split_text_into_chunks(self, text: str, chunk_size: int = 1000) -> list:
        """
        Split text into chunks of approximately the specified size.

        Chunks are created by breaking at natural boundaries like periods or end of lines.
        If no natural boundary is found within a reasonable range, the chunk is split at the exact size.

        Args:
            text: Text to split into chunks
            chunk_size: Target size for each chunk in characters

        Returns:
            List of text chunks
        """
        if not text:
            return []

        chunks = []
        current_pos = 0
        text_length = len(text)

        while current_pos < text_length:
            # Determine end position for this chunk
            end_pos = min(current_pos + chunk_size, text_length)

            # If we're not at the end of the text, try to find a natural break
            if end_pos < text_length:
                # Look for period followed by space or newline
                period_pos = text.rfind('. ', current_pos, end_pos)
                newline_pos = text.rfind('\n', current_pos, end_pos)

                # Find the latest natural break
                natural_break = max(period_pos, newline_pos)

                # If found a natural break, use it
                if natural_break > current_pos:
                    # Include the period or newline in the chunk
                    if natural_break == period_pos:
                        end_pos = period_pos + 2  # Include period and space
                    else:
                        end_pos = newline_pos + 1  # Include newline

            # Extract the chunk and add to list
            chunk = text[current_pos:end_pos].strip()
            if chunk:  # Only add non-empty chunks
                chunks.append(chunk)

            # Move to next position
            current_pos = end_pos

        return chunks

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
