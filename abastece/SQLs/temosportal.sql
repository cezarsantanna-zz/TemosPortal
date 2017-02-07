--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.1
-- Dumped by pg_dump version 9.6.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

--
-- Data for Name: abastece_employee; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY abastece_employee (id, active, name) FROM stdin;
10	t	Raphael
9	t	Wellington
8	t	Vitor
7	t	Adélio
6	t	Roberto
4	t	Weslei
2	t	Alex
1	t	Renan
5	t	Matheus
3	t	Ítalo
\.


--
-- Data for Name: abastece_modeloviatura; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY abastece_modeloviatura (id, active, name, km_rev) FROM stdin;
1	t	HR	10000
2	t	Saveiro	10000
\.


--
-- Data for Name: abastece_viatura; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY abastece_viatura (id, active, placa, celular, coordx, coordy, quilometragem, employee_id, modeloviatura_id) FROM stdin;
1	t	PYF9835	1	1	1	0	8	2
2	t	PYF9836	1	1	1	0	7	2
3	t	GIL7206	1	1	1	0	9	2
4	t	GJD1194	1	1	1	0	10	2
5	t	GKI2072	1	1	1	0	5	2
6	t	FRG8831	1	1	1	0	1	1
7	t	FRS0679	1	1	1	0	6	1
8	t	FZB8670	1	1	1	0	4	1
9	t	FWO8127	1	1	1	0	3	1
10	t	FJM0589	1	1	1	0	2	1
\.


--
-- Data for Name: abastece_warehouse; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY abastece_warehouse (id, active, name) FROM stdin;
1	t	E2i9 - Central
2	t	E2i9 - SP01
3	t	E2i9 - SP02
4	t	E2i9 - SP03
5	t	E2i9 - SP04
6	t	E2i9 - SP05
7	t	E2i9 - SP06
8	t	E2i9 - SOR01
10	t	E2i9 - PR01
11	t	E2i9 - RJ01
9	t	E2i9 - SP07
13	t	Sem Parar
14	t	Perdas
15	t	Posto Shell Ramal
16	t	Posto Shell Orion
17	t	Posto Shell Atlantica
18	t	Posto Shell Agua Espraiada
19	t	Posto Shell Abraao de Morais
20	t	Posto Shell Rimacris
21	t	Posto Shell Hawai
22	t	Posto Shell Napoleão Barros
23	t	Posto Shell Ralpha
24	t	Posto Shell Estacao Carandiru
25	t	Posto Shell Caetano Alvares
26	t	Posto Shell Bristol
27	t	Posto Shell Catalao
28	t	Posto Shell Portal Leste
29	t	Posto Shell Faga e Bizarria
30	t	Posto Shell Fabio Motta Marques
31	t	Posto Shell Alpha Marte
32	t	Posto Shell Monte Carlo
33	t	Posto Shell ABV
34	t	Posto Shell Tasca
35	t	Posto Shell Batalha
36	t	Posto Shell Cote D'azur
37	t	Posto Shell Status do Panamby
38	t	Posto Shell Sao Gualter
39	t	Posto Shell Rio Grande
40	t	Posto Shell Gigante da Imigrantes
41	t	Posto Shell M.A
42	t	Posto Shell Elmar
43	t	Posto Shell Prime
44	t	Posto Shell Mascote
45	t	Posto Shell Mash
46	t	Posto Shell Gipires
47	t	Posto Shell Benets
48	t	Posto Shell Carlos Alberto Papacidero
49	t	Posto Shell Marini
50	t	Posto Shell Jardim Sao Paulo
51	t	Posto Shell Fukuya Kanemoto
52	t	Posto Shell Galena
53	t	Posto Shell Lutaif
54	t	Posto Shell Bellagio
55	t	Posto Shell JJ
56	t	Posto Shell Summer
57	t	Posto Shell Francisco Morato
58	t	Posto Shell BAP
59	t	Posto Shell Independencia do cambuci
60	t	Posto Shell Ponto Solar
61	t	Posto Shell Via Sul
62	t	Posto Shell Vera Cruz
63	t	Posto Shell Veloz
64	t	Posto Shell Center Car
65	t	Posto Shell Moinho Velho
66	t	Posto Shell Bordo
67	t	Posto Shell Asturias
68	t	Posto Shell Macedo
69	t	Posto Shell Kll
70	t	Posto Shell Paraki
71	t	Posto Shell Oitenta
72	t	Posto Shell Tonicar
73	t	Posto Shell Agua Funda 2
74	t	Posto Shell Kobayachi
75	t	Posto Shell 45
76	t	Posto Shell Nova Itapevi
77	t	Posto Shell Nellu
78	t	Posto Shell Star Red
79	t	Posto Shell Agua funda 1
80	t	Posto Shell Turismo
81	t	Posto Shell Joinha de Guarulhos
82	t	Posto Shell Sao Joaquim
83	t	Posto Shell Via 10
84	t	Posto Shell 555
85	t	Posto Shell Alcantara
86	t	Posto Shell Cinadis
87	t	Posto Shell Tapera Grande
88	t	Posto Shell Estonia 5
89	t	Posto Shell Rede Leste
90	t	Posto Shell Sergio Motta Marques
91	t	Posto Shell Vielfe Martins
92	t	Posto Shell Fernão dias
93	t	Posto Shell Arco Verde
94	t	Posto Shell Jaguare
95	t	Posto Shell Saint Germain
96	t	Posto Shell Jardim 10
97	t	Posto Shell Ouro de barueri
98	t	Posto Shell Estonia 2
99	t	Posto Shell Marina
100	t	Posto Shell Tao Set
101	t	Posto Shell Estonia
102	t	Posto Shell Caracas Oil
103	t	Posto Shell ABD
104	t	Posto Shell Hiperpetro
105	t	Posto Shell Avenida dos estados
106	t	Posto Shell Estonia 4
107	t	Posto Shell Humaita
108	t	Posto Shell Phenix
109	t	Posto Shell Martinelli
110	t	Posto Shell 2002
111	t	Posto Shell Santa terezinha
112	t	Posto Shell CPC
113	t	Posto Shell Muraki
114	t	Posto Shell Mairipora
115	t	Posto Shell Vila rica
116	t	Posto Shell Novo Milenio
117	t	Posto Shell Estação Anchieta
118	t	Posto Shell La Caniza
119	t	Posto Shell Osasco Country
120	t	Posto Shell Rally
121	t	Posto Shell Roan
122	t	Posto Shell Recanto da seringueira
123	t	Posto Shell Nautica Frei Gaspar
124	t	Posto Shell Vanessa Santos Silva
125	t	Posto Shell Argetax Anchieta
126	t	Posto Shell Panamby
127	t	Posto Shell Tratto
128	t	Posto Shell Novo Barao 2
129	t	Posto Shell Toninho trinta
130	t	Posto Shell Estonia 3
131	t	Posto Shell Joia de Guarulhos
132	t	Posto Shell O Chefao
133	t	Posto Shell Morumbi Star
134	t	Posto Shell Veiga Filho
135	t	Posto Shell Novo Barao
136	t	Posto Shell Brilhante
137	t	Posto Shell Moraes Sales
138	t	Posto Shell Center Paraiso
139	t	Posto Shell Carlos E L Braga
140	t	Posto Shell Antonio Paes
141	t	Posto Shell Luppi
142	t	Posto Shell Ermano Marchetti
143	t	Posto Shell Isola
144	t	Posto Shell Arco Verde Cotia
145	t	Posto Shell Express Valinhos
146	t	Posto Shell Sao Conrado
147	t	Posto Shell Vida Nova
148	t	Posto Shell Lorena
149	t	Posto Shell Pole Position
150	t	Posto Shell Washington Luiz
151	t	Posto Shell Farol
152	t	Posto Shell Futuro
153	t	Posto Shell Vo Joao
154	t	Posto Shell Presidente Juscelino
155	t	Posto Shell Companheiro
156	t	Posto Shell Portal Mogi
157	t	Posto Shell Cidade Jardim Americana
158	t	Posto Shell Fenix Nova Odessa
159	t	Posto Shell Duque Berrini
160	t	Posto Shell Rebouças
161	t	Posto Shell Mara Miru
162	t	Posto Shell Zonta
163	t	Posto Shell Lavapes
164	t	Posto Shell Montana
165	t	Posto Shell Jardim colonial
166	t	Posto Shell Saci
167	t	Posto Shell SPW
168	t	Posto Shell Maranelo 2
169	t	Posto Shell Jardim do Trevo
170	t	Posto Shell Luiz Venditti
171	t	Posto Shell Tejo
172	t	Posto Shell Casa Grande
173	t	Posto Shell Mingo
174	t	Posto Shell Joruhi
175	t	Posto Shell Andorinhas
176	t	Posto Shell Progresso Mogi
177	t	Posto Shell Barbieri de Barao Geraldo
178	t	Posto Shell Luiz Fantinato Filho
179	t	Posto Shell 3M
180	t	Posto Shell Vila Pagano
181	t	Posto Shell Av Nossa Sra de Fatima
182	t	Posto Shell Savemo
183	t	Posto Shell Gaivota
184	t	Posto Shell Diesel Mac
185	t	Posto Shell Aiwa
186	t	Posto Shell Mestre
187	t	Posto Shell Novo Ouro Negro
188	t	Posto Shell Grand Prix
189	t	Posto Shell G5
190	t	Posto Shell Campineira
191	t	Posto Shell Amigao
192	t	Posto Shell Tropical Gas
193	t	Posto Shell Guarnel
194	t	Posto Shell City Cantareira
195	t	Posto Shell Formula Shell
196	t	Posto Shell Jordanopolis
197	t	Posto Shell Lubricar
198	t	Posto Shell Sol
199	t	Posto Shell Portal do Paraiso
200	t	Posto Shell EG
201	t	Posto Shell Campo limpo
202	t	Posto Shell Veneza
203	t	Posto Shell Albano
204	t	Posto Shell Riolis
205	t	Posto Shell Nova Campinas
206	t	Posto Shell BE
207	t	Posto Shell Padocka
208	t	Posto Shell Vila Galvao
209	t	Posto Shell CRS
210	t	Posto Shell Santo Eduardo
211	t	Posto Shell Carlu
212	t	Posto Shell Moni
213	t	Posto Shell Arinella Brooklin
214	t	Posto Shell Cardeal
215	t	Posto Shell Gondola
216	t	Posto Shell Mister Plus
217	t	Posto Shell Rocar
218	t	Posto Shell Duque e Cia
219	t	Posto Shell Helio Valdivia
220	t	Posto Shell Silvia Maria Pinto Santos Abastece
221	t	Posto Shell Madia
222	t	Posto Shell Castelinho
223	t	Posto Shell Bate Bola
224	t	Posto Shell Parque da Uva
225	t	Posto Shell Progresso
226	t	Posto Shell Keeper
227	t	Posto Shell Cidade Do Vinho
228	t	Posto Shell Soledade Gaucha
229	t	Posto Shell Pimenta
230	t	Posto Shell Turismo 2
231	t	Posto Shell Argetax Guarulhos
232	t	Posto Shell Andrea Santini Rego
233	t	Posto Shell Portal de Americana
234	t	Posto Shell Caxambu
235	t	Posto Shell Telles
236	t	Posto Shell Jardim Santa Monica
237	t	Posto Shell Dom Pedro I
238	t	Posto Shell Grande São Paulo
239	t	Posto Shell Bap Barão
240	t	Posto Shell Dar A
241	t	Posto Shell Abdelnor
242	t	Posto Shell Parque Villa Lobos
243	t	Posto Shell Santa Cruz de Mogi Mirim
244	t	Posto Shell Cristal
245	t	Posto Shell SS
246	t	Posto Shell Agua Branca
247	t	Posto Shell TM
248	t	Posto Shell GT
249	t	Posto Shell Algodoal
250	t	Posto Shell Dona Francisca
251	t	Posto Shell Radial Norte Sul de Piracicaba
252	t	Posto Shell Bongue
253	t	Posto Shell Maravilha
254	t	Posto Shell Presidente Ribeirao
255	t	Posto Shell Sociedade RD
256	t	Posto Shell Espaço Botanico
257	t	Posto Shell Josimar D Lourenco
258	t	Posto Shell Alcides Costa
259	t	Posto Shell Carro Nobre
260	t	Posto Shell Monaco
261	t	Posto Shell Vitrine
262	t	Posto Shell Bela Vista
263	t	Posto Shell Sao Martinho
264	t	Posto Shell Jurua
265	t	Posto Shell Piracena
266	t	Posto Shell Avenida Campinas
267	t	Posto Shell Aeroporto Limeira
268	t	Posto Shell Marun
269	t	Posto Shell Ipe
270	t	Posto Shell Quality Casablanca
271	t	Posto Shell Quality Supra
272	t	Posto Shell M Super
273	t	Posto Shell Portal Presidente
274	t	Posto Shell Alpha De Votorantim
275	t	Posto Shell Universo 2000
276	t	Posto Shell Andorinha de Rio Claro
277	t	Posto Shell Cedro
278	t	Posto Shell Abraao Ribeiro
279	t	Posto Shell Caragua
280	t	Posto Shell Pedro Lessa
281	t	Posto Shell Pontal da Cruz
282	t	Posto Shell Aeroporto de Ubatuba
283	t	Posto Shell Jupia
284	t	Posto Shell Martineli City
285	t	Posto Shell Tiger
286	t	Posto Shell Azulao
287	t	Posto Shell Quinta Avenida
288	t	Posto Shell Agronomia
289	t	Posto Shell Rede Senna
290	t	Posto Shell Lince Taubate
291	t	Posto Shell Avenida Brasil
292	t	Posto Shell Itarare Sao Vicente
293	t	Posto Shell Retiro
294	t	Posto Shell Garcia de Campinas
295	t	Posto Shell Fantinato
296	t	Posto Shell Alpes
297	t	Posto Shell Varsovia
298	t	Posto Shell Restaurante 3 Vias
299	t	Posto Shell Maricar
300	t	Posto Shell Sabella e Sabella
301	t	Posto Shell Virgilio Fernando
302	t	Posto Shell Guigui
303	t	Posto Shell Dias
304	t	Posto Shell Sabella
305	t	Posto Shell Bandeirante
306	t	Posto Shell Sete Estrelas
307	t	Posto Shell Bruno Alves Portero
308	t	Posto Shell Panamericano
309	t	Posto Shell Nelson Scorsolini
310	t	Posto Shell Fera de Itapevi
311	t	Posto Shell Jundiai Mirim
312	t	Posto Shell Ceiba Speciosa
313	t	Posto Shell Castelinho de Sorocaba
314	t	Posto Shell Scofano e Scofano
315	t	Posto Shell Universitario Sao Carlos
316	t	Posto Shell Mixam
317	t	Posto Shell Mediani Pires
318	t	Posto Shell Bela Cintra
319	t	Posto Shell Rio Claro Center Shopping
320	t	Posto Shell Itaipu Bassit
321	t	Posto Shell Primavera Murchid
322	t	Posto Shell Quinta do Golfe
323	t	Posto Shell Atarumin
324	t	Posto Shell Guaruja Andalo
325	t	Posto Shell Axr
326	t	Posto Shell Petro Bady
327	t	Posto Shell Avenida de Itatiba
328	t	Posto Shell Carrossel
329	t	Posto Shell Santos Dummont de Franca
330	t	Posto Shell Duque City
331	t	Posto Shell Hiperion
332	t	Posto Shell Aguia de Haia
333	t	Posto Shell Acc Radial
334	t	Posto Shell Chacaras do Coelho
335	t	Posto Shell Petrodutra
336	t	Posto Shell Vitoria
337	t	Posto Shell Sao Bernardo
338	t	Posto Shell Tigrão da Dutra
339	t	Posto Shell Sigma
340	t	Posto Shell Perola de Ubatuba
341	t	Posto Shell Cassiano Ricardo
342	t	Posto Shell AJ e AR
343	t	Posto Shell Golfe Clube
344	t	Posto Shell Modelo JMLBG
345	t	Posto Shell Catedral
346	t	Posto Shell Excede
347	t	Posto Shell Importação
348	t	Posto Shell Hawai Rio
349	t	Posto Shell Tirol
350	t	Posto Shell Grande Amor
351	t	Posto Shell Karapito da Beira
352	t	Posto Shell Barra Monteiro
353	t	Posto Shell Portela Dois
354	t	Posto Shell Amor da Leopoldina
355	t	Posto Shell Rocar Rio
356	t	Posto Shell Jardim Oceanico
357	t	Posto Shell Jardim Oceanico da Barra
358	t	Posto Shell Rezende Recreio II
359	t	Posto Shell Duck
360	t	Posto Shell Viaduto de Morato Eireli
361	t	Posto Shell Borssato Serrazul
362	t	Posto Shell Siqueira e Carbonari
363	t	Posto Shell Maramar
364	t	Posto Shell Duque Conde Alphaville
365	t	Posto Shell Brasil Santa Cruz
366	t	Posto Shell Estrela
367	t	Posto Shell Amigao de Itaborai
368	t	Posto Shell Amigão da Dutra
369	t	Posto Shell Araujo Leite
370	t	Posto Shell Nações Bauru
371	t	Posto Shell Aeroporto Bauru
372	t	Posto Shell RodoPosto Maristela
373	t	Posto Shell Duque 21 de Moura
374	t	Posto Shell Limoeiro
375	t	Posto Shell Carbonari
376	t	Posto Shell Chalcataya
377	t	Posto Shell JPX
378	t	Posto Shell 2001
379	t	Posto Shell Quinze
380	t	Posto Shell Arrastao
381	t	Posto Shell Gazpark Participaçoes
382	t	Posto Shell Meriti
383	t	Posto Shell Suina Derivados de Petroleo
384	t	Posto Shell Brasil 2000
385	t	Posto Shell Argetax Vila Guilherme
386	t	Posto Shell Portal de Santana
387	t	Posto Shell Tasquinha
388	t	Posto Shell Flor da Luz
389	t	Posto Shell Progresso Eloy Chaves
390	t	Posto Shell Nova Suiça
391	t	Posto Shell Pavao Castelinho
392	t	Posto Shell Gasparzinho
393	t	Posto Shell Higienopolis Santo Andre
394	t	Posto Shell Pistao
395	t	Posto Shell Mato Alto
396	t	Posto Shell Kalota
397	t	Posto Shell Europa Empreendimentos
398	t	Posto Shell Arigato
399	t	Posto Shell Delta Mar
400	t	Posto Shell IATE
401	t	Posto Shell Casa Nova
402	t	Posto Shell Senhor Barcelona
403	t	Posto Shell Malure
404	t	Posto Shell Rodovia de Bauru
405	t	Posto Shell Manhattam
406	t	Posto Shell Reyssol
407	t	Posto Shell Trapezio
408	t	Posto Shell Quatro Trevo
409	t	Posto Shell Campos do Jordao
410	t	Posto Shell Duque Moema
411	t	Posto Shell Trento
412	t	Posto Shell Colossal
413	t	Posto Shell Lipe
414	t	Posto Shell Margodete
415	t	Posto Shell Galo Branco
416	t	Posto Shell Antares
417	t	Posto Shell Copa Ouro
418	t	Posto Shell Alameda Sacoma
419	t	Posto Shell Garage Lisboa
420	t	Posto Shell Aladin Servicos
421	t	Posto Shell Lord Rodrigo
422	t	Posto Shell Verde Curitiba
423	t	Posto Shell Pedrazzoli
424	t	Posto Shell Picheth
425	t	Posto Shell Ducati
426	t	Posto Shell Gisela
427	t	Posto Shell Premiere
428	t	Posto Shell Perola
429	t	Posto Shell Farol do Parque
430	t	Posto Shell Jardim Botanico
431	t	Posto Shell Banc
432	t	Posto Shell Thiago Vinicius
433	t	Posto Shell Monza
434	t	Posto Shell Petrogil
435	t	Posto Shell Sao Jose 3
436	t	Posto Shell MLL
437	t	Posto Shell Artigas
438	t	Posto Shell NSL
439	t	Posto Shell Paraiso Lubrificantes
440	t	Posto Shell Cupim
441	t	Posto Shell Rio Lima
443	t	Posto Shell Santa Amalia
444	t	Posto Shell Avenida Central de Iraja
445	t	Posto Shell Casaca
446	t	Posto Shell LK Vila Universitaria
447	t	Posto Shell Galapagos
448	t	Posto Shell Big Aço
449	t	Posto Shell ALG
450	t	Posto Shell Monte Santo
451	t	Posto Shell Luches
452	t	Posto Shell A P F
453	t	Posto Shell Abreu Dois
454	t	Posto Shell LK Vila Falcao I
455	t	Posto Shell Barra Cachamorra
456	t	Posto Shell JB Caxias
457	t	Posto Shell Vitoria 040
458	t	Posto Shell Forgerini e Inouye São Carlos
459	t	Posto Shell Morro Azul de Itatiba
460	t	Posto Shell Colina Aracatuba
461	t	Posto Shell Forgerine e Inouye Itirapina
462	t	Posto Shell Cardoso Castro
463	t	Posto Shell Gran Penha
464	t	Posto Shell Abreu
465	t	Posto Shell Automix
466	t	Posto Shell Manguinhos de Buzios
467	t	Posto Shell Boa Viagem Friburgo
468	t	Posto Shell Bola Pesada
469	t	Posto Shell LG
470	t	Posto Shell Almeida e L.Oveira
471	t	Posto Shell Bolla Branca
472	t	Posto Shell Santa Luzia Atibaia
473	t	Posto Shell Santana Sao Jose dos Campos
474	t	Posto Shell Parambos
475	t	Posto Shell Beraldo
476	t	Posto Shell Eco Posto
477	t	Posto Shell Sol da Dutra
478	t	Auto Posto Belezura
479	t	Posto Shell Via Ponte
480	t	Posto Shell Mike
481	t	Posto Shell Jardim Marajoara
442	t	Posto Shell FM da Prata
\.


--
-- Data for Name: abastece_base; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY abastece_base (id, active, name, coordx, coordy, employee_id, viatura_id, warehouse_id) FROM stdin;
1	t	PR01	-49.21497	-25.45543	7	2	10
2	t	RJ01	-43.25104	-22.86634	8	1	11
3	t	SP01	-46.743395	-23.553796	4	6	2
4	t	SP02	-46.650138	-23.66895	2	10	3
5	t	SP03	-46.511256	-23.651876	3	9	4
6	t	SP04	-46.51364	-23.46507	1	8	5
7	t	SP05	-49.05586	-22.32594	5	5	6
8	t	SP06	-47.09632	-22.910387	6	7	7
9	t	SP07	-47.49536	-23.52349	10	4	9
10	t	SOR01	-47.49536	-23.52349	9	3	8
\.


--
-- Name: abastece_base_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('abastece_base_id_seq', 10, true);


--
-- Data for Name: abastece_classe; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY abastece_classe (id, name) FROM stdin;
1	A
2	B
3	C
4	D
\.


--
-- Name: abastece_classe_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('abastece_classe_id_seq', 4, true);


--
-- Name: abastece_employee_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('abastece_employee_id_seq', 10, true);


--
-- Data for Name: abastece_empresa; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY abastece_empresa (id, active, name) FROM stdin;
1	t	E2i9
2	t	UNICOM
\.


--
-- Name: abastece_empresa_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('abastece_empresa_id_seq', 2, true);


--
-- Data for Name: abastece_form; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY abastece_form (id, active, name) FROM stdin;
1	t	AÇÕES DE MELHORIA
2	t	CORRETIVA
3	t	DESINSTALAÇÃO DO POSTO
4	t	INVENTÁRIO
5	t	ANTENA 915
6	t	PLANO VERÃO
7	t	PREDITIVA
8	t	PREVENTIVA
9	t	RETIRADA ANTENA 5.8
10	t	SINALIZAÇÃO
11	t	INSTALAÇÃO ICR
12	t	SURVEY
13	t	DESINSTALAÇÃO DO POSTO
\.


