#ifndef SOCKET_H
#define SOCKET_H
//*****************************************************************************
// socket.h
//
// all of the functions needed for working with character sockets
//*****************************************************************************
#include <zlib.h>

typedef HASHTABLE AUX_TABLE;

int init_socket(void);

void init_socket_pipeline(void);

SOCKET_DATA *new_socket(int sock);

void close_socket(SOCKET_DATA *dsock, bool reconnect);

bool read_from_socket(SOCKET_DATA *dsock);

void input_handler(void);

void output_handler(void);

void copyover_recover(void);

void do_copyover(void);

/* sends the output directly */
bool text_to_socket(SOCKET_DATA *dsock, const char *txt);

void send_to_socket(SOCKET_DATA *dsock, const char *format, ...) __attribute__ ((format (printf, 2, 3)));

/* buffers the output        */
void text_to_buffer(SOCKET_DATA *dsock, const char *txt);

void next_cmd_from_buffer(SOCKET_DATA *dsock);

bool flush_output(SOCKET_DATA *dsock);

void handle_new_connections(SOCKET_DATA *dsock, char *arg);

void clear_socket(SOCKET_DATA *sock_new, int sock);

void recycle_sockets(void);

void *lookup_address(void *arg);


//*****************************************************************************
// set and get functions
//*****************************************************************************
int socketGetDNSLookupStatus(SOCKET_DATA *sock);

CHAR_DATA *socketGetChar(SOCKET_DATA *dsock);

void socketSetChar(SOCKET_DATA *dsock, CHAR_DATA *ch);

ACCOUNT_DATA *socketGetAccount(SOCKET_DATA *dsock);

void socketSetAccount(SOCKET_DATA *dsock, ACCOUNT_DATA *account);

void socketPushInputHandler(SOCKET_DATA *socket,
                            void handler(SOCKET_DATA *socket, char *input),
                            void prompt(SOCKET_DATA *socket),
                            const char *state);

void socketReplaceInputHandler(SOCKET_DATA *socket,
                               void handler(SOCKET_DATA *socket, char *input),
                               void prompt(SOCKET_DATA *socket),
                               const char *state);

void socketPushPyInputHandler(SOCKET_DATA *sock, void *handler, void *prompt,
                              const char *state);

void socketReplacePyInputHandler(SOCKET_DATA *sock, void *handler, void *prompt,
                                 const char *state);

void socketPopInputHandler(SOCKET_DATA *socket);

void *socketGetAuxiliaryData(SOCKET_DATA *sock, const char *name);

const char *socketGetHostname(SOCKET_DATA *sock);

BUFFER *socketGetTextEditor(SOCKET_DATA *sock);

BUFFER *socketGetOutbound(SOCKET_DATA *sock);

void socketQueueCommand(SOCKET_DATA *sock, const char *cmd);

int socketGetUID(SOCKET_DATA *sock);

bool socketHasPrompt(SOCKET_DATA *sock);

void socketBustPrompt(SOCKET_DATA *sock);

void socketShowPrompt(SOCKET_DATA *sock);

bool socketHasCommand(SOCKET_DATA *sock);

const char *socketGetLastCmd(SOCKET_DATA *sock);

const char *socketGetState(SOCKET_DATA *sock);

double socketGetIdleTime(SOCKET_DATA *sock);


//
// Here it is... the big ol' datastructure for sockets. Yum.
struct socket_data {
    CHAR_DATA *player;
    ACCOUNT_DATA *account;
    char *hostname;
    char inbuf[MAX_INPUT_LEN];
    char input_work[MAX_INPUT_LEN];
    int input_index;
    BUFFER *next_command;
    BUFFER *iac_sequence;
    // char            next_command[MAX_BUFFER];
    bool cmd_read;
    bool bust_prompt;
    bool closed;
    bool valid_read;
    int lookup_status;
    int control;
    int uid;
    double idle;          // how many pulses have we been idle for?

    char *page_string;   // the string that has been paged to us
    int curr_page;     // the current page we're on
    int tot_pages;     // the total number of pages the string has

    BUFFER *text_editor;   // where we do our actual work
    BUFFER *outbuf;        // our buffer of pending output

    LIST *input_handlers;// a stack of our input handlers and prompts
    LIST *input;         // lines of input we have received
    LIST *command_hist;  // the commands we've executed in the past

    unsigned char compressing;                 /* MCCP support */
    z_stream *out_compress;                /* MCCP support */
    unsigned char *out_compress_buf;            /* MCCP support */

    AUX_TABLE *auxiliary;     // auxiliary data installed by other modules
};


//
// contains an input handler and the socket prompt in one structure, so they
// can be stored together in the socket_data. Allows for the option of Python
// or C input handlers and prompt pairs.
typedef struct input_handler_data {
    void *handler; // (* handler)(SOCKET_DATA *, char *);
    void *prompt; // (*  prompt)(SOCKET_DATA *);
    bool python;
    char *state; // what state does this input handler represent?
} IH_PAIR;


//
// required for looking up a socket's IP in a new thread
typedef struct lookup_data {
    SOCKET_DATA *dsock;   // the socket we wish to do a hostlookup on
    char *buf;     // the buffer it should be stored in
} LOOKUP_DATA;


#endif // SOCKET_H
