# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

INCLUDES = """
#include <openssl/crypto.h>
#include <openssl/evp.h>
"""

TYPES = """
static const long Cryptography_HAS_300_FIPS;
static const long Cryptography_HAS_LEGACY_FIPS;
"""

FUNCTIONS = """
"""

CUSTOMIZATIONS = """
#ifndef OSSL_LIB_CTX
/**
 * HACK: OSSL_LIB_CTX is only defined on 3.x+.
 *
 * Fake it on non-3.x versions with a bogus #define (deviates less than using a
 * typedef).
 */
#define OSSL_LIB_CTX    void
#endif

#if CRYPTOGRAPHY_IS_LIBRESSL
static const long Cryptography_HAS_300_FIPS = 0;
static const long Cryptography_HAS_FIPS = 0;

int (*EVP_default_properties_enable_fips)(OSSL_LIB_CTX *, int) = NULL;
int (*EVP_default_properties_is_fips_enabled)(OSSL_LIB_CTX *) = NULL;
int (*FIPS_mode)(void) = NULL;
int (*FIPS_mode_set)(int) = NULL;

# elif CRYPTOGRAPHY_OPENSSL_300_OR_GREATER
/* Provide a 1.x/3.x version agnostic set of FIPS APIs. */
static const long Cryptography_HAS_300_FIPS = 1;
static const long Cryptography_HAS_LEGACY_FIPS = 0;

int (*FIPS_mode)(void) = NULL;
int (*FIPS_mode_set)(int) = NULL;

# else
static const long Cryptography_HAS_300_FIPS = 0;
static const long Cryptography_HAS_LEGACY_FIPS = 1;

int (*EVP_default_properties_enable_fips)(OSSL_LIB_CTX *, int) = NULL;
int (*EVP_default_properties_is_fips_enabled)(OSSL_LIB_CTX*) = NULL;
#endif
"""
