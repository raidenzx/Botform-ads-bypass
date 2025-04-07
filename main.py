#-*-coding: UTF-8-*-
from botcity.core import DesktopBot
import pyautogui
import pandas as pd
import speech_recognition as sr
from time import sleep
from tkinter import *
import ctypes

time = 12
time2 = 2
print("iniciando Bot")
root=Tk

pyautogui.hotkey('alt', 'tab')

tabela_ids = pd.read_excel("ids.xlsx")
recaptcha_check = 0

class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        for i, id in enumerate(tabela_ids['ID']):
            if not self.find( "entre_em_contato", matching=0.97, waiting_time=10000):
                self.not_found("entre_em_contato")
            self.click()
           
            
            sleep(time2) 
            if not self.find( "contestar", matching=0.97, waiting_time=10000):
                self.not_found("contestar")
            self.click()
            
            sleep(time)
        
            self.scroll_down(2300)
            sleep(2)
            if not self.find( "contagoogle", matching=0.97, waiting_time=10000):
                self.not_found("contagoogle")
            self.click()
            
            
            pyautogui.write(id)
            sleep(5)
            pyautogui.press('tab')
            pyautogui.press('enter')
            #lembrar de colocar em loop
            sleep(time2)
            if not self.find( "click site", matching=0.97, waiting_time=10000):
                self.not_found("click site")
            self.click()
        
            pyautogui.write("https://tudosobrecodigosff.blogspot.com/")
        
            pyautogui.press('tab')
            pyautogui.press('tab')
        
            pyautogui.write("Nao existe palavras chaves")
        
            pyautogui.press('tab')
        
            pyautogui.write('R. Jupiter, 84 - Centro')
        
            pyautogui.press('tab')
       
            pyautogui.write('26553-490')
       
            pyautogui.press('tab')
       
            pyautogui.write('Rio de Janeiro')
            sleep(time2)
            if not self.find( "selecione seu pais", matching=0.97, waiting_time=10000):
                self.not_found("selecione seu pais")
      
            if not self.find( "selecione uma op", matching=0.97, waiting_time=10000):
                self.not_found("selecione uma op")
            self.click()

            sleep(time2)
       
            self.scroll_down(1800)
       
            if not self.find( "click brazil", matching=0.97, waiting_time=10000):
                self.not_found("click brazil")
            self.click()

            self.scroll_down(500)
        
            sleep(time2)
            if not self.find( "click mmc", matching=0.97, waiting_time=10000):
                self.not_found("click mmc")
            self.click()
        
            sleep(time2)
            if not self.find_text( "empresa", threshold=230, waiting_time=10000):
                self.not_found("empresa")
            self.click()
        
            self.scroll_down(500)
            sleep(time2)
            if not self.find( "click quem paga", matching=0.97, waiting_time=10000):
                self.not_found("click quem paga")
            self.click()
            pyautogui.write('Eu mesmo sou responsavel pelos pagamentos dos anuncios nesta conta atraves do meu cartao de credito VISA.')

            self.scroll_down(200)
            sleep(time2)
            if not self.find( "click pagamento", matching=0.97, waiting_time=10000):
                self.not_found("click pagamento")
            self.click()
        
            sleep(time2)
            if not self.find( "click cartao", matching=0.97, waiting_time=10000):
                self.not_found("click cartao")
            self.click()
        
            self.scroll_down(300)

            if not self.find( "quais paises", matching=0.97, waiting_time=10000):
                self.not_found("quais paises")
       
            if not self.find( "selecionar pais", matching=0.97, waiting_time=10000):
                self.not_found("selecionar pais")
            self.click()
        
            self.scroll_down(350)
        
            if not self.find( "find brasil", matching=0.97, waiting_time=10000):
                self.not_found("find brasil")
        
            if not self.find( "click brasil", matching=0.97, waiting_time=10000):
                self.not_found("click brasil")
            self.click()

            self.scroll_down(100)
            sleep(time2)
            if not self.find( "descrever empresa", matching=0.97, waiting_time=10000):
                self.not_found("descrever empresa")
            self.click()
            pyautogui.write("Afiliada profissional pessoa fisica de produtos digitais e/ou fisicos.")
            pyautogui.press('tab')
            sleep(time2)
            pyautogui.write("Relaçao estabelecida por meio de plataformas intermediadoras de pagamento como Hotmart, Clickbank e Monetizze. Ressaltando que não tenho nenhum vinculo com os proprietarios dos dominios que promovo.")
            pyautogui.press('tab')
            sleep(time2)
            pyautogui.write("Os dominios para os quais eu anuncio sao de propriedade de terceiros. Minha funçao e apenas a divulgaçao das paginas de destino visando o recebimento de comissoes por vendas realizadas.")
            pyautogui.press('tab')
            sleep(time2)
            pyautogui.write('Venho por meio deste apelo informar que eu ainda nao criei campanha e nem inserir o faturamento e mesmo assim. Minha conta foi suspensa por pagamento suspeitos, portanto, intercedo para que meu direito de veicular anúncios na plataforma seja restabelecido a fim de evitar maiores danos a minha pessoa porque se nao eu vou tomar as devidas providencias na esfera civel e criminal por danos materiais (esta sem vender) e danos morais, ja que estou sendo privado de receber uma informaçao que lhe diz respeito.')

            self.scroll_down(500)

            def Mbox(title, text, style):
                return ctypes.windll.user32.MessageBoxW(0, text, title, style)
            Mbox('Fim do Formulario', 'Preencha o Captcha e Envie o Formulario', 0,)
            


            sleep(10)
            pyautogui.press('f5')
            sleep(31)
            
            if not self.find( "click fechar", matching=0.97, waiting_time=10000):
                self.not_found("click fechar")
            self.click()
            sleep(time2)
            
        
 
        def not_found(self, label):
            print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
