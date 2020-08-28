CREATE DATABASE datos;

USE [datos]
GO
/****** Object:  Table [dbo].[datos]    Script Date: 04/08/2020 21:33:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[datos](
	[id] [smallint] IDENTITY(1,1) NOT NULL,
	[texto] [varchar](50) NOT NULL,
	[descripcion] [varchar](120) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[datos] ON 

INSERT [dbo].[datos] ([id], [texto], [descripcion]) VALUES (1, N'Godzilla', N'Dinosaurio radiactivo protector')
INSERT [dbo].[datos] ([id], [texto], [descripcion]) VALUES (2, N'Poletergeish', N'Fantasmas que estan atrapados en la realidad.')
INSERT [dbo].[datos] ([id], [texto], [descripcion]) VALUES (3, N'Valiente', N'Historia de lazos rotos y restaurados.sdvsvs')
INSERT [dbo].[datos] ([id], [texto], [descripcion]) VALUES (4, N'Dark', N'Relato de la paradoja del tiempo y espacio')
INSERT [dbo].[datos] ([id], [texto], [descripcion]) VALUES (5, N'50 Sombras de Gris', N'Pelicula por la cual las mujeres lloran mucho')
INSERT [dbo].[datos] ([id], [texto], [descripcion]) VALUES (6, N'Dark', N'Pelicula que no se le encuentra sentido :)')
INSERT [dbo].[datos] ([id], [texto], [descripcion]) VALUES (7, N'Piratas del Caribe', N'Serie buenisima')
INSERT [dbo].[datos] ([id], [texto], [descripcion]) VALUES (8, N'La casa de papel', N'los personales usan Trajes rojos')
INSERT [dbo].[datos] ([id], [texto], [descripcion]) VALUES (15, N'Superman', N'Hombre de capa negra')
INSERT [dbo].[datos] ([id], [texto], [descripcion]) VALUES (16, N'Hombre Araña', N'Tira tela araña')
INSERT [dbo].[datos] ([id], [texto], [descripcion]) VALUES (17, N'Gato con botas', N'Tiene botas')
INSERT [dbo].[datos] ([id], [texto], [descripcion]) VALUES (19, N'Hombre Araña', N'No tiene poderes')
SET IDENTITY_INSERT [dbo].[datos] OFF
