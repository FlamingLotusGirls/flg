// vim:set ts=4 sw=4 ai:
/*
 * Copyright 2009 Erik Gilling
 * Copyright 2014 Michael Toren <mct@toren.net>
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef __libavr_uart_h__
#define __libavr_uart_h__

#include <avr/pgmspace.h>
#include <avr/io.h>

#ifndef FOSC
#error "FOSC not defined"
#endif

static inline void uart_enable_tx(void)
{
	UCSR0B |= _BV(TXCIE0);
}

static inline void uart_disable_tx(void)
{
	UCSR0B &= ~_BV(TXCIE0);
}

static inline uint8_t uart_char_avail(void)
{
	return (UCSR0A & _BV(RXC0));
}

void uart_init(uint32_t ubrr);
void uart_putc(unsigned char data);
void uart_puts(const char *s);
void uart_puts_P(const char *s);
void uart_printhex(uint8_t val);
int uart_has_data(void);
unsigned char uart_poll_getchar(void);

#endif /* __libavr_uart_h__ */
