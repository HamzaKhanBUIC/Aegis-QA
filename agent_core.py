"""
Aegis-QA Agent Core
Orchestration layer for the agentic swarm system with Watsonx.ai integration
"""

import os
import requests
from dotenv import load_dotenv
from typing import Dict, Optional

# Load environment variables
load_dotenv()


class AegisSwarm:
    """
    Main orchestration class for Aegis-QA swarm agents.
    Coordinates unit test generation and security documentation using Watsonx.ai.
    """
    
    def __init__(self) -> None:
        """Initialize the AegisSwarm orchestrator with Watsonx.ai credentials."""
        self.api_key = os.getenv("WATSONX_API_KEY")
        self.project_id = os.getenv("WATSONX_PROJECT_ID")
        self.iam_token_url = "https://iam.cloud.ibm.com/identity/token"
        self.watsonx_url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
        self.model_id = "ibm/granite-3-8b-instruct"
        self.access_token = None
        
        # Validate credentials
        if not self.api_key or not self.project_id:
            raise ValueError(
                "Missing Watsonx.ai credentials. Please set WATSONX_API_KEY and "
                "WATSONX_PROJECT_ID in your .env file."
            )
    
    def _get_iam_token(self) -> str:
        """
        Generate an IAM access token using the API key.
        
        Returns:
            str: The IAM access token
            
        Raises:
            Exception: If token generation fails
        """
        try:
            headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            }
            data = {
                "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
                "apikey": self.api_key
            }
            
            response = requests.post(
                self.iam_token_url,
                headers=headers,
                data=data,
                timeout=30
            )
            response.raise_for_status()
            
            token_data = response.json()
            return token_data["access_token"]
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to generate IAM token: {str(e)}")
        except KeyError:
            raise Exception("Invalid response from IAM token endpoint")
    
    def _call_watsonx(self, prompt: str, max_tokens: int = 2000) -> str:
        """
        Make a call to the Watsonx.ai text generation API.
        
        Args:
            prompt (str): The prompt to send to the model
            max_tokens (int): Maximum number of tokens to generate
            
        Returns:
            str: The generated text from the model
            
        Raises:
            Exception: If the API call fails
        """
        try:
            # Get fresh token if not available
            if not self.access_token:
                self.access_token = self._get_iam_token()
            
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.access_token}"
            }
            
            payload = {
                "input": prompt,
                "parameters": {
                    "decoding_method": "greedy",
                    "max_new_tokens": max_tokens,
                    "min_new_tokens": 50,
                    "stop_sequences": [],
                    "repetition_penalty": 1.1
                },
                "model_id": self.model_id,
                "project_id": self.project_id
            }
            
            response = requests.post(
                self.watsonx_url,
                headers=headers,
                json=payload,
                timeout=60
            )
            
            # If token expired, refresh and retry
            if response.status_code == 401:
                self.access_token = self._get_iam_token()
                headers["Authorization"] = f"Bearer {self.access_token}"
                response = requests.post(
                    self.watsonx_url,
                    headers=headers,
                    json=payload,
                    timeout=60
                )
            
            response.raise_for_status()
            result = response.json()
            
            # Extract generated text
            if "results" in result and len(result["results"]) > 0:
                return result["results"][0]["generated_text"].strip()
            else:
                raise Exception("No generated text in response")
                
        except requests.exceptions.RequestException as e:
            raise Exception(f"Watsonx.ai API call failed: {str(e)}")
        except (KeyError, IndexError) as e:
            raise Exception(f"Invalid response format from Watsonx.ai: {str(e)}")
    
    def run_audit(self, code_snippet: str) -> Dict[str, str]:
        """
        Execute a full swarm audit on the provided code snippet.
        
        Args:
            code_snippet (str): The Python code to analyze
            
        Returns:
            dict: Contains 'unit_tests' and 'security_docs' keys with generated content
        """
        try:
            # Validate input
            if not code_snippet or not code_snippet.strip():
                return {
                    "unit_tests": "# Error: No code snippet provided",
                    "security_docs": "# Error: No code snippet provided"
                }
            
            # First API call: Generate PyTest suite (QA Engineer)
            qa_prompt = f"""You are an expert QA Engineer. Generate a comprehensive PyTest test suite for the following Python code.

Code to test:
```python
{code_snippet}
```

Requirements:
- Write complete, runnable pytest test cases
- Include test_input_validation, test_edge_cases, test_security_validation, and test_performance
- Use proper pytest fixtures and assertions
- Add docstrings to each test function
- Handle edge cases and boundary conditions
- Include security-focused tests (SQL injection, XSS, etc.)

Generate ONLY the pytest code, no explanations:"""

            print("Generating unit tests with Watsonx.ai...")
            unit_tests = self._call_watsonx(qa_prompt, max_tokens=2500)
            
            # Second API call: Generate security report (Cybersecurity Auditor)
            security_prompt = f"""You are an expert Cybersecurity Auditor. Analyze the following Python code and generate a detailed markdown security report.

Code to analyze:
```python
{code_snippet}
```

Requirements:
- Create a markdown report with sections: Security Analysis, Vulnerability Assessment, Security Recommendations, and Comprehensive Documentation
- Identify potential vulnerabilities (SQL injection, XSS, authentication issues, etc.)
- Rate each vulnerability with ✅ (safe), ⚠️ (warning), or ❌ (critical)
- Provide specific, actionable security recommendations
- Include function documentation with parameters, returns, usage examples
- Add performance characteristics and dependencies
- Use professional security audit formatting

Generate ONLY the markdown report, no preamble:"""

            print("Generating security documentation with Watsonx.ai...")
            security_docs = self._call_watsonx(security_prompt, max_tokens=2500)
            
            return {
                "unit_tests": unit_tests,
                "security_docs": security_docs
            }
            
        except Exception as e:
            # Graceful error handling - return error messages instead of crashing
            error_message = f"Error during audit: {str(e)}"
            print(f"⚠️ {error_message}")
            
            return {
                "unit_tests": f"# Error generating unit tests\n# {error_message}\n\n# Please check your Watsonx.ai credentials and try again.",
                "security_docs": f"# Error generating security documentation\n\n**Error:** {error_message}\n\nPlease verify:\n- WATSONX_API_KEY is set correctly\n- WATSONX_PROJECT_ID is set correctly\n- Your IBM Cloud account has access to Watsonx.ai\n- Network connectivity is available"
            }


# Made with Bob
