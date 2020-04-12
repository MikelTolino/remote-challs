/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   mmateo-t.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: miguel <miguel@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/04/01 00:20:53 by miguel            #+#    #+#             */
/*   Updated: 2020/04/01 02:20:29 by miguel           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

char *hv_rgb2hex(int r, int g, int b)
{
    char *hex;
    char *rgb2hex;

    hex = "0123456789abcdef";
    if (!(rgb2hex = malloc(sizeof(char) * 8)))
    {
        return (NULL);
    }
    if (r > 255 || b > 255 || g > 255 || b < 0 || g < 0 || r < 0)
    {
        return ("Error: Values are incorrect");
    }
    
    rgb2hex[0] = '#';
    rgb2hex[1] = hex[r / 16];
    rgb2hex[2] = hex[r % 16];
    rgb2hex[3] = hex[g / 16];
    rgb2hex[4] = hex[g % 16];
    rgb2hex[5] = hex[b / 16];
    rgb2hex[6] = hex[b % 16];
    rgb2hex[7] = '\0';

    return (rgb2hex);
}
