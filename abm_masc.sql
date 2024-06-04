-- Limpiamos la tabla antes de insertar datos nuevos
DELETE FROM modelos_carritoproducto;


INSERT INTO modelos_carritoproducto (cantidad_carrito_producto, fecha_carrito, producto_id, usuario_id)
VALUES
(3, '2024-01-10 14:23:45.123456', 101, 201),
(2, '2024-01-12 09:15:30.654321', 102, 202),
(1, '2024-01-15 11:00:00.000000', 103, 203),
(5, '2024-01-20 16:45:00.000000', 104, 204),
(4, '2024-01-22 08:30:15.123456', 105, 205),
(2, '2024-01-25 13:20:50.654321', 106, 206),
(6, '2024-01-28 10:10:10.000000', 107, 207),
(3, '2024-02-01 12:00:00.000000', 108, 208),
(1, '2024-02-05 17:45:30.123456', 109, 209),
(4, '2024-02-10 19:30:15.654321', 110, 210),
(5, '2024-02-12 14:22:45.000000', 111, 211),
(2, '2024-02-15 09:17:30.123456', 112, 212),
(3, '2024-02-18 11:05:50.654321', 113, 213),
(1, '2024-02-20 16:50:00.000000', 114, 214),
(4, '2024-02-25 08:40:15.000000', 115, 215);


DELETE FROM modelos_categoria;


INSERT INTO modelos_categoria (nombre_categoria, fecha_creacion_categoria)
VALUES
('Pintura', '2023-01-10 10:15:30.123456'),
('Escultura', '2023-02-15 11:45:50.654321'),
('Fotografía', '2023-03-20 09:30:00.000000'),
('Cerámica', '2023-04-25 14:00:00.000000'),
('Textiles', '2023-05-30 16:45:15.123456'),
('Joyería', '2023-06-05 08:20:45.654321'),
('Artesanía', '2023-07-10 12:35:50.000000'),
('Grabado', '2023-08-15 15:50:30.123456'),
('Dibujo', '2023-09-20 17:25:10.654321'),
('Ilustración', '2023-10-25 19:00:00.000000');

DELETE FROM modelos_facturacion;

INSERT INTO modelos_facturacion (total_facturacion, fecha_facturacion, usuario_id)
VALUES
(150.75, '2024-01-10 14:23:45.123456', 201),
(75.50, '2024-01-12 09:15:30.654321', 202),
(300.00, '2024-01-15 11:00:00.000000', 203),
(45.99, '2024-01-20 16:45:00.000000', 204),
(120.50, '2024-01-22 08:30:15.123456', 205),
(200.25, '2024-01-25 13:20:50.654321', 206),
(89.99, '2024-01-28 10:10:10.000000', 207),
(160.00, '2024-02-01 12:00:00.000000', 208),
(45.50, '2024-02-05 17:45:30.123456', 209),
(210.75, '2024-02-10 19:30:15.654321', 210),
(75.00, '2024-02-12 14:22:45.000000', 211),
(320.40, '2024-02-15 09:17:30.123456', 212),
(99.99, '2024-02-18 11:05:50.654321', 213),
(450.00, '2024-02-20 16:50:00.000000', 214),
(180.50, '2024-02-25 08:40:15.000000', 215);


DELETE FROM modelos_historialcarrito;

INSERT INTO modelos_historialcarrito (fecha_historial_carrito, total_historial_carrito, usuario_id)
VALUES
('2024-01-05 10:15:30.123456', 50.75, 201),
('2024-01-10 14:23:45.654321', 150.00, 202),
('2024-01-15 11:00:00.000000', 300.99, 203),
('2024-01-20 16:45:00.000000', 25.50, 204),
('2024-01-25 08:30:15.123456', 60.30, 205),
('2024-01-30 13:20:50.654321', 120.45, 206),
('2024-02-05 10:10:10.000000', 89.99, 207),
('2024-02-10 12:00:00.000000', 160.00, 208),
('2024-02-15 17:45:30.123456', 45.50, 209),
('2024-02-20 19:30:15.654321', 210.75, 210),
('2024-02-25 14:22:45.000000', 75.00, 211),
('2024-03-02 09:17:30.123456', 320.40, 212),
('2024-03-07 11:05:50.654321', 99.99, 213),
('2024-03-12 16:50:00.000000', 450.00, 214),
('2024-03-17 08:40:15.000000', 180.50, 215);

DELETE FROM modelos_pago;

INSERT INTO modelos_pago (metodo_pago, fecha_pago, total_pago, usuario_id)
VALUES
('Tarjeta de Crédito', '2024-01-05 10:15:30.123456', 150.75, 201),
('PayPal', '2024-01-10 14:23:45.654321', 75.50, 202),
('Transferencia Bancaria', '2024-01-15 11:00:00.000000', 300.00, 203),
('Tarjeta de Débito', '2024-01-20 16:45:00.000000', 45.99, 204),
('Efectivo', '2024-01-25 08:30:15.123456', 120.50, 205),
('Tarjeta de Crédito', '2024-01-30 13:20:50.654321', 200.25, 206),
('PayPal', '2024-02-05 10:10:10.000000', 89.99, 207),
('Transferencia Bancaria', '2024-02-10 12:00:00.000000', 160.00, 208),
('Tarjeta de Débito', '2024-02-15 17:45:30.123456', 45.50, 209),
('Efectivo', '2024-02-20 19:30:15.654321', 210.75, 210),
('Tarjeta de Crédito', '2024-02-25 14:22:45.000000', 75.00, 211),
('PayPal', '2024-03-02 09:17:30.123456', 320.40, 212),
('Transferencia Bancaria', '2024-03-07 11:05:50.654321', 99.99, 213),
('Tarjeta de Débito', '2024-03-12 16:50:00.000000', 450.00, 214),
('Efectivo', '2024-03-17 08:40:15.000000', 180.50, 215);


