from sympy.parsing.latex import parse_latex
from evaluation_function_utils.errors import EvaluationException
from evaluation_function_utils.client import EvaluationFunctionClient

# Initialise External Evaluation Function Client using credentials stored in
# .env NOTE: These credentials are already present in the base layer
client = EvaluationFunctionClient(".env")


def evaluation_function(response, answer, params):
    """
    Function used to evaluate a student response.
    ---
    The handler function passes three arguments to evaluation_function():

    - `response` which are the answers provided by the student.
    - `answer` which are the correct answers to compare against.
    - `params` which are any extra parameters that may be useful,
        e.g., error tolerances.

    The output of this function is what is returned as the API response 
    and therefore must be JSON-encodable. It must also conform to the 
    response schema.

    Any standard python library may be used, as well as any package 
    available on pip (provided it is added to requirements.txt).

    The way you wish to structure you code (all in this function, or 
    split into many) is entirely up to you. All that matters are the 
    return types and that evaluation_function() is the main function used 
    to output the evaluation response.
    """

    # Attempt to parse both the response and answer latex strings
    try:
        res = parse_latex(response)
    except (SyntaxError, TypeError) as e:
        raise EvaluationException("There was an error parsing your response",
                                  error_repr=repr(e))

    try:
        ans = parse_latex(answer)
    except (SyntaxError, TypeError) as e:
        raise EvaluationException("There was an error in parsing the answer",
                                  error_repr=repr(e))

    # Convert the SymPy Expr into strings and evaluate using symbolicEqual
    evaluation = client.invoke("symbolicEqual", str(res), str(ans))

    return evaluation