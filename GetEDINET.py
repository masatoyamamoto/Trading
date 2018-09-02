from edinet_xbrl.edinet_xbrl_downloader import EdinetXbrlDownloader

# Download SC's XBRL
# init downloader
xbrl_downloader = EdinetXbrlDownloader()

## set a ticker you want to download xbrl file
ticker = "8053"
target_dir = "."
xbrl_downloader.download_by_ticker(ticker, target_dir)
