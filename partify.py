import spotipy
import spotipy.util as util


if __name__ == '__main__':
    sp = spotipy.Spotify()
    username = "dwj300"
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username, scope)
    playlist_id = "4lEJEXO1sdJ7rwXW8Zm3oN"
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        # results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
        # print results
        playlists = sp.user_playlists(username)
    else:
        print "Can't get token for", username
