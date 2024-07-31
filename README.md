
# Kurdish Speech Corpus

## Introduction

This corpus comprises speech data collected from various sources to facilitate research and development in Automatic Speech Recognition (ASR) for the Kurdish language. The dataset includes recordings from Telegram bot interactions and YouTube broadcasts, processed and normalized for quality and consistency.

## Data Collection

### Sources
1. **Telegram Bot**
   - **Sentences Collected**: 1000 sentences
   - **Recording Method**: Collected speech data amounting to 70 hours using a Telegram bot.
   - **Manual Verification**: The speech and corresponding text were manually checked and mapped for accuracy.

2. **YouTube Broadcasts**
   - **Data Crawling**: 30 hours of broadcast content were crawled from YouTube.
   - **Annotation**: The collected data were manually labeled to ensure correctness.

## Preprocessing Steps

### For Telegram Bot Data
1. **Human Manual Checking**: Ensuring the accuracy of mapping between speech and text.
2. **Normalization**: Applied Asosoft Normalizing to standardize the audio data.

### For YouTube Data
1. **Speech Segmentation**: Applied Voice Activity Detection (VAD) to split speech signals into segments ranging from 3 to 15 seconds.
2. **Normalization**: Applied Asosoft Normalizing to ensure consistency in the audio quality.

## Data Structure

- **End Sources 1**: Contains processed data from Telegram bot recordings.
- **End Sources 2**: Contains processed data from YouTube broadcasts.

## Usage

The dataset is suitable for training ASR systems and can be utilized for both academic research and practical applications in improving Kurdish speech recognition technologies. Researchers and developers can leverage the dataset to fine-tune existing models or develop new algorithms for Kurdish ASR systems.

## Acknowledgments

We acknowledge the contributions of the volunteers who helped in data collection and manual annotation. Special thanks to the teams involved in developing the tools and methodologies used in preprocessing the data.

## Citation

If you use this corpus in your research, please cite the following paper:

Abdullah, A.A., Veisi, H. and Rashid, T., 2024. Breaking Walls: Pioneering Automatic Speech Recognition for Central Kurdish: End-to-End Transformer Paradigm. arXiv preprint arXiv:2406.02561.
