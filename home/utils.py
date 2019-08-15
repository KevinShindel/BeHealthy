from abc import ABCMeta, abstractmethod


class AbstractExpression(metaclass=ABCMeta):

    @abstractmethod
    def interpret(self):
        pass


class Expression(AbstractExpression):
    def __init__(self, dictionary, parameters):
        self.parameters = parameters
        self.parameter = dictionary['parameter']
        self.relating_by_val = dictionary['relating_by_val']
        self.value = dictionary['value']

    def interpret(self):
        return condition_to_bool(self.parameters[self.parameter], self.relating_by_val, self.value)


def define_expression(defined):
    params = {'gender', 'age', 'abdominal_pain', 'systolic_bp', 'diastolic_bp'}
    return params - set(defined.keys())


def condition_to_bool(parameter, operator, value):
    return {
        '=': parameter == value,
        '>': parameter > value,
        '<': parameter < value,
        '>=': parameter >= value,
        '<=': parameter <= value
    }[operator]


def combine_conditions(first_expression, second_expression, operator):
    return {
        'or': first_expression or second_expression,
        'and': first_expression and second_expression,
        'and not': first_expression and not second_expression,
        'or not': first_expression or not second_expression
    }[operator.lower()]


def set_up_expression(parameters, expression_dict, index=0):
    if index == 0:
        expression_dict = eval(expression_dict)
    exp = Expression(expression_dict[index], parameters)
    resulted_bool = exp.interpret()
    if len(expression_dict) > 1 and index < len(expression_dict) - 1:
        resulted_bool = combine_conditions(resulted_bool, set_up_expression(parameters, expression_dict, index + 1),
                                           expression_dict[index + 1]['prev_apart_condition'])
    return resulted_bool
