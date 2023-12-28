# from textblob import TextBlob

# class AnalizadorDeSentimientos:
#     def analizar_sentimiento(self,texto):
#         analisis = TextBlob(texto)
#         if analisis.sentiment.polarity > 0:
#             return "positivio"
#         elif analisis.sentiment.polarity ==0:
#             return "Neutral"
#         else:
#             return "negativo"

# analizador = AnalizadorDeSentimientos()
# resultado = analizador.analizar_sentimiento("hello im bad")
# print(resultado)

import openai

openai.api_key = open