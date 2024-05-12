class Solution(object):
    def validIPAddress(self, queryIP):
        separate = queryIP.split('.')
        if len(separate) == 4:
            for item in separate:
                if not item.isdigit():
                    return 'Neither'
                if len(item) > 1 and item[0] == '0':
                    return 'Neither'
                if not 0 <= int(item) <= 255:
                    return 'Neither'
            return 'IPv4'

        separate = queryIP.split(':')
        if len(separate) == 8:
            for item in separate:
                if len(item) == 0 or len(item) > 4:
                    return 'Neither'
                for char in item:
                    if not char.isdigit() and char.lower() not in 'abcdef':
                        return 'Neither'
            return 'IPv6'

        return 'Neither'
