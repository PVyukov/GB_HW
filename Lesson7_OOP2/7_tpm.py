# class OurClass:
#
#     def __init__(self, a):
#         self.OurAtt = a
#
#     @property
#     def OurAtt(self):
#         return self.__OurAtt
#
#     @OurAtt.setter
#     def OurAtt(self, val):
#         if val < 0:
#             self.__OurAtt = 0
#         elif val > 1000:
#             self.__OurAtt = 1000
#         else:
#             self.__OurAtt = val
#
#
# x = OurClass(10)
# print(x.OurAtt)


# class Tmp:
#     def __init__(self):
#         self.word = 'lol'
#
#     def print_word(self, word):
#         print(self.word + word)
#
#
# t = Tmp()
# t.print_word(' 100')


import os
os.rename('tmp.py', '7_tpm.py')