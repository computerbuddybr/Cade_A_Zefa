----------------------------------------------------
-- Table `casos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `casos` (
  `pk_id_caso` INTEGER PRIMARY KEY AUTOINCREMENT,
  `fk_id_cidade` INTEGER,
  `titulo` VARCHAR,
  `caso` VARCHAR,
  `tarefa` VARCHAR,
  `mensagem_de_vitoria` VARCHAR);

-- -----------------------------------------------------
-- Table `continentes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `continentes` (
  `pk_id_continente` INTEGER PRIMARY KEY AUTOINCREMENT,
  `continente` VARCHAR);

-- -----------------------------------------------------
-- Table `paises`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `paises` (
  `pk_id_pais` INTEGER PRIMARY KEY AUTOINCREMENT,
  `fk_id_continente` INTEGER,
  `pais` VARCHAR,
  `cores_bandeira` VARCHAR,
  `imagem_bandeira` VARCHAR,
  `moeda` VARCHAR
  );

-- -----------------------------------------------------
-- Table `cidades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cidades` (
  `pk_id_cidade` INTEGER PRIMARY KEY AUTOINCREMENT,
  `fk_id_pais` INTEGER,
  `cidade` VARCHAR,
  `latitude` VARCHAR,
  `longitude` VARCHAR);

  -- -----------------------------------------------------
-- Table `curiosidades_cidades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `curiosidades_cidades` (
  `pk_id_curiosidades` INTEGER PRIMARY KEY AUTOINCREMENT,
  `fk_id_cidade` INTEGER,
  `curiosidade` VARCHAR);



-- -----------------------------------------------------
-- Table `personagens`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `personagens` (
  `pk_id_personagem` INTEGER PRIMARY KEY AUTOINCREMENT,
  `personagem` VARCHAR);




-- -----------------------------------------------------
-- Table `locais`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `locais` (
  `pk_id_local` INTEGER PRIMARY KEY AUTOINCREMENT,
  `local` VARCHAR,
  `bandeira` BOOLEAN,
  `pista_cidade` BOOLEAN
  `moeda` BOOLEAN);


  -- -----------------------------------------------------
-- Table `local_personagem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `local_personagem` (
  `pk_id_local_personagem` INTEGER PRIMARY KEY AUTOINCREMENT,
  `fk_id_local` INTEGER,
  `fk_id_personagem` INTEGER);



-- -----------------------------------------------------
-- Table `pista_da_cidade` - Esta pista está relacionada a uma cidade a qual ela descreve
-- ------------------------------------------- -----------
CREATE TABLE IF NOT EXISTS `pista_da_cidade` (
  `pk_id_pista` INTEGER PRIMARY KEY AUTOINCREMENT,
  `fk_id_cidade` INTEGER,
  `pista_tag` VARCHAR,
  `pista` VARCHAR);  




