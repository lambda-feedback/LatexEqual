# LatexEqual
This is an experimental evaluation function for comparing two latex strings. For evaluation, it actually calls the `symbolicEqual` function using the experimental EvaluationFunctionClient.

## Inputs
This function doesn't have any parameters, both `response` and `answer` should be valid LaTeX strings.

## Outputs

```json
{
  "is_correct": "<bool>"
}
```