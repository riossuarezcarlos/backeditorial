create database libreria;
use libreria;

create table t_estante(
	est_id int not null auto_increment primary key,
    est_cap int,
    est_ubic varchar(50),
    est_desc varchar(50)
);

create table t_autor(
	autor_id int not null auto_increment primary key,
    autor_nombre varchar(50)
);

create table t_libro(
	lib_id int not null auto_increment primary key,
    lib_nomb varchar(50),
    lib_editorial varchar(50),
    lib_numpag int,
    lib_precio decimal(5,2),
    lib_publicacion char(4),
    lib_cod text, 
    est_id int, 
    foreign key (est_id) references t_estante(est_id)
);
 

create table t_autorlibro(
	aut_lib_id int not null auto_increment primary key,
    lib_id int,
    autor_id int,
    foreign key (lib_id) references t_libro(lib_id),
    foreign key (autor_id) references t_autor(autor_id)
);