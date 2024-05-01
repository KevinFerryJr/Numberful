class ErrorMessage:
    def operator_overload(self, other, operator):
        error_msg = f"Unsupported operator '{operator}' between types '{type(self).__name__}' and '{type(other).__name__}'. Types must match!"
        return error_msg

    @staticmethod
    def invalid_type(arg_name, expected_type, actual_value):
        error_msg = f"Invalid type for argument '{arg_name}'. Expected type: '{expected_type}', got '{type(actual_value).__name__}'."
        return error_msg

    @staticmethod
    def invalid_value(arg_name, allowed_values):
        error_msg = f"Invalid value for argument '{arg_name}'. Allowed values: {', '.join(map(str, allowed_values))}."
        return error_msg

    @staticmethod
    def missing_argument(arg_name):
        error_msg = f"Missing required argument '{arg_name}'."
        return error_msg

    @staticmethod
    def invalid_operation(operation_name, reason):
        error_msg = f"Invalid operation '{operation_name}'. Reason: {reason}."
        return error_msg
