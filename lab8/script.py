jq -r '.[] | "\(.name),\(.html_url),\(.updated_at),\(.visibility)"' data/schacon.repos.json \
| head -n 5 \
| sed '1i name,html_url,updated_at,visibility' > chacon.csv