--
-- Data for Name: abastece_posto; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY abastece_posto (id, active, name, cgmp, status_opc, status_vip, coordx, coordy, base_id, classe_id, warehouse_id) FROM stdin;
3258	t	Posto Shell Ramal	6001	t	t	-46,7291030883789	-23,517406463623	3	1	15
3259	t	Posto Shell Orion	6002	t	f	-46,7429046630859	-23,5540809631348	3	1	16
3260	t	Posto Shell Atlantica	6005	t	f	-46,6590309143066	-23,5322437286377	4	2	17
3261	t	Posto Shell Agua Espraiada	6006	t	f	-46,6751365661621	-23,6274013519287	4	1	18
3262	t	Posto Shell Abraao de Morais	6007	t	t	-46,6286468505859	-23,6248607635498	4	1	19
3263	t	Posto Shell Rimacris	6008	t	f	-46,8314971923828	-23,502462387085	3	2	20
3264	t	Posto Shell Hawai	6009	t	f	-46,6991539001465	-23,5147075653076	3	1	21
3265	t	Posto Shell Napoleão Barros	6010	t	f	-46,6445655822754	-23,6013031005859	4	2	22
3266	t	Posto Shell Ralpha	6011	t	f	-46,8520812988281	-23,4986171722412	3	1	23
3267	t	Posto Shell Estacao Carandiru	6013	t	f	-46,6238632202148	-23,5063953399658	4	1	24
3268	t	Posto Shell Caetano Alvares	6014	t	t	-46,6595993041992	-23,4939880371094	3	1	25
3269	t	Posto Shell Bristol	6015	t	f	-46,5721817016602	-23,5573635101318	5	1	26
3270	t	Posto Shell Catalao	6016	t	f	-46,6816825866699	-23,5458526611328	4	2	27
3271	t	Posto Shell Portal Leste	6017	t	t	-46,6067504882813	-23,5507431030273	4	1	28
3272	t	Posto Shell Faga e Bizarria	6018	t	f	-46,7232475280762	-23,5880374908447	3	2	29
3273	t	Posto Shell Fabio Motta Marques	6019	t	t	-46,5551643371582	-23,5206413269043	5	1	30
3274	t	Posto Shell Alpha Marte	6020	t	f	-46,8752288818359	-23,4628772735596	3	2	31
3275	t	Posto Shell Monte Carlo	6021	t	f	-46,6637573242188	-23,609920501709	4	2	32
3276	t	Posto Shell ABV	6023	t	f	-46,6991500854492	-23,6429328918457	4	4	33
3277	t	Posto Shell Tasca	6024	t	t	-46,7725486755371	-23,5360507965088	3	1	34
3278	t	Posto Shell Batalha	6025	t	t	-46,7307014465332	-23,5810241699219	3	1	35
3279	t	Posto Shell Cote D'azur	6026	t	f	-46,57177734375	-23,5500621795654	5	2	36
3280	t	Posto Shell Status do Panamby	6027	t	f	-46,7370223999023	-23,6387004852295	3	2	37
3281	t	Posto Shell Sao Gualter	6028	t	f	-46,7114067077637	-23,5433807373047	3	3	38
3282	t	Posto Shell Rio Grande	6029	t	f	-46,643253326416	-23,5868091583252	4	2	39
3283	t	Posto Shell Gigante da Imigrantes	6030	t	t	-46,6274261474609	-23,6147918701172	4	1	40
3284	t	Posto Shell M.A	6032	t	f	-46,5213775634766	-23,558614730835	5	2	41
3285	t	Posto Shell Elmar	6033	t	f	-46,6428451538086	-23,639196395874	4	2	42
3286	t	Posto Shell Prime	6034	t	f	-46,6381034851074	-23,6327781677246	4	2	43
3287	t	Posto Shell Mascote	6035	t	f	-46,6663208007813	-23,6422157287598	4	4	44
3288	t	Posto Shell Mash	6036	t	t	-46,6089935302734	-23,6160182952881	4	1	45
3289	t	Posto Shell Gipires	6037	t	f	-46,6672859191895	-23,5069351196289	3	2	46
3290	t	Posto Shell Benets	6038	t	f	-46,7093734741211	-23,5784912109375	3	1	47
3291	t	Posto Shell Carlos Alberto Papacidero	6040	t	t	-46,6718711853027	-23,5135536193848	3	1	48
3292	t	Posto Shell Marini	6041	t	t	-46,6862487792969	-23,500638961792	3	1	49
3293	t	Posto Shell Jardim Sao Paulo	6042	t	f	-46,6207656860352	-23,4869422912598	6	2	50
3294	t	Posto Shell Fukuya Kanemoto	6043	t	t	-46,6851692199707	-23,5088939666748	3	1	51
3295	t	Posto Shell Galena	6044	t	f	-46,6256828308105	-23,6030426025391	4	1	52
3296	t	Posto Shell Lutaif	6045	t	t	-46,6113967895508	-23,4919681549072	6	1	53
3297	t	Posto Shell Bellagio	6046	t	f	-46,673038482666	-23,4788932800293	3	2	54
3298	t	Posto Shell JJ	6047	t	f	-46,6257209777832	-23,6047134399414	4	2	55
3299	t	Posto Shell Summer	6048	t	f	-46,6913261413574	-23,6548633575439	4	1	56
3300	t	Posto Shell Francisco Morato	6049	t	f	-46,7133750915527	-23,5827598571777	3	2	57
3301	t	Posto Shell BAP	6050	t	f	-46,6597862243652	-23,6642379760742	4	2	58
3302	t	Posto Shell Independencia do cambuci	6051	t	f	-46,6131935119629	-23,567626953125	4	2	59
3303	t	Posto Shell Ponto Solar	6052	t	f	-46,6631736755371	-23,6466579437256	4	3	60
3304	t	Posto Shell Via Sul	6053	t	f	-46,7422752380371	-23,615255355835	3	1	61
3305	t	Posto Shell Vera Cruz	6054	t	f	-46,5227088928223	-23,531852722168	5	1	62
3306	t	Posto Shell Veloz	6055	t	f	-46,5398445129395	-23,5930767059326	5	1	63
3307	t	Posto Shell Center Car	6056	t	t	-46,7433967590332	-23,5537967681885	3	1	64
3308	t	Posto Shell Moinho Velho	6057	t	f	-46,7459335327148	-23,5961627960205	3	2	65
3309	t	Posto Shell Bordo	6058	t	f	-46,7320442199707	-23,5873508453369	3	2	66
3310	t	Posto Shell Asturias	6062	t	f	-46,7205200195313	-23,6375293731689	4	4	67
3311	t	Posto Shell Macedo	6063	t	f	-46,5136451721191	-23,4650726318359	6	2	68
3312	t	Posto Shell Kll	6068	t	f	-46,4694976806641	-23,6839866638184	5	4	69
3313	t	Posto Shell Paraki	6070	t	f	-46,6719665527344	-23,6218662261963	4	3	70
3314	t	Posto Shell Oitenta	6071	t	f	-46,4588737487793	-23,6716213226318	5	2	71
3315	t	Posto Shell Tonicar	6072	t	f	-46,6277465820313	-23,5918483734131	4	3	72
3316	t	Posto Shell Agua Funda 2	6073	t	f	-46,6179084777832	-23,58518409729	4	3	73
3317	t	Posto Shell Kobayachi	6074	t	f	-47,0349502563477	-23,6076793670654	3	2	74
3318	t	Posto Shell 45	6075	t	f	-47,0223960876465	-23,6052093505859	3	2	75
3319	t	Posto Shell Nova Itapevi	6076	t	f	-46,9398345947266	-23,5362434387207	3	2	76
3320	t	Posto Shell Nellu	6077	t	f	-46,4653434753418	-23,6769142150879	5	3	77
3321	t	Posto Shell Star Red	6078	t	f	-46,5755844116211	-23,7074661254883	5	2	78
3322	t	Posto Shell Agua funda 1	6079	t	f	-46,6276817321777	-23,6077976226807	4	2	79
3323	t	Posto Shell Turismo	6080	t	f	-46,6334075927734	-23,6838893890381	4	2	80
3324	t	Posto Shell Joinha de Guarulhos	6081	t	f	-46,5272216796875	-23,463659286499	6	2	81
3325	t	Posto Shell Sao Joaquim	6082	t	f	-46,5600967407227	-23,4559230804443	6	2	82
3326	t	Posto Shell Via 10	6083	t	f	-46,6501388549805	-23,6689491271973	4	3	83
3327	t	Posto Shell 555	6084	t	f	-46,569450378418	-23,4503555297852	6	4	84
3328	t	Posto Shell Alcantara	6085	t	f	-46,7148284912109	-23,6966590881348	3	2	85
3329	t	Posto Shell Cinadis	6086	t	f	-46,5525054931641	-23,7316913604736	5	2	86
3330	t	Posto Shell Tapera Grande	6087	t	f	-46,4745941162109	-23,4514389038086	6	2	87
3331	t	Posto Shell Estonia 5	6088	t	f	-46,5554084777832	-23,7472553253174	5	2	88
3332	t	Posto Shell Rede Leste	6089	t	f	-46,5084838867188	-23,5500411987305	5	2	89
3333	t	Posto Shell Sergio Motta Marques	6091	t	f	-46,4452171325684	-23,5583209991455	5	2	90
3334	t	Posto Shell Vielfe Martins	6092	t	f	-46,4615097045898	-23,6250038146973	5	4	91
3335	t	Posto Shell Fernão dias	6093	t	t	-46,5689010620117	-23,4688911437988	6	1	92
3336	t	Posto Shell Arco Verde	6094	t	f	-46,4157791137695	-23,5643901824951	5	2	93
3337	t	Posto Shell Jaguare	6095	t	f	-46,7271041870117	-23,5296573638916	3	2	94
3338	t	Posto Shell Saint Germain	6097	t	f	-46,7867126464844	-23,5304069519043	3	2	95
3339	t	Posto Shell Jardim 10	6099	t	f	-46,7300415039063	-23,6454639434814	3	2	96
3340	t	Posto Shell Ouro de barueri	6100	t	f	-46,8803596496582	-23,4933052062988	3	1	97
3341	t	Posto Shell Estonia 2	6101	t	f	-46,5112571716309	-23,651876449585	5	2	98
3342	t	Posto Shell Marina	6102	t	f	-46,5507202148438	-23,6421012878418	5	3	99
3343	t	Posto Shell Tao Set	6103	t	f	-46,5478363037109	-23,6499366760254	5	2	100
3344	t	Posto Shell Estonia	6104	t	f	-46,5031547546387	-23,634147644043	5	2	101
3345	t	Posto Shell Caracas Oil	6106	t	f	-46,8365173339844	-23,5552234649658	3	2	102
3346	t	Posto Shell ABD	6107	t	f	-46,596019744873	-23,679594039917	4	2	103
3347	t	Posto Shell Hiperpetro	6108	t	f	-46,5572395324707	-23,6267108917236	5	2	104
3348	t	Posto Shell Avenida dos estados	6109	t	f	-46,5341606140137	-23,6381893157959	5	2	105
3349	t	Posto Shell Estonia 4	6110	t	f	-46,5425605773926	-23,6376934051514	5	2	106
3350	t	Posto Shell Humaita	6111	t	f	-46,5093231201172	-23,6643257141113	5	2	107
3351	t	Posto Shell Phenix	6112	t	f	-46,6020278930664	-23,5852165222168	4	2	108
3352	t	Posto Shell Martinelli	6113	t	f	-46,7088279724121	-23,5248012542725	3	2	109
3353	t	Posto Shell 2002	6115	t	f	-46,7369117736816	-23,6261863708496	3	2	110
3354	t	Posto Shell Santa terezinha	6116	t	f	-46,8546981811523	-23,5189304351807	3	1	111
3355	t	Posto Shell CPC	6117	t	f	-46,8527717590332	-23,5181198120117	3	1	112
3356	t	Posto Shell Muraki	6118	t	f	-46,3673706054688	-23,6827697753906	5	4	113
3357	t	Posto Shell Mairipora	6119	t	f	-46,5739898681641	-23,2923240661621	6	2	114
3358	t	Posto Shell Vila rica	6120	t	f	-46,6054267883301	-23,5089015960693	6	2	115
3359	t	Posto Shell Novo Milenio	6121	t	f	-46,4461135864258	-23,5592460632324	5	1	116
3360	t	Posto Shell Estação Anchieta	6123	t	f	-46,5677947998047	-23,6897258758545	5	1	117
3361	t	Posto Shell La Caniza	6124	t	f	-46,2869567871094	-23,99001121521	5	2	118
3362	t	Posto Shell Osasco Country	6127	t	f	-46,7924194335938	-23,5529651641846	3	2	119
3363	t	Posto Shell Rally	6128	t	f	-46,5521697998047	-23,582010269165	5	3	120
3364	t	Posto Shell Roan	6129	t	f	-46,667293548584	-23,6087646484375	4	2	121
3365	t	Posto Shell Recanto da seringueira	6130	t	t	-46,8118743896484	-23,5246772766113	3	1	122
3366	t	Posto Shell Nautica Frei Gaspar	6131	t	f	-46,4079093933105	-23,9543266296387	5	4	123
3367	t	Posto Shell Vanessa Santos Silva	6132	t	f	-46,4899673461914	-23,6648120880127	5	3	124
3368	t	Posto Shell Argetax Anchieta	6133	t	f	-46,60107421875	-23,6138229370117	4	2	125
3369	t	Posto Shell Panamby	6134	t	f	-46,726806640625	-23,6496620178223	3	2	126
3370	t	Posto Shell Tratto	6135	t	f	-46,6037254333496	-23,7184028625488	4	2	127
3371	t	Posto Shell Novo Barao 2	6136	t	f	-46,4341735839844	-23,665189743042	5	4	128
3372	t	Posto Shell Toninho trinta	6137	t	f	-46,7021789550781	-23,7055149078369	3	2	129
3373	t	Posto Shell Estonia 3	6138	t	t	-46,5506324768066	-23,705680847168	5	1	130
3374	t	Posto Shell Joia de Guarulhos	6139	t	f	-46,5267791748047	-23,463399887085	6	2	131
3375	t	Posto Shell O Chefao	6140	t	f	-46,5510063171387	-23,4516143798828	6	2	132
3376	t	Posto Shell Morumbi Star	6142	t	f	-46,7342491149902	-23,6115055084229	3	2	133
3377	t	Posto Shell Veiga Filho	6143	t	f	-46,6613693237305	-23,5389995574951	4	2	134
3378	t	Posto Shell Novo Barao	6145	t	f	-46,6455612182617	-23,5320568084717	4	3	135
3379	t	Posto Shell Brilhante	6146	t	f	-46,6332969665527	-23,5715465545654	4	3	136
3380	t	Posto Shell Moraes Sales	6150	t	f	-47,0513496398926	-22,9052658081055	8	2	137
3381	t	Posto Shell Center Paraiso	6151	t	f	-46,6456108093262	-23,572322845459	4	4	138
3382	t	Posto Shell Carlos E L Braga	6154	t	f	-46,7120323181152	-23,6732120513916	3	2	139
3383	t	Posto Shell Antonio Paes	6155	t	f	-46,6978569030762	-23,7308025360107	3	2	140
3384	t	Posto Shell Luppi	6156	t	f	-46,7269401550293	-23,5876979827881	3	3	141
3385	t	Posto Shell Ermano Marchetti	6159	t	f	-46,6966514587402	-23,5153846740723	3	2	142
3386	t	Posto Shell Isola	6160	t	f	-46,7125587463379	-23,6739807128906	3	2	143
3387	t	Posto Shell Arco Verde Cotia	6161	t	f	-46,9321899414063	-23,6122741699219	3	2	144
3388	t	Posto Shell Express Valinhos	6163	t	f	-47,0007438659668	-22,9791603088379	8	2	145
3389	t	Posto Shell Sao Conrado	6167	t	f	-46,7268295288086	-23,4795589447021	3	1	146
3390	t	Posto Shell Vida Nova	6168	t	f	-46,6402587890625	-23,6510467529297	4	2	147
3391	t	Posto Shell Lorena	6169	t	f	-46,6629257202148	-23,566385269165	4	2	148
3392	t	Posto Shell Pole Position	6170	t	f	-47,0508003234863	-22,9227542877197	8	2	149
3393	t	Posto Shell Washington Luiz	6171	t	f	-47,0564804077148	-22,9254264831543	8	2	150
3394	t	Posto Shell Farol	6172	t	f	-46,394889831543	-23,4230098724365	6	3	151
3395	t	Posto Shell Futuro	6173	t	f	-47,0793342590332	-22,835470199585	8	2	152
3396	t	Posto Shell Vo Joao	6174	t	f	-47,0812721252441	-22,8186302185059	8	3	153
3397	t	Posto Shell Presidente Juscelino	6175	t	f	-47,1019897460938	-22,9302883148193	8	1	154
3398	t	Posto Shell Companheiro	6180	t	f	-47,2307510375977	-22,8908367156982	8	2	155
3399	t	Posto Shell Portal Mogi	6181	t	f	-46,1856880187988	-23,5345230102539	5	2	156
3400	t	Posto Shell Cidade Jardim Americana	6183	t	f	-47,3396911621094	-22,7611904144287	5	2	157
3401	t	Posto Shell Fenix Nova Odessa	6184	t	f	-47,2964286804199	-22,7902965545654	8	4	158
3402	t	Posto Shell Duque Berrini	6185	t	f	-46,6938667297363	-23,6075458526611	4	3	159
3403	t	Posto Shell Rebouças	6186	t	f	-47,2779312133789	-22,8144798278809	8	2	160
3404	t	Posto Shell Mara Miru	6187	t	f	-46,6652526855469	-23,6118125915527	4	2	161
3405	t	Posto Shell Zonta	6189	t	f	-46,6780700683594	-23,665283203125	4	3	162
3406	t	Posto Shell Lavapes	6190	t	f	-46,6294708251953	-23,559907913208	4	4	163
3407	t	Posto Shell Montana	6191	t	f	-46,6347198486328	-23,5867481231689	4	3	164
3408	t	Posto Shell Jardim colonial	6193	t	f	-47,2310562133789	-23,1091136932373	8	3	165
3409	t	Posto Shell Saci	6195	t	f	-47,0341873168945	-22,9968757629395	8	2	166
3410	t	Posto Shell SPW	6196	t	f	-46,906623840332	-23,6028671264648	3	2	167
3411	t	Posto Shell Maranelo 2	6198	t	f	-46,6369285583496	-23,5030746459961	4	1	168
3412	t	Posto Shell Jardim do Trevo	6199	t	t	-47,0699195861816	-22,9291725158691	8	1	169
3413	t	Posto Shell Luiz Venditti	6200	t	f	-47,053108215332	-22,9200096130371	8	4	170
3414	t	Posto Shell Tejo	6201	t	f	-46,5896911621094	-23,5649356842041	5	2	171
3415	t	Posto Shell Casa Grande	6203	t	f	-46,6585960388184	-23,614330291748	4	1	172
3416	t	Posto Shell Mingo	6204	t	f	-46,709644317627	-23,5542221069336	3	2	173
3417	t	Posto Shell Joruhi	6208	t	f	-46,6697196960449	-23,5954360961914	4	3	174
3418	t	Posto Shell Andorinhas	6209	t	t	-47,0449333190918	-22,8872718811035	8	1	175
3419	t	Posto Shell Progresso Mogi	6210	t	f	-46,9529800415039	-22,4327239990234	8	4	176
3420	t	Posto Shell Barbieri de Barao Geraldo	6211	t	f	-47,0788269042969	-22,8299865722656	8	2	177
3421	t	Posto Shell Luiz Fantinato Filho	6213	t	f	-47,0034141540527	-22,9629383087158	8	2	178
3422	t	Posto Shell 3M	6214	t	f	-46,3183479309082	-23,4009323120117	6	2	179
3423	t	Posto Shell Vila Pagano	6215	t	f	-47,0053901672363	-22,9920501708984	8	3	180
3424	t	Posto Shell Av Nossa Sra de Fatima	6216	t	f	-47,0434875488281	-22,8772411346436	8	3	181
3425	t	Posto Shell Savemo	6217	t	f	-46,6856384277344	-23,6110725402832	4	3	182
3426	t	Posto Shell Gaivota	6218	t	f	-46,6707611083984	-23,6072940826416	4	2	183
3427	t	Posto Shell Diesel Mac	6219	t	f	-46,5650291442871	-23,4896507263184	6	2	184
3428	t	Posto Shell Aiwa	6220	t	f	-46,5765953063965	-23,5015335083008	6	2	185
3429	t	Posto Shell Mestre	6222	t	f	-46,5686874389648	-23,4580211639404	6	2	186
3430	t	Posto Shell Novo Ouro Negro	6223	t	f	-46,4665565490723	-23,6655769348145	5	2	187
3431	t	Posto Shell Grand Prix	6224	t	f	-46,6987152099609	-23,6930599212646	3	2	188
3432	t	Posto Shell G5	6226	t	f	-46,455451965332	-23,4171695709229	6	4	189
3433	t	Posto Shell Campineira	6227	t	f	-47,0797119140625	-22,8253402709961	8	3	190
3434	t	Posto Shell Amigao	6230	t	f	-47,3576316833496	-22,73583984375	8	2	191
3435	t	Posto Shell Tropical Gas	6234	t	f	-46,6215171813965	-23,5524921417236	4	3	192
3436	t	Posto Shell Guarnel	6235	t	f	-46,7047386169434	-23,5277671813965	3	2	193
3437	t	Posto Shell City Cantareira	6237	t	f	-46,6161003112793	-23,4580402374268	3	2	194
3438	t	Posto Shell Formula Shell	6238	t	f	-46,6778793334961	-23,667652130127	4	2	195
3439	t	Posto Shell Jordanopolis	6239	t	f	-46,5727806091309	-23,6835632324219	5	4	196
3440	t	Posto Shell Lubricar	6240	t	f	-46,5397109985352	-23,6724262237549	5	2	197
3441	t	Posto Shell Sol	6241	t	f	-46,5340309143066	-23,6523780822754	5	4	198
3442	t	Posto Shell Portal do Paraiso	6242	t	f	-46,7273979187012	-23,610523223877	3	3	199
3443	t	Posto Shell EG	6244	t	f	-46,742561340332	-23,6439895629883	3	2	200
3444	t	Posto Shell Campo limpo	6245	t	f	-46,7647285461426	-23,6248760223389	3	3	201
3445	t	Posto Shell Veneza	6246	t	f	-46,7451286315918	-23,5571708679199	3	2	202
3446	t	Posto Shell Albano	6249	t	f	-46,5824966430664	-23,5685997009277	5	4	203
3447	t	Posto Shell Riolis	6250	t	f	-46,6480407714844	-23,6699542999268	4	4	204
3448	t	Posto Shell Nova Campinas	6252	t	f	-47,0462188720703	-22,9024677276611	8	3	205
3449	t	Posto Shell BE	6253	t	f	-46,690990447998	-23,6208000183105	4	2	206
3450	t	Posto Shell Padocka	6254	t	f	-46,535587310791	-23,6270618438721	5	3	207
3451	t	Posto Shell Vila Galvao	6255	t	f	-46,5664672851563	-23,4548721313477	6	3	208
3452	t	Posto Shell CRS	6256	t	f	-46,8834953308105	-23,4886283874512	3	4	209
3453	t	Posto Shell Santo Eduardo	6257	t	f	-46,8034286499023	-23,6726322174072	3	3	210
3454	t	Posto Shell Carlu	6261	t	f	-46,7173805236816	-23,6569805145264	3	2	211
3455	t	Posto Shell Moni	6262	t	f	-46,5833511352539	-23,4642601013184	6	3	212
3456	t	Posto Shell Arinella Brooklin	6264	t	f	-46,6869316101074	-23,6297931671143	4	3	213
3457	t	Posto Shell Cardeal	6266	t	f	-46,6738090515137	-23,5529613494873	4	4	214
3458	t	Posto Shell Gondola	6268	t	f	-46,6585502624512	-23,6350193023682	4	4	215
3459	t	Posto Shell Mister Plus	6269	t	f	-46,6753387451172	-23,6052417755127	4	4	216
3460	t	Posto Shell Rocar	6270	t	f	-46,6869316101074	-23,5773849487305	4	3	217
3461	t	Posto Shell Duque e Cia	6272	t	f	-46,6580848693848	-23,5465564727783	4	3	218
3462	t	Posto Shell Helio Valdivia	6273	t	f	-47,0583152770996	-22,9003200531006	8	4	219
3463	t	Posto Shell Silvia Maria Pinto Santos Abastece	6274	t	f	-46,6181907653809	-23,5856876373291	4	4	220
3464	t	Posto Shell Madia	6277	t	f	-47,0025672912598	-22,9679279327393	8	3	221
3465	t	Posto Shell Castelinho	6280	t	f	-47,0737571716309	-22,8959350585938	8	2	222
3466	t	Posto Shell Bate Bola	6281	t	f	-46,8917007446289	-23,1869983673096	6	2	223
3467	t	Posto Shell Parque da Uva	6282	t	f	-46,8978500366211	-23,1905879974365	6	1	224
3468	t	Posto Shell Progresso	6283	t	f	-46,864315032959	-23,2119064331055	6	3	225
3469	t	Posto Shell Keeper	6284	t	f	-46,8477630615234	-23,2091121673584	6	2	226
3470	t	Posto Shell Cidade Do Vinho	6285	t	f	-46,8849449157715	-23,2070026397705	6	2	227
3471	t	Posto Shell Soledade Gaucha	6286	t	t	-47,466121673584	-23,4964237213135	9	1	228
3472	t	Posto Shell Pimenta	6288	t	f	-47,2254447937012	-23,1230888366699	8	4	229
3473	t	Posto Shell Turismo 2	6289	t	f	-46,6004981994629	-23,6802082061768	4	2	230
3474	t	Posto Shell Argetax Guarulhos	6290	t	f	-46,5511817932129	-23,4856719970703	6	2	231
3475	t	Posto Shell Andrea Santini Rego	6291	t	f	-47,0610198974609	-22,8933715820313	8	3	232
3476	t	Posto Shell Portal de Americana	6292	t	f	-47,2959747314453	-22,7291870117188	8	2	233
3477	t	Posto Shell Caxambu	6293	t	f	-46,846248626709	-23,1494789123535	6	4	234
3478	t	Posto Shell Telles	6294	t	t	-46,8851737976074	-23,1734237670898	6	1	235
3479	t	Posto Shell Jardim Santa Monica	6295	t	f	-47,1106567382813	-22,8553581237793	8	4	236
3480	t	Posto Shell Dom Pedro I	6296	t	f	-46,9716911315918	-22,9091968536377	8	4	237
3481	t	Posto Shell Grande São Paulo	6297	t	f	-46,64404296875	-23,5697975158691	4	3	238
3482	t	Posto Shell Bap Barão	6298	t	f	-46,433521270752	-23,665096282959	5	4	239
3483	t	Posto Shell Dar A	6299	t	t	-46,6787223815918	-23,338020324707	3	1	240
3484	t	Posto Shell Abdelnor	6300	t	f	-47,2273788452148	-23,1191101074219	8	4	241
3485	t	Posto Shell Parque Villa Lobos	6302	t	f	-46,7176704406738	-23,5456256866455	3	2	242
3486	t	Posto Shell Santa Cruz de Mogi Mirim	6303	t	f	-46,975341796875	-22,4363899230957	8	3	243
3487	t	Posto Shell Cristal	6304	t	f	-46,73193359375	-23,5922451019287	3	4	244
3488	t	Posto Shell SS	6305	t	f	-46,678596496582	-23,5607872009277	4	3	245
3489	t	Posto Shell Agua Branca	6307	t	f	-47,6391410827637	-22,7459392547607	8	4	246
3490	t	Posto Shell TM	6308	t	f	-47,6333160400391	-22,7242736816406	8	3	247
3491	t	Posto Shell GT	6309	t	f	-47,6341896057129	-22,7328605651855	8	3	248
3492	t	Posto Shell Algodoal	6310	t	f	-47,6600379943848	-22,6971378326416	8	4	249
3493	t	Posto Shell Dona Francisca	6311	t	f	-47,6555023193359	-22,710823059082	8	2	250
3494	t	Posto Shell Radial Norte Sul de Piracicaba	6312	t	f	-47,6731910705566	-22,6896629333496	8	4	251
3495	t	Posto Shell Bongue	6313	t	f	-47,6748580932617	-22,6999530792236	8	4	252
3496	t	Posto Shell Maravilha	6314	t	f	-47,8068084716797	-21,1728744506836	7	2	253
3497	t	Posto Shell Presidente Ribeirao	6315	t	f	-47,8097152709961	-21,2034740447998	7	2	254
3498	t	Posto Shell Sociedade RD	6316	t	f	-47,7892227172852	-21,1661357879639	7	3	255
3499	t	Posto Shell Espaço Botanico	6318	t	f	-47,796085357666	-21,2125091552734	7	2	256
3500	t	Posto Shell Josimar D Lourenco	6319	t	f	-47,7981224060059	-21,1882438659668	7	3	257
3501	t	Posto Shell Alcides Costa	6320	t	f	-47,8080787658691	-21,1986885070801	7	2	258
3502	t	Posto Shell Carro Nobre	6321	t	f	-47,793529510498	-21,2038192749023	7	4	259
3503	t	Posto Shell Monaco	6322	t	f	-47,7568893432617	-21,1889896392822	7	3	260
3504	t	Posto Shell Vitrine	6323	t	f	-46,8964157104492	-23,1905040740967	6	1	261
3505	t	Posto Shell Bela Vista	6324	t	f	-46,7195243835449	-23,6448154449463	3	2	262
3506	t	Posto Shell Sao Martinho	6325	t	f	-46,6728324890137	-23,5341987609863	4	2	263
3507	t	Posto Shell Jurua	6326	t	f	-46,6679191589355	-23,5375461578369	4	3	264
3508	t	Posto Shell Piracena	6327	t	f	-47,6305160522461	-22,738826751709	8	4	265
3509	t	Posto Shell Avenida Campinas	6329	t	f	-47,3872108459473	-22,5817794799805	8	3	266
3510	t	Posto Shell Aeroporto Limeira	6330	t	f	-47,4087905883789	-22,5839729309082	8	2	267
3511	t	Posto Shell Marun	6331	t	f	-47,6455078125	-22,7594928741455	8	4	268
3512	t	Posto Shell Ipe	6332	t	f	-45,9012641906738	-23,2317504882813	6	2	269
3513	t	Posto Shell Quality Casablanca	6334	t	f	-46,3197059631348	-23,5518932342529	5	2	270
3514	t	Posto Shell Quality Supra	6335	t	f	-46,3326606750488	-23,5590591430664	5	4	271
3515	t	Posto Shell M Super	6336	t	f	-46,2526741027832	-23,5449085235596	5	2	272
3516	t	Posto Shell Portal Presidente	6338	t	f	-47,8065528869629	-21,1893215179443	7	4	273
3517	t	Posto Shell Alpha De Votorantim	6342	t	f	-47,4650955200195	-23,5525455474854	9	2	274
3518	t	Posto Shell Universo 2000	6343	t	f	-47,6354560852051	-22,7109966278076	8	4	275
3519	t	Posto Shell Andorinha de Rio Claro	6344	t	f	-47,5601654052734	-22,4128398895264	7	3	276
3520	t	Posto Shell Cedro	6345	t	f	-47,4747772216797	-23,4874229431152	9	2	277
3521	t	Posto Shell Abraao Ribeiro	6346	t	f	-46,6599311828613	-23,522777557373	4	2	278
3522	t	Posto Shell Caragua	6347	t	f	-45,4174346923828	-23,6244583129883	6	3	279
3523	t	Posto Shell Pedro Lessa	6348	t	f	-46,3123588562012	-23,9689502716064	5	2	280
3524	t	Posto Shell Pontal da Cruz	6349	t	f	-45,3992195129395	-23,7798595428467	6	4	281
3525	t	Posto Shell Aeroporto de Ubatuba	6350	t	f	-45,0704383850098	-23,443473815918	6	4	282
3526	t	Posto Shell Jupia	6351	t	f	-46,7829704284668	-23,6652603149414	3	2	283
3527	t	Posto Shell Martineli City	6352	t	f	-47,8197975158691	-21,2166976928711	7	3	284
3528	t	Posto Shell Tiger	6353	t	f	-47,647533416748	-22,702844619751	8	4	285
3529	t	Posto Shell Azulao	6354	t	f	-46,7101631164551	-23,5735836029053	3	2	286
3530	t	Posto Shell Quinta Avenida	6355	t	f	-46,6548271179199	-23,5546283721924	4	4	287
3531	t	Posto Shell Agronomia	6356	t	f	-47,6326675415039	-22,7151947021484	8	2	288
3532	t	Posto Shell Rede Senna	6357	t	f	-46.40539	-23.43251	6	2	289
3533	t	Posto Shell Lince Taubate	6358	t	f	-45,5460968017578	-23,0034656524658	6	2	290
3534	t	Posto Shell Avenida Brasil	6359	t	f	-47,3482666015625	-22,7525367736816	8	2	291
3535	t	Posto Shell Itarare Sao Vicente	6360	t	f	-46,3973197937012	-23,9616088867188	5	3	292
3536	t	Posto Shell Retiro	6361	t	f	-46,9130935668945	-23,1786231994629	6	2	293
3537	t	Posto Shell Garcia de Campinas	6362	t	f	-47,1125144958496	-22,8885478973389	8	2	294
3538	t	Posto Shell Fantinato	6363	t	f	-47,1491241455078	-22,766773223877	8	2	295
3539	t	Posto Shell Alpes	6364	t	f	-45,5567436218262	-23,0322513580322	6	2	296
3540	t	Posto Shell Varsovia	6365	t	f	-45,8823585510254	-23,2433185577393	6	2	297
3541	t	Posto Shell Restaurante 3 Vias	6366	t	f	-47,1512985229492	-22,8558254241943	8	2	298
3542	t	Posto Shell Maricar	6367	t	f	-46,6556015014648	-23,4816875457764	3	3	299
3543	t	Posto Shell Sabella e Sabella	6373	t	f	-46,548900604248	-22,9153785705566	6	4	300
3544	t	Posto Shell Virgilio Fernando	6374	t	f	-46,5908584594727	-23,5127143859863	6	4	301
3545	t	Posto Shell Guigui	6377	t	f	-46,5367851257324	-23,6539268493652	5	4	302
3546	t	Posto Shell Dias	6378	t	f	-46,5267448425293	-23,6718807220459	5	4	303
3547	t	Posto Shell Sabella	6379	t	f	-46,5357208251953	-22,9417514801025	6	4	304
3548	t	Posto Shell Bandeirante	6383	t	f	-45,8857383728027	-23,200475692749	6	2	305
3549	t	Posto Shell Sete Estrelas	6384	t	f	-46,7468452453613	-23,5069351196289	3	2	306
3550	t	Posto Shell Bruno Alves Portero	6385	t	f	-46,5613708496094	-23,5436305999756	5	4	307
3551	t	Posto Shell Panamericano	6387	t	f	-46,7357902526855	-23,4447898864746	3	2	308
3552	t	Posto Shell Nelson Scorsolini	6389	t	f	-47,7727127075195	-21,211181640625	7	2	309
3553	t	Posto Shell Fera de Itapevi	6390	t	f	-46,9360961914063	-23,5532131195068	3	4	310
3554	t	Posto Shell Jundiai Mirim	6391	t	f	-46,8735656738281	-23,1527824401855	6	4	311
3555	t	Posto Shell Ceiba Speciosa	6392	t	f	-47,285587310791	-23,2628803253174	8	2	312
3556	t	Posto Shell Castelinho de Sorocaba	6393	t	f	-47,3594131469727	-23,4261665344238	9	2	313
3557	t	Posto Shell Scofano e Scofano	6395	t	f	-45,5999870300293	-22,7442855834961	6	4	314
3558	t	Posto Shell Universitario Sao Carlos	6396	t	f	-47,8983001708984	-22,008752822876	7	2	315
3559	t	Posto Shell Mixam	6397	t	f	-51,3978500366211	-22,1396102905273	7	2	316
3560	t	Posto Shell Mediani Pires	6398	t	f	-49,3665084838867	-20,8251342773438	7	4	317
3561	t	Posto Shell Bela Cintra	6399	t	f	-46,6583137512207	-23,5534362792969	4	2	318
3562	t	Posto Shell Rio Claro Center Shopping	6400	t	f	-47,5562324523926	-22,4112205505371	7	4	319
3563	t	Posto Shell Itaipu Bassit	6401	t	f	-49,4026565551758	-20,8238735198975	7	4	320
3564	t	Posto Shell Primavera Murchid	6402	t	f	-49,3658294677734	-20,8273334503174	7	4	321
3565	t	Posto Shell Quinta do Golfe	6403	t	f	-49,404956817627	-20,831563949585	7	3	322
3566	t	Posto Shell Atarumin	6404	t	f	-49,3936424255371	-20,7923984527588	7	4	323
3567	t	Posto Shell Guaruja Andalo	6405	t	f	-49,3850555419922	-20,8229732513428	7	4	324
3568	t	Posto Shell Axr	6406	t	f	-49,3925590515137	-20,8228416442871	7	4	325
3569	t	Posto Shell Petro Bady	6407	t	f	-49,3955612182617	-20,8177738189697	7	4	326
3570	t	Posto Shell Avenida de Itatiba	6408	t	f	-46,8481254577637	-22,9981727600098	8	2	327
3571	t	Posto Shell Carrossel	6410	t	f	-46,5316505432129	-23,4745712280273	6	2	328
3572	t	Posto Shell Santos Dummont de Franca	6411	t	f	-47,4222793579102	-20,5426807403564	7	4	329
3573	t	Posto Shell Duque City	6412	t	f	-46,7061767578125	-23,5489521026611	3	4	330
3574	t	Posto Shell Hiperion	6413	t	f	-46,677417755127	-23,6105155944824	4	2	331
3575	t	Posto Shell Aguia de Haia	6415	t	f	-46,4766006469727	-23,5377807617188	5	2	332
3576	t	Posto Shell Acc Radial	6417	t	t	-46,5607452392578	-23,5375595092773	5	1	333
3577	t	Posto Shell Chacaras do Coelho	6418	t	f	-47,1672439575195	-22,888500213623	8	4	334
3578	t	Posto Shell Petrodutra	6419	t	f	-46,3821182250977	-23,4186706542969	6	2	335
3579	t	Posto Shell Vitoria	6420	t	f	-46,5677185058594	-23,6543788909912	5	2	336
3580	t	Posto Shell Sao Bernardo	6421	t	f	-46,5490036010742	-23,7172203063965	5	4	337
3581	t	Posto Shell Tigrão da Dutra	6422	t	f	-44,7013511657715	-22,5146884918213	5	4	338
3582	t	Posto Shell Sigma	6424	t	f	-46,999828338623	-22,9801940917969	8	4	339
3583	t	Posto Shell Perola de Ubatuba	6425	t	f	-45,0727272033691	-23,4354629516602	6	4	340
3584	t	Posto Shell Cassiano Ricardo	6426	t	f	-45,911548614502	-23,2231540679932	6	2	341
3585	t	Posto Shell AJ e AR	6428	t	f	-45,4009246826172	-23,6189403533936	6	3	342
3586	t	Posto Shell Golfe Clube	6432	t	f	-43,2552757263184	-22,9929752349854	2	4	343
3587	t	Posto Shell Modelo JMLBG	6434	t	f	-43,1931457519531	-22,9511528015137	2	4	344
3588	t	Posto Shell Catedral	6435	t	f	-43,1808853149414	-22,9133396148682	2	4	345
3589	t	Posto Shell Excede	6436	t	f	-43,2034568786621	-22,9669380187988	2	2	346
3590	t	Posto Shell Importação	6437	t	f	-43,223274230957	-22,9854888916016	2	4	347
3591	t	Posto Shell Hawai Rio	6438	t	f	-43,2097702026367	-22,80517578125	2	2	348
3592	t	Posto Shell Tirol	6440	t	f	-43,3330955505371	-22,9369144439697	2	3	349
3593	t	Posto Shell Grande Amor	6442	t	f	-43,4302024841309	-22,6249866485596	2	4	350
3594	t	Posto Shell Karapito da Beira	6443	t	f	-43,5541725158691	-22,8748226165771	2	4	351
3595	t	Posto Shell Barra Monteiro	6444	t	f	-43,565357208252	-22,9238033294678	2	4	352
3596	t	Posto Shell Portela Dois	6445	t	f	-43,671947479248	-22,8927917480469	2	4	353
3597	t	Posto Shell Amor da Leopoldina	6446	t	f	-43,2702178955078	-22,8307247161865	2	2	354
3598	t	Posto Shell Rocar Rio	6447	t	f	-43,3262634277344	-23,0020751953125	2	4	355
3599	t	Posto Shell Jardim Oceanico	6448	t	f	-43,3051567077637	-23,0122833251953	2	3	356
3600	t	Posto Shell Jardim Oceanico da Barra	6449	t	f	-43,3089485168457	-23,0065879821777	2	4	357
3601	t	Posto Shell Rezende Recreio II	6450	t	f	-43,4828147888184	-23,0181465148926	2	2	358
3602	t	Posto Shell Duck	6453	t	f	-43,2962265014648	-22,7948932647705	2	3	359
3603	t	Posto Shell Viaduto de Morato Eireli	6454	t	f	-46,745002746582	-23,2757873535156	6	3	360
3604	t	Posto Shell Borssato Serrazul	6455	t	f	-47,0101890563965	-23,1047992706299	8	2	361
3605	t	Posto Shell Siqueira e Carbonari	6456	t	f	-47,0448684692383	-23,1562004089355	8	2	362
3606	t	Posto Shell Maramar	6458	t	f	-43,5007171630859	-23,0206298828125	2	4	363
3607	t	Posto Shell Duque Conde Alphaville	6459	t	f	-46,8632431030273	-23,484504699707	3	2	364
3608	t	Posto Shell Brasil Santa Cruz	6461	t	f	-43,6580276489258	-22,8885860443115	2	4	365
3609	t	Posto Shell Estrela	6462	t	f	-46,8862380981445	-23,1748504638672	6	4	366
3610	t	Posto Shell Amigao de Itaborai	6463	t	f	-42,8120498657227	-22,7472591400146	2	3	367
3611	t	Posto Shell Amigão da Dutra	6464	t	f	-43,4762916564941	-22,7382507324219	2	3	368
3612	t	Posto Shell Araujo Leite	6465	t	f	-49,0669555664063	-22,3283977508545	7	2	369
3613	t	Posto Shell Nações Bauru	6466	t	f	-49,0637054443359	-22,325647354126	7	3	370
3614	t	Posto Shell Aeroporto Bauru	6468	t	f	-49,0520133972168	-22,3437061309814	7	2	371
3615	t	Posto Shell RodoPosto Maristela	6469	t	f	-48,4468612670898	-23,1385593414307	7	4	372
3616	t	Posto Shell Duque 21 de Moura	6470	t	f	-49,0558662414551	-22,3259410858154	7	2	373
3617	t	Posto Shell Limoeiro	6471	t	f	-49,5340995788574	-22,8074131011963	7	4	374
3618	t	Posto Shell Carbonari	6472	t	f	-48,4419021606445	-22,8623027801514	7	3	375
3619	t	Posto Shell Chalcataya	6473	t	f	-43,4737930297852	-23,0165157318115	2	2	376
3620	t	Posto Shell JPX	6474	t	f	-43,3752517700195	-23,0006504058838	2	2	377
3621	t	Posto Shell 2001	6475	t	f	-42,8556632995605	-22,7459888458252	2	4	378
3622	t	Posto Shell Quinze	6476	t	f	-43,4203491210938	-22,80153465271	2	2	379
3623	t	Posto Shell Arrastao	6477	t	f	-43,0044593811035	-22,8710193634033	2	2	380
3624	t	Posto Shell Gazpark Participaçoes	6478	t	f	-43,0285758972168	-22,8598480224609	2	4	381
3625	t	Posto Shell Meriti	6479	t	f	-43,3664588928223	-22,7934303283691	2	4	382
3626	t	Posto Shell Suina Derivados de Petroleo	6480	t	f	-44,0920944213867	-22,4929008483887	2	4	383
3627	t	Posto Shell Brasil 2000	6481	t	f	-43,5168190002441	-22,8603687286377	2	3	384
3628	t	Posto Shell Argetax Vila Guilherme	6484	t	f	-46,6002731323242	-23,5087356567383	6	2	385
3629	t	Posto Shell Portal de Santana	6486	t	f	-46,489185333252	-23,4239234924316	6	2	386
3630	t	Posto Shell Tasquinha	6487	t	f	-46,5430870056152	-22,9667434692383	6	4	387
3631	t	Posto Shell Flor da Luz	6489	t	f	-46,629753112793	-23,533224105835	4	4	388
3632	t	Posto Shell Progresso Eloy Chaves	6490	t	f	-46,9600944519043	-23,1872062683105	6	2	389
3633	t	Posto Shell Nova Suiça	6491	t	f	-47,209602355957	-23,0767574310303	8	2	390
3634	t	Posto Shell Pavao Castelinho	6492	t	f	-47,3460502624512	-23,4162292480469	9	2	391
3635	t	Posto Shell Gasparzinho	6494	t	f	-46,475040435791	-23,5236587524414	5	2	392
3636	t	Posto Shell Higienopolis Santo Andre	6496	t	f	-46,5397529602051	-23,6720561981201	5	2	393
3637	t	Posto Shell Pistao	6498	t	f	-43,3609771728516	-22,9272785186768	2	2	394
3638	t	Posto Shell Mato Alto	6499	t	f	-43,3602752685547	-22,9117012023926	2	2	395
3639	t	Posto Shell Kalota	6501	t	f	-46,5603637695313	-23,529125213623	5	2	396
3640	t	Posto Shell Europa Empreendimentos	6502	t	f	-46,543586730957	-22,9682731628418	6	2	397
3641	t	Posto Shell Arigato	6503	t	f	-46,4838600158691	-23,6246948242188	5	2	398
3642	t	Posto Shell Delta Mar	6504	t	f	-46,481819152832	-24,0266418457031	5	2	399
3643	t	Posto Shell IATE	6505	t	f	-43,1774444580078	-22,9499568939209	2	4	400
3644	t	Posto Shell Casa Nova	6506	t	f	-46,5505561828613	-23,5912017822266	5	3	401
3645	t	Posto Shell Senhor Barcelona	6507	t	f	-49,2314758300781	-25,5141277313232	1	4	402
3646	t	Posto Shell Malure	6508	t	t	-46,5779724121094	-23,5845146179199	5	1	403
3647	t	Posto Shell Rodovia de Bauru	6509	t	f	-49,0714454650879	-22,3120803833008	7	2	404
3648	t	Posto Shell Manhattam	6510	t	f	-50,4377708435059	-21,2285060882568	7	2	405
3649	t	Posto Shell Reyssol	6511	t	f	-48,1795539855957	-21,7790546417236	7	2	406
3650	t	Posto Shell Trapezio	6512	t	f	-46,5426292419434	-23,6027317047119	5	2	407
3651	t	Posto Shell Quatro Trevo	6514	t	f	-45,8832321166992	-23,2049407958984	6	2	408
3652	t	Posto Shell Campos do Jordao	6516	t	f	-45,5866813659668	-22,7345314025879	6	4	409
3653	t	Posto Shell Duque Moema	6521	t	f	-46,6674461364746	-23,6001758575439	4	2	410
3654	t	Posto Shell Trento	6522	t	f	-46,7908515930176	-23,563045501709	3	2	411
3655	t	Posto Shell Colossal	6523	t	f	-49,304615020752	-25,4450435638428	1	4	412
3656	t	Posto Shell Lipe	6525	t	f	-43,2929191589355	-22,8819103240967	2	2	413
3657	t	Posto Shell Margodete	6527	t	f	-46,570613861084	-23,5427589416504	5	4	414
3658	t	Posto Shell Galo Branco	6531	t	f	-47,4099922180176	-20,552267074585	7	2	415
3659	t	Posto Shell Antares	6532	t	f	-49,3347015380859	-25,4772758483887	1	4	416
3660	t	Posto Shell Copa Ouro	6533	t	f	-49,332462310791	-25,5117816925049	1	4	417
3661	t	Posto Shell Alameda Sacoma	6534	t	f	-46,6016235351563	-23,6191291809082	4	1	418
3662	t	Posto Shell Garage Lisboa	6535	t	f	-43,2775993347168	-22,8731594085693	2	4	419
3663	t	Posto Shell Aladin Servicos	6536	t	f	-49,348274230957	-25,4189128875732	1	4	420
3664	t	Posto Shell Lord Rodrigo	6537	t	f	-43,3039207458496	-22,7924098968506	2	4	421
3665	t	Posto Shell Verde Curitiba	6538	t	f	-49,2557678222656	-25,4069023132324	1	2	422
3666	t	Posto Shell Pedrazzoli	6539	t	f	-49,263744354248	-25,4684600830078	1	4	423
3667	t	Posto Shell Picheth	6541	t	f	-49,2740936279297	-25,5120887756348	1	4	424
3668	t	Posto Shell Ducati	6542	t	f	-49,2564544677734	-25,3914470672607	1	4	425
3669	t	Posto Shell Gisela	6543	t	f	-49,2497177124023	-25,4994068145752	1	4	426
3670	t	Posto Shell Premiere	6544	t	f	-49,3273391723633	-25,4355926513672	1	4	427
3671	t	Posto Shell Perola	6546	t	f	-49,2679252624512	-25,4434986114502	1	2	428
3672	t	Posto Shell Farol do Parque	6549	t	f	-49,343074798584	-25,4300270080566	1	4	429
3673	t	Posto Shell Jardim Botanico	6550	t	f	-49,2476768493652	-25,4466514587402	1	2	430
3674	t	Posto Shell Banc	6551	t	f	-51,1591567993164	-23,3422393798828	1	4	431
3675	t	Posto Shell Thiago Vinicius	6552	t	f	-51,1863784790039	-23,3005352020264	1	4	432
3676	t	Posto Shell Monza	6553	t	f	-43,0316696166992	-22,9467258453369	2	3	433
3677	t	Posto Shell Petrogil	6562	t	f	-51,9179649353027	-23,3959217071533	1	4	434
3678	t	Posto Shell Sao Jose 3	6563	t	f	-51,9374160766602	-23,4276027679443	1	4	435
3679	t	Posto Shell MLL	6564	t	f	-48,5520248413086	-25,5521106719971	1	4	436
3680	t	Posto Shell Artigas	6566	t	f	-49,1793937683105	-25,4510364532471	1	4	437
3681	t	Posto Shell NSL	6567	t	f	-49,1677703857422	-25,436206817627	1	4	438
3682	t	Posto Shell Paraiso Lubrificantes	6568	t	f	-44,4372062683105	-22,460018157959	2	4	439
3683	t	Posto Shell Cupim	6570	t	f	-49,1722373962402	-25,609546661377	1	4	440
3684	t	Posto Shell Rio Lima	6571	t	f	-43,3174819946289	-22,836784362793	2	3	441
3685	t	Posto Shell FM da Prata	6573	t	f	-43,4264984130859	-22,7609195709229	2	3	442
3686	t	Posto Shell Santa Amalia	6575	t	f	-43,6710929870605	-22,4099617004395	2	4	443
3687	t	Posto Shell Avenida Central de Iraja	6576	t	f	-43,565357208252	-22,9238033294678	2	4	444
3688	t	Posto Shell Casaca	6577	t	f	-42,9994506835938	-22,5633792877197	2	4	445
3689	t	Posto Shell LK Vila Universitaria	6578	t	f	-49,0538139343262	-22,3353710174561	7	3	446
3690	t	Posto Shell Galapagos	6580	t	f	-43,3512153625488	-22,8017559051514	2	3	447
3691	t	Posto Shell Big Aço	6581	t	f	-44,0861701965332	-22,5115299224854	2	4	448
3692	t	Posto Shell ALG	6591	t	f	-43,2584114074707	-22,8721122741699	2	4	449
3693	t	Posto Shell Monte Santo	6593	t	f	-47,4079437255859	-23,4176025390625	9	4	450
3694	t	Posto Shell Luches	6594	t	f	-48,4516677856445	-22,9245567321777	7	4	451
3695	t	Posto Shell A P F	6595	t	f	-44,0876502990723	-22,5124320983887	2	4	452
3696	t	Posto Shell Abreu Dois	6596	t	f	-42,9837417602539	-22,7848281860352	2	4	453
3697	t	Posto Shell LK Vila Falcao I	6598	t	f	-49,0855484008789	-22,331033706665	7	4	454
3698	t	Posto Shell Barra Cachamorra	6600	t	f	-43,5539932250977	-22,927490234375	2	4	455
3699	t	Posto Shell JB Caxias	6602	t	f	-43,2863540649414	-22,6785335540771	2	4	456
3700	t	Posto Shell Vitoria 040	6603	t	f	-43,2285804748535	-22,5168476104736	2	4	457
3701	t	Posto Shell Forgerini e Inouye São Carlos 	6604	t	f	-47,867431640625	-22,0105304718018	7	4	458
3702	t	Posto Shell Morro Azul de Itatiba	6605	t	f	-46,7489013671875	-23,0290908813477	6	4	459
3703	t	Posto Shell Colina Aracatuba	6606	t	f	-50,4446220397949	-21,2255001068115	7	4	460
3704	t	Posto Shell Forgerine e Inouye Itirapina	6609	t	f	-47,7402610778809	-22,2310695648193	7	4	461
3705	t	Posto Shell Cardoso Castro	6610	t	f	-43,4084548950195	-22,8215026855469	2	4	462
3706	t	Posto Shell Gran Penha	6611	t	f	-46,5262031555176	-23,5221843719482	5	1	463
3707	t	Posto Shell Abreu	6612	t	f	-43,0736083984375	-22,8137836456299	2	4	464
3708	t	Posto Shell Automix	6620	t	f	-46,5771064758301	-23,6905345916748	5	2	465
3709	t	Posto Shell Manguinhos de Buzios	6622	t	f	-41,9285278320313	-22,774227142334	2	4	466
3710	t	Posto Shell Boa Viagem Friburgo	6623	t	f	-42,5267562866211	-22,2953567504883	2	4	467
3711	t	Posto Shell Bola Pesada	6625	t	f	-46,6570091247559	-23,6123104095459	4	4	468
3712	t	Posto Shell LG	6627	t	f	-47,0722808837891	-22,8815288543701	8	2	469
3713	t	Posto Shell Almeida e L.Oveira	6628	t	f	-47,096321105957	-22,9103870391846	8	1	470
3714	t	Posto Shell Bolla Branca	6629	t	f	-45,9007759094238	-23,2230644226074	6	3	471
3715	t	Posto Shell Santa Luzia Atibaia	6630	t	f	-46,5802726745605	-23,1172657012939	6	2	472
3716	t	Posto Shell Santana Sao Jose dos Campos	6634	t	f	-45,8946685791016	-23,1637096405029	6	4	473
3717	t	Posto Shell Parambos	6652	t	f	-46,618522644043	-23,6123180389404	4	4	474
3718	t	Posto Shell Beraldo	6653	t	f	-46,5456352233887	-23,6473255157471	5	4	475
3719	t	Posto Shell Eco Posto	6654	t	t	-46,6665992736816	-23,6155242919922	4	1	476
3720	t	Posto Shell Sol da Dutra	6655	t	f	-45,6308135986328	-23,1021041870117	6	4	477
3721	t	Auto Posto Belezura	6656	t	f	-46,5836791992188	-23,5338306427002	5	2	478
3722	t	Posto Shell Via Ponte	6657	t	f	-43,1149482727051	-22,8878078460693	2	3	479
3723	t	Posto Shell Mike	6658	t	f	-46,6168518066406	-23,6857376098633	4	3	480
3724	t	Posto Shell Jardim Marajoara	6659	t	f	-46,6859741210938	-23,6600799560547	4	4	481
\.


