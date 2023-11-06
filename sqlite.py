from asyncio.windows_events import NULL # para poder usar NULL en la BBDD
import sqlite3 as sq3 # la librería que maneja la BD

con = sq3.connect('mi_db.db')
cur = con.cursor()

instruct1 = '''CREATE TABLE IF NOT EXISTS escuelas (
  _id INTEGER PRIMARY KEY AUTOINCREMENT,  
  nombre varchar(45) DEFAULT NULL,
  localidad varchar(45) DEFAULT NULL,
  provincia varchar(45) DEFAULT NULL,
  capacidad INTEGER DEFAULT NULL)'''

instruct2 = '''CREATE TABLE IF NOT EXISTS alumnos (
	_id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_escuela INTEGER DEFAULT NULL,
	legajo INTEGER DEFAULT NULL,
	apellido VARCHAR(50) DEFAULT NULL,
	nombre VARCHAR(50) DEFAULT NULL,
	nota DECIMAL(10,0) DEFAULT NULL,
	grado INTEGER DEFAULT NULL,
	email VARCHAR(50) DEFAULT NULL,
	FOREIGN KEY (id_escuela) REFERENCES escuelas(id))'''

cur.execute(instruct1)
cur.execute(instruct2)

lista1 = [(1,'Carlos Guido y Spano','Ciudad de Buenos Aires','Buenos Aires',1250),(2,'Paula Albarracín de Sarmiento','Tres Arroyos','Buenos Aires',1100),(3,'Escuela Nro.392','Sijan','Catamarca',250),(4,'General Las Heras','Las Heras','Córdoba',1500),(5,'Gdor. Valentín Virasoro','Goya','Corrientes',750),(6,'E.E.P. Nro.852','El Sauzalito','Chaco',452),(7,'Tutú Maramba','Sarmiento','Chubut',356),(8,'Justo José de Urquiza','Colonia San Jorge','Entre Ríos',365),(9,'Sor Clotilde León', 'Clorinda', 'Formosa', 484),(10,'Escuela Nro.264','General Pico','La Pampa',652)]

lista2 = [(1, 8, 1035, 'Glandon', 'Aili', 10, 3, 'aglandon0@people.com.cn'),(2, 10, 1036, 'O''Carran', 'Davidson', 8, 3, 'docarran1@howstuffworks.com'),(3, 3, 1037, 'MacGiolla Pheadair', 'Godfry', 5, 6, 'gmacgiollapheadair2@deviantart.com'),(4, 9, 1038, 'Hame', 'Nesta', 9, 6, 'nhame3@seesaa.net'),(5, 6, 1039, 'Plume', 'Agna', 6, 3, 'aplume4@slate.com'),(6, 8, 1040, 'Scholl', 'Falkner', 8, 2, 'fscholl5@netvibes.com'),(7, 9, 1041, 'Shevelin', 'Artus', 4, 5, 'ashevelin6@nasa.gov'),(8, 10, 1042, 'Colleford', 'Debby', 10, 7, 'dcolleford7@hatena.ne.jp'),(9, 5, 1043, 'Aickin', 'Giacopo', 10, 5, 'gaickin8@seattletimes.com'),(10, 10, 1044, 'Cammomile', 'Lorri', 6, 5, 'lcammomile9@etsy.com'),(11, 5, 1045, 'Wharby', 'Tara', 6, 5, 'twharbya@dedecms.com'),(12, 5, 1046, 'Inman', 'Aimil', 7, 6, 'ainmanb@example.com'),(13, 2, 1047, 'Bakes', 'Sascha', 3, 3, 'sbakesc@tumblr.com'),(14, 2, 1048, 'Dismore', 'Ursola', 1, 5, 'udismored@theguardian.com'),(15, 4, 1049, 'Josling', 'Delcina', 3, 3, 'djoslinge@soup.io'),(16, 2, 1050, 'Scrannage', 'Chip', 2, 5, 'cscrannagef@squarespace.com'),(17, 3, 1051, 'Bakes', 'Sumner', 7, 3, 'sbakesg@bloglines.com'),(18, 4, 1052, 'Fleeman', 'Crysta', 5, 2, 'cfleemanh@ihg.com'),(19, 6, 1053, 'Fitchet', 'Nerty', 8, 1, 'nfitcheti@dagondesign.com'),(20, 5, 1054, 'Legister', 'Marcie', 7, 6, 'mlegisterj@wisc.edu'),(21, 6, 1055, 'Stading', 'Judas', 9, 7, 'jstadingk@prweb.com'),(22, 7, 1056, 'Jouannisson', 'Nonie', 6, 6, 'njouannissonl@sitemeter.com'),(23, 5, 1057, 'Corfield', 'Anny', 1, 3, 'acorfieldm@merriam-webster.com')]

cur.executemany('INSERT INTO escuelas VALUES (?,?,?,?,?)', lista1)
cur.executemany('INSERT INTO alumnos VALUES (?,?,?,?,?,?,?,?)', lista2)

query1 ='SELECT alumnos.legajo, alumnos.apellido, alumnos.nombre, alumnos.nota, alumnos.email, escuelas.nombre, escuelas.localidad, escuelas.provincia FROM alumnos INNER JOIN escuelas ON alumnos.id_escuela = escuelas._id LIMIT 5'

for registro in cur.execute(query1):
    print(registro)

con.commit() # confirma las operaciones sobre la bbdd
con.close() # cierra la conexión