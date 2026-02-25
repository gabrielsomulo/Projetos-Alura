programa {
  funcao inicio() {
    real km, taxa
    caracter chuva


    escreva("Insira a kilometragem, e se está chovendo: \n")
    leia(km, chuva)

    se (km < 5){
      taxa = 5
    }
    senao se (km >= 5 ou km <= 10){
      taxa = 10
    }
    senao{
      taxa = 15
    }

    se(chuva == 's'){
      taxa += 2
    }

    escreva(taxa)
  }
}
