# AI Agent Context

## Objective

Explain the AI coding agent workflow behind the prediction task.

## Key Concept

The model predicts the next action an AI coding agent should take while working with a user. Each action represents a tool-use or response decision.

## Action Classes

| Class | Meaning | Notes |
| --- | --- | --- |
| `read_file` | Read a file | File inspection |
| `grep_search` | Search text patterns | Code or document search |
| `list_directory` | List folder contents | Workspace navigation |
| `glob_pattern` | Search by file pattern | File discovery |
| `edit_file` | Modify an existing file | Direct edit |
| `write_file` | Create a new file | New artifact |
| `apply_patch` | Apply a diff patch | Structured code edit |
| `run_bash` | Run shell command | General command execution |
| `run_tests` | Run tests | Verification |
| `lint_or_typecheck` | Run lint/type checks | Quality verification |
| `ask_user` | Ask clarification | Human input required |
| `plan_task` | Create a plan | Task decomposition |
| `web_search` | Search the web | External information |
| `respond_only` | Reply without tool use | Direct response |

## Agent Decision Signals

- Current user intent
- Workspace state
- Previous tool calls
- Recent failures or test results
- Remaining token budget
- Language preference

## Questions To Investigate

- Which prompts strongly imply file inspection?
- Which history patterns precede tests or linting?
- How often does low token budget lead to direct response?
- Which action pairs are commonly confused?

## Related Files

- [EDA Notebook](../notebooks/EDA.ipynb)
- [Error Analysis Notebook](../notebooks/Error_Analysis.ipynb)
