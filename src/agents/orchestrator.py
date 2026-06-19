from langgraph.graph import StateGraph

class AgentState(dict):
    pass

def business_logic_node(state):

    state["business_logic"] = True

    return state

def race_condition_node(state):

    state["race_condition"] = True

    return state

builder = StateGraph(AgentState)

builder.add_node(
    "business_logic",
    business_logic_node
)

builder.add_node(
    "race_condition",
    race_condition_node
)

builder.set_entry_point(
    "business_logic"
)

builder.add_edge(
    "business_logic",
    "race_condition"
)

workflow = builder.compile()
