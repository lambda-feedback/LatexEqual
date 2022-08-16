# LatexEqual
This is an experimental evaluation function for comparing two latex strings. For evaluation, it actually calls the `symbolicEqual` function using the experimental EvaluationFunctionClient.

## Inputs
This function doesn't have any parameters, both `response` and `answer` should be valid LaTeX strings. If you wish, you can pass parameters that are relayed to the `symbolicEqual` function (refer to it's documentation for more information about those).

## Outputs

```json
{
  "is_correct": "<bool>"
}
```