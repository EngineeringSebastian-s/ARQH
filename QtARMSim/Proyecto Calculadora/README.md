# Calculadora en Assembly ARM

## Descripción
Este programa implementa una calculadora básica en lenguaje ensamblador ARM que admite operaciones como suma, resta, multiplicación, división, potencia y módulo. Además, maneja valores decimales con tres decimales de precisión y permite valores negativos.

## Variables
- **num1**: Almacena el primer operando.
- **num2**: Almacena el segundo operando.
- **ope**: Almacena el operador ingresado.
- **sym**: Almacena el símbolo para indicar un resultado negativo.
- **res**: Almacena el resultado de la operación.
- **point**: Almacena el símbolo de punto decimal.
- **dec1, dec2, dec3**: Variables para cálculos internos de decimales.
- **str_f**: Cadena de formato para la salida del resultado.

## Subrutinas
- **sum**: Suma los operandos.
- **subtract**: Resta el segundo operando del primero.
- **multiply**: Multiplica los operandos.
- **divide**: Divide el primer operando por el segundo.
- **potencia**: Calcula la potencia de un número.
- **modulo**: Calcula el módulo de una división.
- **print_result**: Imprime el resultado formateado según la cadena `str_f`.

## Formato de `str_f`
La cadena de formato `str_f` se utiliza para formatear la salida del resultado. Está compuesta por los siguientes elementos:
- `%d`: Número entero.
- `%c`: Carácter.
- `%c%d%c%c%c%c`: Utilizado para mostrar el resultado en formato "Número Operador Número = Resultado".

Ejemplo de uso de `str_f`: `%d %c %d = %c%d%c%c%c%c`

El formato utilizado `%d %c %d = %c%d%c%c%c%c` se emplea para formatear la salida de las operaciones matemáticas en el código de ensamblador ARM. A continuación, se detalla cada parte del formato:

- `%d`: Este especificador de formato se usa para imprimir un número entero decimal. Por ejemplo, en `10 / 2 = 5`, `%d` imprime el resultado entero `5`.

- `%c`: Este especificador se utiliza para imprimir un carácter ASCII. En este contexto, se emplea para mostrar el signo del resultado y el punto decimal. Para el ejemplo `10 / 2 = 5`, `%c` representa el espacio en blanco que indica el punto decimal.

- `=`: Este símbolo se imprime tal como está para indicar la operación de igualdad.

- `%c%d%c%c%c%c`: Estos especificadores se usan para imprimir los dígitos decimales del resultado. En `10 / 2 = 5`, `%c%d%c%c%c%c` se traduce en el espacio (`%c`), el dígito `5` (`%d`), y otros caracteres que representan los decimales si los hay.

En resumen, este formato permite representar números enteros y decimales, junto con el signo y el punto decimal en el caso de números negativos y decimales.

## Instrucciones
- **main**: Función principal que inicia el programa y maneja las operaciones.
- **print_ind**: Imprime mensajes indicando casos especiales como división por cero o potencia de cero.
- **print_result**: Imprime el resultado formateado según `str_f`.
- **read**: Lee los valores de entrada desde la memoria.
- **write**: Escribe los valores de entrada en la memoria.

## Uso
1. Se inicia el programa en la función `main`.
2. Se ingresan los operandos y el operador.
3. Se selecciona la operación deseada.
4. El programa calcula y muestra el resultado formateado según `str_f`.

## Consideraciones
- Se manejan valores decimales con tres decimales de precisión.
- Se implementa la división entre cero y la potencia de cero.
- Se gestiona correctamente la salida de resultados y mensajes de error.
