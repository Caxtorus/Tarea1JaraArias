#importa la libreria de pytest y los metodos de el archivo metodos.py
import pytest
import metodos

#se definen un grupo de argumentos para ser evaluados en prueba
@pytest.mark.parametrize("test", "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
#se define el metodo de prueba para un caso de exito en check_char, para todos los caracteres entre a-z y A-Z
def test_check_char(test):
    assert metodos.check_char(test) == 0

#se definen un grupo de argumentos para ser evaluados en prueba
@pytest.mark.parametrize("test", "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
#se define el metodo de prueba para un caso de exito en caps_switch, para todos los caracteres entre a-z y A-Z
def test_caps_switch(test):
    assert metodos.caps_switch(test) == test.swapcase()

#se definen un grupo de argumentos para ser evaluados en prueba
@pytest.mark.parametrize("test, error", [("af", 400), ("@", 404), (1, 502)])
#se define el metodo de prueba para los diferentes casos de error en check char, primero con más de un caracter
#entre el rango a-z o A-Z; luego con uno o mas caracteres que no sean parte del rango descrito anteriormente; finalmente
#que el caracter no sea de tipo "string/char"
def test_error_check_char(test, error):
    assert metodos.check_char(test) == error