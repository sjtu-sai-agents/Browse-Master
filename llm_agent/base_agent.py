from llm_agent.utils import LLMConfig
from typing import Dict, List, Any
from openai import OpenAI
import re
from llm_agent.context import BaseContextManager

class BaseAgent:
    def __init__(self, llm_config:Dict[str, Any]):

        self.llm_config:LLMConfig = LLMConfig(llm_config)
        self.client = OpenAI(base_url=self.llm_config.base_url, api_key=self.llm_config.api_key)
        self.print = self.llm_config.get('print', False)
        # print(f"self.print: {self.print}")

    def check_condition(self, input_str:str):
        if not self.llm_config.stop_condition:
            return False
        matches = list(re.finditer(self.llm_config.stop_condition, input_str, re.DOTALL))
        detected_num = len(matches)
        
        if detected_num > 0:
            return True
        return False


    def extract_tool_content(self, input_str:str):
        if not self.llm_config.tool_condition:
            return input_str, ''
        matches = list(re.finditer(self.llm_config.tool_condition, input_str, re.DOTALL))
        detected_num = len(matches)
        
        if detected_num > 0:
            match = matches[0]
            match_start_index = match.start()
            cut_text = input_str[:match_start_index]
            
            matched_text = match.group(0)
            if matched_text.startswith('<code'):
                code_content = match.group(1)
                return cut_text, code_content
            elif matched_text.startswith('<task>'):
                task_content = matched_text
                return cut_text, task_content

        return input_str, ''


    def call_api(self, prompt: str):
        try:
            with self.client.completions.create(
                model=self.llm_config.model,
                prompt=prompt,
                stream=True,
                **self.llm_config.generation_config
            ) as stream:
                full_response = ""
                for chunk in stream:
                    if 'delta' in chunk.choices[0]:
                        if chunk.choices[0].delta.content is not None:
                            content = chunk.choices[0].delta.content
                            if self.print:
                                print_in_color(content, 'yellow', end="", flush=True)
                            full_response += content
                    else:
                        content = chunk.choices[0].text
                        if self.print:
                            print_in_color(content, 'yellow', end="", flush=True)
                        full_response += content

                    stop_flag = self.check_condition(full_response)

                    if stop_flag:
                        return full_response.strip()

        except KeyboardInterrupt:
            print("Request interrupted")
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()

        return full_response.strip()


    def step(self, input_prompt:str):
        step_response = self.call_api(input_prompt)
        
        agent_response, tool_call_content = self.extract_tool_content(step_response)
        
        return {
            "step_response":agent_response,
            "tool_call_content":tool_call_content
        }



def print_in_color(text, color, *args, **kwargs):
    if color == 'red':
        print(f'\033[91m{text}\033[0m', *args, **kwargs)
    elif color == 'green':
        print(f'\033[92m{text}\033[0m', *args, **kwargs)
    elif color == 'yellow':
        print(f'\033[93m{text}\033[0m', *args, **kwargs)
    elif color == 'blue':
        print(f'\033[94m{text}\033[0m', *args, **kwargs)
    elif color == 'purple':
        print(f'\033[95m{text}\033[0m', *args, **kwargs)
    elif color == 'cyan':
        print(f'\033[96m{text}\033[0m', *args, **kwargs)
