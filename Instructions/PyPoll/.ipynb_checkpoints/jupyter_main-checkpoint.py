{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Resources\\election_data.csv\n"
     ]
    },
    {
     "ename": "FileNotFoundError",
     "evalue": "File b'Resources\\\\election_data.csv' does not exist",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-13-fca6899d8a6a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     12\u001b[0m \u001b[1;31m# Read our Data file with the pandas library\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[1;31m# Not every CSV requires an encoding, but be aware this can come up\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 14\u001b[1;33m \u001b[0mPyPollPath_df\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mPyPollPath_df\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mencoding\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"ISO-8859-1\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     15\u001b[0m \u001b[0mdf\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mPyPollPath_df\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcopy\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     16\u001b[0m \u001b[0mdf\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'change'\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdf\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'Profit/Losses'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdiff\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36mparser_f\u001b[1;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, escapechar, comment, encoding, dialect, tupleize_cols, error_bad_lines, warn_bad_lines, skipfooter, doublequote, delim_whitespace, low_memory, memory_map, float_precision)\u001b[0m\n\u001b[0;32m    676\u001b[0m                     skip_blank_lines=skip_blank_lines)\n\u001b[0;32m    677\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 678\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0m_read\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    679\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    680\u001b[0m     \u001b[0mparser_f\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__name__\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m_read\u001b[1;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[0;32m    438\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    439\u001b[0m     \u001b[1;31m# Create the parser.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 440\u001b[1;33m     \u001b[0mparser\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mTextFileReader\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    441\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    442\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mchunksize\u001b[0m \u001b[1;32mor\u001b[0m \u001b[0miterator\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[0;32m    785\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'has_index_names'\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mkwds\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'has_index_names'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    786\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 787\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_make_engine\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mengine\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    788\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    789\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mclose\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m_make_engine\u001b[1;34m(self, engine)\u001b[0m\n\u001b[0;32m   1012\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_make_engine\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mengine\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'c'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1013\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mengine\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m'c'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1014\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_engine\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mCParserWrapper\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1015\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1016\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mengine\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m'python'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, src, **kwds)\u001b[0m\n\u001b[0;32m   1706\u001b[0m         \u001b[0mkwds\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'usecols'\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0musecols\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1707\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1708\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_reader\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mparsers\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mTextReader\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msrc\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1709\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1710\u001b[0m         \u001b[0mpassed_names\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnames\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader.__cinit__\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader._setup_parser_source\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: File b'Resources\\\\election_data.csv' does not exist"
     ]
    }
   ],
   "source": [
    "#-main script to run for Pypoll analysis\n",
    "# Modules\n",
    "import os\n",
    "import pandas as pd\n",
    "import csv\n",
    "# Store filepath in a variable\n",
    "#PyPollPath_df = \"D:\\\\deym\\\\GWU_Boot Camp\\\\GWARL201902DATA3\\\\GWARL201902DATA3\\\\02-Homework\\\\03-Python\\\\Instructions\\\\PyPoll\\\\Resources\\election_data.csv\"\n",
    "PyPollPath_df = \"Resources\\election_data.csv\"\n",
    "print(PyPollPath_df)\n",
    "os.getcwd()\n",
    "\n",
    "# Read our Data file with the pandas library\n",
    "# Not every CSV requires an encoding, but be aware this can come up\n",
    "PyPollPath_df = pd.read_csv(PyPollPath_df, encoding=\"ISO-8859-1\")\n",
    "df = PyPollPath_df.copy()\n",
    "df['change'] = df['Profit/Losses'].diff()\n",
    "df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
