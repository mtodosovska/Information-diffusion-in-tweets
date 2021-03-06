# Information-diffusion-in-tweets
Analysing the difference between diffusion of information between positive and negative tweets.


## Problem discription
The goal of this project is to show the different ways in which diffusion happens between positive and negative information through analysis of the different ways in which tweets spread depending on whether their sentiment is positive or negative. Towards this goal, we analysed the tweets in our dataset from two perspectives:
* Quantitatively: average number of retweets and faves normalised by the number of followers for every users, the average number of steps of propagation of tweets, average and total number of followers of the users who posted them, etc
* Temporally: the time of posting of the first retweet and number of retweets during X amount of hours. From this data we extracted statistics about the way tweets spread temporally: the shortest time of retweeting in every category, maximum number of retweets of every category, a maximum number of categories during 1 hour and 24 hours, etc.

## Conclusion
The short conclusion of this analysis is that on average positive tweets are retweeted more, and reach further. However, if the raw numbers are looked at we can conclude that there is a higher total number of retweets and favourites for negative tweets. This indicates that the volume of negative tweets is bigger, even though a positive tweet carries a bigger value for effort. 


## Опис на проблемот
Целта на овој проект беше да се покаже различниот начин на кој постои дифузија на информациите помеѓу позитивни и негативни информации, односно, различниот начин на кој се шират твитовите на Твитер во зависност од тоа дали се позитивни или негативни. За оваа цел, ние ги анализиравме твитовите од нашето податочно множество од два аспекти:
* Квантитативен аспект: оваа анализа вклучуваше наоѓање на просечниот број на retweets и faves нормализирани по бројот на следачи за секој корисник, вкупниот број на retweets и faves, просечниот број на чекори на пропагација на некој твит, просечниот и вкупниот број на следачи кои ги имаат корисниците кои ги постирале твитовите.
* Временски аспект : со овој аспект ги анлизиравме времето на објавување на првиот retweet (под услов да бил ретвитнат твиот) и наоѓање на број на retweets  за Х часови. Потоа од овие податоци ги издвоивме најкрaткото време на објавување retweet на секоја категорија како и максимум retweets по категорија за време од 1 час и 24 часа.



## Податоци
Податоците кои ги искористивме беа дел од податочното множество Tweets annotated for sentiment and stance towards pre-chosen targets [1]. Oва податочно множество содржи податоци лабелирани според тоа дали содржат позитивен, негативен или неутрален став спрема одредена личност или тема. Податочното множество содржи вкупно 4870 твитови, кои се однесуваат на следните теми или личности: атеизам, загриженост за климатските промени, Доналд Трамп, феминистичкото движење, Хилари Клинтон, и легализација на абортусот. Ова податочно множество било искористено како официјално множество за тренирање и тестирање на SemEval-2016 на споделената задача „Детекција на став во твитови“ (Detecting Stance in Tweets (Task 6)).
Податоците во ова податочно множество се поделени во четири групи, од кои секоја содржи по 2 датотеки, првата ги содржи: текстот на твитот, целта на твитот, дали ставот е позитивен, негативен или неутрален, и мислењето на оценувачот за сентиментот на твитот. Втората датотека содржи мапирање кон id-то на секој твит. Id-то е значајно заради тоа што може да се искористи со цел да се добијат дополнителни информации за самиот твит, како и за личноста која го напишала.


## Методи

### Структурирање на податоците
Првиот чекор кон решението кое го замисливме беше тоа да ги структурираме податоците на начин на кој ќе можеме да ги процесираме. Како што беше кажано погоре, податочното множество се состои од 4 групи на податоци кои содржат по 2 датотеки. Прво, ги поврзавме датотеките од секоја група меѓусебно. По ова, ги поврзавме сите групи заедно. Со ова добивме еден фајл кој го содржи, за нас, значајните информации за секој твит: Id, став, и текст на твитот. 
Следниот чекор беше да се соберат другите потребни информации за секој твит: листа на retweets, timestamp, faves, и број на следачи на корисникот кој го постирал твитот. За да ги добиеме овие податоци ние го искористивме Twitter API-то tweepy. Со цел да можеме да добиеме податоци од Твитер, прво, беше потребно да креираме Твитер апликација, со која беа генерирани сигурносни токени (consumer_token, consumer_secret, access_token, access_token_secre), кои АПИ-то ги користи за автентикација. tweepy има релативно едноставен интерфејс за повлекување на податоците. Покрај ова, единствената потешкотија со која се соочивме беше фактот што Твитер поставува ограничување за повлекување на најмногу 15 твита на секои 15 минути.

Понатаму врз овие новодобиени податоци изведовме статистички анализи со цел да ги добиеме потребните податоци за да ја извршиме конечната анализа.

## Резултати
Резултатите кои се однесуваат на квантитативната анализа се следните: 

* Просечен број на retweets:
	* Positive: 0.799086757991
	* Negative: 0.757211538462
	* Neutral:  0.254545454545

Од овие резултати може да ги донесеме следните заклучоци: просечниот број на позитивни retweets e поголем од просечниот број на негативни. 

* Просечен број на retweets нормализиран според бројот на следачи:
	* Positive: 0.000790697405863
	* Negative: 0.00311153474396
	* Neutral 0.000194208870525

* Просечен број на favuourites:
	* Positive: 1.17351598174
	* Negative: 1.51923076923
	* Neutral 0.581818181818	

* Просечен број на favuourites според бројот на следачи:
	* Positive: 0.00478023983167
	* Negative: 0.00227974375056
	* Neutral 0.00144415401185

* Просечен број на чекори на пропагација на твитот:
	* Positive: 0.24200913242
	* Negative: 0.209134615385
	* Neutral 0.181818181818

* Просечен број на следачи:
	* Positive: 9893.21004566
	* Negative: 4289.38221154
	* Neutral 2895.12727273

* Вкупен број на retweets:
	* Positive: 175.0
	* Negative: 315.0
	* Neutral 14.0

* Вкупен број на retweets нормализиран според бројот на следачи:
	* Positive: 0.173162731884
	* Negative: 1.29439845349
	* Neutral 0.0106814878789

* Вкупен број на favourites:
	* Positive: 257.0
	* Negative: 632.0
	* Neutral 32.0

* Вкупен број на favourites нормализиран според бројот на следачи:
	* Positive: 1.04687252313
	* Negative: 0.948373400234
	* Neutral 0.0794284706519

* Вкупен број на чекори на пропагација на твитовите:
	* Positive: 53.0
	* Negative: 87.0
	* Neutral 10.0

## Референци
[1] Mohammad, Saif, et al. "A Dataset for Detecting Stance in Tweets." LREC. 2016.