DELETE FROM modelos_producto;

INSERT INTO modelos_producto (nombre_producto, descripcion_producto, precio_producto, fecha_creacion_producto, categoria_id, subcategoria_id)
VALUES
('Pintura al Óleo', 'Una hermosa pintura al óleo de un paisaje.', 150.75, '2024-01-05 10:15:30.123456', 1, 101),
('Escultura de Mármol', 'Escultura tallada en mármol blanco.', 2500.00, '2024-01-10 14:23:45.654321', 2, 102),
('Fotografía en Blanco y Negro', 'Fotografía artística en blanco y negro.', 300.00, '2024-01-15 11:00:00.000000', 3, 103),
('Vasija de Cerámica', 'Vasija de cerámica hecha a mano.', 45.99, '2024-01-20 16:45:00.000000', 4, 104),
('Manta de Lana', 'Manta tejida a mano con lana de alpaca.', 120.50, '2024-01-25 08:30:15.123456', 5, 105),
('Collar de Plata', 'Collar de plata con diseño único.', 200.25, '2024-01-30 13:20:50.654321', 6, 106),
('Cesta de Mimbre', 'Cesta artesanal de mimbre.', 89.99, '2024-02-05 10:10:10.000000', 7, 107),
('Grabado en Madera', 'Grabado artístico en madera.', 160.00, '2024-02-10 12:00:00.000000', 8, 108),
('Retrato a Lápiz', 'Retrato detallado a lápiz.', 45.50, '2024-02-15 17:45:30.123456', 9, 109),
('Ilustración Digital', 'Ilustración digital de fantasía.', 210.75, '2024-02-20 19:30:15.654321', 10, 110),
('Acrílico sobre Lienzo', 'Pintura acrílica sobre lienzo.', 175.00, '2024-02-25 14:22:45.000000', 1, 101),
('Escultura en Bronce', 'Escultura fundida en bronce.', 3200.40, '2024-03-02 09:17:30.123456', 2, 102),
('Foto de Paisaje', 'Fotografía de un paisaje natural.', 99.99, '2024-03-07 11:05:50.654321', 3, 103),
('Jarrón de Cerámica', 'Jarrón de cerámica con motivos florales.', 85.00, '2024-03-12 16:50:00.000000', 4, 104),
('Bufanda de Seda', 'Bufanda de seda pintada a mano.', 180.50, '2024-03-17 08:40:15.000000', 5, 105);


DELETE FROM modelos_subcategoria;

INSERT INTO modelos_subcategoria (nombre_subcategoria, fecha_creacion_subcategoria, categoria_id)
VALUES
('Pintura Abstracta', '2024-01-05 10:15:30.123456', 1),
('Pintura Realista', '2024-01-10 14:23:45.654321', 1),
('Escultura Clásica', '2024-01-15 11:00:00.000000', 2),
('Escultura Moderna', '2024-01-20 16:45:00.000000', 2),
('Fotografía Digital', '2024-01-25 08:30:15.123456', 3),
('Fotografía Analógica', '2024-01-30 13:20:50.654321', 3),
('Cerámica Utilitaria', '2024-02-05 10:10:10.000000', 4),
('Cerámica Decorativa', '2024-02-10 12:00:00.000000', 4),
('Textiles Tradicionales', '2024-02-15 17:45:30.123456', 5),
('Textiles Modernos', '2024-02-20 19:30:15.654321', 5),
('Joyería Contemporánea', '2024-02-25 14:22:45.000000', 6),
('Joyería Tradicional', '2024-03-02 09:17:30.123456', 6),
('Artesanía de Mimbre', '2024-03-07 11:05:50.654321', 7),
('Artesanía de Madera', '2024-03-12 16:50:00.000000', 7),
('Grabado en Metal', '2024-03-17 08:40:15.000000', 8),
('Grabado en Piedra', '2024-03-22 10:15:30.123456', 8),
('Dibujo a Lápiz', '2024-03-27 14:23:45.654321', 9),
('Dibujo a Tinta', '2024-04-01 11:00:00.000000', 9),
('Ilustración Digital', '2024-04-06 16:45:00.000000', 10),
('Ilustración Tradicional', '2024-04-11 08:30:15.123456', 10);


DELETE FROM modelos_usuario;


INSERT INTO modelos_usuario (nombre_usuario, email_usuario, password_usuario, telefono_usuario, token_usuario, bio_usuario, fotodeperfil_usuario, fecha_creacion_usuario)
VALUES
('user1', 'user1@example.com', 'password1', '123456789', 'token1', 'Bienvenido a mi perfil.', 'avatar1.jpg', '2024-01-01 10:00:00'),
('user2', 'user2@example.com', 'password2', '987654321', 'token2', 'Soy un amante del arte.', 'avatar2.jpg', '2024-01-02 11:00:00'),
('user3', 'user3@example.com', 'password3', '456789123', 'token3', 'Artista en crecimiento.', 'avatar3.jpg', '2024-01-03 12:00:00'),
('user4', 'user4@example.com', 'password4', '789123456', 'token4', 'Explorando nuevas técnicas.', 'avatar4.jpg', '2024-01-04 13:00:00'),
('user5', 'user5@example.com', 'password5', '321654987', 'token5', 'Comparto mi pasión por el arte.', 'avatar5.jpg', '2024-01-05 14:00:00');













