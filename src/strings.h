/*
 * strings.h - header file for strings library used by NakedMud, some 
 * superficial renaming done for consistency, but strings.c and strings.h
 * are derived from STRLIB 2. See: LICENSE.MD for details
 * ---
 * STRLib 2.0 -- A C dynamic strings library
 *
 * Copyright (c) 2006-2015, Salvatore Sanfilippo <antirez at gmail dot com>
 * Copyright (c) 2015, Oran Agra
 * Copyright (c) 2015, Redis Labs, Inc
 * All rights reserved.
 */
#define s_malloc malloc
#define s_realloc realloc
#define s_free free

#ifndef __STR_H
#define __STR_H

#define STR_MAX_PREALLOC (1024*1024)
extern const char *STR_NOINIT;

#include <sys/types.h>
#include <stdarg.h>
#include <stdint.h>

typedef char *string;

/* Note: sdshdr5 is never used, we just access the flags byte directly.
 * However is here to document the layout of type 5 STR strings. */
struct __attribute__ ((__packed__)) sdshdr5 {
    unsigned char flags; /* 3 lsb of type, and 5 msb of string length */
    char buf[];
};
struct __attribute__ ((__packed__)) sdshdr8 {
    uint8_t len; /* used */
    uint8_t alloc; /* excluding the header and null terminator */
    unsigned char flags; /* 3 lsb of type, 5 unused bits */
    char buf[];
};
struct __attribute__ ((__packed__)) sdshdr16 {
    uint16_t len; /* used */
    uint16_t alloc; /* excluding the header and null terminator */
    unsigned char flags; /* 3 lsb of type, 5 unused bits */
    char buf[];
};
struct __attribute__ ((__packed__)) sdshdr32 {
    uint32_t len; /* used */
    uint32_t alloc; /* excluding the header and null terminator */
    unsigned char flags; /* 3 lsb of type, 5 unused bits */
    char buf[];
};
struct __attribute__ ((__packed__)) sdshdr64 {
    uint64_t len; /* used */
    uint64_t alloc; /* excluding the header and null terminator */
    unsigned char flags; /* 3 lsb of type, 5 unused bits */
    char buf[];
};

#define STR_TYPE_5  0
#define STR_TYPE_8  1
#define STR_TYPE_16 2
#define STR_TYPE_32 3
#define STR_TYPE_64 4
#define STR_TYPE_MASK 7
#define STR_TYPE_BITS 3
#define STR_HDR_VAR(T,s) struct sdshdr##T *sh = (void*)((s)-(sizeof(struct sdshdr##T)));
#define STR_HDR(T,s) ((struct sdshdr##T *)((s)-(sizeof(struct sdshdr##T))))
#define STR_TYPE_5_LEN(f) ((f)>>STR_TYPE_BITS)

static inline size_t str_length(const string s) {
    unsigned char flags = s[-1];
    switch(flags&STR_TYPE_MASK) {
        case STR_TYPE_5:
            return STR_TYPE_5_LEN(flags);
        case STR_TYPE_8:
            return STR_HDR(8,s)->len;
        case STR_TYPE_16:
            return STR_HDR(16,s)->len;
        case STR_TYPE_32:
            return STR_HDR(32,s)->len;
        case STR_TYPE_64:
            return STR_HDR(64,s)->len;
    }
    return 0;
}

static inline size_t str_avail(const string s) {
    unsigned char flags = s[-1];
    switch(flags&STR_TYPE_MASK) {
        case STR_TYPE_5: {
            return 0;
        }
        case STR_TYPE_8: {
            STR_HDR_VAR(8,s);
            return sh->alloc - sh->len;
        }
        case STR_TYPE_16: {
            STR_HDR_VAR(16,s);
            return sh->alloc - sh->len;
        }
        case STR_TYPE_32: {
            STR_HDR_VAR(32,s);
            return sh->alloc - sh->len;
        }
        case STR_TYPE_64: {
            STR_HDR_VAR(64,s);
            return sh->alloc - sh->len;
        }
    }
    return 0;
}

static inline void str_set_length(string s, size_t newlen) {
    unsigned char flags = s[-1];
    switch(flags&STR_TYPE_MASK) {
        case STR_TYPE_5:
            {
                unsigned char *fp = ((unsigned char*)s)-1;
                *fp = STR_TYPE_5 | (newlen << STR_TYPE_BITS);
            }
            break;
        case STR_TYPE_8:
            STR_HDR(8,s)->len = newlen;
            break;
        case STR_TYPE_16:
            STR_HDR(16,s)->len = newlen;
            break;
        case STR_TYPE_32:
            STR_HDR(32,s)->len = newlen;
            break;
        case STR_TYPE_64:
            STR_HDR(64,s)->len = newlen;
            break;
    }
}

