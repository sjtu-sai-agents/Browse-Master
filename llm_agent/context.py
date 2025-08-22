from jinja2 import Template


class BaseContextManager:
    def __init__(self, chat_template:str):
        self.chat_template:Template = Template(chat_template)
        self.agent_logs = []
    
    def replace_agent_logs(self, agent_logs:list):
        self.agent_logs = agent_logs
        
    def return_logs(self):
        return self.agent_logs
    
    def build_input_prompt(self):
        result = self.chat_template.render(tool_logs=self.agent_logs)
        return result

    def log_agent(self, agent_action:str):
        self.agent_logs.append(
            {"role":"assistant", "content":agent_action}
        )

    def log_tool_call(self, tool_call_content:str):
        self.agent_logs.append(
            {"role":"tool_call", "content":tool_call_content}
        )

    def log_tool_call_result(self, tool_call_result_content:str):
        self.agent_logs.append(
            {"role":"tool_call_result", "content":tool_call_result_content}
        )

    def log_turn_summary(self, turn_summary:str):
        self.agent_logs = [log for log in self.agent_logs if log["role"] == "user" or log["role"] == "turn_summary"]
        self.agent_logs.append(
            {"role":"turn_summary", "content":turn_summary}
        )
    
    def refresh_user_log(self, user_log_content:str):
        self.agent_logs = [
            {"role":"user", "content":user_log_content},
        ]

    def refresh(self, ):
        self.agent_logs = []

