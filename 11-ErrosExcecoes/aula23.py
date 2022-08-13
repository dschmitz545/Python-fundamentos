try:
    a = input("Numerador: ")
    b = input("Denominador: ")
    r = a / b

except TypeError as err:
    print(f"Problema de TIPO.{err.__cause__}")

except ZeroDivisionError as err1:
    print(f"divisão por zero. {err1.__cause__}")
    print(f"divisão por zero. {err1.__class__}")

except ValueError as err2:
    print(f"divisão por texto.{err2.__cause__}")
    print(f"divisão por texto.{err2.__class__}")

except KeyboardInterrupt:
    print("O usuário cancelou")
else:
    print(f"O resultado é {r}")

finally:
    print("Volte sempre")
