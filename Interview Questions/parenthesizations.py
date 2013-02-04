"""
given an input n write a code to generate all possible parenthesizations
for ex if n=3
then print

((()))
(())()
()()()
(()())
()(())
"""

def parenthesizations(n):
    def _parenthesizations(n, have_opened):
        if n  == 0:
            yield ''
        else:
            if have_opened > 0:
                for i in _parenthesizations(n-1, have_opened -1):
                    yield ')' + i
            if have_opened < n:
                for i in _parenthesizations(n-1, have_opened + 1):
                    yield '(' + i
    for x in _parenthesizations(n*2,0):
        yield x


for x in parenthesizations(4):
    print x
