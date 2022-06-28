
## [[xyz.png]] -> ![resources/xyz.png]
## [[xyz]]     -> ![xyz]

## per line:
                # m = re.search (r'\[\[([^]]*.png)\]\]', line)
                # if (m):
                #     s = re.sub (r'\[\[([^]]*)\]\]', f'![{m.group(1)}](resources/' + markua (m.group(1)) + ')', line)
                #     ...
                # else:
                #     m = re.search (r'\[\[([^]]*)\]\]', line)
                #     if (m):
                #         s = re.sub (r'\[\[([^]]*)\]\]', f'[{m.group(1)}](#' + markua (m.group(1)) + ')', line)
                #     ...
                    
