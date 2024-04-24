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
[attributeName]:not([attributeName='attributeValue'])  -> Encontrando elementos que possuem o atributo attributeName e que o attributeName é diferente de 'attributeValue1'


'''

    