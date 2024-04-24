'''
page.locator('Css Locator')

tagname -> Encontrando elemento por tag
#idValue -> Encontrando elemento por id (id simples)
.classValue -> Encontrando elemento por classe que possui o termo classValue
.classValue1.classValue2 -> Encontrando elemento por classe que possui os termos classValue1 e classValue2
tagname#idValue.classValue ou tagname.classValue#idValue-> Encontrando elementos que possuem a tagname, o idValue e o classValue ao mesmo tempo.
tagname[attributeName='attributeValue'] -> Fórmula Geral do Css Selector
tagname[attributeName1='attributeValue1'][attributeName2='attributeValue2'] -> Encontrando elementos por quaisquer dois atributos diferentes

[attributeName='attributeValue'] -> Omitir a tagname se ela não for relevante
[attributeName1='attributeValue1'], [attributeName2='attributeValue2'] -> Encontrando elementos que possuem um ou outro atributo.
[attributeName1='attributeValue1']:not([attributeName2='attributeValue2'])  -> Encontrando elementos que possui attributeName1='attributeValue1' e que não possui attributeName2='attributeValue2'
[attributeName]:not([attributeName='attributeValue'])  -> Encontrando elementos que possuem o atributo attributeName e que o attributeName é diferente de 'attributeValue'

tagname[attributeName$='valor final de attributeValue']
tagname[attributeName^='valor inicial de attributeValue']
tagname[attributeName*='valor contido em attributeValue']

> -> Filhos  
:first-child -> Elementos que são os primeiros filhos de seus pais
:last-child -> Elementos que são os últimos fihos de seus pais
:nth-child(number) -> Elementos que são os filhos de posição number de seus pais, começando do primeiro filho -> Base 1
:nth-last-child(number) -> Elementos que são os filhos de posição number de seus pais, começando do último filho
+ -> Primeiro irmão para frente  (necessariamente tem que ser o irmão adjacente)
~ -> Irmãos para frente 

space ou >> -> Descendentes
>> nth=number-1 -> Elementos de posição number de seu tipo (podem estar em qualquer lugar, não precisa serem irmãos) -> Base 0
:nth-match(cssvalue, number) -> Elementos de posição number de seu tipo (podem estar em qualquer lugar, não precisa serem irmãos) -> Base 1
:has(cssvalue) -> Elementos que contém locators específicos (em seus descendentes)

:text-is('Texto') -> Elementos cujo seu texto exato é 'Texto'
:text('Texto')  -> Elementos cujo seu texto possui o termo 'Texto'
:has-text('Texto') -> Elementos cujo seu texto ou de seus descendentes possui o termo 'Texto'
Obs: elementos input de type 'button' ou 'submit' são encontrados, em todos os casos de localização pelo texto, pelo seu atributo 'value' no lugar do seu texto.

Exemplos de User Facing Attributes:
td:has-text('Nome:') + td > input
td:has-text('Organização:') + td > input
[placeholder='Digite sua Organização']
td:has-text('Masculino') > input
:text-is('Dropdown')
tr:has-text('Links Interessantes:') + tr >> button

Localizando elementos pelo layout:
:right-of(cssvalue) -> Elementos à direita do elemento identificado por cssvalue
:left-of(cssvalue) -> Elementos à esquerda do elemento identificado por cssvalue
:above(cssvalue) -> Elementos acima do elemento identificado por cssvalue
:below(cssvalue) -> Elementos abaixo do elemento identificado por cssvalue
:near(cssvalue) -> Elementos próximos do elemento identificado por cssvalue

Exemplos:
input:right-of(:text-is('Nome:')) >> nth=0
input:left-of(:text-is(' Masculino')) >> nth=0
input:above(:text-is('Organização:')) >> nth=0
button:below(:text-is(' Links Interessantes:'))
input:near(:text-is('Nome:')) >> nth=0

'''

    