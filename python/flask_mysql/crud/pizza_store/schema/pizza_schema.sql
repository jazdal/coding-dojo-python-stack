-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema pizza_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `pizza_schema` ;

-- -----------------------------------------------------
-- Schema pizza_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pizza_schema` DEFAULT CHARACTER SET utf8 ;
USE `pizza_schema` ;

-- -----------------------------------------------------
-- Table `pizza_schema`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pizza_schema`.`customers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pizza_schema`.`pizzas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pizza_schema`.`pizzas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `pizza_type` VARCHAR(255) NULL,
  `pizza_crust` VARCHAR(255) NULL,
  `pizza_size` VARCHAR(255) NULL,
  `pizza_sauce` VARCHAR(255) NULL,
  `amount_of_toppings` INT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `customer_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pizzas_customers_idx` (`customer_id` ASC) VISIBLE,
  CONSTRAINT `fk_pizzas_customers`
    FOREIGN KEY (`customer_id`)
    REFERENCES `pizza_schema`.`customers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
