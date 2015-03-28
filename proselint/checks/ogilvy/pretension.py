# -*- coding: utf-8 -*-
"""EES: Pretension.

---
layout:     post
error_code: SCH
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10 12:31:19
categories: writing
---

Never use the phrase 'all hell broke loose'.

"""
from tools import existence_check, memoize


@memoize
def check_repeated_exclamations(blob):
    """Check the text."""
    err = "ogilvy.pretension"
    msg = u"Jargon words like this one are the hallmarks of a pretentious ass."

    list = [
        "reconceptualize",
        "demassification",
        "attitudinally",
        "judgmentally",
    ]

    return existence_check(blob, list, err, msg, max_errors=1)
