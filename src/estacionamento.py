from areas import Areas
from eventos import Eventos
from proprietario import Proprietario
from usuario import Usuario
from veiculo import Veiculo
from ocorrencias import Ocorrencia


class Estacionamento:
    """Representa o estacionamento e cotrola a integração dos métodos das classes"""

    def __init__(self):
        self.controle_areas = list()
        self.cadastro_veiculos = list()
        self.cadastro_ocorrencias = list()
        self.categorias = list()
        self.cadastro_usuario = list()
        self.controle_eventos = list()

    #getters
    def get_controle_areas(self):
        return self.controle_areas

    def get_cadastro_veiculos(self):
        return self.cadastro_veiculos

    def get_cadastro_ocorrencias(self):
        return self.cadastro_ocorrencias

    def get_categorias(self):
        return self.categorias

    def get_relatorio_entradas(self):
        return self.relatorio_entradas

    def get_relatorio_status(self):
        return self.relatorio_status

    def get_cadastro_usuario(self):
        return self.cadastro_usuario

    def get_controle_eventos(self):
        return self.controle_eventos

    #METODOS RELACIONADOS A CATEGORIAS
    def adicionar_categoria(self, categoria):
        self.categorias.append(categoria.upper())

    def validar_cetegoria(self, categoria):
        if categoria.upper() not in self.categorias:
            print("Categoria inválida! A categoria deve ser uma dessas opções:  ", self.categorias)
            categoria = input("Insira a categoria: ").upper()
            return categoria


    # METODOS RELACIONADOS A VEICULOS
    def cadastrar_veiculo(self, nome, matricula, curso, placa, modelo, categoria):
        prop = Proprietario(nome, matricula, curso)
        veic = Veiculo(prop, placa, modelo, categoria)
        self.cadastro_veiculos.append(veic)

    def validar_veiculo(self, placa):
        for veiculo in self.cadastro_veiculos:
            if placa.upper() == veiculo.get_placa():
                return veiculo
            return None

    def remover_veiculo(self, placa):
        veiculo = self.validar_veiculo(placa.upper())
        self.cadastro_veiculos.remove(veiculo)

    def validar_entrada(self, placa):
        pass #aquivou precisar da classe area pra finalizar

    def validar_saida(self, placa):
        pass  # aquivou precisar da classe area pra finalizar


    #METODOS RELACIONADOS A USUARIOS
    def cadastrar_usuario(self,nome, cpf, funcao, setor, usuario, senha):
        user = Usuario(nome, cpf, funcao, setor, usuario, senha)
        self.cadastro_usuario.append(user)

    def validar_usuario(self, nome_usuario):
        for usuario in self.cadastro_usuario:
            if nome_usuario == usuario.get_usuario():
                return usuario
        return None

    def login(self, usuario, senha):
        user = self.validar_usuario(usuario)
        if user != None:
            if user.get_usuario() == usuario and user.get_senha() == senha:
                return True
            else:
                return False
        else:
            return False

#METODOS RELACIONADOS A ÁREAS
    def cadastrar_area(self, nome, capacidade, categoria):
        area = Areas(nome, capacidade, categoria)
        self.controle_areas.append(area)

    def ocupacao_areas(self, categoria):
        percent = 0
        area = Areas()
        for area in self.controle_areas:
            if categoria == area.getCategoria:
                quantidade = area.getVeiculos_area
                percent = (quantidade * 100 / area.getCapacidade)
        return percent

    #METODOS RELACIONADOS A OCORRÊNCIAS
    def cadastrar_ocorrencia(self, id, tipo, quantidade_veiculos, data, hora, null=None):
        ocorrencia = Ocorrencia(id, tipo, quantidade_veiculos, data, hora)
        self.cadastro_ocorrencias.append(ocorrencia)
        for  i in range(quantidade_veiculos):
            placa = input("Insira a placa da ocorrência: ")
            veiculo = self.validar_veiculo(placa)
            if veiculo != null:
                ocorrencia.adicionar_veiculo(veiculo)
            else:
                print("Veículo não cadastrado!")


    # METODOS RELACIONADOS A EVENTOS
    def cadastrar_evento(self, nome, data, duracao, vagas):
        for i in range(duracao):
            evento = Eventos(nome, data, vagas)
            self.controle_eventos.append(evento)


