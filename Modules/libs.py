import os
import re
import sys
import json
import logging
import asyncio
from pathlib import Path

from curl_cffi import requests as curl
from curl_cffi.requests import AsyncSession as CurlAsyncSession
