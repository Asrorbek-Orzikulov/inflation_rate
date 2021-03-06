from numpy import nan

convert_dict = {
    'Оқолтин': 'Акалтынский',
    'Оқдарё': 'Акдарьинский',
    'Оққўрғон': 'Аккурганский',
    'Олот': 'Алатский',
    'Олмазор': 'Алмазарский',
    'Олтиариқ': 'Алтыарыкский',
    'Олтинкўл': 'Алтынкульский',
    'Олтинсой': 'Алтынсайский',
    'Амударё': 'Амударьинский',
    'Ангор': 'Ангорский',
    'Андижон': 'Андижанский',
    'Арнасой': 'Арнасайский',
    'Асака': 'Асакинский',
    'Охангарон': 'Ахангаранский',
    'Қўштепа': 'Куштепинский',
    'Боғот': 'Багатский',
    'Боғдод': 'Багдадский',
    'Бойсун': 'Байсунский',
    'Балиқчи': 'Балыкчинский',
    'Бандихон': nan,
    'Бахмал': 'Бахмальский',
    'Боёвут': 'Баяутский',
    'Бекобод': 'Бекабадский',
    'Бектемир': 'Бектемирский',
    'Беруний': 'Берунийский',
    'Бешариқ': 'Бешарыкский',
    'Бўзатов': nan,
    'Бўстон': 'Бозский',
    'Бўстонлиқ': 'Бостанлыкский',
    'Бувайда': 'Бувайдинский',
    'Бўка': 'Букинский',
    'Булоқбоши': 'Булакбашинский',
    'Булунғур': 'Булунгурский',
    'Бухоро': 'Бухарский',
    'Вобкент': 'Вабкентский',
    'Олмалиқ ш.': 'г.Алмалык',
    'Ангрен ш.': 'г.Ангрен',
    'Андижон ш.': 'г.Андижан',
    'Охангарон ш.': 'г.Ахангаран',
    'Бекобод ш.': 'г.Бекабад',
    'Бухоро ш.': 'г.Бухара',
    'Гулистон ш.': 'г.Гулистан',
    'Жиззах ш.': 'г.Джизак',
    'Зарафшон ш.': 'г.Заpафшан',
    'Когон': 'г.Каган',
    'Қарши ш.': 'г.Карши',
    'Каттақўрғон ш.': 'г.Каттакурган',
    'Қўқон ш.': 'г.Коканд',
    'Қувасой ш.': 'г.Кувасай',
    'Марғилон ш.': 'г.Маpгилан',
    'Навоий ш.': 'г.Навои',
    'Наманган ш.': 'г.Наманган',
    'Нукус ш.': 'г.Нукус',
    'Нурафшон ш.': 'г.Нурафшон',
    'Самарканд ш.': 'г.Самарканд',
    'Термез ш.': 'г.Термез',
    'Урганч ш.': 'г.Ургенч',
    'Фарғона ш.': 'г.Фергана',
    'Хонобод ш.': 'г.Ханабад',
    'Хива ш.': 'г.Хивинский',
    'Чиpчиқ ш.': 'г.Чиpчик',
    'Шахрисабз ш.': 'Шахрисабзский',
    'Шиpин ш.': 'г.Шиpин',
    'Янгиеp ш.': 'г.Янгиеp',
    'Янгийўл ш.': 'г.Янгиюль',
    'Ғаллаорол': 'Галляаральский',
    'Ғиждувон': 'Гиждуванский',
    'Ғузор': 'Гузарский',
    'Гулистон': 'Гулистанский',
    'Гурлан': 'Гурленский',
    'Данғара': 'Дангаринский',
    'Денов': 'Денауский',
    'Дехқонобод': 'Дехканабадский',
    'Жалақудуқ': 'Жалакудукский',
    'Жомбой': 'Джамбайский',
    'Жарқўрғон': 'Джаркурганский',
    'Жиззах': 'Шароф Рашидовский',
    'Дўстлик': 'Дустликский',
    'Жондор': 'Жондоpский',
    'Зомин': 'Зааминский',
    'Зангиота': 'Зангиатинский',
    'Зарбдор': 'Зарбдарский',
    'Зафаробод': 'Зафарабадский',
    'Избоскан': 'Избасканский',
    'Иштихон': 'Иштыханский',
    'Когон ш.': 'Каганский',
    'Қамаши': 'Камашинский',
    'Конимех': 'Канимехский',
    'Қонликўл': 'Канлыкульский',
    'Қоракўл': 'Каракульский',
    'Қораўзак': 'Караузякский',
    'Қоровул-бозор': 'Караулбазарский',
    'Кармана': 'Карманинский',
    'Қарши': 'Каршинский',
    'Косонсой': 'Касансайский',
    'Косон': 'Касанский',
    'Касби': 'Касбинский',
    'Каттақўрғон': 'Каттакурганский',
    'Кегейли': 'Кегейлийский',
    'Қибрай': 'Кибрайский',
    'Қизириқ': 'Кизирикский',
    'Китоб': 'Китабский',
    'Қўшкўпир': 'Кошкупырский',
    'Қўшработ': 'Кошрабадский',
    'Қува': 'Кувинский',
    'Қуйичирчиқ': 'Куйичирчикский',
    'Қумқўрғон': 'Кумкурганский',
    'Қўнғирот': 'Кунградский',
    'Қўрғонтепа': 'Кургантепинский',
    'Қизилтепа': 'Кызылтепинский',
    'Мархамат': 'Мархаматский',
    'Мингбулоқ': 'Мингбулакский',
    'Миробод': 'Мирабадский',
    'Мирзаобод': 'Мирзаабадский',
    'Мирзачўл': 'Мирзачульский',
    'Мирзо-Улуғбек': 'Мирзо-Улугбекский',
    'Миришкор': 'Миришкорский',
    'Муборак': 'Мубарекский',
    'Музработ': 'Музрабадский',
    'Мўйноқ': 'Муйнакский',
    'Навбахор': 'Навбахорский',
    'Наманган': 'Наманганский',
    'Нарпай': 'Нарпайский',
    'Норин': 'Нарынский',
    'Нишон': 'Нишанский',
    'Нукус': 'Нукусский',
    'Нуробод': 'Нурабадский',
    'Нурота': 'Нуратинский',
    'Пайариқ': 'Пайарыкский',
    'Поп': 'Папский',
    'Паркент': 'Паркентский',
    'Пастдарғом': 'Пастдаргомский',
    'Пахтаобод': 'Пахтаабадский',
    'Пахтакор': 'Пахтакорский',
    'Пахтачи': 'Пахтачийский',
    'Пешку': 'Пешкунский',
    'Пискент': 'Пскентский',
    'Риштон': 'Риштанский',
    'Ромитан': 'Ромитанский',
    'Сайхунонбод': 'Сайхунабадский',
    'Самарқанд': 'Самаркандский',
    'Сардоба': 'Сардобский',
    'Сариосиё': 'Сариасийский',
    'Сергели': 'Сергелийский',
    'Сўх': 'Сохский',
    'Сирдарё': 'Сырдарьинский',
    'Тайлоқ': 'Тайлякский',
    'Томди': 'Тамдынский',
    'Тахиатош': nan,
    'Тахтакўпир': 'Тахтакупырский',
    'Тошкент': 'Ташкентский',
    'Тошлоқ': 'Ташлакский',
    'Термиз': 'Термезский',
    'Тупроққала': nan,
    'Тўрақўрғон': 'Туракурганский',
    'Тўрткўл': 'Турткульский',
    'Ўзбекистон': 'Узбекистанский',
    'Узун': 'Узунский',
    'Уйчи': 'Уйчинский',
    'Улуғнор': 'Улугноpский',
    'Урганч': 'Ургенчский',
    'Ургут': 'Ургутский',
    'Ўртачир-чиқ': 'Уртачирчикский',
    'Учқудуқ': 'Учкудукский',
    'Учкўприк': 'Учкуприкский',
    'Учқўрғон': 'Учкурганский',
    'Учтепа': 'Учтепинский',
    'Фориш': 'Фаришский',
    'Фарғона': 'Ферганский',
    'Фурқат': 'Фуркатский',
    'Ховос': 'Хавасский',
    'Хазорасп': 'Хазараспский',
    'Хонқа': 'Ханкинский',
    'Хатирчи': 'Хатырчинский',
    'Хива': 'Хивинский',
    'Хўжаобод': 'Ходжаабадский',
    'Хўжайли': 'Ходжейлийский',
    'Чортоқ': 'Чартакский',
    'Чилонзор': 'Чиланзарский',
    'Чимбой': 'Чимбайский',
    'Чиноз': 'Чиназский',
    'Чироқчи': 'Чиракчинский',
    'Чуст': 'Чустский',
    'Шовот': 'Шаватский',
    'Шайхон-тохур': 'Шайхантахурский',
    'Шофиркон': 'Шафирканский',
    'Шахрихон': 'Шахриханский',
    'Шеробод': 'Шерабадский',
    'Шуманай': 'Шуманайский',
    'Шўрчи': 'Шурчинский',
    'Элликқалъа': 'Элликкалинский',
    'Юқори-чирчиқ': 'Юкоричирчикский',
    'Юнусобод': 'Юнусабадский',
    'Ёзёвон': 'Язъяванский',
    'Яккабоғ': 'Яккабагский',
    'Яккасарой': 'Яккасарайский',
    'Янгиариқ': 'Янгиарыкский',
    'Янгибозор': 'Янгибазарский',
    'Янгиқўрғон': 'Янгикурганский',
    'Янгиобод': 'Янгиободский',
    'Янгийўл': 'Янгиюльский',
    'Яшнаобод': 'Яшнободский'
}