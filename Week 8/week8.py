from collections import namedtuple

bankaccount = namedtuple("bankaccount", ["owner_name", "branch", "bank_name", "balance"])

bank_acct_list = [bankaccount(owner_name='Hassan Statler', branch='Newport Beach', bank_name='US Bank', balance=2695), bankaccount(owner_name='Chet Bischoff', branch='Newport Beach', bank_name='Bank of America', balance=2351), bankaccount(owner_name='Damon Heier', branch='Orange', bank_name='Chase', balance=3021), bankaccount(owner_name='Eugenio Saavedra', branch='Newport Beach', bank_name='Bank of America', balance=1491), bankaccount(owner_name='Edward Wittenberg', branch='Anaheim', bank_name='Chase', balance=2731), bankaccount(owner_name='Bennett Salvia', branch='Orange', bank_name='Chase', balance=3055), bankaccount(owner_name='Gil Hendrickson', branch='Newport Beach', bank_name='Chase', balance=2021), bankaccount(owner_name='Daryl Hiatt', branch='Anaheim', bank_name='Bank of America', balance=3973), bankaccount(owner_name='Maxwell Gloster', branch='Anaheim', bank_name='Bank of America', balance=2292), bankaccount(owner_name='Desmond Vincent', branch='Orange', bank_name='Wells Fargo', balance=2288), bankaccount(owner_name='Marty Neblett', branch='Aliso Viejo', bank_name='US Bank', balance=3097), bankaccount(owner_name='Aurelio Schroeder', branch='Irvine', bank_name='Wells Fargo', balance=2794), bankaccount(owner_name='Lucio Semmes', branch='Irvine', bank_name='Wells Fargo', balance=2326), bankaccount(owner_name='Duncan Dorr', branch='Aliso Viejo', bank_name='Wells Fargo', balance=1878), bankaccount(owner_name='Fred Pecora', branch='Irvine', bank_name='US Bank', balance=2438), bankaccount(owner_name='Ian Ulloa', branch='Orange', bank_name='Chase', balance=2672), bankaccount(owner_name='Gerardo Crow', branch='Newport Beach', bank_name='Chase', balance=2538), bankaccount(owner_name='Ken Teaster', branch='Orange', bank_name='Chase', balance=3653), bankaccount(owner_name='Lanny Brinker', branch='Orange', bank_name='Wells Fargo', balance=2790), bankaccount(owner_name='Percy Atkison', branch='Orange', bank_name='Bank of America', balance=2902), bankaccount(owner_name='Virgil Steed', branch='Aliso Viejo', bank_name='Bank of America', balance=2915), bankaccount(owner_name='Arnold Paton', branch='Irvine', bank_name='US Bank', balance=2880), bankaccount(owner_name='Alonzo Hover', branch='Orange', bank_name='Bank of America', balance=3072), bankaccount(owner_name='Huey Predmore', branch='Newport Beach', bank_name='Wells Fargo', balance=2279), bankaccount(owner_name='Otto Furness', branch='Newport Beach', bank_name='Wells Fargo', balance=2176), bankaccount(owner_name='Michale Doles', branch='Aliso Viejo', bank_name='Chase', balance=1915), bankaccount(owner_name='Rashad Miguez', branch='Irvine', bank_name='Wells Fargo', balance=2820), bankaccount(owner_name='Samuel Bundrick', branch='Anaheim', bank_name='Wells Fargo', balance=3102), bankaccount(owner_name='Lenard Parry', branch='Newport Beach', bank_name='Wells Fargo', balance=2853), bankaccount(owner_name='Willie Stutes', branch='Aliso Viejo', bank_name='Bank of America', balance=2482), bankaccount(owner_name='Paris Ziemer', branch='Anaheim', bank_name='Wells Fargo', balance=2431), bankaccount(owner_name='Phillip Echevarria', branch='Orange', bank_name='Chase', balance=2634), bankaccount(owner_name='Solomon Seda', branch='Irvine', bank_name='Wells Fargo', balance=2821), bankaccount(owner_name='Jae Akerley', branch='Irvine', bank_name='Chase', balance=3260), bankaccount(owner_name='Garland Roehl', branch='Newport Beach', bank_name='US Bank', balance=1672), bankaccount(owner_name='Chase Coate', branch='Irvine', bank_name='Bank of America', balance=3122), bankaccount(owner_name='Dudley Jared', branch='Los Angeles', bank_name='Bank of America', balance=3143), bankaccount(owner_name='Mario Sollars', branch='Orange', bank_name='Chase', balance=3432), bankaccount(owner_name='Beau Chalfant', branch='Los Angeles', bank_name='Wells Fargo', balance=2869), bankaccount(owner_name='Lawrence Immel', branch='Orange', bank_name='Wells Fargo', balance=3029), bankaccount(owner_name='Derek Gress', branch='Los Angeles', bank_name='Wells Fargo', balance=2121), bankaccount(owner_name='Dario Breton', branch='Newport Beach', bank_name='Bank of America', balance=2476), bankaccount(owner_name='Cedric Myrie', branch='Anaheim', bank_name='Bank of America', balance=2816), bankaccount(owner_name='Rex Amero', branch='Orange', bank_name='Wells Fargo', balance=1841), bankaccount(owner_name='Harris Martinez', branch='Irvine', bank_name='Chase', balance=2709), bankaccount(owner_name='Rogelio Stuck', branch='Aliso Viejo', bank_name='Chase', balance=2745), bankaccount(owner_name='Erwin Hickok', branch='Anaheim', bank_name='Bank of America', balance=3460), bankaccount(owner_name='Cristobal Halliwell', branch='Newport Beach', bank_name='US Bank', balance=3195), bankaccount(owner_name='Tyrone Swoboda', branch='Irvine', bank_name='Bank of America', balance=2805), bankaccount(owner_name='Jude Olmo', branch='Los Angeles', bank_name='Chase', balance=3187), bankaccount(owner_name='Kymberly Sunseri', branch='Aliso Viejo', bank_name='Wells Fargo', balance=3100), bankaccount(owner_name='Trudy Minnick', branch='Newport Beach', bank_name='Wells Fargo', balance=3399), bankaccount(owner_name='Mirna Husband', branch='Newport Beach', bank_name='US Bank', balance=2560), bankaccount(owner_name='Bao Yeaton', branch='Newport Beach', bank_name='US Bank', balance=2065), bankaccount(owner_name='Meghann Stahl', branch='Newport Beach', bank_name='Wells Fargo', balance=2582), bankaccount(owner_name='Irish Hallinan', branch='Aliso Viejo', bank_name='US Bank', balance=2758), bankaccount(owner_name='Thomasine Delmont', branch='Anaheim', bank_name='Wells Fargo', balance=3381), bankaccount(owner_name='Myrtis Bogner', branch='Los Angeles', bank_name='Wells Fargo', balance=3435), bankaccount(owner_name='Christie Hamm', branch='Newport Beach', bank_name='Chase', balance=2967), bankaccount(owner_name='Rosalee Mcadoo', branch='Orange', bank_name='US Bank', balance=2015), bankaccount(owner_name='Katelin Edney', branch='Los Angeles', bank_name='Bank of America', balance=3349), bankaccount(owner_name='Madalyn Conrad', branch='Los Angeles', bank_name='Wells Fargo', balance=3542), bankaccount(owner_name='Britteny Zayas', branch='Anaheim', bank_name='Wells Fargo', balance=2852), bankaccount(owner_name='Eulalia Mckean', branch='Irvine', bank_name='Bank of America', balance=3197), bankaccount(owner_name='Beverley Stricklin', branch='Los Angeles', bank_name='Wells Fargo', balance=2704), bankaccount(owner_name='Maye Boster', branch='Newport Beach', bank_name='US Bank', balance=2110), bankaccount(owner_name='Christel Schulze', branch='Orange', bank_name='Chase', balance=2742), bankaccount(owner_name='Halley Madsen', branch='Newport Beach', bank_name='Chase', balance=2040), bankaccount(owner_name='Zana Adolph', branch='Newport Beach', bank_name='US Bank', balance=2832), bankaccount(owner_name='Kate Ayars', branch='Anaheim', bank_name='Bank of America', balance=3364), bankaccount(owner_name='Linn Beers', branch='Los Angeles', bank_name='Bank of America', balance=3072), bankaccount(owner_name='Kyra Busbee', branch='Newport Beach', bank_name='Chase', balance=2975), bankaccount(owner_name='Hang Scarboro', branch='Irvine', bank_name='Chase', balance=2710), bankaccount(owner_name='Mammie Rodrick', branch='Orange', bank_name='Wells Fargo', balance=2004), bankaccount(owner_name='Catalina Zackery', branch='Irvine', bank_name='Wells Fargo', balance=2588), bankaccount(owner_name='Loan Scholl', branch='Irvine', bank_name='Bank of America', balance=3474), bankaccount(owner_name='Trang Krupp', branch='Aliso Viejo', bank_name='Chase', balance=3260), bankaccount(owner_name='Kaleigh Deering', branch='Los Angeles', bank_name='US Bank', balance=2690), bankaccount(owner_name='Almeta Housley', branch='Irvine', bank_name='Bank of America', balance=2777), bankaccount(owner_name='Evalyn Bechtold', branch='Irvine', bank_name='US Bank', balance=2699), bankaccount(owner_name='Elvina Rainer', branch='Los Angeles', bank_name='Wells Fargo', balance=3718), bankaccount(owner_name='Nadia Moretti', branch='Newport Beach', bank_name='Wells Fargo', balance=3129), bankaccount(owner_name='Alexandria Necessary', branch='Irvine', bank_name='US Bank', balance=3383), bankaccount(owner_name='Gwenda Adkinson', branch='Irvine', bank_name='US Bank', balance=3180), bankaccount(owner_name='Tashia Nevius', branch='Irvine', bank_name='US Bank', balance=2155), bankaccount(owner_name='Ronna Caraballo', branch='Irvine', bank_name='US Bank', balance=2997), bankaccount(owner_name='Nia Muldowney', branch='Orange', bank_name='Wells Fargo', balance=2382), bankaccount(owner_name='Charlesetta Berrey', branch='Irvine', bank_name='Chase', balance=2731), bankaccount(owner_name='Jenelle Tuller', branch='Irvine', bank_name='Wells Fargo', balance=3264), bankaccount(owner_name='Rebeca Almeda', branch='Irvine', bank_name='Bank of America', balance=2071), bankaccount(owner_name='Araceli Gangestad', branch='Irvine', bank_name='Bank of America', balance=3703), bankaccount(owner_name='Tomeka Peffer', branch='Orange', bank_name='Chase', balance=2169), bankaccount(owner_name='Yuonne Zurita', branch='Anaheim', bank_name='Wells Fargo', balance=2932), bankaccount(owner_name='Lizabeth Skeens', branch='Los Angeles', bank_name='US Bank', balance=4046), bankaccount(owner_name='Suzan Chappel', branch='Newport Beach', bank_name='US Bank', balance=3208), bankaccount(owner_name='Marisela Feinstein', branch='Aliso Viejo', bank_name='Chase', balance=2333), bankaccount(owner_name='Camille Hessel', branch='Irvine', bank_name='Chase', balance=3523), bankaccount(owner_name='Golden Santora', branch='Newport Beach', bank_name='US Bank', balance=3755), bankaccount(owner_name='Vikki Spadoni', branch='Newport Beach', bank_name='Wells Fargo', balance=3584), bankaccount(owner_name='Marylou Eastham', branch='Irvine', bank_name='US Bank', balance=2134)]

