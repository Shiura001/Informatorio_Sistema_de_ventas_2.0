-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-11-2025 a las 18:41:25
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tiendaropa2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `login`
--

CREATE TABLE `login` (
  `id_user` int(11) NOT NULL,
  `username` varchar(40) NOT NULL,
  `password` varchar(150) NOT NULL,
  `level` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `login`
--

INSERT INTO `login` (`id_user`, `username`, `password`, `level`) VALUES
(1, 'admin', '$2b$12$MZR5s9q5ds0AFflGFOb5YeqxqkoUZuDkvpzkfxzFjFXiRRkqGlZ.q', 'admin'),
(2, 'Dylan', '$2b$12$GwhQ27uQxlPtYNcRZ4r.vOZ4OoVyl.GxVZ/WGswE793awCXTbzHaK', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `photos`
--

CREATE TABLE `photos` (
  `id_photo` int(11) NOT NULL,
  `ruta` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `photos`
--

INSERT INTO `photos` (`id_photo`, `ruta`) VALUES
(1522, 'Fotos/f.png'),
(1523, 'Fotos/1542-8074-ROJO_1.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id_producto` int(11) NOT NULL,
  `codigo_producto` varchar(100) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `color` varchar(40) NOT NULL,
  `talle` varchar(40) NOT NULL,
  `marca` varchar(40) NOT NULL,
  `categoria` varchar(40) NOT NULL,
  `stock_total` int(11) NOT NULL,
  `stock_min` int(11) NOT NULL,
  `precio_compra` decimal(10,0) NOT NULL,
  `precio_venta` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id_producto`, `codigo_producto`, `nombre`, `color`, `talle`, `marca`, `categoria`, `stock_total`, `stock_min`, `precio_compra`, `precio_venta`) VALUES
(1522, '001', 'Zapato', 'Negro', '42', 'Stone', 'Zapatos', 9, 5, 10000, 20000),
(1523, '002', 'Zapatilla', 'Rojo', '42', 'Jaguar', 'Zapatillas', 3, 1, 7500, 15000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro`
--

CREATE TABLE `registro` (
  `id_registro` int(11) NOT NULL,
  `usuario` varchar(40) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `tipo` varchar(40) NOT NULL,
  `total` decimal(20,0) NOT NULL,
  `fecha` varchar(40) NOT NULL,
  `metodo_pago` varchar(100) NOT NULL,
  `fecha2` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `registro`
--

INSERT INTO `registro` (`id_registro`, `usuario`, `nombre`, `descripcion`, `cantidad`, `tipo`, `total`, `fecha`, `metodo_pago`, `fecha2`) VALUES
(56, 'admin', 'zanadalia', 'color: negro talle: 41 marca: stone ', 1, 'Ventas', 15000, '30/05/2025 13:21:02', 'Efectivo', '31/07/2025'),
(57, 'admin', 'zanadalia', 'color: negro talle: 41 marca: stone ', 3, 'Ventas', 15000, '26/08/2025 13:30:28', 'Efectivo', '31/08/2025'),
(58, 'admin', 'zanadalia', 'color: negro talle: 41 marca: stone ', 1, 'Ventas', 15000, '31/07/2025 15:19:42', 'Efectivo', '31/07/2025'),
(59, 'admin', 'zanadalia', 'color: negro talle: 41 marca: stone ', 1, 'Ventas', 15000, '30/07/2025 13:21:02', 'Efectivo', '31/07/2025'),
(60, 'admin', ' ', 'color:   talle:  marca: ', 2, 'Ingreso de productos', 4, '25/08/2025 00:51:04', '-', '25/08/2025'),
(61, 'admin', ' ', 'color:   talle:  marca:  ', 2, 'Eliminación', 4, '26/08/2025 21:23:26', '-', '26/08/2025'),
(62, 'admin', 'as', 'color: q talle:q marca:q', 1, 'Ingreso de productos', 5555, '11/11/2025 14:12:59', '-', '11/11/2025'),
(63, 'admin', 'as', 'color: q talle:q marca:q ', 1, 'Eliminación', 5555, '11/11/2025 14:12:59', '-', '11/11/2025'),
(64, 'admin', 'zanadalia', 'color: negro talle:41 marca:stone ', 4, 'Eliminación', 40000, '11/11/2025 14:13:50', '-', '11/11/2025'),
(65, 'admin', 'zapatro', 'color: negro talle:41 marca:stone ', 5, 'Eliminación', 250000, '11/11/2025 14:13:55', '-', '11/11/2025'),
(66, 'admin', 'Zapato', 'color: Negro talle:42 marca:Stone', 10, 'Ingreso de productos', 100000, '11/11/2025 14:15:00', '-', '11/11/2025'),
(67, 'admin', 'Zapatilla', 'color: Rojo talle:42 marca:Jaguar', 5, 'Ingreso de productos', 37500, '11/11/2025 14:17:00', '-', '11/11/2025'),
(68, 'admin', 'Zapatilla', 'color: Rojo talle: 42 marca: Jaguar ', 4, 'Ventas', 60000, '11/11/2025 14:18:46', 'Efectivo', '11/11/2025'),
(69, 'admin', 'Zapato', 'color: Negro talle: 42 marca: Stone ', 1, 'Ventas', 20000, '11/11/2025 14:21:05', 'Efectivo', '11/11/2025'),
(70, 'admin', 'Zapatilla', 'color: Rojo talle: 42 marca: Jaguar ', 1, 'Ventas', 15000, '11/11/2025 14:32:36', 'Efectivo', '11/11/2025'),
(71, 'admin', 'Zapatilla', 'color: Rojo talle: 42 marca: Jaguar ', 1, 'Ventas', 15000, '11/11/2025 14:32:36', 'Efectivo', '11/11/2025');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id_user`);

--
-- Indices de la tabla `photos`
--
ALTER TABLE `photos`
  ADD PRIMARY KEY (`id_photo`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id_producto`);

--
-- Indices de la tabla `registro`
--
ALTER TABLE `registro`
  ADD PRIMARY KEY (`id_registro`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `login`
--
ALTER TABLE `login`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `photos`
--
ALTER TABLE `photos`
  MODIFY `id_photo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1524;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1524;

--
-- AUTO_INCREMENT de la tabla `registro`
--
ALTER TABLE `registro`
  MODIFY `id_registro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
