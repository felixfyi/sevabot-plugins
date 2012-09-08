require 'soundcloud'

# register a client with YOUR_CLIENT_ID as client_id_
client = Soundcloud.new(:client_id => 'YOUR_CLIENT_ID')
# get 10 hottest tracks
tracks = client.get('/tracks', :limit => 10, :order => 'hotness')
# print each link
tracks.each do |track|
  puts track.permalink_url
end
