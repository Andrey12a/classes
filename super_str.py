class SuperStr(str):
    def is_repeatance(s):
        ...

    def is_palindrom(s):
        s_lower = s.lower()
        return s_lower == s_lower[::-1]
