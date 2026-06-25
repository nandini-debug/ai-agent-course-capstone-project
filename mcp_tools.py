import re

class URLScannerTool:

    def scan(self, text):

        urls = re.findall(
            r"https?://[^\s]+",
            text
        )

        return {
            "urls_found": urls,
            "count": len(urls)
        }