--
-- Data for Name: abastece_evento; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY abastece_evento (id, active, data_planejado, data_realizado, number, resumo, base_id, employee_id, empresa_id, form_id, posto_id, entry_date) FROM stdin;
\.


--
-- Name: abastece_evento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('abastece_evento_id_seq', 1772, true);


--
-- Name: abastece_form_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('abastece_form_id_seq', 13, true);


--
-- Data for Name: abastece_item; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY abastece_item (id, active, name, model, maker, width, height, depth, prazocompra) FROM stdin;
\.


--
-- Data for Name: abastece_inventory; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY abastece_inventory (id, entrydate, item_new, item_used, item_broaked, item_id, warehouse_id) FROM stdin;
\.


--
-- Name: abastece_inventory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('abastece_inventory_id_seq', 1, false);


--
-- Name: abastece_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('abastece_item_id_seq', 1, false);


--
-- Data for Name: abastece_itemcontrolado; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY abastece_itemcontrolado (identificador, serial, assetnumber, item_id, warehouse_id, posto_id) FROM stdin;
\.


--
-- Name: abastece_modeloviatura_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('abastece_modeloviatura_id_seq', 2, true);


--
-- Data for Name: abastece_moveitem; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY abastece_moveitem (id, "timestamp", warehouse_dest_id, warehouse_origin_id) FROM stdin;
\.


