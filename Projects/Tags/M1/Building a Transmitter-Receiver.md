- [Squarer Circuits](https://resources.pcb.cadence.com/blog/2019-what-is-a-squarer-circuit)
- [Multiplier](https://www.ti.com/lit/ds/symlink/mpy634.pdf)
- https://www.argos-system.org/make-your-own-argos-transmitter/
- https://www.woodsholegroup.com/solutions/sustainable-fisheries-management/
- https://arribada.org/



Is it just open source now?
- https://arribada.org/
- https://blog.st.com/kineis/
- https://www.st.com/content/st_com/en/products/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus/stm32-wireless-mcus/stm32wl-series.html
- https://www.digikey.com/en/products/category/rf-and-wireless/37?s=N4IgjCBcoLQBxVAYygMwIYBsDOBTANCAPZQDaIALAJwDsIAugL6OEBMZIAygCoCyAzKwDqAGX78A0nABqANgaMgA
	- 5 bucks??????
- https://www.st.com/content/st_com/en/partner/partner-program/partnerpage/Kineis.html
- https://www.kineis.com/en/kineis-stack-for-a-quick-integration-2/
- https://telemetry.groupcls.com/argos-solutions/argos-products/modems/

CLS is the group! And they've been providing hardware like this for a long while. 

## I2C

https://wiki.st.com/stm32mcu/wiki/Getting_started_with_I2C#Configure_I-
https://embeddedespresso.com/temperature-measurement-never-so-easy-with-stm32-and-mcp9808/

Current question is - how do I get data onto and off of the tag without using an antenna. With that I'll be able to build my own tag and maybe even try geolocating :D 

## SPI 

https://wiki.st.com/stm32mcu/wiki/Getting_started_with_SPI
https://www.digikey.com/en/maker/projects/getting-started-with-stm32-how-to-use-spi/09eab3dfe74c4d0391aaaa99b0a8ee17

MAKE SURE THE BYTE SIZE IS 8 BITS... not the default 4 (screams)


```
const uint8_t RDSR = 0x05;

const uint8_t WREN = 0x06;

const uint8_t READ = 0x03;

const uint8_t SERASE = 0x20;

const uint8_t PP = 0x02;

  

int main(void)

{

  

/* USER CODE BEGIN 1 */

  

/* USER CODE END 1 */

  

/* MCU Configuration--------------------------------------------------------*/

  

/* Reset of all peripherals, Initializes the Flash interface and the Systick. */

HAL_Init();

  

uint8_t spi_buf;

char read_address[4];

read_address[0] = READ;

read_address[1] = 0x0;

read_address[2] = 0x0;

read_address[3] = 0x0;

  

char serase_address[4];

serase_address[0] = SERASE;

serase_address[1] = 0x0;

serase_address[2] = 0x0;

serase_address[3] = 0x0;

  

char page[256];

uint16_t i;

for (i=0; i<256; i++) {

page[i] = 0x0;

}

  

/* USER CODE BEGIN Init */

  

/* USER CODE END Init */

  

/* Configure the system clock */

SystemClock_Config();

  

/* USER CODE BEGIN SysInit */

  

/* USER CODE END SysInit */

  

/* Initialize all configured peripherals */

MX_GPIO_Init();

MX_SPI1_Init();

/* USER CODE BEGIN 2 */

  

/* USER CODE END 2 */

  

do {

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_RESET);

HAL_SPI_Transmit(&hspi1, (uint8_t *)&RDSR, 1, 100);

HAL_SPI_Receive(&hspi1, (uint8_t *)&spi_buf, 1, 100);

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_SET);

} while (spi_buf & 0x01); // bit 0 is WIP

  

  

/*HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_RESET);

HAL_SPI_Transmit(&hspi1, (uint8_t *)&WREN, 1, 100);

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_SET);*/

  

// READ DATA

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_RESET);

HAL_StatusTypeDef command_status = HAL_SPI_Transmit(&hspi1, (uint8_t *)&read_address, 4, 100);

HAL_StatusTypeDef read_status = HAL_SPI_Receive(&hspi1, (uint8_t *)&page, 256, 100);

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_SET);

  

  

// WRITE ENABLE

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_RESET);

HAL_SPI_Transmit(&hspi1, (uint8_t *)&WREN, 1, 100);

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_SET);

  

do {

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_RESET);

HAL_SPI_Transmit(&hspi1, (uint8_t *)&RDSR, 1, 100);

HAL_SPI_Receive(&hspi1, (uint8_t *)&spi_buf, 1, 100);

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_SET);

} while (!(spi_buf & 0b00000010));

  

// ERASE SECTOR

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_RESET);

HAL_StatusTypeDef serase_status = HAL_SPI_Transmit(&hspi1, (uint8_t *)&serase_address, 4, 100);

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_SET);

  

do {

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_RESET);

HAL_SPI_Transmit(&hspi1, (uint8_t *)&RDSR, 1, 100);

HAL_SPI_Receive(&hspi1, (uint8_t *)&spi_buf, 1, 100);

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_SET);

} while (spi_buf & 0x01); // bit 0 is WIP

  

// READ DATA

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_RESET);

HAL_StatusTypeDef command_status2 = HAL_SPI_Transmit(&hspi1, (uint8_t *)&read_address, 4, 100);

HAL_StatusTypeDef read_status2 = HAL_SPI_Receive(&hspi1, (uint8_t *)&page, 256, 100);

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_SET);

  

// WRITE ENABLE

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_RESET);

HAL_SPI_Transmit(&hspi1, (uint8_t *)&WREN, 1, 100);

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_SET);

  

do {

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_RESET);

HAL_SPI_Transmit(&hspi1, (uint8_t *)&RDSR, 1, 100);

HAL_SPI_Receive(&hspi1, (uint8_t *)&spi_buf, 1, 100);

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_SET);

} while (!(spi_buf & 0b00000010));

  

// WRITE DATA

char write_stuff[5];

write_stuff[0] = PP;

write_stuff[1] = 0x0;

write_stuff[2] = 0x0;

write_stuff[3] = 0x0;

write_stuff[4] = 0b10101010;

  

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_RESET);

HAL_StatusTypeDef write_status = HAL_SPI_Transmit(&hspi1, (uint8_t *)&write_stuff, 5, 100);

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_SET);

  

do {

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_RESET);

HAL_SPI_Transmit(&hspi1, (uint8_t *)&RDSR, 1, 100);

HAL_SPI_Receive(&hspi1, (uint8_t *)&spi_buf, 1, 100);

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_SET);

} while (spi_buf & 0x01);

  

// READ DATA

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_RESET);

HAL_StatusTypeDef command_status3 = HAL_SPI_Transmit(&hspi1, (uint8_t *)&read_address, 4, 100);

HAL_StatusTypeDef read_status3 = HAL_SPI_Receive(&hspi1, (uint8_t *)&page, 256, 100);

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_SET);

  

  

  

  

  

/* Infinite loop */

/* USER CODE BEGIN WHILE */

while (1)

{

/* USER CODE END WHILE */

  

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_RESET);

HAL_SPI_Transmit(&hspi1, (uint8_t *)&RDSR, 1, 100);

HAL_SPI_Receive(&hspi1, (uint8_t *)&spi_buf, 1, 100);

HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, GPIO_PIN_SET);

  

/* USER CODE BEGIN 3 */

}

/* USER CODE END 3 */

}
```