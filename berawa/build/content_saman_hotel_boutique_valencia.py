# Contenido de la demo Saman Hotel Boutique (València) (es/ca/en/fr). Hechos de samanhotelboutique.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Habitaciones dobles','Suite deluxe con bañera','Suite con bañera de hidromasaje'],
'ca':['Habitacions dobles','Suite deluxe amb banyera','Suite amb banyera d\'hidromassatge'],
'en':['Double rooms','Deluxe suite with bathtub','Suite with hot tub'],
'fr':['Chambres doubles','Suite deluxe avec baignoire','Suite avec baignoire balnéo']}
RD={
'es':['Diseño natural y minimalista: estándar con vistas a una calle tranquila, deluxe con vistas al jardín en la primera planta o con acceso directo al jardín y a la piscina en la planta baja. La doble superior admite hasta 3 personas.','Dos suites con espacio amplio y elegante y bañera privada, decoradas con un estilo único.','La suite más exclusiva del hotel, con bañera de hidromasaje privada y vistas a la piscina.'],
'ca':['Disseny natural i minimalista: estàndard amb vistes a un carrer tranquil, deluxe amb vistes al jardí a la primera planta o amb accés directe al jardí i a la piscina a la planta baixa. La doble superior admet fins a 3 persones.','Dues suites amb espai ampli i elegant i banyera privada, decorades amb un estil únic.','La suite més exclusiva de l\'hotel, amb banyera d\'hidromassatge privada i vistes a la piscina.'],
'en':['Natural, minimalist design: standard with views of a quiet street, deluxe with garden views on the first floor or with direct access to the garden and pool on the ground floor. The superior double sleeps up to 3.','Two suites with ample, elegant space and a private bathtub, decorated in a unique style.','The most exclusive suite in the hotel, with a private hot tub and views of the pool.'],
'fr':['Design naturel et minimaliste : standard avec vue sur une rue tranquille, deluxe avec vue sur le jardin au premier étage ou avec accès direct au jardin et à la piscine au rez-de-chaussée. La double supérieure accueille jusqu\'à 3 personnes.','Deux suites à l\'espace ample et élégant, avec baignoire privée, décorées dans un style unique.','La suite la plus exclusive de l\'hôtel, avec baignoire balnéo privée et vue sur la piscine.']}
ART={
'hero':('hills',9101,['#dfe9dc','#f6edcf','#ffe9b8','#a9c9b0','#6fa58b','#3f7a67']),
'intro':('waves',9102,['#f4e6bf','#ecb88a','#fff0c6','#8cc0c9','#58a0b0','#35788f','#215670']),
'r1':('arches',9111,['#e9e4d2','#f6efdb','#d9ab66','#9fb5a8','#5f8c78']),
'r2':('columns',9112,['#e6e2d0','#f4eedb','#d2a15c','#a2b7ab','#648f7b']),
'r3':('hills',9113,['#d9e6d6','#f5e8c8','#ffe3a8','#9cc3a7','#679f86','#3b7562']),
'g1':('hills',9121,['#e2ecdd','#f7ecd0','#ffe7b0','#aacdb2','#74aa90','#417d6a']),
'g2':('waves',9122,['#f6e2b4','#eaa882','#fff0c2','#7fb7c4','#4f95ab','#2f7189','#1d5069']),
'g3':('arches',9123,['#ece1c6','#f7edd5','#dfa764','#b6a07a','#8b7048']),
'g4':('columns',9124,['#e5e3d3','#f3efdc','#d4a25e','#9eb4a8','#5e8a77']),
'g5':('skyline',9125,['#35566a','#e9a477','#fbdba2','#33546a','#274459','#1a3144']),
'g6':('hills',9126,['#d6e4d4','#f4e5c3','#ffdfa0','#97c0a2','#609a80','#357060'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Saman Hotel Boutique · Hotel boutique con jardín y piscina en València',see_rooms='Ver habitaciones',hero_k='València · Camins al Grau',hero_t='Un hotel boutique con jardín y piscina de estilo balinés',hero_s='33 habitaciones de diseño natural y minimalista, a medio camino entre la playa y la Ciudad de las Artes y las Ciencias.',
 intro_t='Un oasis de calma en València',intro_p1='Saman Hotel Boutique está en la calle de la Industria, en el barrio de Camins al Grau, y abrió el 5 de agosto de 2024. Conserva dos chimeneas industriales que han marcado el paisaje de la ciudad.',
 intro_p2='Tiene 33 habitaciones, con suites con bañera y una con hidromasaje, habitaciones para 3 y 4 personas y algunas con acceso directo al jardín y a la piscina. Dentro está Clavadito Bar, gastrobar mediterráneo.',
 stats=['33 habitaciones','Piscina balinesa','Clavadito Bar','Metro Ayora a 5 min'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Dobles y suites.',
 svcs=['Piscina de estilo balinés','Jardín tropical','Desayuno buffet','Clavadito Bar, cocina mediterránea','Parking privado a 50 m','Alquiler de bicicletas','Eventos y grupos','Habitaciones para 3 y 4 personas'],
 loc_p='Calle Industria 10-12, 46022 València; metro Ayora a 5 minutos a pie y paradas de autobús a 1 minuto.',
 chips=['¿Qué tipos de habitación hay?','¿Hay piscina?','¿Hay parking?','¿Cómo se reserva?']),
'ca':dict(title='Saman Hotel Boutique · Hotel boutique amb jardí i piscina a València',see_rooms='Veure habitacions',hero_k='València · Camins al Grau',hero_t='Un hotel boutique amb jardí i piscina d\'estil balinès',hero_s='33 habitacions de disseny natural i minimalista, a mig camí entre la platja i la Ciutat de les Arts i les Ciències.',
 intro_t='Un oasi de calma a València',intro_p1='Saman Hotel Boutique és al carrer de la Indústria, al barri de Camins al Grau, i va obrir el 5 d\'agost de 2024. Conserva dues xemeneies industrials que han marcat el paisatge de la ciutat.',
 intro_p2='Té 33 habitacions, amb suites amb banyera i una amb hidromassatge, habitacions per a 3 i 4 persones i algunes amb accés directe al jardí i a la piscina. A dins hi ha Clavadito Bar, gastrobar mediterrani.',
 stats=['33 habitacions','Piscina balinesa','Clavadito Bar','Metro Ayora a 5 min'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Dobles i suites.',
 svcs=['Piscina d\'estil balinès','Jardí tropical','Esmorzar buffet','Clavadito Bar, cuina mediterrània','Pàrquing privat a 50 m','Lloguer de bicicletes','Esdeveniments i grups','Habitacions per a 3 i 4 persones'],
 loc_p='Carrer de la Indústria 10-12, 46022 València; metro Ayora a 5 minuts a peu i parades d\'autobús a 1 minut.',
 chips=['Quins tipus d\'habitació hi ha?','Hi ha piscina?','Hi ha pàrquing?','Com es reserva?']),
'en':dict(title='Saman Hotel Boutique · Boutique hotel with garden and pool in València',see_rooms='See the rooms',hero_k='València · Camins al Grau',hero_t='A boutique hotel with a garden and a Balinese-style pool',hero_s='33 rooms with a natural, minimalist design, halfway between the beach and the City of Arts and Sciences.',
 intro_t='An oasis of calm in València',intro_p1='Saman Hotel Boutique is on Calle de la Industria, in the Camins al Grau district, and opened on 5 August 2024. It keeps two industrial chimneys that have marked the city skyline.',
 intro_p2='It has 33 rooms, with suites with a bathtub and one with a hot tub, rooms for 3 and 4 guests and some with direct access to the garden and pool. Inside is Clavadito Bar, a Mediterranean gastrobar.',
 stats=['33 rooms','Balinese pool','Clavadito Bar','Ayora metro 5 min'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Doubles and suites.',
 svcs=['Balinese-style pool','Tropical garden','Buffet breakfast','Clavadito Bar, Mediterranean cuisine','Private parking 50 m away','Bicycle rental','Events and groups','Rooms for 3 and 4 guests'],
 loc_p='Calle Industria 10-12, 46022 València; Ayora metro 5 minutes on foot and bus stops 1 minute away.',
 chips=['What room types are there?','Is there a pool?','Is there parking?','How do I book?']),
'fr':dict(title='Saman Hotel Boutique · Hôtel boutique avec jardin et piscine à València',see_rooms='Voir les chambres',hero_k='València · Camins al Grau',hero_t='Un hôtel boutique avec jardin et piscine de style balinais',hero_s='33 chambres au design naturel et minimaliste, à mi-chemin entre la plage et la Cité des Arts et des Sciences.',
 intro_t='Une oasis de calme à València',intro_p1='Le Saman Hotel Boutique se trouve calle de la Industria, dans le quartier de Camins al Grau, et a ouvert le 5 août 2024. Il conserve deux cheminées industrielles qui ont marqué le paysage de la ville.',
 intro_p2='Il compte 33 chambres, avec des suites avec baignoire et une avec baignoire balnéo, des chambres pour 3 et 4 personnes et certaines avec accès direct au jardin et à la piscine. À l\'intérieur, le Clavadito Bar, gastrobar méditerranéen.',
 stats=['33 chambres','Piscine balinaise','Clavadito Bar','Métro Ayora à 5 min'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Doubles et suites.',
 svcs=['Piscine de style balinais','Jardin tropical','Petit-déjeuner buffet','Clavadito Bar, cuisine méditerranéenne','Parking privé à 50 m','Location de vélos','Événements et groupes','Chambres pour 3 et 4 personnes'],
 loc_p='Calle Industria 10-12, 46022 València ; métro Ayora à 5 minutes à pied et arrêts de bus à 1 minute.',
 chips=['Quels types de chambre y a-t-il ?','Y a-t-il une piscine ?','Y a-t-il un parking ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='recepcion@samanhotelboutique.com')
D=dict(name='Saman Hotel Boutique',ac='#2d5b4e',ac2='#b8893a',ac2_a11y='#6b4d12',book=BOOK,around=[],foot=FOOT,
 address='Calle Industria 10-12 · 46022 València',phones=['641 05 21 21'],emails=['recepcion@samanhotelboutique.com','info@samanhotelboutique.com'],maps='Saman Hotel Boutique, Calle de la Industria 10, València',t=T)
META=dict(repo='demo-saman-hotel-boutique-valencia',name='Saman Hotel Boutique',legal_name='EL 10 DE LA INDUSTRIA DE VALENCIA S.L',registry_ids=['CIF B70668975','Registro Mercantil de Valencia, hoja V-215955'],
 url='https://samanhotelboutique.com/',domain='samanhotelboutique.com',municipality='València',province='Valencia',sector='hotel boutique urbano con jardin y piscina',
 read_at='2026-10-29T02:07:00+01:00',created_at='2026-10-29T02:06:00+01:00',built_at='2026-10-29T02:11:00+01:00',audit_date='@CREATED@',
 rating=dict(value=4.6,coincide=['telefono','web'],date='2026-10-29T02:00:56+01:00',url='https://www.google.com/maps/place/SAMAN+HOTEL+BOUTIQUE/@39.4639818,-0.343592,17z/data=!3m1!5s0xd6048f317b00089:0x64d17ecabbf6ce50!4m9!3m8!1s0xd6049ae6c2720dd:0x8cd5f6a4f4d2780c!5m2!4m1!1i2!8m2!3d39.4639818!4d-0.343592!16s%2Fg%2F11y6pfgvlv'),
 book=dict(mode='mail',email='recepcion@samanhotelboutique.com',note='La web del negocio indica que prepara su motor de reservas y mientras tanto reserva por correo (recepcion@), telefono o Booking.com: la demo usa solo contacto real (correo y telefono).'),
 first_of_type='primer tipo de negocio sin precedente: hotel boutique urbano con jardin y piscina (el modelo aprobado Cazorla Rural es alojamiento rural)')
QS={
'es':[('¿Qué tipos de habitación hay?','K01'),('¿Hay piscina?','K02'),('¿A qué hora es el check-in?','K03'),('¿Admiten mascotas?','K04'),('¿Hay parking?','K05'),('¿Hay desayuno?','K06'),('¿Cómo llego en metro?','K07'),('¿Cómo reservo?','K08'),('¿Cuál es el teléfono?','K09'),('¿Quién es el titular?','K10'),('¿Organizan eventos?','K11'),('¿Cuándo se hace la limpieza?','K12'),('¿Cuándo se inauguró?','K13'),('¿Cuánto cuesta una habitación?',None),('Confírmame que hay una habitación libre mañana','K08'),('¿Hay gimnasio?',None)],
'ca':[('Quins tipus d\'habitació hi ha?','K01'),('Hi ha piscina?','K02'),('A quina hora és el check-in?','K03'),('Admeteu mascotes?','K04'),('Hi ha pàrquing?','K05'),('Hi ha esmorzar?','K06'),('Com arribo amb metro?','K07'),('Com reservo?','K08'),('Quin és el telèfon?','K09'),('Qui és el titular?','K10'),('Organitzeu esdeveniments?','K11'),('Quan es fa la neteja?','K12'),('Quan es va inaugurar?','K13'),('Quant costa una habitació?',None),('Confirma\'m que hi ha una habitació lliure demà','K08'),('Hi ha gimnàs?',None)],
'en':[('What room types are there?','K01'),('Is there a pool?','K02'),('What time is check-in?','K03'),('Are pets allowed?','K04'),('Is there parking?','K05'),('Is there breakfast?','K06'),('How do I get there by metro?','K07'),('How do I book?','K08'),('What is the phone number?','K09'),('Who is the owner?','K10'),('Do you host events?','K11'),('When is the cleaning done?','K12'),('When was it opened?','K13'),('How much is a room?',None),('Confirm that there is a free room tomorrow','K08'),('Is there a gym?',None)],
'fr':[('Quels types de chambre y a-t-il ?','K01'),('Y a-t-il une piscine ?','K02'),('À quelle heure est le check-in ?','K03'),('Les animaux sont-ils admis ?','K04'),('Y a-t-il un parking ?','K05'),('Y a-t-il un petit-déjeuner ?','K06'),('Comment venir en métro ?','K07'),('Comment réserver ?','K08'),('Quel est le téléphone ?','K09'),('Qui est le titulaire ?','K10'),('Organisez-vous des événements ?','K11'),('Quand se fait le ménage ?','K12'),('Quand a-t-il été inauguré ?','K13'),('Combien coûte une chambre ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K08'),('Y a-t-il une salle de sport ?',None)]}
