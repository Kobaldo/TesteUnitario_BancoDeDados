import unittest 
from unittest.mock import patch 
from CRUD import UsersCRUD 
import coverage 
import webbrowser 
import os 

 
class TestUsersCRUD(unittest.TestCase): 
    def setUp(self):  
        self.crud = UsersCRUD() 
        self.crud.create_user("Alice", 25) 
        self.crud.create_user("Bob", 30) 
        self.crud.create_user("Charlie", 20) 

    def test_create_user(self): 
        print('Coloque seu teste de criação de usuário aqui') 

    def test_read_users(self): 
        print('Coloque seu teste de leitura de usuário aqui') 


    def test_update_user(self): 
         print('Coloque seu teste de leitura de usuário aqui') 


    def test_update_user_invalid_index(self): 
         print('Coloque seu teste de leitura de usuário inválido aqui') 
 

    def test_delete_user(self): 
         print('Coloque seu teste de deleção de usuário aqui') 


    def test_delete_user_invalid_index(self): 
         print('Coloque seu teste de deleção de usuário inválido aqui') 


if __name__ == '__main__': 
    # Criar uma instância do Coverage com o arquivo .coveragerc 
    cov = coverage.Coverage(config_file='.coveragerc.txt') 

    # Iniciar a medição da cobertura 
    cov.start() 

    # Executar os testes 
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUsersCRUD) 
    unittest.TextTestRunner(verbosity=2).run(suite) 

    # Encerrar a medição da cobertura após os testes 
    cov.stop() 

    # Salvar os dados de cobertura em um arquivo 
    cov.save() 
    cov.html_report(directory='htmlcov') 

    # Abra o relatório no navegador 
    index_file = os.path.join('htmlcov', 'index.html') 
    webbrowser.open('file://' + os.path.abspath(index_file)) 

 

 