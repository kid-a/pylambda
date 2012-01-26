
class Variable:
    def __init__ (self, uName):
        self._name = uName

    def __str__ (self):
        return str (self._name)

    def __eq__ (self, other):
        if isinstance (other, Variable):
            if other._name == self._name:
                return True
        return False

    # def __hash__ (self):
    #     return hash (self._name)

    # def unify (self, uTerm):
    #     if not isinstance (uTerm, Variable):
    #         return False
    #     return (Variable (self._name), Variable (uTerm._name))


class Application:
    def __init__ (self, uFirst, uSecond):
        self._first = uFirst
        self._second = uSecond

    def __str__ (self):
        #return '(' + str (self._first) + ')' + '(' + str (self._second) + ')'
        return str (self._first) + str (self._second)

    def __eq__ (self, other):
        if isinstance (other, Application):
            return (other._first == self._first) and \
                (other._second == self._second)
        return False

    # def __hash__ (self):
    #     return hash ((self._first, self._second))


class Abstraction:
    def __init__ (self, uVariable, uBody):
        self._variable = uVariable
        self._body = uBody

    def __str__ (self):
        return '(\\' + str (self._variable) + '.' + str (self._body) + ')'

    def __eq__ (self, other):
        if isinstance (other, Abstraction):
            return (other._variable == self._variable) and \
                (other._body == self._body)
        return False

    # def __hash__ (self):
    #     return hash ((self._variable, self._body))

    # def unify (self, uTerm):
    #     if not isinstance (uTerm, Abstraction):
    #         return False

    #     ## calculate the substitutions for the body of the abstraction
    #     body_substitutions = self._body.unify (uTerm._body)

    #     ## then do the same for the head
    #     head_substitutions = self._variable.unify (uTerm._variable)

    #     ## check, whether a clash exists, that the substitution
    #     ## to perform is the same
    #     # for sub in head_substitutions:
    #     #     if sub in body_substitutions:
    #     #         (to_subtitute, new_term) = sub






            # # try:
            # #     new_term = body_substitutions [sub]
            # #     if new_term == head_substitutions [sub]: continue
            # #     else: return False

            # # except: continue

        ## return the merged dict of substitutions
        # for s in head_substitutions:
        #     body_substitutions.append (s)
        # return body_substitutions
