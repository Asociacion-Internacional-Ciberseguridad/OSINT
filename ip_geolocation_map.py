# ip_geolocation_map.py
import requests
import folium

def get_geolocation(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    return response.json()

def show_map(lat, lon, location_data):
    # Create a map centered at the given latitude and longitude
    map_obj = folium.Map(location=[lat, lon], zoom_start=10)

    # Add a marker with location details
    popup_info = f"""
    IP: {location_data['query']}<br>
    City: {location_data['city']}<br>
    Region: {location_data['regionName']}<br>
    Country: {location_data['country']}<br>
    ISP: {location_data['isp']}<br>
    Lat, Lon: {lat}, {lon}
    """
    folium.Marker([lat, lon], popup=folium.Popup(popup_info, max_width=300)).add_to(map_obj)

    # Save the map as an HTML file
    map_obj.save("geolocation_map.html")
    print("Map saved as 'geolocation_map.html'. Open it in your browser to view the location.")

if __name__ == "__main__":
    ip = input("Enter IP address: ")
    location_data = get_geolocation(ip)

    if location_data["status"] == "success":
        lat = location_data["lat"]
        lon = location_data["lon"]
        show_map(lat, lon, location_data)
    else:
        print("Failed to retrieve geolocation data. Please check the IP address.")
