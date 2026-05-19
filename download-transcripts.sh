#!/bin/bash
# Run this script from inside the ai-seo-content-research folder:
#   bash download-transcripts.sh

set -e
cd "$(dirname "$0")"

echo "Starting all 15 downloads in parallel..."

bash scripts/fetch_youtube.sh "https://www.youtube.com/watch?v=HXcEDHl4D-4" "bernard-huang" "how-to-win-at-answer-engine-optimization-aeo-with-ethan-smith" &
bash scripts/fetch_youtube.sh "https://www.youtube.com/watch?v=c-VtgjXWsK4" "bernard-huang" "the-future-of-search-seo-ai-seo-aeo-geo-with-lily-ray-kevin-indig-ross-hudgens-steve-toth" &
bash scripts/fetch_youtube.sh "https://www.youtube.com/watch?v=8RVUqitFcVk" "bernard-huang" "optimizing-your-aeo-and-seo-workflows-using-ai-claude-code-with-eric-siu" &
bash scripts/fetch_youtube.sh "https://www.youtube.com/watch?v=L7qfCzlQjxY" "aleyda-solis" "how-to-measure-the-impact-of-ai-overviews-on-organic-search-traffic" &
bash scripts/fetch_youtube.sh "https://www.youtube.com/watch?v=-4cu882OJ8E" "aleyda-solis" "traditional-seo-vs-ai-search-optimization-geo-aeo" &
bash scripts/fetch_youtube.sh "https://www.youtube.com/watch?v=ec8jDgmiksw" "aleyda-solis" "google-ai-mode-announcement-analysis" &
bash scripts/fetch_youtube.sh "https://www.youtube.com/watch?v=gReszNnykpg" "tim-soulo" "the-new-seo-playbook-for-ai-search-top-geo-ranking-factors" &
bash scripts/fetch_youtube.sh "https://www.youtube.com/watch?v=3iNJeArrUu4" "tim-soulo" "outsourced-our-digital-marketing-to-ai-heres-what-happened" &
bash scripts/fetch_youtube.sh "https://www.youtube.com/watch?v=KjK5-L-wDVg" "tim-soulo" "keyword-research-tutorial-for-google-and-ai-seo" &
bash scripts/fetch_youtube.sh "https://www.youtube.com/watch?v=p0XPAM-kQUk" "michael-king" "seo-is-not-ready-for-what-ai-is-about-to-do-mike-king-inside-seo-week" &
bash scripts/fetch_youtube.sh "https://www.youtube.com/watch?v=Bs6-ROULCLk" "michael-king" "the-brave-new-world-of-seo-seo-week-2025" &
bash scripts/fetch_youtube.sh "https://www.youtube.com/watch?v=pXNh0UYZ2C0" "tom-critchlow" "input-metrics-in-seo-leading-indicators-in-an-ai-world" &
bash scripts/fetch_youtube.sh "https://www.youtube.com/watch?v=z1qxqB_Cg3Q" "tom-critchlow" "the-future-of-search-and-the-death-of-links" &
bash scripts/fetch_youtube.sh "https://www.youtube.com/watch?v=qujABKOAThA" "kevin-indig" "seo-in-the-age-of-ai-kevin-indig-on-google-overviews-e-commerce-and-the-future-of-search" &
bash scripts/fetch_youtube.sh "https://www.youtube.com/watch?v=jQXvbeYF5go" "kevin-indig" "google-will-kill-your-traffic-heres-how-you-adapt" &

wait
echo "All downloads done! Converting .srt to .md..."

python3 scripts/clean_transcripts.py

echo "Done! Transcripts are in research/youtube-transcripts/"
find research/youtube-transcripts -type f | sort
