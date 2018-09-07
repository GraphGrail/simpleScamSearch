Класс для оценки уровня скамности текста назвается SimpleScamSearcher. Его функция documentScamLevel возвращает вещественное число - уровень скамности, если он больше 1.0, то считаем текст скамом.
Этот класс является обёрткой для класса ScamEvaluation (собственно класс SimpleScamSearcher предназначен, чтобы вообще ничего не настраивать, создать его и использовать)
В классе ScamEvaluation определение того является ли текст скамным происходит двумя способами:
1) мошенники для того, чтобы обойти системы анализа текста вставляют вместо латинских букв, символы которые выглядят очень на них похожими. Была мысль, что если искать тексты, где в токене есть сочетание латинских букв и данных символов, то это скам. Я думал таких комментариев будет не много, но их из 130 тысяч твитов чуть более 11 тысяч, что много, надо как-то это подкорректировать (возможно смотреть на количество слов с этими символами). Тем не менее в этих 11 тысячах прилично скама, но далеко не всё. 
Проверка данным способом осуществляется функцией _checkConfusionBetweenLatinLettersAndSpecialSymbols (класс ScamEvaluation)
2) поиск ключевых фраз в тексте осуществляется функцией _scamLevelByKeyPhrases (класс ScamEvaluation). Класс, непосредственно производящий поиск фразы в тексте - Collocation

Ключевые фразы задаются в методе __init__ класса SimpleScamSearcher

В классе Collocation есть проблема, которую я не успеваю поправить. Этот класс может искать фразу как последовательность слов с учётом их порядка и без его учёта (тоесть просто искать заданный набор слов в тексте). За поиск без учёта порядка отвечает функция _findCollocationInDiapasonWithoutOrderRespect, я сегодня понял что своял фигню, её нужно переделать .пока я просто добавил в метод __init__ класса SimpleScamSearcher разные сочетания ключевых фраз.

В классе Collocation можно включать режим поиска без учёта порядка и отключать его функцией setOrderRespect.
Также можно задать количество токенов, которые могут быть между словами из ключевой фразы методом setMaxDistance (например если задать 1, то между словами из ключевой фразы может быть один токен).
