//
// Created by Kevin Morgan on 2020-04-18.
//
#include "mud.h"
#include "socket_channel.h"
#include "socket.h"
#include "hooks.h"

void socket_read(const char *info)
{
    SOCKET_DATA *dsock = NULL;
    int size;
    extern int errno;

    hookParseInfo(info, &dsock);

    /* check for buffer overflows, and drop connection in that case */
    size = strlen(dsock->inbuf);
    if (size >= sizeof(dsock->inbuf) - 2)
    {
        text_to_socket(dsock, "\n\r!!!! Input Overflow !!!!\n\r");
        dsock->valid_read = FALSE;
        return;
    }

    /* start reading from the socket */
    for (;;)
    {
        int sInput;
        int wanted = sizeof(dsock->inbuf) - 2 - size;

        sInput = read(dsock->control, dsock->inbuf + size, wanted);

        if (sInput > 0)
        {
            size += sInput;

            if (dsock->inbuf[size-1] == '\n' || dsock->inbuf[size-1] == '\r')
                break;
        }
        else if (sInput == 0)
        {
            log_string("Read_from_socket: EOF");
            dsock->valid_read = FALSE;
            return;
        }
        else if (errno == EAGAIN || sInput == wanted)
            break;
        else
        {
            perror("Read_from_socket");
            dsock->valid_read = FALSE;
            return;
        }
    }
    dsock->inbuf[size] = '\0';
    dsock->valid_read = TRUE;
    return;

}