--
-- Name: abastece_moveitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('abastece_moveitem_id_seq', 1, false);


--
-- Name: abastece_posto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('abastece_posto_id_seq', 3724, true);


--
-- Data for Name: abastece_punch; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY abastece_punch (id, active, in_time, out_time, entry_date, in_coordx, in_coordy, out_coordx, out_coordy, employee_id) FROM stdin;
\.


--
-- Name: abastece_punch_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('abastece_punch_id_seq', 1133, true);


--
-- Data for Name: abastece_tarefa; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY abastece_tarefa (id, active, number, status, description, name, start_date, end_date, start_coordx, start_coordy, end_coordx, end_coordy, employee_id, posto_id) FROM stdin;
\.


--
-- Name: abastece_tarefa_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('abastece_tarefa_id_seq', 1, false);


--
-- Name: abastece_viatura_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('abastece_viatura_id_seq', 10, true);


--
-- Name: abastece_warehouse_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('abastece_warehouse_id_seq', 1415, true);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY django_content_type (id, app_label, model) FROM stdin;
2	abastece	classe
3	abastece	modeloviatura
4	abastece	itemcontrolado
5	abastece	punch
6	abastece	tarefa
7	abastece	base
8	abastece	empresa
9	abastece	employee
10	abastece	moveitem
11	abastece	item
12	abastece	warehouse
13	abastece	viatura
14	abastece	form
15	abastece	inventory
16	abastece	posto
17	abastece	evento
18	admin	logentry
19	auth	user
20	auth	group
21	auth	permission
22	contenttypes	contenttype
23	sessions	session
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
4	Can add classe	2	add_classe
5	Can change classe	2	change_classe
6	Can delete classe	2	delete_classe
7	Can add modelo viatura	3	add_modeloviatura
8	Can change modelo viatura	3	change_modeloviatura
9	Can delete modelo viatura	3	delete_modeloviatura
10	Can add item controlado	4	add_itemcontrolado
11	Can change item controlado	4	change_itemcontrolado
12	Can delete item controlado	4	delete_itemcontrolado
13	Can add punch	5	add_punch
14	Can change punch	5	change_punch
15	Can delete punch	5	delete_punch
16	Can add tarefa	6	add_tarefa
17	Can change tarefa	6	change_tarefa
18	Can delete tarefa	6	delete_tarefa
19	Can add base	7	add_base
20	Can change base	7	change_base
21	Can delete base	7	delete_base
22	Can add empresa	8	add_empresa
23	Can change empresa	8	change_empresa
24	Can delete empresa	8	delete_empresa
25	Can add employee	9	add_employee
26	Can change employee	9	change_employee
27	Can delete employee	9	delete_employee
28	Can add move item	10	add_moveitem
29	Can change move item	10	change_moveitem
30	Can delete move item	10	delete_moveitem
31	Can add item	11	add_item
32	Can change item	11	change_item
33	Can delete item	11	delete_item
34	Can add warehouse	12	add_warehouse
35	Can change warehouse	12	change_warehouse
36	Can delete warehouse	12	delete_warehouse
37	Can add viatura	13	add_viatura
38	Can change viatura	13	change_viatura
39	Can delete viatura	13	delete_viatura
40	Can add form	14	add_form
41	Can change form	14	change_form
42	Can delete form	14	delete_form
43	Can add inventory	15	add_inventory
44	Can change inventory	15	change_inventory
45	Can delete inventory	15	delete_inventory
46	Can add posto	16	add_posto
47	Can change posto	16	change_posto
48	Can delete posto	16	delete_posto
49	Can add evento	17	add_evento
50	Can change evento	17	change_evento
51	Can delete evento	17	delete_evento
52	Can add log entry	18	add_logentry
53	Can change log entry	18	change_logentry
54	Can delete log entry	18	delete_logentry
55	Can add user	19	add_user
56	Can change user	19	change_user
57	Can delete user	19	delete_user
58	Can add group	20	add_group
59	Can change group	20	change_group
60	Can delete group	20	delete_group
61	Can add permission	21	add_permission
62	Can change permission	21	change_permission
63	Can delete permission	21	delete_permission
64	Can add content type	22	add_contenttype
65	Can change content type	22	change_contenttype
66	Can delete content type	22	delete_contenttype
67	Can add session	23	add_session
68	Can change session	23	change_session
69	Can delete session	23	delete_session
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('auth_permission_id_seq', 69, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$30000$3DIHtrYRg1KX$Wv75NJnhXo9GlmLqxt2cnqUkj8FSqYQgviANhTNwuF8=	2017-01-17 20:10:52.201833-02	t	cezar.santanna			cezar.santanna@e2i9.com	t	t	2017-01-04 11:31:04.454759-02
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2017-01-04 11:31:44.688559-02	1	SP01 - Wesley	1	[{"added": {}}]	9	1
2	2017-01-04 11:31:49.475014-02	2	SP02 - Alex	1	[{"added": {}}]	9	1
3	2017-01-04 11:31:54.110468-02	3	SP03 - Italo	1	[{"added": {}}]	9	1
4	2017-01-04 11:32:12.121084-02	4	SP04 - Nenhum	1	[{"added": {}}]	9	1
5	2017-01-04 11:32:17.062052-02	5	SP05 - Fabio	1	[{"added": {}}]	9	1
6	2017-01-04 11:32:21.451957-02	6	SP06 - Diego	1	[{"added": {}}]	9	1
7	2017-01-04 11:32:27.549347-02	7	PR01 - Adélio	1	[{"added": {}}]	9	1
8	2017-01-04 11:32:32.858597-02	8	RJ01 - Vitor	1	[{"added": {}}]	9	1
9	2017-01-04 11:32:39.782001-02	9	SOR01 - Wellington	1	[{"added": {}}]	9	1
10	2017-01-04 11:32:45.181548-02	10	SOR02 - Raphael	1	[{"added": {}}]	9	1
11	2017-01-04 11:33:07.993352-02	1	E2i9	1	[{"added": {}}]	8	1
12	2017-01-04 11:33:12.697431-02	2	UNICOM	1	[{"added": {}}]	8	1
13	2017-01-04 11:34:38.849011-02	1	AÇÕES DE MELHORIA	1	[{"added": {}}]	14	1
14	2017-01-04 11:34:47.408216-02	2	CORRETIVA	1	[{"added": {}}]	14	1
15	2017-01-04 11:35:00.062454-02	3	DESINSTALAÇÃO DO POSTO	1	[{"added": {}}]	14	1
16	2017-01-04 11:35:08.973882-02	4	INVENTÁRIO	1	[{"added": {}}]	14	1
17	2017-01-04 11:35:16.007075-02	5	ANTENA 915	1	[{"added": {}}]	14	1
18	2017-01-04 11:35:25.256109-02	6	PLANO VERÃO	1	[{"added": {}}]	14	1
19	2017-01-04 11:35:30.891823-02	7	PREDITIVA	1	[{"added": {}}]	14	1
20	2017-01-04 11:35:37.553591-02	8	PREVENTIVA	1	[{"added": {}}]	14	1
21	2017-01-04 11:35:59.316814-02	9	RETIRADA ANTENA 5.8	1	[{"added": {}}]	14	1
22	2017-01-04 14:27:10.369224-02	1	E2i9 - Sorocaba	1	[{"added": {}}]	12	1
23	2017-01-04 14:27:33.459902-02	1	E2i9 - Central	2	[{"changed": {"fields": ["name"]}}]	12	1
24	2017-01-04 14:27:41.8364-02	2	E2i9 - SP01	1	[{"added": {}}]	12	1
25	2017-01-04 14:27:48.153379-02	3	E2i9 - SP02	1	[{"added": {}}]	12	1
26	2017-01-04 14:27:54.188132-02	4	E2i9 - SP03	1	[{"added": {}}]	12	1
27	2017-01-04 14:28:00.372252-02	5	E2i9 - SP04	1	[{"added": {}}]	12	1
28	2017-01-04 14:28:07.846946-02	6	E2i9 - SP05	1	[{"added": {}}]	12	1
29	2017-01-04 14:28:14.500947-02	7	E2i9 - SP06	1	[{"added": {}}]	12	1
30	2017-01-04 14:28:21.356735-02	8	E2i9 - SOR01	1	[{"added": {}}]	12	1
31	2017-01-04 14:28:31.24649-02	9	E2i9 - SOR02	1	[{"added": {}}]	12	1
32	2017-01-04 14:28:38.031866-02	10	E2i9 - PR01	1	[{"added": {}}]	12	1
33	2017-01-04 14:28:48.376661-02	11	E2i9 - RJ01	1	[{"added": {}}]	12	1
34	2017-01-04 14:29:31.294294-02	9	E2i9 - SP07	2	[{"changed": {"fields": ["name"]}}]	12	1
35	2017-01-04 14:30:42.699667-02	1	A	1	[{"added": {}}]	2	1
36	2017-01-04 14:30:46.342781-02	2	B	1	[{"added": {}}]	2	1
37	2017-01-04 14:30:59.392637-02	3	C	1	[{"added": {}}]	2	1
38	2017-01-04 14:31:02.061292-02	4	D	1	[{"added": {}}]	2	1
39	2017-01-04 14:37:52.573381-02	12	Postos	1	[{"added": {}}]	12	1
40	2017-01-04 14:37:58.563687-02	13	Sem Parar	1	[{"added": {}}]	12	1
41	2017-01-04 14:38:20.610124-02	14	Perdas	1	[{"added": {}}]	12	1
42	2017-01-04 14:50:36.626494-02	10	SINALIZAÇÃO	1	[{"added": {}}]	14	1
43	2017-01-04 15:41:47.572558-02	1	HR	1	[{"added": {}}]	3	1
44	2017-01-04 15:41:56.828595-02	2	Saveiro	1	[{"added": {}}]	3	1
45	2017-01-18 11:33:50.63087-02	12	Postos	3		12	1
46	2017-01-18 14:22:12.492313-02	10	Raphael	2	[{"changed": {"fields": ["name"]}}]	9	1
47	2017-01-18 14:22:20.900132-02	9	Wellington	2	[{"changed": {"fields": ["name"]}}]	9	1
48	2017-01-18 14:22:28.174837-02	8	Vitor	2	[{"changed": {"fields": ["name"]}}]	9	1
49	2017-01-18 14:22:57.759805-02	7	Adélio	2	[{"changed": {"fields": ["name"]}}]	9	1
50	2017-01-18 14:23:04.537433-02	6	Diego	2	[{"changed": {"fields": ["name"]}}]	9	1
51	2017-01-18 14:23:14.996108-02	6	Roberto	2	[{"changed": {"fields": ["name"]}}]	9	1
52	2017-01-18 14:23:26.799148-02	5	SP05	2	[{"changed": {"fields": ["name"]}}]	9	1
53	2017-01-18 14:23:39.092553-02	4	Weslei	2	[{"changed": {"fields": ["name"]}}]	9	1
54	2017-01-18 14:23:46.109254-02	3	Italo	2	[{"changed": {"fields": ["name"]}}]	9	1
55	2017-01-18 14:23:54.218772-02	2	Alex	2	[{"changed": {"fields": ["name"]}}]	9	1
56	2017-01-18 14:24:02.580179-02	1	Renan	2	[{"changed": {"fields": ["name"]}}]	9	1
57	2017-01-18 14:52:21.942078-02	1	PYF9835	1	[{"added": {}}]	13	1
58	2017-01-18 14:52:40.834182-02	2	PYF9836	1	[{"added": {}}]	13	1
59	2017-01-18 14:53:06.218972-02	3	GIL7206	1	[{"added": {}}]	13	1
60	2017-01-18 14:53:56.318557-02	4	GJD1194	1	[{"added": {}}]	13	1
61	2017-01-18 14:54:17.304012-02	5	Matheus	2	[{"changed": {"fields": ["name"]}}]	9	1
62	2017-01-18 14:54:39.331182-02	5	GKI2072	1	[{"added": {}}]	13	1
63	2017-01-18 14:54:58.159601-02	6	FRG8831	1	[{"added": {}}]	13	1
64	2017-01-18 14:55:14.953833-02	7	FRS0679	1	[{"added": {}}]	13	1
65	2017-01-18 14:55:47.997355-02	8	FZB8670	1	[{"added": {}}]	13	1
66	2017-01-18 14:56:05.385434-02	9	FWO8127	1	[{"added": {}}]	13	1
67	2017-01-18 14:56:21.167306-02	10	FJM0589	1	[{"added": {}}]	13	1
68	2017-01-18 15:03:51.25016-02	1	PR01	1	[{"added": {}}]	7	1
69	2017-01-18 15:04:37.854718-02	2	RJ01	1	[{"added": {}}]	7	1
70	2017-01-18 15:09:26.984203-02	3	SP01	1	[{"added": {}}]	7	1
71	2017-01-18 15:10:32.715135-02	4	SP02	1	[{"added": {}}]	7	1
72	2017-01-18 15:11:28.780362-02	4	SP02	2	[]	7	1
73	2017-01-18 15:12:07.67023-02	5	SP03	1	[{"added": {}}]	7	1
74	2017-01-18 15:12:39.43333-02	6	SP04	1	[{"added": {}}]	7	1
75	2017-01-18 15:13:12.549589-02	7	SP05	1	[{"added": {}}]	7	1
76	2017-01-18 15:13:38.565861-02	8	SP06	1	[{"added": {}}]	7	1
77	2017-01-18 15:14:36.832747-02	9	SP07	1	[{"added": {}}]	7	1
78	2017-01-18 15:15:05.05098-02	10	SOR01	1	[{"added": {}}]	7	1
79	2017-01-18 15:39:56.372482-02	442	Posto Shell FM da Prata	2	[{"changed": {"fields": ["name"]}}]	12	1
80	2017-01-18 16:18:17.339604-02	3	Ítalo	2	[{"changed": {"fields": ["name"]}}]	9	1
81	2017-01-18 16:48:21.892554-02	2	INC0197401	3		17	1
82	2017-01-18 16:50:00.990939-02	3	INC0197401	3		17	1
83	2017-01-18 16:50:48.934096-02	11	INSTALAÇÃO ICR	1	[{"added": {}}]	14	1
84	2017-01-18 16:51:14.848411-02	12	SURVEY	1	[{"added": {}}]	14	1
85	2017-01-18 16:51:38.393834-02	13	DESINSTALAÇÃO DO POSTO	1	[{"added": {}}]	14	1
86	2017-01-18 17:07:48.315487-02	554	INC0197401	3		17	1
87	2017-01-18 17:07:48.331719-02	553	INC0198051	3		17	1
88	2017-01-18 17:07:48.340013-02	552	TASK0158655	3		17	1
89	2017-01-18 17:07:48.348418-02	551	INC0198350	3		17	1
90	2017-01-18 17:07:48.356727-02	550	TASK0158655	3		17	1
91	2017-01-18 17:07:48.365049-02	549	INC0197515	3		17	1
92	2017-01-18 17:07:48.373408-02	548	INC0198225	3		17	1
93	2017-01-18 17:07:48.381708-02	547	TASK0164414	3		17	1
94	2017-01-18 17:07:48.390197-02	546	TAsk0125446	3		17	1
95	2017-01-18 17:07:48.398525-02	545	INC0198257	3		17	1
96	2017-01-18 17:07:48.406906-02	544	TASK0125443	3		17	1
97	2017-01-18 17:07:48.415193-02	543	TASK0164303	3		17	1
98	2017-01-18 17:07:48.423559-02	542	INC0198049	3		17	1
99	2017-01-18 17:07:48.431664-02	541	TASK0164303	3		17	1
100	2017-01-18 17:07:48.440039-02	540	INC0198009	3		17	1
101	2017-01-18 17:07:48.44834-02	539	INC0198395	3		17	1
102	2017-01-18 17:07:48.456742-02	538	TASK0164230	3		17	1
103	2017-01-18 17:07:48.465461-02	537	TASK0164230	3		17	1
104	2017-01-18 17:07:48.47362-02	536	INC0198116	3		17	1
105	2017-01-18 17:07:48.481912-02	535	INC0197898	3		17	1
106	2017-01-18 17:07:48.490233-02	534	INC0198053	3		17	1
107	2017-01-18 17:07:48.498591-02	533	INC0197826	3		17	1
108	2017-01-18 17:07:48.506902-02	532	INC0198149	3		17	1
109	2017-01-18 17:07:48.515226-02	531	TASK0164227	3		17	1
110	2017-01-18 17:07:48.523592-02	530	INC0197789	3		17	1
111	2017-01-18 17:07:48.531908-02	529	INC0198169	3		17	1
112	2017-01-18 17:07:48.54025-02	528	INC0198241	3		17	1
113	2017-01-18 17:07:48.54854-02	527	INC0197982	3		17	1
114	2017-01-18 17:07:48.55682-02	526	INC0198000	3		17	1
115	2017-01-18 17:07:48.565263-02	525	INC0197878	3		17	1
116	2017-01-18 17:07:48.573585-02	524	TASK0161473	3		17	1
117	2017-01-18 17:07:48.581905-02	523	TASK0161473	3		17	1
118	2017-01-18 17:07:48.590212-02	522	TASK0131832	3		17	1
119	2017-01-18 17:07:48.598643-02	521	TASK0131832	3		17	1
120	2017-01-18 17:07:48.606865-02	520	TASK0131832	3		17	1
121	2017-01-18 17:07:48.615295-02	519	INC0197470	3		17	1
122	2017-01-18 17:07:48.623602-02	518	INC0197476	3		17	1
123	2017-01-18 17:07:48.631982-02	517	INC0197689	3		17	1
124	2017-01-18 17:07:48.640348-02	516	INC0197653	3		17	1
125	2017-01-18 17:07:48.648591-02	515	INC0197646	3		17	1
126	2017-01-18 17:07:48.656959-02	514	INC0197472	3		17	1
127	2017-01-18 17:07:48.665296-02	513	TASK0163833	3		17	1
128	2017-01-18 17:07:48.673606-02	512	TASk0163833	3		17	1
129	2017-01-18 17:07:48.681977-02	511	INC0197423	3		17	1
130	2017-01-18 17:07:48.690292-02	510	INC0197315	3		17	1
131	2017-01-18 17:07:48.69859-02	509	TASK0163839	3		17	1
132	2017-01-18 17:07:48.706865-02	508	TASK0163839	3		17	1
133	2017-01-18 17:07:48.715277-02	507	INC0197223	3		17	1
134	2017-01-18 17:07:48.723629-02	506	INC0197462	3		17	1
135	2017-01-18 17:07:48.731947-02	505	INC0197466	3		17	1
136	2017-01-18 17:07:48.740313-02	504	INC0197464	3		17	1
137	2017-01-18 17:07:48.748656-02	503	INC0197507	3		17	1
138	2017-01-18 17:07:48.756955-02	502	TASK0163819	3		17	1
139	2017-01-18 17:07:48.765404-02	501	INC0197481	3		17	1
140	2017-01-18 17:07:48.773759-02	500	INC0197478	3		17	1
141	2017-01-18 17:07:48.782107-02	499	INC0197238	3		17	1
142	2017-01-18 17:07:48.790364-02	498	TASK0163614	3		17	1
143	2017-01-18 17:07:48.798715-02	497	INC0197001	3		17	1
144	2017-01-18 17:07:48.806955-02	496	INC0197238	3		17	1
145	2017-01-18 17:07:48.81525-02	495	INC0196800	3		17	1
146	2017-01-18 17:07:48.823538-02	494	TASK0161959	3		17	1
147	2017-01-18 17:07:48.831992-02	493	INC0196764	3		17	1
148	2017-01-18 17:07:48.840325-02	492	INC0196825	3		17	1
149	2017-01-18 17:07:48.848663-02	491	INC0196742	3		17	1
150	2017-01-18 17:07:48.85698-02	490	TASK0	3		17	1
151	2017-01-18 17:07:48.865308-02	489	INC0196882	3		17	1
152	2017-01-18 17:07:48.873627-02	488	TASK0163224	3		17	1
153	2017-01-18 17:07:48.8822-02	487	TASK0163336	3		17	1
154	2017-01-18 17:07:48.907126-02	486	INC0196741	3		17	1
155	2017-01-18 17:07:48.965555-02	485	TASK0163335	3		17	1
156	2017-01-18 17:07:49.007015-02	484	INC0196207	3		17	1
157	2017-01-18 17:07:49.040328-02	483	INC0196672	3		17	1
158	2017-01-18 17:07:49.048652-02	482	TASK0162990	3		17	1
159	2017-01-18 17:07:49.056966-02	481	TASK0162990	3		17	1
160	2017-01-18 17:07:49.065344-02	480	INC0196281	3		17	1
161	2017-01-18 17:07:49.073616-02	479	INC0196636	3		17	1
162	2017-01-18 17:07:49.082066-02	478	task0135637	3		17	1
163	2017-01-18 17:07:49.090328-02	477	task0135637	3		17	1
164	2017-01-18 17:07:49.098568-02	476	TASK0162136	3		17	1
165	2017-01-18 17:07:49.10707-02	475	TASK0162136	3		17	1
166	2017-01-18 17:07:49.11527-02	474	TASK0162863	3		17	1
167	2017-01-18 17:07:49.123569-02	473	TASK0162863	3		17	1
168	2017-01-18 17:07:49.1319-02	472	INC0196790	3		17	1
169	2017-01-18 17:07:49.140265-02	471	INC0196493	3		17	1
170	2017-01-18 17:07:49.14856-02	470	INC0196176	3		17	1
171	2017-01-18 17:07:49.156898-02	469	0196337	3		17	1
172	2017-01-18 17:07:49.164991-02	468	INC0196114	3		17	1
173	2017-01-18 17:07:49.173334-02	467	INC0196352	3		17	1
174	2017-01-18 17:07:49.181641-02	466	task0160092	3		17	1
175	2017-01-18 17:07:49.190164-02	465	tasc0160092	3		17	1
176	2017-01-18 17:07:49.198632-02	464	task0160092	3		17	1
177	2017-01-18 17:07:49.206918-02	463	task0160092	3		17	1
178	2017-01-18 17:07:49.215237-02	462	TASK0162452	3		17	1
179	2017-01-18 17:07:49.22352-02	461	TASK0162452	3		17	1
180	2017-01-18 17:07:49.232062-02	460	INC0195715	3		17	1
181	2017-01-18 17:07:49.24031-02	459	TASK0262439	3		17	1
182	2017-01-18 17:07:49.248629-02	458	INC0195810	3		17	1
183	2017-01-18 17:07:49.256834-02	457	TASK0162439	3		17	1
184	2017-01-18 17:07:49.265267-02	456	INC0196059	3		17	1
185	2017-01-18 17:07:49.273609-02	455	inc0196219	3		17	1
186	2017-01-18 17:07:49.281933-02	454	INC0196228	3		17	1
187	2017-01-18 17:07:49.290264-02	453	INC0196216	3		17	1
188	2017-01-18 17:07:49.298555-02	452	inc0198952	3		17	1
189	2017-01-18 17:07:49.306856-02	451	Inc0196200	3		17	1
190	2017-01-18 17:07:49.315483-02	450	TASK0162185	3		17	1
191	2017-01-18 17:07:49.323619-02	449	TASK0162185	3		17	1
192	2017-01-18 17:07:49.332029-02	448	0182181	3		17	1
193	2017-01-18 17:07:49.340458-02	447	task0162181	3		17	1
194	2017-01-18 17:07:49.348663-02	446	INC0195988	3		17	1
195	2017-01-18 17:07:49.356994-02	445	INC0195884	3		17	1
196	2017-01-18 17:07:49.365353-02	444	TASK0162184	3		17	1
197	2017-01-18 17:07:49.373667-02	443	TASK0162184	3		17	1
198	2017-01-18 17:07:49.382075-02	442	INC0195470	3		17	1
199	2017-01-18 17:07:49.390462-02	441	INC0196211	3		17	1
200	2017-01-18 17:07:49.398749-02	440	INC0195472	3		17	1
201	2017-01-18 17:07:49.407116-02	439	TASK0161448	3		17	1
202	2017-01-18 17:07:49.415399-02	438	TASK0161448	3		17	1
203	2017-01-18 17:07:49.42364-02	437	TASK0162175	3		17	1
204	2017-01-18 17:07:49.43196-02	436	TASK0161964	3		17	1
205	2017-01-18 17:07:49.440309-02	435	inc0195767	3		17	1
206	2017-01-18 17:07:49.44865-02	434	TASK0162175	3		17	1
207	2017-01-18 17:07:49.456981-02	433	TASK0161964	3		17	1
208	2017-01-18 17:07:49.465329-02	432	INC0195713	3		17	1
209	2017-01-18 17:07:49.473609-02	431	INC0196025	3		17	1
210	2017-01-18 17:07:49.482006-02	430	INC0195756	3		17	1
211	2017-01-18 17:07:49.490334-02	429	Inc0195414	3		17	1
212	2017-01-18 17:07:49.498732-02	428	INC0195453	3		17	1
213	2017-01-18 17:07:49.507153-02	427	INC0195520	3		17	1
214	2017-01-18 17:07:49.515479-02	426	INC0195249	3		17	1
215	2017-01-18 17:07:49.523776-02	425	Inc0195302	3		17	1
216	2017-01-18 17:07:49.532124-02	424	INC0195740	3		17	1
217	2017-01-18 17:07:49.540471-02	423	TASK0161959	3		17	1
218	2017-01-18 17:07:49.548808-02	422	INC0195674	3		17	1
219	2017-01-18 17:07:49.557121-02	421	INC0195716	3		17	1
220	2017-01-18 17:07:49.565416-02	420	INC0195488	3		17	1
221	2017-01-18 17:07:49.573756-02	419	INC0195171	3		17	1
222	2017-01-18 17:07:49.582089-02	418	TASK0161880	3		17	1
223	2017-01-18 17:07:49.59041-02	417	task0161887	3		17	1
224	2017-01-18 17:07:49.598737-02	416	INC0195660	3		17	1
225	2017-01-18 17:07:49.607201-02	415	INC0195670	3		17	1
226	2017-01-18 17:07:49.615388-02	414	INC0195481	3		17	1
227	2017-01-18 17:07:49.623679-02	413	TASK0161887	3		17	1
228	2017-01-18 17:07:49.632071-02	412	INC0195535	3		17	1
229	2017-01-18 17:07:49.640506-02	411	0195613	3		17	1
230	2017-01-18 17:07:49.648803-02	410	INC0195652	3		17	1
231	2017-01-18 17:07:49.657161-02	409	TASK0161877	3		17	1
232	2017-01-18 17:07:49.665537-02	408	TASK0161877	3		17	1
233	2017-01-18 17:07:49.673883-02	407	INC0195585	3		17	1
234	2017-01-18 17:07:49.682195-02	406	INC0195491	3		17	1
235	2017-01-18 17:07:49.690434-02	405	TASK0157086	3		17	1
236	2017-01-18 17:07:49.698747-02	404	TASK0157086	3		17	1
237	2017-01-18 17:07:49.74874-02	403	task0158683	3		17	1
238	2017-01-18 17:07:49.756946-02	402	INC0195173	3		17	1
239	2017-01-18 17:07:49.765321-02	401	TASK0161466	3		17	1
240	2017-01-18 17:07:49.773622-02	400	INC0195320	3		17	1
241	2017-01-18 17:07:49.782011-02	399	TASK0161466	3		17	1
242	2017-01-18 17:07:49.790276-02	398	INC0195174	3		17	1
243	2017-01-18 17:07:49.798626-02	397	INC0194192	3		17	1
244	2017-01-18 17:07:49.806909-02	396	INC0195053	3		17	1
245	2017-01-18 17:07:49.815316-02	395	inc0194845	3		17	1
246	2017-01-18 17:07:49.823651-02	394	TASK0161117	3		17	1
247	2017-01-18 17:07:49.831932-02	393	TASK0161117	3		17	1
248	2017-01-18 17:07:49.840492-02	392	TASK0158977	3		17	1
249	2017-01-18 17:07:49.848751-02	391	TASK0158977	3		17	1
250	2017-01-18 17:07:49.857025-02	390	INC0194945	3		17	1
251	2017-01-18 17:07:49.865295-02	389	INC0194513	3		17	1
252	2017-01-18 17:07:49.873798-02	388	TASK0119411	3		17	1
253	2017-01-18 17:07:49.881943-02	387	TASK0119411	3		17	1
254	2017-01-18 17:07:49.89038-02	386	TASK0119411	3		17	1
255	2017-01-18 17:07:49.898675-02	385	TASK0119411	3		17	1
256	2017-01-18 17:07:49.907131-02	384	INC0194883	3		17	1
257	2017-01-18 17:07:49.915245-02	383	INC0194972	3		17	1
258	2017-01-18 17:07:49.923664-02	382	TASK0161099	3		17	1
259	2017-01-18 17:07:49.932017-02	381	TASK0161099	3		17	1
260	2017-01-18 17:07:49.940336-02	380	INC0194886	3		17	1
261	2017-01-18 17:07:49.948675-02	379	Inc0194749	3		17	1
262	2017-01-18 17:07:49.957013-02	378	inc0194880	3		17	1
263	2017-01-18 17:07:49.965483-02	377	INC9194555	3		17	1
264	2017-01-18 17:07:49.973834-02	376	TASK0160770	3		17	1
265	2017-01-18 17:07:49.982193-02	375	TASK0160770	3		17	1
266	2017-01-18 17:07:49.990523-02	374	INC0190084	3		17	1
267	2017-01-18 17:07:49.998785-02	373	INC0194064	3		17	1
268	2017-01-18 17:07:50.007405-02	372	inc0194783	3		17	1
269	2017-01-18 17:07:50.015582-02	371	tasc0194563	3		17	1
270	2017-01-18 17:07:50.023744-02	370	TASK0159433	3		17	1
271	2017-01-18 17:07:50.032232-02	369	TASK0159433	3		17	1
272	2017-01-18 17:07:50.040501-02	368	TASK01259433	3		17	1
273	2017-01-18 17:07:50.048821-02	367	TASK0159433	3		17	1
274	2017-01-18 17:07:50.057106-02	366	TASK0160778	3		17	1
275	2017-01-18 17:07:50.065466-02	365	TASK0160778	3		17	1
276	2017-01-18 17:07:50.073763-02	364	Inc0194620	3		17	1
277	2017-01-18 17:07:50.082114-02	363	INC0194542	3		17	1
278	2017-01-18 17:07:50.090501-02	362	TASK0151540	3		17	1
279	2017-01-18 17:07:50.09879-02	361	TASK0151540	3		17	1
280	2017-01-18 17:07:50.107098-02	360	TASK0151540	3		17	1
281	2017-01-18 17:07:50.115491-02	359	TASK0160095	3		17	1
282	2017-01-18 17:07:50.123854-02	358	TASK0160094	3		17	1
283	2017-01-18 17:07:50.132183-02	357	TASK0160095	3		17	1
284	2017-01-18 17:07:50.140613-02	356	TASK00160095	3		17	1
285	2017-01-18 17:07:50.148918-02	355	INC0193920	3		17	1
286	2017-01-18 17:07:50.157227-02	354	TASK0160471	3		17	1
287	2017-01-18 17:07:50.165555-02	353	TASK0160471	3		17	1
288	2017-01-18 17:07:50.173876-02	352	TASK0160471	3		17	1
289	2017-01-18 17:07:50.182209-02	351	INC0193983	3		17	1
290	2017-01-18 17:07:50.190475-02	350	TASK0160436	3		17	1
291	2017-01-18 17:07:50.19885-02	349	TASK0160436	3		17	1
292	2017-01-18 17:07:50.207241-02	348	0194070	3		17	1
293	2017-01-18 17:07:50.215541-02	347	TASK159437	3		17	1
294	2017-01-18 17:07:50.223869-02	346	TASK159437	3		17	1
295	2017-01-18 17:07:50.232175-02	344	TASK0159892	3		17	1
296	2017-01-18 17:07:50.240539-02	343	TASK0159892	3		17	1
297	2017-01-18 17:07:50.248865-02	342	TASK0159892	3		17	1
298	2017-01-18 17:07:50.257245-02	341	TASK0138409	3		17	1
299	2017-01-18 17:07:50.265486-02	340	TASK0138409	3		17	1
300	2017-01-18 17:07:50.273914-02	339	TASK0138409	3		17	1
301	2017-01-18 17:07:50.282394-02	338	TASK0138409	3		17	1
302	2017-01-18 17:07:50.29067-02	337	TASK0159946	3		17	1
303	2017-01-18 17:07:50.299007-02	336	INC0193823	3		17	1
304	2017-01-18 17:07:50.307261-02	335	0159538	3		17	1
305	2017-01-18 17:07:50.315578-02	334	0159438	3		17	1
306	2017-01-18 17:07:50.324035-02	333	0159438	3		17	1
307	2017-01-18 17:07:50.332352-02	332	INC0193665	3		17	1
308	2017-01-18 17:07:50.340678-02	331	INC0193983\t	3		17	1
309	2017-01-18 17:07:50.348973-02	330	TASK0159947	3		17	1
310	2017-01-18 17:07:50.357221-02	329	TASK0159947	3		17	1
311	2017-01-18 17:07:50.365646-02	328	INC0193666	3		17	1
312	2017-01-18 17:07:50.373846-02	327	TASK0159947	3		17	1
313	2017-01-18 17:07:50.382251-02	326	TASK0159947	3		17	1
314	2017-01-18 17:07:50.390591-02	325	INC0194066	3		17	1
315	2017-01-18 17:07:50.398899-02	324	TASK0159888	3		17	1
316	2017-01-18 17:07:50.407277-02	323	TASK0159888	3		17	1
317	2017-01-18 17:07:50.415649-02	322	0193822	3		17	1
318	2017-01-18 17:07:50.423992-02	321	INC0192962	3		17	1
319	2017-01-18 17:07:50.432415-02	320	TASK0159440	3		17	1
320	2017-01-18 17:07:50.440793-02	319	TASK0159440	3		17	1
321	2017-01-18 17:07:50.448993-02	318	TASK0159440	3		17	1
322	2017-01-18 17:07:50.457366-02	317	TASK0159431	3		17	1
323	2017-01-18 17:07:50.465689-02	316	TASK0119403	3		17	1
324	2017-01-18 17:07:50.473924-02	315	TASK0119403	3		17	1
325	2017-01-18 17:07:50.482311-02	314	TASK0119403	3		17	1
326	2017-01-18 17:07:50.490635-02	313	TASK0119422	3		17	1
327	2017-01-18 17:07:50.498971-02	312	0159434	3		17	1
328	2017-01-18 17:07:50.507219-02	311	TASK0159436	3		17	1
329	2017-01-18 17:07:50.515616-02	310	0144334	3		17	1
330	2017-01-18 17:07:50.52389-02	309	0144334	3		17	1
331	2017-01-18 17:07:50.532215-02	308	0144334	3		17	1
332	2017-01-18 17:07:50.54057-02	307	0144334	3		17	1
333	2017-01-18 17:07:50.548939-02	306	INC0193825	3		17	1
334	2017-01-18 17:07:50.557269-02	305	INC0193757/INC019371	3		17	1
335	2017-01-18 17:07:50.56566-02	304	TASK0119422	3		17	1
336	2017-01-18 17:07:50.574035-02	303	TASK0119422	3		17	1
337	2017-01-18 17:07:50.582353-02	302	TASK0119414	3		17	1
338	2017-01-18 17:07:50.590684-02	301	TASK0119414	3		17	1
339	2017-01-18 17:07:50.59906-02	300	TASK0119414	3		17	1
340	2017-01-18 17:07:50.607463-02	299	TASK0159422	3		17	1
341	2017-01-18 17:07:50.615703-02	298	TASK0159431	3		17	1
342	2017-01-18 17:07:50.624031-02	297	TASK0159422	3		17	1
343	2017-01-18 17:07:50.632288-02	296	TASK0159422	3		17	1
344	2017-01-18 17:07:50.640667-02	295	TASK0159431	3		17	1
345	2017-01-18 17:07:50.649068-02	294	TASK0159414\t	3		17	1
346	2017-01-18 17:07:50.657326-02	293	TASK0159414	3		17	1
347	2017-01-18 17:07:50.665658-02	292	TASK0152062	3		17	1
348	2017-01-18 17:07:50.674073-02	291	TASK0158223	3		17	1
349	2017-01-18 17:07:50.682373-02	290	TASK0158983	3		17	1
350	2017-01-18 17:07:50.690694-02	289	INC0192900INC0193514	3		17	1
351	2017-01-18 17:07:50.699014-02	288	159064	3		17	1
352	2017-01-18 17:07:50.707271-02	287	TASK0156302	3		17	1
353	2017-01-18 17:07:50.715671-02	286	0193179	3		17	1
354	2017-01-18 17:07:50.723973-02	285	TASK0159004	3		17	1
355	2017-01-18 17:07:50.732494-02	284	TASK0158988	3		17	1
356	2017-01-18 17:07:50.740794-02	283	TASK0158988	3		17	1
357	2017-01-18 17:07:50.749153-02	282	TASK0159001	3		17	1
358	2017-01-18 17:07:50.757486-02	281	TASK0158988	3		17	1
359	2017-01-18 17:07:50.765802-02	280	TASK156302	3		17	1
360	2017-01-18 17:07:50.774192-02	279	TASK0159064	3		17	1
361	2017-01-18 17:07:50.782468-02	278	TASK0159064	3		17	1
362	2017-01-18 17:07:50.790769-02	277	TASK0158980	3		17	1
363	2017-01-18 17:07:50.799045-02	276	0193000	3		17	1
364	2017-01-18 17:07:50.807292-02	275	INC0193095	3		17	1
365	2017-01-18 17:07:50.81573-02	274	TASK0158978	3		17	1
366	2017-01-18 17:07:50.824078-02	273	0192997	3		17	1
367	2017-01-18 17:07:50.832425-02	272	0193055	3		17	1
368	2017-01-18 17:07:50.840663-02	271	TASK0158976	3		17	1
369	2017-01-18 17:07:50.849092-02	270	TASK0158976\t	3		17	1
370	2017-01-18 17:07:50.857337-02	269	INC0191408	3		17	1
371	2017-01-18 17:07:50.865664-02	268	INC0192952	3		17	1
372	2017-01-18 17:07:50.874064-02	267	inc0192797	3		17	1
373	2017-01-18 17:07:50.882306-02	266	TASK0119428	3		17	1
374	2017-01-18 17:07:50.890686-02	265	TASK0119428	3		17	1
375	2017-01-18 17:07:50.899027-02	264	TASK0119428	3		17	1
376	2017-01-18 17:07:50.907417-02	263	0158576	3		17	1
377	2017-01-18 17:07:50.915716-02	262	0158580	3		17	1
378	2017-01-18 17:07:50.924052-02	261	0158578	3		17	1
379	2017-01-18 17:07:50.932385-02	260	TASK0188273	3		17	1
380	2017-01-18 17:07:50.940663-02	259	TASK0158586	3		17	1
381	2017-01-18 17:07:50.949042-02	258	TASK0158751	3		17	1
382	2017-01-18 17:07:50.95741-02	257	TASK0158581	3		17	1
383	2017-01-18 17:07:50.96579-02	256	INC0192845	3		17	1
384	2017-01-18 17:07:50.974129-02	255	TASK0158581	3		17	1
385	2017-01-18 17:07:50.982404-02	254	INC0193116	3		17	1
386	2017-01-18 17:07:50.990789-02	253	TASK0158677	3		17	1
387	2017-01-18 17:07:50.99904-02	252	INC0193004	3		17	1
388	2017-01-18 17:07:51.007469-02	251	TASK0158573	3		17	1
389	2017-01-18 17:07:51.015944-02	250	TASK0158583	3		17	1
390	2017-01-18 17:07:51.0242-02	249	INC0193075	3		17	1
391	2017-01-18 17:07:51.032516-02	248	inc0192710	3		17	1
392	2017-01-18 17:07:51.040822-02	247	0158577	3		17	1
393	2017-01-18 17:07:51.074228-02	246	TASK0158582	3		17	1
394	2017-01-18 17:07:51.082475-02	245	TASK0158539	3		17	1
395	2017-01-18 17:07:51.090784-02	244	TASK0158539	3		17	1
396	2017-01-18 17:07:51.099199-02	243	TASK0158223	3		17	1
397	2017-01-18 17:07:51.1075-02	242	inc0192966	3		17	1
398	2017-01-18 17:07:51.115857-02	241	0134625	3		17	1
399	2017-01-18 17:07:51.124051-02	240	INC0192773	3		17	1
400	2017-01-18 17:07:51.132499-02	239	0134625	3		17	1
401	2017-01-18 17:07:51.140955-02	238	TASK0158227	3		17	1
402	2017-01-18 17:07:51.149169-02	237	TASK0158227	3		17	1
403	2017-01-18 17:07:51.157505-02	236	TASK0151538	3		17	1
404	2017-01-18 17:07:51.16582-02	235	TASK0151538	3		17	1
405	2017-01-18 17:07:51.174172-02	234	inc193070	3		17	1
406	2017-01-18 17:07:51.182459-02	233	inc0192977	3		17	1
407	2017-01-18 17:07:51.190814-02	232	TASK0126619	3		17	1
408	2017-01-18 17:07:51.19911-02	231	INC0193047\t	3		17	1
409	2017-01-18 17:07:51.207581-02	230	TASK0126619	3		17	1
410	2017-01-18 17:07:51.215841-02	229	TASK0126619	3		17	1
411	2017-01-18 17:07:51.224243-02	228	0158176	3		17	1
412	2017-01-18 17:07:51.232587-02	227	0158176	3		17	1
413	2017-01-18 17:07:51.24087-02	226	0192920	3		17	1
414	2017-01-18 17:07:51.249205-02	225	TASK0147357	3		17	1
415	2017-01-18 17:07:51.25753-02	224	TASK0147357	3		17	1
416	2017-01-18 17:07:51.265862-02	223	TASK0147357	3		17	1
417	2017-01-18 17:07:51.274184-02	222	INC0192811	3		17	1
418	2017-01-18 17:07:51.282506-02	221	INC0192812	3		17	1
419	2017-01-18 17:07:51.290862-02	220	TASK0158212	3		17	1
420	2017-01-18 17:07:51.299079-02	219	TASK0158212	3		17	1
421	2017-01-18 17:07:51.307442-02	218	INC0192418	3		17	1
422	2017-01-18 17:07:51.315816-02	217	TASK0158209	3		17	1
423	2017-01-18 17:07:51.32434-02	216	TASK0158209	3		17	1
424	2017-01-18 17:07:51.332681-02	215	TASK0158125	3		17	1
425	2017-01-18 17:07:51.340917-02	214	INC0192801	3		17	1
426	2017-01-18 17:07:51.349249-02	213	TASK0157973	3		17	1
427	2017-01-18 17:07:51.357701-02	212	TASK0158107	3		17	1
428	2017-01-18 17:07:51.365864-02	211	TASK0158107	3		17	1
429	2017-01-18 17:07:51.374246-02	210	INC0192264	3		17	1
430	2017-01-18 17:07:51.382548-02	209	INC0192689	3		17	1
431	2017-01-18 17:07:51.390863-02	208	inc0192447	3		17	1
432	2017-01-18 17:07:51.399206-02	207	inc0192468	3		17	1
433	2017-01-18 17:07:51.407521-02	206	INC0192606	3		17	1
434	2017-01-18 17:07:51.415844-02	205	INC0192073	3		17	1
435	2017-01-18 17:07:51.424217-02	204	TASK0157973	3		17	1
436	2017-01-18 17:07:51.432479-02	203	0191645	3		17	1
437	2017-01-18 17:07:51.440797-02	202	TASK0157807	3		17	1
438	2017-01-18 17:07:51.449196-02	201	TASK0157807	3		17	1
439	2017-01-18 17:07:51.457522-02	200	task0157818	3		17	1
440	2017-01-18 17:07:51.466069-02	199	task0157818	3		17	1
441	2017-01-18 17:07:51.474399-02	198	task0157818	3		17	1
442	2017-01-18 17:07:51.482736-02	197	TASK0157806	3		17	1
443	2017-01-18 17:07:51.491023-02	196	TASK0157806	3		17	1
444	2017-01-18 17:07:51.499357-02	195	TASK0157804	3		17	1
445	2017-01-18 17:07:51.507678-02	194	TASK0157804	3		17	1
446	2017-01-18 17:07:51.516004-02	193	inc0192267	3		17	1
447	2017-01-18 17:07:51.524368-02	192	INC0192443\t	3		17	1
448	2017-01-18 17:07:51.532688-02	191	TASK0157723	3		17	1
449	2017-01-18 17:07:51.541007-02	190	TASK0157723	3		17	1
450	2017-01-18 17:07:51.549287-02	189	TASK0157723	3		17	1
451	2017-01-18 17:07:51.557601-02	188	task0157061	3		17	1
452	2017-01-18 17:07:51.566016-02	187	task0191645	3		17	1
453	2017-01-18 17:07:51.574288-02	186	task0157061	3		17	1
454	2017-01-18 17:07:51.582642-02	185	TASK0157604	3		17	1
455	2017-01-18 17:07:51.590979-02	184	TASK0157604	3		17	1
456	2017-01-18 17:07:51.599303-02	183	TASK0157334	3		17	1
457	2017-01-18 17:07:51.607636-02	182	TASK0157334	3		17	1
458	2017-01-18 17:07:51.616148-02	181	TASK0157334	3		17	1
459	2017-01-18 17:07:51.624314-02	180	TASK0157334	3		17	1
460	2017-01-18 17:07:51.632675-02	179	INC0191464	3		17	1
461	2017-01-18 17:07:51.640997-02	178	INC0191464	3		17	1
462	2017-01-18 17:07:51.649375-02	177	INC0191464	3		17	1
463	2017-01-18 17:07:51.657665-02	176	TASK0157334	3		17	1
464	2017-01-18 17:07:51.666057-02	175	0157336	3		17	1
465	2017-01-18 17:07:51.674336-02	174	0157336	3		17	1
466	2017-01-18 17:07:51.682693-02	173	0192184	3		17	1
467	2017-01-18 17:07:51.690912-02	172	TASK0157338	3		17	1
468	2017-01-18 17:07:51.69934-02	171	TASK0157338	3		17	1
469	2017-01-18 17:07:51.707854-02	170	TASK01573	3		17	1
470	2017-01-18 17:07:51.715983-02	169	task0157337	3		17	1
471	2017-01-18 17:07:51.724302-02	168	task0157337	3		17	1
472	2017-01-18 17:07:51.732579-02	167	task0157337	3		17	1
473	2017-01-18 17:07:51.740923-02	166	INC0187997	3		17	1
474	2017-01-18 17:07:51.749258-02	165	task0157001	3		17	1
475	2017-01-18 17:07:51.757671-02	164	inc0191645	3		17	1
476	2017-01-18 17:07:51.766167-02	163	TASK0126654	3		17	1
477	2017-01-18 17:07:51.774423-02	162	0157251	3		17	1
478	2017-01-18 17:07:51.782784-02	161	0157251	3		17	1
479	2017-01-18 17:07:51.791027-02	160	0157251	3		17	1
480	2017-01-18 17:07:51.799407-02	159	0191286	3		17	1
481	2017-01-18 17:07:51.807686-02	158	TASK0126654	3		17	1
482	2017-01-18 17:07:51.815989-02	157	TASK0126654	3		17	1
483	2017-01-18 17:07:51.824268-02	156	TASK0126654	3		17	1
484	2017-01-18 17:07:51.832679-02	155	TASK014896	3		17	1
485	2017-01-18 17:07:51.840996-02	154	TASK0148926	3		17	1
486	2017-01-18 17:07:51.849236-02	153	TASK0148926	3		17	1
487	2017-01-18 17:07:51.857574-02	152	TASK0157194	3		17	1
488	2017-01-18 17:07:51.866076-02	151	0119406	3		17	1
489	2017-01-18 17:07:51.874337-02	150	TESTETELEFONEDIEGO	3		17	1
490	2017-01-18 17:07:51.882686-02	149	0119406	3		17	1
491	2017-01-18 17:07:51.890945-02	148	0119406	3		17	1
492	2017-01-18 17:07:51.899318-02	147	0191414	3		17	1
493	2017-01-18 17:07:51.907657-02	146	INC0191954	3		17	1
494	2017-01-18 17:07:51.915957-02	145	Task0156725	3		17	1
495	2017-01-18 17:07:51.924445-02	144	Task0156725	3		17	1
496	2017-01-18 17:07:51.932808-02	143	0153565	3		17	1
497	2017-01-18 17:07:51.941111-02	142	0153565	3		17	1
498	2017-01-18 17:07:51.949456-02	141	TASK0119450	3		17	1
499	2017-01-18 17:07:51.957743-02	140	TASK0154478	3		17	1
500	2017-01-18 17:07:51.96611-02	139	TASK0154478	3		17	1
501	2017-01-18 17:07:51.97441-02	138	TASK0156990	3		17	1
502	2017-01-18 17:07:51.982763-02	137	TASK0156990	3		17	1
503	2017-01-18 17:07:51.991043-02	136	TASK0	3		17	1
504	2017-01-18 17:07:51.999405-02	135	TASK0	3		17	1
505	2017-01-18 17:07:52.007786-02	134	inc0191457	3		17	1
506	2017-01-18 17:07:52.016233-02	133	TASK0156669	3		17	1
507	2017-01-18 17:07:52.024516-02	132	INC0196669	3		17	1
508	2017-01-18 17:07:52.032911-02	131	inc0191256	3		17	1
509	2017-01-18 17:07:52.041206-02	130	0191493	3		17	1
510	2017-01-18 17:07:52.04945-02	129	0191455	3		17	1
511	2017-01-18 17:07:52.057759-02	128	task0186677	3		17	1
512	2017-01-18 17:07:52.066062-02	127	INC0191401	3		17	1
513	2017-01-18 17:07:52.074379-02	126	TASK0156664	3		17	1
514	2017-01-18 17:07:52.082783-02	125	INC0191413	3		17	1
515	2017-01-18 17:07:52.091078-02	124	TASK0156623	3		17	1
516	2017-01-18 17:07:52.099407-02	123	TASK0156623	3		17	1
517	2017-01-18 17:07:52.107794-02	122	0191465	3		17	1
518	2017-01-18 17:07:52.116105-02	121	0190935	3		17	1
519	2017-01-18 17:07:52.124491-02	120	INC0191478	3		17	1
520	2017-01-18 17:07:52.132706-02	119	TASK0156623	3		17	1
521	2017-01-18 17:07:52.14106-02	118	TASK0156627	3		17	1
522	2017-01-18 17:07:52.149459-02	117	TASK0156627	3		17	1
523	2017-01-18 17:07:52.157894-02	116	0191304	3		17	1
524	2017-01-18 17:07:52.166239-02	115	INC0191458	3		17	1
525	2017-01-18 17:07:52.174537-02	114	TASK0156659	3		17	1
526	2017-01-18 17:07:52.18288-02	113	inc0191368inc0191426	3		17	1
527	2017-01-18 17:07:52.191215-02	112	Task0156346	3		17	1
528	2017-01-18 17:07:52.19957-02	111	TASK0119408	3		17	1
529	2017-01-18 17:07:52.207997-02	110	TASK0138428	3		17	1
530	2017-01-18 17:07:52.216234-02	109	0126179	3		17	1
531	2017-01-18 17:07:52.224494-02	108	task0126179	3		17	1
532	2017-01-18 17:07:52.23293-02	107	0126179	3		17	1
533	2017-01-18 17:07:52.24127-02	106	Task0156346	3		17	1
534	2017-01-18 17:07:52.249549-02	105	Task0156346	3		17	1
535	2017-01-18 17:07:52.257781-02	104	INC0191428	3		17	1
536	2017-01-18 17:07:52.266183-02	103	TASK0156303	3		17	1
537	2017-01-18 17:07:52.274506-02	102	TASK0156303	3		17	1
538	2017-01-18 17:07:52.282766-02	101	0190629	3		17	1
539	2017-01-18 17:07:52.291156-02	100	0190724	3		17	1
540	2017-01-18 17:07:52.299506-02	99	0190666	3		17	1
541	2017-01-18 17:07:52.307993-02	98	0188700	3		17	1
542	2017-01-18 17:07:52.316313-02	97	INC191496	3		17	1
543	2017-01-18 17:07:52.324599-02	96	TASK0156393	3		17	1
544	2017-01-18 17:07:52.332955-02	95	TASK156335	3		17	1
545	2017-01-18 17:07:52.341218-02	94	TASK0156301	3		17	1
546	2017-01-18 17:07:52.34953-02	93	TASK0156301	3		17	1
547	2017-01-18 17:07:52.357797-02	92	INC0190688	3		17	1
548	2017-01-18 17:07:52.366195-02	91	TASK0156393	3		17	1
549	2017-01-18 17:07:52.374565-02	90	INC0189705	3		17	1
550	2017-01-18 17:07:52.382853-02	89	TASK0156019	3		17	1
551	2017-01-18 17:07:52.391165-02	88	TASK0152544	3		17	1
552	2017-01-18 17:07:52.399574-02	87	TASK0152544	3		17	1
553	2017-01-18 17:07:52.407815-02	86	TASK0155287	3		17	1
554	2017-01-18 17:07:52.416242-02	85	TASK0156019	3		17	1
555	2017-01-18 17:07:52.424609-02	84	TASK0155287	3		17	1
556	2017-01-18 17:07:52.432883-02	83	TASK0156019	3		17	1
557	2017-01-18 17:07:52.441228-02	82	INC0190651	3		17	1
558	2017-01-18 17:07:52.449525-02	81	0190507	3		17	1
559	2017-01-18 17:07:52.457915-02	80	0190815	3		17	1
560	2017-01-18 17:07:52.466189-02	79	INC0190660	3		17	1
561	2017-01-18 17:07:52.474591-02	78	INC0191044	3		17	1
562	2017-01-18 17:07:52.482907-02	77	TASK0152428	3		17	1
563	2017-01-18 17:07:52.491194-02	76	TASK0152428	3		17	1
564	2017-01-18 17:07:52.499513-02	75	INC0190722	3		17	1
565	2017-01-18 17:07:52.507881-02	74	137351	3		17	1
566	2017-01-18 17:07:52.516278-02	73	137351	3		17	1
567	2017-01-18 17:07:52.524571-02	72	137351	3		17	1
568	2017-01-18 17:07:52.53288-02	71	task0119411	3		17	1
569	2017-01-18 17:07:52.541297-02	70	task0119411	3		17	1
570	2017-01-18 17:07:52.54965-02	69	task0119411	3		17	1
571	2017-01-18 17:07:52.5579-02	68	0119436	3		17	1
572	2017-01-18 17:07:52.566268-02	67	0149158	3		17	1
573	2017-01-18 17:07:52.574565-02	66	0138404	3		17	1
574	2017-01-18 17:07:52.582865-02	65	0149158	3		17	1
575	2017-01-18 17:07:52.591218-02	64	0154190	3		17	1
576	2017-01-18 17:07:52.599632-02	63	INC0190438	3		17	1
577	2017-01-18 17:07:52.608072-02	62	INC0190438	3		17	1
578	2017-01-18 17:07:52.616371-02	61	TASK0119447	3		17	1
579	2017-01-18 17:07:52.624716-02	60	TASK0119449	3		17	1
580	2017-01-18 17:07:52.633036-02	59	0114730	3		17	1
581	2017-01-18 17:07:52.641353-02	58	0114730	3		17	1
582	2017-01-18 17:07:52.649689-02	57	0155301	3		17	1
583	2017-01-18 17:07:52.657994-02	56	0155301	3		17	1
584	2017-01-18 17:07:52.666333-02	55	0190212	3		17	1
585	2017-01-18 17:07:52.674604-02	54	INC0190456	3		17	1
586	2017-01-18 17:07:52.682947-02	53	INC189886	3		17	1
587	2017-01-18 17:07:52.691343-02	52	TASK0155168	3		17	1
588	2017-01-18 17:07:52.699674-02	51	TASK0155168	3		17	1
589	2017-01-18 17:07:52.708035-02	50	INC0189765	3		17	1
590	2017-01-18 17:07:52.716379-02	49	INC0190038	3		17	1
591	2017-01-18 17:07:52.724629-02	48	INC0190161	3		17	1
592	2017-01-18 17:07:52.732949-02	47	inc0189955	3		17	1
593	2017-01-18 17:07:52.741258-02	46	INC0189738INC0189668	3		17	1
594	2017-01-18 17:07:52.74961-02	45	INC0189892	3		17	1
595	2017-01-18 17:07:52.758141-02	44	0154804	3		17	1
596	2017-01-18 17:07:52.766458-02	43	190022	3		17	1
597	2017-01-18 17:07:52.774761-02	42	INC0189859	3		17	1
598	2017-01-18 17:07:52.783129-02	41	0189860	3		17	1
599	2017-01-18 17:07:52.791367-02	40	INC0190126	3		17	1
600	2017-01-18 17:07:52.799728-02	39	INC0190165	3		17	1
601	2017-01-18 17:07:52.80804-02	38	INC0189952	3		17	1
602	2017-01-18 17:07:52.816304-02	37	INC0189883	3		17	1
603	2017-01-18 17:07:52.824658-02	36	TASK0150540	3		17	1
604	2017-01-18 17:07:52.83302-02	35	TASK0150540	3		17	1
605	2017-01-18 17:07:52.841375-02	34	TASK0154785	3		17	1
606	2017-01-18 17:07:52.84968-02	33	TASK0154785	3		17	1
607	2017-01-18 17:07:52.858112-02	32	0190023	3		17	1
608	2017-01-18 17:07:52.866343-02	31	inc0189933	3		17	1
609	2017-01-18 17:07:52.875201-02	30	TASK0154788	3		17	1
610	2017-01-18 17:07:52.908352-02	29	INC0189814	3		17	1
611	2017-01-18 17:07:52.933346-02	28	INC0189877	3		17	1
612	2017-01-18 17:07:52.9663-02	27	task0141845	3		17	1
613	2017-01-18 17:07:52.999734-02	26	task0141845	3		17	1
614	2017-01-18 17:07:53.075082-02	25	TASK0150540	3		17	1
615	2017-01-18 17:07:53.108101-02	24	INC0189438	3		17	1
616	2017-01-18 17:07:53.116366-02	23	INC0189893	3		17	1
617	2017-01-18 17:07:53.124691-02	22	TASK0189882	3		17	1
618	2017-01-18 17:07:53.133077-02	21	TASK0189464	3		17	1
619	2017-01-18 17:07:53.141239-02	20	TASK0189464	3		17	1
620	2017-01-18 17:07:53.149672-02	19	TASK0189464	3		17	1
621	2017-01-18 17:07:53.157947-02	18	TASK0154480	3		17	1
622	2017-01-18 17:07:53.166384-02	17	TASK0154480	3		17	1
623	2017-01-18 17:07:53.174704-02	16	TASK0154480	3		17	1
624	2017-01-18 17:07:53.183002-02	15	TASK	3		17	1
625	2017-01-18 17:07:53.191223-02	14	TASK	3		17	1
626	2017-01-18 17:07:53.199619-02	13	0154450	3		17	1
627	2017-01-18 17:07:53.207943-02	12	TASK	3		17	1
628	2017-01-18 17:07:53.216246-02	11	INC0189628	3		17	1
629	2017-01-18 17:07:53.224603-02	10	123105/126681	3		17	1
630	2017-01-18 17:07:53.232862-02	9	TASK0120952	3		17	1
631	2017-01-18 17:07:53.24136-02	8	TASK0124957	3		17	1
632	2017-01-18 17:07:53.249699-02	7	Inc0154490	3		17	1
633	2017-01-18 17:07:53.258152-02	6	INC0189677	3		17	1
634	2017-01-18 17:07:53.266399-02	5	INC0189677/0189679	3		17	1
635	2017-01-18 17:07:53.274699-02	4	0189228	3		17	1
636	2017-01-18 17:46:07.907791-02	603	task0141845	3		17	1
637	2017-01-18 17:46:07.924635-02	602	task0141845	3		17	1
638	2017-01-18 17:46:07.933012-02	601	TASK0150540	3		17	1
639	2017-01-18 17:46:07.941478-02	600	INC0189438	3		17	1
640	2017-01-18 17:46:07.949664-02	599	INC0189893	3		17	1
641	2017-01-18 17:46:07.958102-02	598	TASK0189882	3		17	1
642	2017-01-18 17:46:07.966416-02	597	TASK0189464	3		17	1
643	2017-01-18 17:46:07.97474-02	596	TASK0189464	3		17	1
644	2017-01-18 17:46:07.983136-02	595	TASK0189464	3		17	1
645	2017-01-18 17:46:07.991353-02	594	TASK0154480	3		17	1
646	2017-01-18 17:46:07.999847-02	593	TASK0154480	3		17	1
647	2017-01-18 17:46:08.008183-02	592	TASK0154480	3		17	1
648	2017-01-18 17:46:08.016496-02	591	TASK	3		17	1
649	2017-01-18 17:46:08.025103-02	590	TASK	3		17	1
650	2017-01-18 17:46:08.050131-02	589	0154450	3		17	1
651	2017-01-18 17:46:08.108583-02	588	TASK	3		17	1
652	2017-01-18 17:46:08.133601-02	587	INC0189628	3		17	1
653	2017-01-18 17:46:08.166438-02	586	123105/126681	3		17	1
654	2017-01-18 17:46:08.191493-02	585	TASK0120952	3		17	1
655	2017-01-18 17:46:08.22496-02	584	TASK0124957	3		17	1
656	2017-01-18 17:46:08.233163-02	583	Inc0154490	3		17	1
657	2017-01-18 17:46:08.241442-02	582	INC0189677	3		17	1
658	2017-01-18 17:46:08.24968-02	581	INC0189677/0189679	3		17	1
659	2017-01-18 17:46:08.25803-02	580	0189228	3		17	1
660	2017-01-18 17:46:08.26637-02	623	inc0189955	3		17	1
661	2017-01-18 17:46:08.274761-02	622	INC0189738INC0189668	3		17	1
662	2017-01-18 17:46:08.283074-02	621	INC0189892	3		17	1
663	2017-01-18 17:46:08.291451-02	620	0154804	3		17	1
664	2017-01-18 17:46:08.29979-02	619	190022	3		17	1
665	2017-01-18 17:46:08.30804-02	618	INC0189859	3		17	1
666	2017-01-18 17:46:08.316384-02	617	0189860	3		17	1
667	2017-01-18 17:46:08.324751-02	616	INC0190126	3		17	1
668	2017-01-18 17:46:08.333084-02	615	INC0190165	3		17	1
669	2017-01-18 17:46:08.341366-02	614	INC0189952	3		17	1
670	2017-01-18 17:46:08.350057-02	613	INC0189883	3		17	1
671	2017-01-18 17:46:08.391986-02	612	TASK0150540	3		17	1
672	2017-01-18 17:46:08.424791-02	611	TASK0150540	3		17	1
673	2017-01-18 17:46:08.433005-02	610	TASK0154785	3		17	1
674	2017-01-18 17:46:08.441473-02	609	TASK0154785	3		17	1
675	2017-01-18 17:46:08.449725-02	608	0190023	3		17	1
676	2017-01-18 17:46:08.458151-02	607	inc0189933	3		17	1
677	2017-01-18 17:46:08.466397-02	606	TASK0154788	3		17	1
678	2017-01-18 17:46:08.474772-02	605	INC0189814	3		17	1
679	2017-01-18 17:46:08.483015-02	604	INC0189877	3		17	1
680	2017-01-18 17:46:08.491603-02	638	TASK0119449	3		17	1
681	2017-01-18 17:46:08.499807-02	637	0114730	3		17	1
682	2017-01-18 17:46:08.508234-02	636	0114730	3		17	1
683	2017-01-18 17:46:08.518025-02	635	0155301	3		17	1
684	2017-01-18 17:46:08.52633-02	634	0155301	3		17	1
685	2017-01-18 17:46:08.534532-02	633	0190212	3		17	1
686	2017-01-18 17:46:08.542912-02	632	INC0190456	3		17	1
687	2017-01-18 17:46:08.551243-02	631	INC189886	3		17	1
688	2017-01-18 17:46:08.559648-02	630	TASK0155168	3		17	1
689	2017-01-18 17:46:08.567949-02	629	TASK0155168	3		17	1
690	2017-01-18 17:46:08.576286-02	628	INC0189765	3		17	1
691	2017-01-18 17:46:08.584481-02	627	INC0190038	3		17	1
692	2017-01-18 17:46:08.592945-02	626	INC0190161	3		17	1
693	2017-01-18 17:46:08.601178-02	625	TASK0155196	3		17	1
694	2017-01-18 17:46:08.609513-02	624	TASK0155196	3		17	1
695	2017-01-18 17:46:08.617766-02	649	task0119411	3		17	1
696	2017-01-18 17:46:08.626178-02	648	task0119411	3		17	1
697	2017-01-18 17:46:08.634527-02	647	task0119411	3		17	1
698	2017-01-18 17:46:08.642841-02	646	0119436	3		17	1
699	2017-01-18 17:46:08.651144-02	645	0149158	3		17	1
700	2017-01-18 17:46:08.659597-02	644	0138404	3		17	1
701	2017-01-18 17:46:08.668-02	643	0149158	3		17	1
702	2017-01-18 17:46:08.67627-02	642	0154190	3		17	1
703	2017-01-18 17:46:08.684616-02	641	INC0190438	3		17	1
704	2017-01-18 17:46:08.692907-02	640	INC0190438	3		17	1
705	2017-01-18 17:46:08.701355-02	639	TASK0119447	3		17	1
706	2017-01-18 17:46:08.709686-02	656	190114	3		17	1
707	2017-01-18 17:46:08.717914-02	655	TASK0152428	3		17	1
708	2017-01-18 17:46:08.726225-02	654	TASK0152428	3		17	1
709	2017-01-18 17:46:08.734575-02	653	INC0190722	3		17	1
710	2017-01-18 17:46:08.742935-02	652	137351	3		17	1
711	2017-01-18 17:46:08.751264-02	651	137351	3		17	1
712	2017-01-18 17:46:08.759752-02	650	137351	3		17	1
713	2017-01-18 17:46:08.767856-02	661	INC0190651	3		17	1
714	2017-01-18 17:46:08.77622-02	660	0190507	3		17	1
715	2017-01-18 17:46:08.784521-02	659	0190815	3		17	1
716	2017-01-18 17:46:08.792892-02	658	INC0190660	3		17	1
717	2017-01-18 17:46:08.801199-02	657	INC0191044	3		17	1
718	2017-01-18 17:46:08.809668-02	691	Task0156346	3		17	1
719	2017-01-18 17:46:08.817913-02	690	TASK0119408	3		17	1
720	2017-01-18 17:46:08.82638-02	689	TASK0138428	3		17	1
721	2017-01-18 17:46:08.834688-02	688	0126179	3		17	1
722	2017-01-18 17:46:08.843023-02	687	task0126179	3		17	1
723	2017-01-18 17:46:08.851294-02	686	0126179	3		17	1
724	2017-01-18 17:46:08.859801-02	685	Task0156346	3		17	1
725	2017-01-18 17:46:08.868023-02	684	Task0156346	3		17	1
726	2017-01-18 17:46:08.876344-02	683	INC0191428	3		17	1
727	2017-01-18 17:46:08.884723-02	682	TASK0156303	3		17	1
728	2017-01-18 17:46:08.893051-02	681	TASK0156303	3		17	1
729	2017-01-18 17:46:08.901453-02	680	0190629	3		17	1
730	2017-01-18 17:46:08.909696-02	679	0190724	3		17	1
731	2017-01-18 17:46:08.918294-02	678	0190666	3		17	1
732	2017-01-18 17:46:08.943043-02	677	0188700	3		17	1
733	2017-01-18 17:46:09.018004-02	676	INC191496	3		17	1
734	2017-01-18 17:46:09.051364-02	675	TASK0156393	3		17	1
735	2017-01-18 17:46:09.059618-02	674	TASK156335	3		17	1
736	2017-01-18 17:46:09.067997-02	673	TASK0156301	3		17	1
737	2017-01-18 17:46:09.076316-02	672	TASK0156301	3		17	1
738	2017-01-18 17:46:09.084601-02	671	INC0190688	3		17	1
739	2017-01-18 17:46:09.092983-02	670	TASK0156393	3		17	1
740	2017-01-18 17:46:09.101319-02	669	INC0189705	3		17	1
741	2017-01-18 17:46:09.109732-02	668	TASK0156019	3		17	1
742	2017-01-18 17:46:09.118067-02	667	TASK0152544	3		17	1
743	2017-01-18 17:46:09.126331-02	666	TASK0152544	3		17	1
744	2017-01-18 17:46:09.134735-02	665	TASK0155287	3		17	1
745	2017-01-18 17:46:09.14305-02	664	TASK0156019	3		17	1
746	2017-01-18 17:46:09.151327-02	663	TASK0155287	3		17	1
747	2017-01-18 17:46:09.159657-02	662	TASK0156019	3		17	1
748	2017-01-18 17:46:09.167931-02	713	inc0191457	3		17	1
749	2017-01-18 17:46:09.176276-02	712	TASK0156669	3		17	1
750	2017-01-18 17:46:09.184551-02	711	INC0196669	3		17	1
751	2017-01-18 17:46:09.19293-02	710	inc0191256	3		17	1
752	2017-01-18 17:46:09.201239-02	709	0191493	3		17	1
753	2017-01-18 17:46:09.209722-02	708	0191455	3		17	1
754	2017-01-18 17:46:09.218135-02	707	task0186677	3		17	1
755	2017-01-18 17:46:09.226365-02	706	INC0191401	3		17	1
756	2017-01-18 17:46:09.234768-02	705	TASK0156664	3		17	1
757	2017-01-18 17:46:09.24306-02	704	INC0191413	3		17	1
758	2017-01-18 17:46:09.251336-02	703	TASK0156623	3		17	1
759	2017-01-18 17:46:09.259746-02	702	TASK0156623	3		17	1
760	2017-01-18 17:46:09.267987-02	701	0191465	3		17	1
761	2017-01-18 17:46:09.276322-02	700	0190935	3		17	1
762	2017-01-18 17:46:09.284723-02	699	INC0191478	3		17	1
763	2017-01-18 17:46:09.293082-02	698	TASK0156623	3		17	1
764	2017-01-18 17:46:09.301294-02	697	TASK0156627	3		17	1
765	2017-01-18 17:46:09.309868-02	696	TASK0156627	3		17	1
766	2017-01-18 17:46:09.318066-02	695	0191304	3		17	1
767	2017-01-18 17:46:09.326304-02	694	INC0191458	3		17	1
768	2017-01-18 17:46:09.334705-02	693	TASK0156659	3		17	1
769	2017-01-18 17:46:09.343-02	692	inc0191368inc0191426	3		17	1
770	2017-01-18 17:46:09.35133-02	745	INC0187997	3		17	1
771	2017-01-18 17:46:09.359657-02	744	task0157001	3		17	1
772	2017-01-18 17:46:09.368123-02	743	inc0191645	3		17	1
773	2017-01-18 17:46:09.376448-02	742	TASK0126654	3		17	1
774	2017-01-18 17:46:09.384777-02	741	0157251	3		17	1
775	2017-01-18 17:46:09.393084-02	740	0157251	3		17	1
776	2017-01-18 17:46:09.401521-02	739	0157251	3		17	1
777	2017-01-18 17:46:09.409812-02	738	0191286	3		17	1
778	2017-01-18 17:46:09.418131-02	737	TASK0126654	3		17	1
779	2017-01-18 17:46:09.426463-02	736	TASK0126654	3		17	1
780	2017-01-18 17:46:09.434853-02	735	TASK0126654	3		17	1
781	2017-01-18 17:46:09.443176-02	734	TASK014896	3		17	1
782	2017-01-18 17:46:09.451506-02	733	TASK0148926	3		17	1
783	2017-01-18 17:46:09.459847-02	732	TASK0148926	3		17	1
784	2017-01-18 17:46:09.468071-02	731	TASK0157194	3		17	1
785	2017-01-18 17:46:09.476457-02	730	0119406	3		17	1
786	2017-01-18 17:46:09.484827-02	729	TESTETELEFONEDIEGO	3		17	1
787	2017-01-18 17:46:09.493145-02	728	0119406	3		17	1
788	2017-01-18 17:46:09.501583-02	727	0119406	3		17	1
789	2017-01-18 17:46:09.509911-02	726	0191414	3		17	1
790	2017-01-18 17:46:09.518187-02	725	INC0191954	3		17	1
791	2017-01-18 17:46:09.526587-02	724	Task0156725	3		17	1
792	2017-01-18 17:46:09.534832-02	723	Task0156725	3		17	1
793	2017-01-18 17:46:09.543208-02	722	0153565	3		17	1
794	2017-01-18 17:46:09.551509-02	721	0153565	3		17	1
795	2017-01-18 17:46:09.559873-02	720	TASK0119450	3		17	1
796	2017-01-18 17:46:09.568235-02	719	TASK0154478	3		17	1
797	2017-01-18 17:46:09.576517-02	718	TASK0154478	3		17	1
798	2017-01-18 17:46:09.584794-02	717	TASK0156990	3		17	1
799	2017-01-18 17:46:09.593081-02	716	TASK0156990	3		17	1
800	2017-01-18 17:46:09.601488-02	715	TASK0	3		17	1
801	2017-01-18 17:46:09.609882-02	714	TASK0	3		17	1
802	2017-01-18 17:46:09.618174-02	767	task0157061	3		17	1
803	2017-01-18 17:46:09.626351-02	766	task0191645	3		17	1
804	2017-01-18 17:46:09.634707-02	765	task0157061	3		17	1
805	2017-01-18 17:46:09.643053-02	764	TASK0157604	3		17	1
806	2017-01-18 17:46:09.651464-02	763	TASK0157604	3		17	1
807	2017-01-18 17:46:09.659826-02	762	TASK0157334	3		17	1
808	2017-01-18 17:46:09.66823-02	761	TASK0157334	3		17	1
809	2017-01-18 17:46:09.676545-02	760	TASK0157334	3		17	1
810	2017-01-18 17:46:09.684864-02	759	TASK0157334	3		17	1
811	2017-01-18 17:46:09.693281-02	758	INC0191464	3		17	1
812	2017-01-18 17:46:09.70159-02	757	INC0191464	3		17	1
813	2017-01-18 17:46:09.710087-02	756	INC0191464	3		17	1
814	2017-01-18 17:46:09.718306-02	755	TASK0157334	3		17	1
815	2017-01-18 17:46:09.726614-02	754	0157336	3		17	1
816	2017-01-18 17:46:09.734914-02	753	0157336	3		17	1
817	2017-01-18 17:46:09.743265-02	752	0192184	3		17	1
818	2017-01-18 17:46:09.751596-02	751	TASK0157338	3		17	1
819	2017-01-18 17:46:09.759904-02	750	TASK0157338	3		17	1
820	2017-01-18 17:46:09.768197-02	749	TASK01573	3		17	1
821	2017-01-18 17:46:09.776545-02	748	task0157337	3		17	1
822	2017-01-18 17:46:09.784889-02	747	task0157337	3		17	1
823	2017-01-18 17:46:09.793189-02	746	task0157337	3		17	1
824	2017-01-18 17:46:09.80163-02	792	TASK0157973	3		17	1
825	2017-01-18 17:46:09.809885-02	784	INC0192073	3		17	1
826	2017-01-18 17:46:09.818253-02	783	TASK0157973	3		17	1
827	2017-01-18 17:46:09.826506-02	782	0191645	3		17	1
828	2017-01-18 17:46:09.834891-02	781	TASK0157807	3		17	1
829	2017-01-18 17:46:09.843312-02	780	TASK0157807	3		17	1
830	2017-01-18 17:46:09.851638-02	779	task0157818	3		17	1
831	2017-01-18 17:46:09.859933-02	778	task0157818	3		17	1
832	2017-01-18 17:46:09.868267-02	777	task0157818	3		17	1
833	2017-01-18 17:46:09.876655-02	776	TASK0157806	3		17	1
834	2017-01-18 17:46:09.884917-02	775	TASK0157806	3		17	1
835	2017-01-18 17:46:09.893233-02	774	TASK0157804	3		17	1
836	2017-01-18 17:46:09.901511-02	773	TASK0157804	3		17	1
837	2017-01-18 17:46:09.909895-02	772	inc0192267	3		17	1
838	2017-01-18 17:46:09.918198-02	771	INC0192443\t	3		17	1
839	2017-01-18 17:46:09.926536-02	770	TASK0157723	3		17	1
840	2017-01-18 17:46:09.934816-02	769	TASK0157723	3		17	1
841	2017-01-18 17:46:09.943125-02	768	TASK0157723	3		17	1
842	2017-01-18 17:46:09.951618-02	789	INC0192264	3		17	1
843	2017-01-18 17:46:09.959967-02	788	INC0192689	3		17	1
844	2017-01-18 17:46:09.968332-02	787	inc0192447	3		17	1
845	2017-01-18 17:46:09.976746-02	786	inc0192468	3		17	1
846	2017-01-18 17:46:09.984992-02	785	INC0192606	3		17	1
847	2017-01-18 17:46:09.993291-02	791	TASK0158107	3		17	1
848	2017-01-18 17:46:10.001616-02	790	TASK0158107	3		17	1
849	2017-01-18 17:46:10.009917-02	822	TASK0158223	3		17	1
850	2017-01-18 17:46:10.018251-02	821	inc0192966	3		17	1
851	2017-01-18 17:46:10.026646-02	820	0134625	3		17	1
852	2017-01-18 17:46:10.034963-02	819	INC0192773	3		17	1
853	2017-01-18 17:46:10.043303-02	818	0134625	3		17	1
854	2017-01-18 17:46:10.051549-02	817	TASK0158227	3		17	1
855	2017-01-18 17:46:10.05991-02	816	TASK0158227	3		17	1
856	2017-01-18 17:46:10.068265-02	815	TASK0151538	3		17	1
857	2017-01-18 17:46:10.076617-02	814	TASK0151538	3		17	1
858	2017-01-18 17:46:10.084918-02	813	inc193070	3		17	1
859	2017-01-18 17:46:10.093269-02	812	inc0192977	3		17	1
860	2017-01-18 17:46:10.101666-02	811	TASK0126619	3		17	1
861	2017-01-18 17:46:10.110006-02	810	INC0193047\t	3		17	1
862	2017-01-18 17:46:10.118303-02	809	TASK0126619	3		17	1
863	2017-01-18 17:46:10.126661-02	808	TASK0126619	3		17	1
864	2017-01-18 17:46:10.134991-02	807	0158176	3		17	1
865	2017-01-18 17:46:10.143307-02	806	0158176	3		17	1
866	2017-01-18 17:46:10.151638-02	805	0192920	3		17	1
867	2017-01-18 17:46:10.16-02	804	TASK0147357	3		17	1
868	2017-01-18 17:46:10.168384-02	803	TASK0147357	3		17	1
869	2017-01-18 17:46:10.176618-02	802	TASK0147357	3		17	1
870	2017-01-18 17:46:10.184976-02	801	INC0192811	3		17	1
871	2017-01-18 17:46:10.193179-02	800	INC0192812	3		17	1
872	2017-01-18 17:46:10.201475-02	799	TASK0158212	3		17	1
873	2017-01-18 17:46:10.20982-02	798	TASK0158212	3		17	1
874	2017-01-18 17:46:10.218157-02	797	INC0192418	3		17	1
875	2017-01-18 17:46:10.226781-02	796	TASK0158209	3		17	1
876	2017-01-18 17:46:10.260076-02	795	TASK0158209	3		17	1
877	2017-01-18 17:46:10.293268-02	794	TASK0158125	3		17	1
878	2017-01-18 17:46:10.30164-02	793	INC0192801	3		17	1
879	2017-01-18 17:46:10.309874-02	846	inc0192797	3		17	1
880	2017-01-18 17:46:10.318325-02	845	TASK0119428	3		17	1
881	2017-01-18 17:46:10.32665-02	844	TASK0119428	3		17	1
882	2017-01-18 17:46:10.334901-02	843	TASK0119428	3		17	1
883	2017-01-18 17:46:10.343251-02	842	0158576	3		17	1
884	2017-01-18 17:46:10.351563-02	841	0158580	3		17	1
885	2017-01-18 17:46:10.360011-02	840	0158578	3		17	1
886	2017-01-18 17:46:10.368258-02	839	TASK0188273	3		17	1
887	2017-01-18 17:46:10.376565-02	838	TASK0158586	3		17	1
888	2017-01-18 17:46:10.384872-02	837	TASK0158751	3		17	1
889	2017-01-18 17:46:10.393347-02	836	TASK0158581	3		17	1
890	2017-01-18 17:46:10.401589-02	835	INC0192845	3		17	1
891	2017-01-18 17:46:10.409903-02	834	TASK0158581	3		17	1
892	2017-01-18 17:46:10.418183-02	833	INC0193116	3		17	1
893	2017-01-18 17:46:10.426528-02	832	TASK0158677	3		17	1
894	2017-01-18 17:46:10.434917-02	831	INC0193004	3		17	1
895	2017-01-18 17:46:10.443225-02	830	TASK0158573	3		17	1
896	2017-01-18 17:46:10.451616-02	829	TASK0158583	3		17	1
897	2017-01-18 17:46:10.460011-02	828	INC0193075	3		17	1
898	2017-01-18 17:46:10.468246-02	827	inc0192710	3		17	1
899	2017-01-18 17:46:10.47667-02	826	0158577	3		17	1
900	2017-01-18 17:46:10.484988-02	825	TASK0158582	3		17	1
901	2017-01-18 17:46:10.493424-02	824	TASK0158539	3		17	1
902	2017-01-18 17:46:10.501673-02	823	TASK0158539	3		17	1
903	2017-01-18 17:46:10.510033-02	870	TASK0158223	3		17	1
904	2017-01-18 17:46:10.518307-02	869	TASK0158983	3		17	1
905	2017-01-18 17:46:10.526647-02	868	INC0192900INC0193514	3		17	1
906	2017-01-18 17:46:10.534926-02	867	159064	3		17	1
907	2017-01-18 17:46:10.543294-02	866	TASK0156302	3		17	1
908	2017-01-18 17:46:10.551567-02	865	0193179	3		17	1
909	2017-01-18 17:46:10.559927-02	864	TASK0159004	3		17	1
910	2017-01-18 17:46:10.568257-02	863	TASK0158988	3		17	1
911	2017-01-18 17:46:10.576578-02	862	TASK0158988	3		17	1
912	2017-01-18 17:46:10.584888-02	861	TASK0159001	3		17	1
913	2017-01-18 17:46:10.593262-02	860	TASK0158988	3		17	1
914	2017-01-18 17:46:10.60162-02	859	TASK156302	3		17	1
915	2017-01-18 17:46:10.61012-02	858	TASK0159064	3		17	1
916	2017-01-18 17:46:10.618433-02	857	TASK0159064	3		17	1
917	2017-01-18 17:46:10.626914-02	856	TASK0158980	3		17	1
918	2017-01-18 17:46:10.635006-02	855	0193000	3		17	1
919	2017-01-18 17:46:10.643452-02	854	INC0193095	3		17	1
920	2017-01-18 17:46:10.651661-02	853	TASK0158978	3		17	1
921	2017-01-18 17:46:10.660096-02	852	0192997	3		17	1
922	2017-01-18 17:46:10.668383-02	851	0193055	3		17	1
923	2017-01-18 17:46:10.676764-02	850	TASK0158976	3		17	1
924	2017-01-18 17:46:10.685055-02	849	TASK0158976\t	3		17	1
925	2017-01-18 17:46:10.693512-02	848	INC0191408	3		17	1
926	2017-01-18 17:46:10.701875-02	847	INC0192952	3		17	1
927	2017-01-18 17:46:10.71018-02	899	TASK0159440	3		17	1
928	2017-01-18 17:46:10.718816-02	898	TASK0159440	3		17	1
929	2017-01-18 17:46:10.726921-02	897	TASK0159440	3		17	1
930	2017-01-18 17:46:10.735082-02	896	TASK0159431	3		17	1
931	2017-01-18 17:46:10.743492-02	895	TASK0119403	3		17	1
932	2017-01-18 17:46:10.751819-02	894	TASK0119403	3		17	1
933	2017-01-18 17:46:10.760147-02	893	TASK0119403	3		17	1
934	2017-01-18 17:46:10.768397-02	892	TASK0119422	3		17	1
935	2017-01-18 17:46:10.776763-02	891	0159434	3		17	1
936	2017-01-18 17:46:10.785021-02	890	TASK0159436	3		17	1
937	2017-01-18 17:46:10.793529-02	889	0144334	3		17	1
938	2017-01-18 17:46:10.801747-02	888	0144334	3		17	1
939	2017-01-18 17:46:10.810129-02	887	0144334	3		17	1
940	2017-01-18 17:46:10.818321-02	886	0144334	3		17	1
941	2017-01-18 17:46:10.826736-02	885	INC0193825	3		17	1
942	2017-01-18 17:46:10.835188-02	884	INC0193757/INC019371	3		17	1
943	2017-01-18 17:46:10.843522-02	883	TASK0119422	3		17	1
944	2017-01-18 17:46:10.85181-02	882	TASK0119422	3		17	1
945	2017-01-18 17:46:10.860177-02	881	TASK0119414	3		17	1
946	2017-01-18 17:46:10.868446-02	880	TASK0119414	3		17	1
947	2017-01-18 17:46:10.876833-02	879	TASK0119414	3		17	1
948	2017-01-18 17:46:10.885077-02	878	TASK0159422	3		17	1
949	2017-01-18 17:46:10.893474-02	877	TASK0159431	3		17	1
950	2017-01-18 17:46:10.901769-02	876	TASK0159422	3		17	1
951	2017-01-18 17:46:10.910118-02	875	TASK0159422	3		17	1
952	2017-01-18 17:46:10.918402-02	874	TASK0159431	3		17	1
953	2017-01-18 17:46:10.926855-02	873	TASK0159414\t	3		17	1
954	2017-01-18 17:46:10.935197-02	872	TASK0159414	3		17	1
955	2017-01-18 17:46:10.943547-02	871	TASK0152062	3		17	1
956	2017-01-18 17:46:10.951998-02	923	TASK0159892	3		17	1
957	2017-01-18 17:46:10.960231-02	922	TASK0159892	3		17	1
958	2017-01-18 17:46:10.968475-02	921	TASK0159892	3		17	1
959	2017-01-18 17:46:10.976887-02	920	TASK0138409	3		17	1
960	2017-01-18 17:46:10.985272-02	919	TASK0138409	3		17	1
961	2017-01-18 17:46:10.993599-02	918	TASK0138409	3		17	1
962	2017-01-18 17:46:11.001821-02	917	TASK0138409	3		17	1
963	2017-01-18 17:46:11.010182-02	916	TASK0159946	3		17	1
964	2017-01-18 17:46:11.018458-02	915	INC0193823	3		17	1
965	2017-01-18 17:46:11.026909-02	914	0159538	3		17	1
966	2017-01-18 17:46:11.035184-02	913	0159438	3		17	1
967	2017-01-18 17:46:11.043559-02	912	0159438	3		17	1
968	2017-01-18 17:46:11.051891-02	911	INC0193665	3		17	1
969	2017-01-18 17:46:11.060214-02	910	INC0193983\t	3		17	1
970	2017-01-18 17:46:11.068491-02	909	TASK0159947	3		17	1
971	2017-01-18 17:46:11.076953-02	908	TASK0159947	3		17	1
972	2017-01-18 17:46:11.085313-02	907	INC0193666	3		17	1
973	2017-01-18 17:46:11.09364-02	906	TASK0159947	3		17	1
974	2017-01-18 17:46:11.101907-02	905	TASK0159947	3		17	1
975	2017-01-18 17:46:11.110303-02	904	INC0194066	3		17	1
976	2017-01-18 17:46:11.118582-02	903	TASK0159888	3		17	1
977	2017-01-18 17:46:11.127002-02	902	TASK0159888	3		17	1
978	2017-01-18 17:46:11.135328-02	901	0193822	3		17	1
979	2017-01-18 17:46:11.143599-02	900	INC0192962	3		17	1
980	2017-01-18 17:46:11.151855-02	941	TASK0151540	3		17	1
981	2017-01-18 17:46:11.160246-02	940	TASK0151540	3		17	1
982	2017-01-18 17:46:11.168645-02	939	TASK0151540	3		17	1
983	2017-01-18 17:46:11.17699-02	938	TASK0160095	3		17	1
984	2017-01-18 17:46:11.18518-02	937	TASK0160094	3		17	1
985	2017-01-18 17:46:11.193655-02	936	TASK0160095	3		17	1
986	2017-01-18 17:46:11.20191-02	935	TASK00160095	3		17	1
987	2017-01-18 17:46:11.210324-02	934	INC0193920	3		17	1
988	2017-01-18 17:46:11.218568-02	933	TASK0160471	3		17	1
989	2017-01-18 17:46:11.227062-02	932	TASK0160471	3		17	1
990	2017-01-18 17:46:11.235339-02	931	TASK0160471	3		17	1
991	2017-01-18 17:46:11.243658-02	930	INC0193983	3		17	1
992	2017-01-18 17:46:11.25191-02	929	TASK0160436	3		17	1
993	2017-01-18 17:46:11.260379-02	928	TASK0160436	3		17	1
994	2017-01-18 17:46:11.268676-02	927	0194070	3		17	1
995	2017-01-18 17:46:11.277072-02	926	TASK159437	3		17	1
996	2017-01-18 17:46:11.285267-02	925	TASK159437	3		17	1
997	2017-01-18 17:46:11.293562-02	959	INC0194886	3		17	1
998	2017-01-18 17:46:11.301937-02	958	Inc0194749	3		17	1
999	2017-01-18 17:46:11.310275-02	957	inc0194880	3		17	1
1000	2017-01-18 17:46:11.318632-02	956	INC9194555	3		17	1
1001	2017-01-18 17:46:11.326962-02	955	TASK0160770	3		17	1
1002	2017-01-18 17:46:11.33531-02	954	TASK0160770	3		17	1
1003	2017-01-18 17:46:11.343639-02	953	INC0190084	3		17	1
1004	2017-01-18 17:46:11.351963-02	952	INC0194064	3		17	1
1005	2017-01-18 17:46:11.360353-02	951	inc0194783	3		17	1
1006	2017-01-18 17:46:11.368525-02	950	tasc0194563	3		17	1
1007	2017-01-18 17:46:11.377044-02	949	TASK0159433	3		17	1
1008	2017-01-18 17:46:11.385306-02	948	TASK0159433	3		17	1
1009	2017-01-18 17:46:11.393753-02	947	TASK01259433	3		17	1
1010	2017-01-18 17:46:11.402039-02	946	TASK0159433	3		17	1
1011	2017-01-18 17:46:11.410446-02	945	TASK0160778	3		17	1
1012	2017-01-18 17:46:11.41872-02	944	TASK0160778	3		17	1
1013	2017-01-18 17:46:11.4271-02	943	Inc0194620	3		17	1
1014	2017-01-18 17:46:11.43535-02	942	INC0194542	3		17	1
1015	2017-01-18 17:46:11.443712-02	974	inc0194845	3		17	1
1016	2017-01-18 17:46:11.451999-02	973	TASK0161117	3		17	1
1017	2017-01-18 17:46:11.460329-02	972	TASK0161117	3		17	1
1018	2017-01-18 17:46:11.468649-02	971	TASK0158977	3		17	1
1019	2017-01-18 17:46:11.476981-02	970	TASK0158977	3		17	1
1020	2017-01-18 17:46:11.485358-02	969	INC0194945	3		17	1
1021	2017-01-18 17:46:11.493683-02	968	INC0194513	3		17	1
1022	2017-01-18 17:46:11.502013-02	967	TASK0119411	3		17	1
1023	2017-01-18 17:46:11.510244-02	966	TASK0119411	3		17	1
1024	2017-01-18 17:46:11.518578-02	965	TASK0119411	3		17	1
1025	2017-01-18 17:46:11.527124-02	964	TASK0119411	3		17	1
1026	2017-01-18 17:46:11.535497-02	963	INC0194883	3		17	1
1027	2017-01-18 17:46:11.543812-02	962	INC0194972	3		17	1
1028	2017-01-18 17:46:11.551994-02	961	TASK0161099	3		17	1
1029	2017-01-18 17:46:11.560269-02	960	TASK0161099	3		17	1
1030	2017-01-18 17:46:11.568612-02	982	task0158683	3		17	1
1031	2017-01-18 17:46:11.577029-02	981	INC0195173	3		17	1
1032	2017-01-18 17:46:11.585262-02	980	TASK0161466	3		17	1
1033	2017-01-18 17:46:11.593634-02	979	INC0195320	3		17	1
1034	2017-01-18 17:46:11.601896-02	978	TASK0161466	3		17	1
1035	2017-01-18 17:46:11.610205-02	977	INC0195174	3		17	1
1036	2017-01-18 17:46:11.61873-02	976	INC0194192	3		17	1
1037	2017-01-18 17:46:11.626981-02	975	INC0195053	3		17	1
1038	2017-01-18 17:46:11.635324-02	1075	TASK0161959	3		17	1
1039	2017-01-18 17:46:11.643628-02	1007	INC0195453	3		17	1
1040	2017-01-18 17:46:11.652051-02	1006	INC0195520	3		17	1
1041	2017-01-18 17:46:11.660268-02	1005	INC0195249	3		17	1
1042	2017-01-18 17:46:11.668551-02	1004	Inc0195302	3		17	1
1043	2017-01-18 17:46:11.677061-02	1003	INC0195740	3		17	1
1044	2017-01-18 17:46:11.685391-02	1002	TASK0161959	3		17	1
1045	2017-01-18 17:46:11.693685-02	1001	INC0195674	3		17	1
1046	2017-01-18 17:46:11.702034-02	1000	INC0195716	3		17	1
1047	2017-01-18 17:46:11.710385-02	999	INC0195488	3		17	1
1048	2017-01-18 17:46:11.718638-02	998	INC0195171	3		17	1
1049	2017-01-18 17:46:11.727101-02	997	TASK0161880	3		17	1
1050	2017-01-18 17:46:11.73541-02	996	task0161887	3		17	1
1051	2017-01-18 17:46:11.743677-02	995	INC0195660	3		17	1
1052	2017-01-18 17:46:11.751969-02	994	INC0195670	3		17	1
1053	2017-01-18 17:46:11.760397-02	993	INC0195481	3		17	1
1054	2017-01-18 17:46:11.768717-02	992	TASK0161887	3		17	1
1055	2017-01-18 17:46:11.777022-02	991	INC0195535	3		17	1
1056	2017-01-18 17:46:11.785499-02	990	0195613	3		17	1
1057	2017-01-18 17:46:11.793826-02	989	INC0195652	3		17	1
1058	2017-01-18 17:46:11.802036-02	988	TASK0161877	3		17	1
1059	2017-01-18 17:46:11.810352-02	987	TASK0161877	3		17	1
1060	2017-01-18 17:46:11.81876-02	986	INC0195585	3		17	1
1061	2017-01-18 17:46:11.82723-02	985	INC0195491	3		17	1
1062	2017-01-18 17:46:11.835521-02	984	TASK0157086	3		17	1
1063	2017-01-18 17:46:11.843803-02	983	TASK0157086	3		17	1
1064	2017-01-18 17:46:11.852163-02	1009	INC0195756	3		17	1
1065	2017-01-18 17:46:11.860491-02	1008	Inc0195414	3		17	1
1066	2017-01-18 17:46:11.86881-02	1031	inc0198952	3		17	1
1067	2017-01-18 17:46:11.877214-02	1030	Inc0196200	3		17	1
1068	2017-01-18 17:46:11.885516-02	1029	TASK0162185	3		17	1
1069	2017-01-18 17:46:11.893866-02	1028	TASK0162185	3		17	1
1070	2017-01-18 17:46:11.902211-02	1027	0182181	3		17	1
1071	2017-01-18 17:46:11.910512-02	1026	task0162181	3		17	1
1072	2017-01-18 17:46:11.918837-02	1025	INC0195988	3		17	1
1073	2017-01-18 17:46:11.927149-02	1024	INC0195884	3		17	1
1074	2017-01-18 17:46:11.935542-02	1023	TASK0162184	3		17	1
1075	2017-01-18 17:46:11.943823-02	1022	TASK0162184	3		17	1
1076	2017-01-18 17:46:11.952051-02	1021	INC0195470	3		17	1
1077	2017-01-18 17:46:11.960505-02	1020	INC0196211	3		17	1
1078	2017-01-18 17:46:11.968738-02	1019	INC0195472	3		17	1
1079	2017-01-18 17:46:11.97722-02	1018	TASK0161448	3		17	1
1080	2017-01-18 17:46:11.985538-02	1017	TASK0161448	3		17	1
1081	2017-01-18 17:46:11.993868-02	1016	TASK0162175	3		17	1
1082	2017-01-18 17:46:12.002285-02	1015	TASK0161964	3		17	1
1083	2017-01-18 17:46:12.010358-02	1014	inc0195767	3		17	1
1084	2017-01-18 17:46:12.018828-02	1013	TASK0162175	3		17	1
1085	2017-01-18 17:46:12.027162-02	1012	TASK0161964	3		17	1
1086	2017-01-18 17:46:12.0355-02	1011	INC0195713	3		17	1
1087	2017-01-18 17:46:12.043764-02	1010	INC0196025	3		17	1
1088	2017-01-18 17:46:12.052133-02	1046	INC0196352	3		17	1
1089	2017-01-18 17:46:12.060431-02	1045	task0160092	3		17	1
1090	2017-01-18 17:46:12.068797-02	1044	tasc0160092	3		17	1
1091	2017-01-18 17:46:12.077231-02	1043	task0160092	3		17	1
1092	2017-01-18 17:46:12.085546-02	1042	task0160092	3		17	1
1093	2017-01-18 17:46:12.093875-02	1041	TASK0162452	3		17	1
1094	2017-01-18 17:46:12.102136-02	1040	TASK0162452	3		17	1
1095	2017-01-18 17:46:12.110482-02	1039	INC0195715	3		17	1
1096	2017-01-18 17:46:12.118802-02	1038	TASK0262439	3		17	1
1097	2017-01-18 17:46:12.127337-02	1037	INC0195810	3		17	1
1098	2017-01-18 17:46:12.135553-02	1036	TASK0162439	3		17	1
1099	2017-01-18 17:46:12.144021-02	1035	INC0196059	3		17	1
1100	2017-01-18 17:46:12.152272-02	1034	inc0196219	3		17	1
1101	2017-01-18 17:46:12.160591-02	1033	INC0196228	3		17	1
1102	2017-01-18 17:46:12.168946-02	1032	INC0196216	3		17	1
1103	2017-01-18 17:46:12.177242-02	1061	TASK0162990	3		17	1
1104	2017-01-18 17:46:12.185524-02	1060	TASK0162990	3		17	1
1105	2017-01-18 17:46:12.193832-02	1059	INC0196281	3		17	1
1106	2017-01-18 17:46:12.202218-02	1058	INC0196636	3		17	1
1107	2017-01-18 17:46:12.210655-02	1057	task0135637	3		17	1
1108	2017-01-18 17:46:12.218878-02	1056	task0135637	3		17	1
1109	2017-01-18 17:46:12.227248-02	1055	TASK0162136	3		17	1
1110	2017-01-18 17:46:12.235553-02	1054	TASK0162136	3		17	1
1111	2017-01-18 17:46:12.243862-02	1053	TASK0162863	3		17	1
1112	2017-01-18 17:46:12.252221-02	1052	TASK0162863	3		17	1
1113	2017-01-18 17:46:12.260499-02	1051	INC0196790	3		17	1
1114	2017-01-18 17:46:12.268824-02	1050	INC0196493	3		17	1
1115	2017-01-18 17:46:12.27736-02	1049	INC0196176	3		17	1
1116	2017-01-18 17:46:12.28565-02	1048	0196337	3		17	1
1117	2017-01-18 17:46:12.29399-02	1047	INC0196114	3		17	1
1118	2017-01-18 17:46:12.30222-02	1074	INC0196764	3		17	1
1119	2017-01-18 17:46:12.310764-02	1073	INC0196825	3		17	1
1120	2017-01-18 17:46:12.318795-02	1072	INC0196742	3		17	1
1121	2017-01-18 17:46:12.327197-02	1071	TASK0	3		17	1
1122	2017-01-18 17:46:12.335575-02	1070	INC0196882	3		17	1
1123	2017-01-18 17:46:12.343786-02	1069	TASK0163224	3		17	1
1124	2017-01-18 17:46:12.352105-02	1068	TASK0163336	3		17	1
1125	2017-01-18 17:46:12.36047-02	1067	INC0196741	3		17	1
1126	2017-01-18 17:46:12.368828-02	1066	TASK0163335	3		17	1
1127	2017-01-18 17:46:12.377172-02	1065	INC0196747	3		17	1
1128	2017-01-18 17:46:12.385507-02	1064	INC0196527	3		17	1
1129	2017-01-18 17:46:12.393798-02	1063	INC0196207	3		17	1
1130	2017-01-18 17:46:12.402161-02	1062	INC0196672	3		17	1
1131	2017-01-18 17:46:12.410415-02	1080	INC0197238	3		17	1
1132	2017-01-18 17:46:12.418898-02	1079	TASK0163614	3		17	1
1133	2017-01-18 17:46:12.427266-02	1078	INC0197001	3		17	1
1134	2017-01-18 17:46:12.435757-02	1077	INC0197238	3		17	1
1135	2017-01-18 17:46:12.443936-02	1076	INC0196800	3		17	1
1136	2017-01-18 17:46:12.452226-02	1106	INC0197878	3		17	1
1137	2017-01-18 17:46:12.460623-02	1105	TASK0161473	3		17	1
1138	2017-01-18 17:46:12.469038-02	1104	TASK0161473	3		17	1
1139	2017-01-18 17:46:12.477205-02	1103	TASK0131832	3		17	1
1140	2017-01-18 17:46:12.485577-02	1102	TASK0131832	3		17	1
1141	2017-01-18 17:46:12.494049-02	1101	TASK0131832	3		17	1
1142	2017-01-18 17:46:12.502233-02	1100	INC0197470	3		17	1
1143	2017-01-18 17:46:12.51068-02	1099	INC0197476	3		17	1
1144	2017-01-18 17:46:12.519023-02	1098	INC0197689	3		17	1
1145	2017-01-18 17:46:12.527318-02	1097	INC0197653	3		17	1
1146	2017-01-18 17:46:12.535687-02	1096	INC0197646	3		17	1
1147	2017-01-18 17:46:12.543955-02	1095	INC0197472	3		17	1
1148	2017-01-18 17:46:12.552242-02	1094	TASK0163833	3		17	1
1149	2017-01-18 17:46:12.560766-02	1093	TASk0163833	3		17	1
1150	2017-01-18 17:46:12.569088-02	1092	INC0197423	3		17	1
1151	2017-01-18 17:46:12.577397-02	1091	INC0197315	3		17	1
1152	2017-01-18 17:46:12.585657-02	1090	TASK0163839	3		17	1
1153	2017-01-18 17:46:12.594013-02	1089	TASK0163839	3		17	1
1154	2017-01-18 17:46:12.602284-02	1088	INC0197223	3		17	1
1155	2017-01-18 17:46:12.610769-02	1087	INC0197462	3		17	1
1156	2017-01-18 17:46:12.618981-02	1086	INC0197466	3		17	1
1157	2017-01-18 17:46:12.627299-02	1085	INC0197464	3		17	1
1158	2017-01-18 17:46:12.635576-02	1084	INC0197507	3		17	1
1159	2017-01-18 17:46:12.644089-02	1083	TASK0163819	3		17	1
1160	2017-01-18 17:46:12.652285-02	1082	INC0197481	3		17	1
1161	2017-01-18 17:46:12.660698-02	1081	INC0197478	3		17	1
1162	2017-01-18 17:46:12.668998-02	1130	INC0197515	3		17	1
1163	2017-01-18 17:46:12.677319-02	1129	INC0198225	3		17	1
1164	2017-01-18 17:46:12.685663-02	1128	TASK0164414	3		17	1
1165	2017-01-18 17:46:12.694008-02	1127	TAsk0125446	3		17	1
1166	2017-01-18 17:46:12.702303-02	1126	INC0198257	3		17	1
1167	2017-01-18 17:46:12.710762-02	1125	TASK0125443	3		17	1
1168	2017-01-18 17:46:12.7191-02	1124	TASK0164303	3		17	1
1169	2017-01-18 17:46:12.727372-02	1123	INC0198049	3		17	1
1170	2017-01-18 17:46:12.735744-02	1122	TASK0164303	3		17	1
1171	2017-01-18 17:46:12.744056-02	1121	INC0198009	3		17	1
1172	2017-01-18 17:46:12.75239-02	1120	INC0198395	3		17	1
1173	2017-01-18 17:46:12.760709-02	1119	TASK0164230	3		17	1
1174	2017-01-18 17:46:12.769063-02	1118	TASK0164230	3		17	1
1175	2017-01-18 17:46:12.77735-02	1117	INC0198116	3		17	1
1176	2017-01-18 17:46:12.78575-02	1116	INC0197898	3		17	1
1177	2017-01-18 17:46:12.794197-02	1115	INC0198053	3		17	1
1178	2017-01-18 17:46:12.802398-02	1114	INC0197826	3		17	1
1179	2017-01-18 17:46:12.810713-02	1113	INC0198149	3		17	1
1180	2017-01-18 17:46:12.819127-02	1112	TASK0164227	3		17	1
1181	2017-01-18 17:46:12.827468-02	1111	INC0197789	3		17	1
1182	2017-01-18 17:46:12.835792-02	1110	INC0198169	3		17	1
1183	2017-01-18 17:46:12.844105-02	1109	INC0198241	3		17	1
1184	2017-01-18 17:46:12.852354-02	1108	INC0197982	3		17	1
1185	2017-01-18 17:46:12.860742-02	1107	INC0198000	3		17	1
1186	2017-01-18 17:46:12.869103-02	1135	INC0197401	3		17	1
1187	2017-01-18 17:46:12.877587-02	1134	INC0198051	3		17	1
1188	2017-01-18 17:46:12.885887-02	1133	TASK0158655	3		17	1
1189	2017-01-18 17:46:12.894213-02	1132	INC0198350	3		17	1
1190	2017-01-18 17:46:12.902601-02	1131	TASK0158655	3		17	1
1191	2017-01-18 17:48:45.182601-02	2	Saveiro	2	[{"changed": {"fields": ["km_rev"]}}]	3	1
1192	2017-01-18 17:48:56.866682-02	2	Saveiro	2	[{"changed": {"fields": ["km_rev"]}}]	3	1
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1192, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('django_content_type_id_seq', 23, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	abastece	0001_initial	2017-01-03 13:43:10.162647-02
2	contenttypes	0001_initial	2017-01-03 13:43:10.262009-02
3	auth	0001_initial	2017-01-03 13:43:11.099807-02
4	admin	0001_initial	2017-01-03 13:43:11.26697-02
5	admin	0002_logentry_remove_auto_add	2017-01-03 13:43:11.333455-02
6	contenttypes	0002_remove_content_type_name	2017-01-03 13:43:11.383688-02
7	auth	0002_alter_permission_name_max_length	2017-01-03 13:43:11.408678-02
8	auth	0003_alter_user_email_max_length	2017-01-03 13:43:11.433646-02
9	auth	0004_alter_user_username_opts	2017-01-03 13:43:11.451772-02
10	auth	0005_alter_user_last_login_null	2017-01-03 13:43:11.475315-02
11	auth	0006_require_contenttypes_0002	2017-01-03 13:43:11.483532-02
12	auth	0007_alter_validators_add_error_messages	2017-01-03 13:43:11.504142-02
13	auth	0008_alter_user_username_max_length	2017-01-03 13:43:11.567184-02
14	sessions	0001_initial	2017-01-03 13:43:11.734198-02
15	abastece	0002_auto_20170104_1436	2017-01-04 14:37:00.39473-02
16	abastece	0003_auto_20170118_1441	2017-01-18 14:42:05.570183-02
17	abastece	0004_auto_20170118_1443	2017-01-18 14:43:43.429118-02
18	abastece	0005_evento_entry_date	2017-01-18 17:07:12.718762-02
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: temos
--

SELECT pg_catalog.setval('django_migrations_id_seq', 18, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: temos
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
omh21zsyejyrx7io2c0278di75x242ky	MmEyM2I2NjBiNjY2NjYyMGNkNmJkMzI0NTgwYWE4YzhhMzg5MjQ1Mzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzA4ZmFkMDg3MjhmNmRiZmEzZGI2ZDk4NGE3ODljZTUxNWUwNGZlYyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=	2017-01-18 11:31:13.956149-02
2irf9niwc10j7u2n7z74t1j04t5jpdvb	M2UwMTlmNzIxMjAzN2FmNzA2ZjU3MzcyZDdjZTdkOWUyZDZlZjg0OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzA4ZmFkMDg3MjhmNmRiZmEzZGI2ZDk4NGE3ODljZTUxNWUwNGZlYyIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2017-01-31 20:10:52.211151-02
\.


--
-- PostgreSQL database dump complete
--

