

export lat="33.44"
export lon="-94.04"
export api_key="c4cff409a04c1a3b55349f77cd26d0dd"

curl -X GET --header 'Accept: application/json' \
"https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&exclude=hourly,daily&appid=${api_key}"

