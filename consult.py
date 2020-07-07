#testa o tamanho do cpf
def test_lengh(cpf):
    if len(clean_cpf(cpf)) == 11:
        return True
    else:
        return False
    

#limpa os pontos e hífens
def clean_cpf(cpf):
    cpf1 = cpf.replace('.','')
    cpf2 = cpf1.replace('-','')
    return cpf2


#compara o cpf com os dados salvos
def compare_cpf(cpf):
    data_bank = open('blacklist.txt', 'r')
    clean_list = clean_cpf(data_bank.read()) #o ideal seria deixar uma lista limpa ao invés do arquivo atual para que o peso no processamento seja menor!
    if clean_cpf(cpf) in clean_list:
        return True
    else:
        return False


#gera a resposta para a api
def response_cpf(cpf):
    if test_lengh(cpf):
        if compare_cpf(cpf):
            return 'BLOCK'
        else:
            return 'FREE'
    elif test_lengh(cpf) == False:
        return 'WRONG CPF LENGTH'
    else:
        return 'ERROR!'