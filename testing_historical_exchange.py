# import the library
from appJar import gui

#Setando variavel para ver se o input ja foi salvo no arquivo
repetido = False

# handle button events
def press(button):
   repetido = False
   #Setando contadores de nucleotidios
   acount = 0
   ccount = 0
   gcount = 0
   tcount = 0
   ucount = 0
   #Setando variaveis para indentificacao se e um dna ou rna
   dna = False
   rna = False
   transposed = ""
   #Se o botao apertado == cancel, sair do appjar
   if button == "Cancel":
       app.stop()
   else:
       #Pegar input do usuario para analise posterior
        inputuser = app.getEntry("Input")
        #Loop para contar quantos nucleotidios de cada na string de input
        for char in inputuser:
            #Se tiver um U, setar RNA como true
            if char == "u":
                if not rna:
                    rna = True
                ucount = ucount + 1
            #Se tiver um T, setar DNA como true
            if char == "t":
                if not dna:
                    dna = True
                tcount = tcount + 1
            if char == "a":
                acount = acount + 1
            if char == "g":
                gcount = gcount + 1
            if char == "c":
                ccount = ccount + 1

        if dna:
            #Transformar dna em mrna utilizando a funcao .replace
            transposed = inputuser.replace("t", "u")
            #criando mensagem de resposta
            msg = "  A: " + str(acount) + "  C: " + str(ccount)
            msg = msg + "  G: " + str(gcount) + "  T:" + str(tcount)
            msg = msg + "\n" + "Transposta: " + transposed
        if rna:
            transposed = inputuser.replace("u", "t")
            msg = "  A: " + str(acount) + "  C: " + str(ccount)
            msg = msg + "  G: " + str(gcount) + "  U:" + str(ucount)
            msg = msg + "\n" + "Transposta: " + transposed
        #abrindo arquivo no modo de leitura e escrita
        f = open("backup.txt", "r+")
        #lendo linhas individuais do arquivo como lista de linhas
        data = f.readlines()
        #colocar quebra de linha no final do input para salvar no arquivo
        inputuser = inputuser + "\n"
        #Loop para ler cada linha do arquivo
        for line in data:
            #comparando linhas com input, se houver alguma igual, setar repetido
            if line == inputuser:
                repetido = True
        #Se nao ouver o input dentro do arquivo, escrever nova linha no arquivo
        if repetido == False:
            f.write(inputuser)
        #fechando o arquivo
        f.close()
        #abrir um popup com mensagem de resultado criada
        app.infoBox("Resultado", msg, parent=None)

# create a GUI variable called app
app = gui("Calcifer", "400x200")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Calcifer - Ferramenta para DNA e RNA")

app.addLabelEntry("Input")

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)

app.setFocus("Input")

# start the GUI
app.go()
