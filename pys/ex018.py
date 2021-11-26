import math

teta = float(input('Digite o ângulo em radianos: '))
rad = teta*(math.pi)
seno = math.sin(rad)
cos = math.cos(rad)
tg = math.tan(rad)
print('Esse ângulo corresponde a {} radianos. \n O seno desse ângulo vale {}. \n O cosseno desse ângulo vale {}. '
      '\n A tangente desse ângulo vale {}.' .format(rad, seno, cos, tg))
