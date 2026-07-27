import io
import ast
import contextlib
import traceback


def execute_python_code(code, df):
    """
    Execute Python code and return:
    - printed output
    - last evaluated object
    """

    local_namespace = {
        "df": df
    }

    output_buffer = io.StringIO()

    try:

        with contextlib.redirect_stdout(output_buffer):

            parsed = ast.parse(code)

            result = None

            # -----------------------------------------
            # If last statement is an expression
            # Example:
            #
            # fig
            # df.head()
            # df.describe()
            # -----------------------------------------

            if parsed.body and isinstance(parsed.body[-1], ast.Expr):

                body = parsed.body[:-1]

                if body:

                    exec(
                        compile(
                            ast.Module(body=body, type_ignores=[]),
                            "<string>",
                            "exec"
                        ),
                        {},
                        local_namespace
                    )

                result = eval(
                    compile(
                        ast.Expression(parsed.body[-1].value),
                        "<string>",
                        "eval"
                    ),
                    {},
                    local_namespace
                )

            else:

                exec(code, {}, local_namespace)

                # -----------------------------------------
                # Automatically detect common variables
                # -----------------------------------------

                if "fig" in local_namespace:
                    result = local_namespace["fig"]

                elif "result" in local_namespace:
                    result = local_namespace["result"]

                elif "_" in local_namespace:
                    result = local_namespace["_"]

                else:
                    result = None

        printed_output = output_buffer.getvalue()

        return True, printed_output, result

    except Exception:

        return False, traceback.format_exc(), None