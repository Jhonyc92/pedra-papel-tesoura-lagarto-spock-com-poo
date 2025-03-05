# Importando o módulo 'random' para usar funções que geram valores 
# aleatórios (necessário para a escolha do computador).
import random

# Definindo uma classe chamada "JogoPedraPapelTesouraLagartoSpock" para 
# encapsular a lógica e estado do jogo.
class JogoPedraPapelTesouraLagartoSpock:

    # Método construtor (__init__) da classe. Esse método é chamado automaticamente 
    # sempre que um objeto dessa classe é instanciado.
    def __init__(self):

        # Inicializando a pontuação do jogador como 0. Este atributo armazenará 
        # os pontos que o jogador ganhará durante o jogo.
        self.pontuacao_jogador = 0

        # Inicializando a pontuação do computador como 0. Este atributo 
        # armazenará os pontos que o computador ganhará durante o jogo.
        self.pontuacao_computador = 0

        # Inicializando uma lista com as possíveis escolhas no jogo. Estas são 
        # as opções que jogador e computador podem escolher durante uma rodada.
        self.escolhas = ['Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock']

    # Método para obter a escolha do jogador.
    def obter_escolha_jogador(self):

        # Imprimindo opções disponíveis para o jogador escolher. Cada opção 
        # corresponde a uma escolha no jogo.
        print("\n1. Pedra")
        print("2. Papel")
        print("3. Tesoura")
        print("4. Lagarto")
        print("5. Spock")

        # Solicitando a escolha do jogador através da entrada do teclado. A 
        # entrada é convertida para um valor inteiro.
        escolha = int(input("Escolha sua opção (1 a 5): "))

        # Retorna a escolha do jogador como uma string. 
        # O índice da lista 'self.escolhas' é acessado convertendo o número         
        # escolhido pelo jogador para o índice apropriado (0 a 4). 
        # Subtraímos 1 do valor inserido porque as listas em Python são indexadas a partir de 0.
        return self.escolhas[escolha - 1]
    
    # Método para obter a escolha do computador.
    def obter_escolha_computador(self):

        # Usando a função 'choice' do módulo 'random' para fazer uma escolha
        # aleatória de uma opção da lista 'self.escolhas'.
        # Retorna essa escolha aleatória como a escolha do computador para a rodada atual.
        return random.choice(self.escolhas)


    # Método para determinar o vencedor de uma rodada, baseado nas escolhas do jogador e do computador.
    def determinar_vencedor(self, escolha_jogador, escolha_computador):

        # Exibe a escolha feita pelo jogador.
        print(f"Você escolheu {escolha_jogador}")

        # Exibe a escolha feita pelo computador.
        print(f"O computador escolheu {escolha_computador}")

        # Define as regras do jogo e a razão pela qual uma escolha ganha da outra.
        regras = {
            'Pedra': {'vence': ['Tesoura', 'Lagarto'], 'razao': ['quebra', 'esmaga']},
            'Papel': {'vence': ['Pedra', 'Spock'], 'razao': ['cobre', 'refuta']},
            'Tesoura': {'vence': ['Papel', 'Lagarto'], 'razao': ['corta', 'decapita']},
            'Lagarto': {'vence': ['Spock', 'Papel'], 'razao': ['envenena', 'come']},
            'Spock': {'vence': ['Tesoura', 'Pedra'], 'razao': ['esmaga', 'vaporiza']}
        }

        # Verifica se a escolha do jogador é a mesma do computador.
        if escolha_jogador == escolha_computador:
            print("É um empate!")

        # Verifica se a escolha feita pelo computador está na lista de escolhas que 
        # a escolha do jogador consegue vencer.
        elif escolha_computador in regras[escolha_jogador]['vence']:
            
            # Obtém o índice da escolha do computador na lista de escolhas que a escolha do jogador vence.
            # Isso é feito para, em seguida, encontrar a razão correspondente pela qual o jogador venceu.
            indice = regras[escolha_jogador]['vence'].index(escolha_computador)

            # Usando o índice obtido anteriormente, esta linha pega a razão específica pela qual 
            # a escolha do jogador vence a escolha do computador.
            razao = regras[escolha_jogador]['razao'][indice]

            # Imprime uma mensagem para o jogador explicando por que ele venceu, usando as escolhas feitas 
            # e a razão específica encontrada anteriormente.
            print(f"Você ganhou porque {escolha_jogador} {razao} {escolha_computador}!")

            # Incrementa a pontuação do jogador em 1, pois ele venceu esta rodada.
            self.pontuacao_jogador += 1

        # Se a rodada não resultou em um empate e o jogador não venceu, então a única possibilidade restante é que 
        # o computador venceu. O código a seguir lida com esse caso.
        else:

            # Obtém o índice da escolha do jogador na lista de escolhas que a escolha do computador vence.
            # Isso é feito para, em seguida, encontrar a razão correspondente pela qual o computador venceu.
            indice = regras[escolha_computador]['vence'].index(escolha_jogador)

            # Usando o índice obtido anteriormente, esta linha pega a razão específica pela qual 
            # a escolha do computador vence a escolha do jogador.
            razao = regras[escolha_computador]['razao'][indice]

            # Imprime uma mensagem para o jogador explicando por que ele perdeu, usando as escolhas feitas 
            # e a razão específica encontrada anteriormente.
            print(f"Você perdeu porque {escolha_computador} {razao} {escolha_jogador}!")

            # Incrementa a pontuação do computador em 1, pois ele venceu esta rodada.
            self.pontuacao_computador += 1
                        
    # Método para exibir a pontuação atual do jogo.
    def exibir_pontuacao(self):

        # Imprimindo a pontuação atual do jogador e do computador usando f-strings.
        print(f"Pontuação: Você {self.pontuacao_jogador} x Computador {self.pontuacao_computador}")


    # Método principal para iniciar e controlar o fluxo do jogo.
    def jogar(self):

        # Imprime uma mensagem de boas-vindas ao jogador.
        print("Bem-vindo ao jogo Pedra, Papel, Tesoura, Lagarto e Spock!")

        # Solicita ao usuário para inserir o número de rodadas que deseja jogar 
        # e converte essa entrada em um número inteiro.
        rodadas = int(input("Quantas rodadas você quer jogar? "))

        # Loop para jogar o número de rodadas especificado pelo jogador.
        for _ in range(rodadas):

            # Chama o método para obter a escolha do jogador e armazena na variável 'escolha_jogador'.
            escolha_jogador = self.obter_escolha_jogador()

            # Chama o método para obter a escolha aleatória do computador e armazena 
            # na variável 'escolha_computador'.
            escolha_computador = self.obter_escolha_computador()

            # Chama o método para determinar o vencedor da rodada atual usando as escolhas feitas.
            self.determinar_vencedor(escolha_jogador, escolha_computador)

            # Chama o método para exibir a pontuação atual após cada rodada.
            self.exibir_pontuacao()

        # Imprime uma mensagem indicando o fim do jogo.
        print("Fim do jogo!")

# Verifica se este script é o ponto de entrada principal. Esta é uma prática comum em Python para garantir 
# que o código dentro deste bloco só será executado se o arquivo for executado diretamente e não quando importado como um módulo.
if __name__ == "__main__":

    # Cria um objeto 'jogo' da classe 'JogoPedraPapelTesouraLagartoSpock' (inicializa uma nova instância do jogo).
    jogo = JogoPedraPapelTesouraLagartoSpock()

    # Chama o método 'jogar' do objeto 'jogo' para iniciar o jogo.
    jogo.jogar()