static inline void str_grow(string s, size_t inc) {
    unsigned char flags = s[-1];
    switch(flags&STR_TYPE_MASK) {
        case STR_TYPE_5:
            {
                unsigned char *fp = ((unsigned char*)s)-1;
                unsigned char newlen = STR_TYPE_5_LEN(flags)+inc;
                *fp = STR_TYPE_5 | (newlen << STR_TYPE_BITS);
            }
            break;
        case STR_TYPE_8:
            STR_HDR(8,s)->len += inc;
            break;
        case STR_TYPE_16:
            STR_HDR(16,s)->len += inc;
            break;
        case STR_TYPE_32:
            STR_HDR(32,s)->len += inc;
            break;
        case STR_TYPE_64:
            STR_HDR(64,s)->len += inc;
            break;
    }
}

/* str_alloc() = str_avail() + str_length() */
static inline size_t str_alloc(const string s) {
    unsigned char flags = s[-1];
    switch(flags&STR_TYPE_MASK) {
        case STR_TYPE_5:
            return STR_TYPE_5_LEN(flags);
        case STR_TYPE_8:
            return STR_HDR(8,s)->alloc;
        case STR_TYPE_16:
            return STR_HDR(16,s)->alloc;
        case STR_TYPE_32:
            return STR_HDR(32,s)->alloc;
        case STR_TYPE_64:
            return STR_HDR(64,s)->alloc;
    }
    return 0;
}

static inline void str_set_alloc(string s, size_t newlen) {
    unsigned char flags = s[-1];
    switch(flags&STR_TYPE_MASK) {
        case STR_TYPE_5:
            /* Nothing to do, this type has no total allocation info. */
            break;
        case STR_TYPE_8:
            STR_HDR(8,s)->alloc = newlen;
            break;
        case STR_TYPE_16:
            STR_HDR(16,s)->alloc = newlen;
            break;
        case STR_TYPE_32:
            STR_HDR(32,s)->alloc = newlen;
            break;
        case STR_TYPE_64:
            STR_HDR(64,s)->alloc = newlen;
            break;
    }
}

string str_new_length(const void *init, size_t initlen);
string str_new(const char *init);
string str_empty(void);
string str_duplicate(const string s);
void str_free(string s);
string str_grow_zero(string s, size_t len);
string str_append_len(string s, const void *t, size_t len);
string str_append(string s, const char *t);
string str_add(string s, const string t);
string str_copy_length(string s, const char *t, size_t len);
string str_copy(string s, const char *t);

string str_add_vprintf(string s, const char *fmt, va_list ap);
#ifdef __GNUC__
string str_add_printf(string s, const char *fmt, ...)
    __attribute__((format(printf, 2, 3)));
#else
string str_add_printf(string s, const char *fmt, ...);
#endif

string str_add_fmt(string s, char const *fmt, ...);
string str_trim_chars(string s, const char *cset);
void str_range(string s, ssize_t start, ssize_t end);
void str_fix_length(string s);
void str_clear(string s);
int str_compare(const string s1, const string s2);
string *str_split_len(const char *s, ssize_t len, const char *sep, int seplen, int *count);
void str_free_splitres(string *tokens, int count);
void str_to_lower(string s);
void str_to_upper(string s);
string str_from_longlong(long long value);
string str_add_repr(string s, const char *p, size_t len);
string *str_split_args(const char *line, int *argc);
string str_map_chars(string s, const char *from, const char *to, size_t setlen);
string str_join(char **argv, int argc, char *sep);
string str_join_str(string *argv, int argc, const char *sep, size_t seplen);

/* Low level functions exposed to the user API */
string strMakeRoomFor(string s, size_t addlen);
void strIncrLen(string s, ssize_t incr);
string strRemoveFreeSpace(string s);
size_t strAllocSize(string s);
void *strAllocPtr(string s);

/* Export the allocator used by STR to the program using STR.
 * Sometimes the program STR is linked to, may use a different set of
 * allocators, but may want to allocate or free things that STR will
 * respectively free or allocate. */
void *str_malloc(size_t size);
void *str_realloc(void *ptr, size_t size);
void str_free_alloc(void *ptr);

#endif