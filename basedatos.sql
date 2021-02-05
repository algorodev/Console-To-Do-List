CREATE DATABASE IF NOT EXISTS todo_list;
use todo_list;

CREATE TABLE usuarios(
    id          integer(25) auto_increment not null,
    nombre      varchar(100),
    apellidos   varchar(255),
    email       varchar(255) not null,
    password    varchar(100) not null,
    fecha       date not null,

    constraint pk_usuarios PRIMARY KEY(id),
    constraint uq_email UNIQUE(email)
)ENGINE = InnoDb;

CREATE TABLE notas(
    id          integer(25) auto_increment not null,
    usuario_id  integer(25) not null,
    titulo      varchar(255) not null,
    descripcion mediumtext,
    fecha       date not null,

    constraint pk_notas PRIMARY KEY(id),
    constraint fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE = InnoDb;
