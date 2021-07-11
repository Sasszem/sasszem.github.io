---
title: "TBD"
layout: page
---

- hard

TBD

Note: You should be able to mount the file system and view every file without running into corrupted files. If you encounter corrupted files, it is probably because the filesystem was not correctly mounted/unpacked.

Also note: For this challenge, you'll have only 100 attempt to find the flag, so don't guess too much!

_author: kapi_

Attached file:
- [finalfinalversionforrealthistime](finalfinalversionforrealthistime)

## Writeup

`file` reports `finalfinalversionforrealthistime: Linux jffs2 filesystem data little endian` for the file given.

If we extract it using `jefferson`, we can see 2 filesystems and a few interesting files (for example the one with 10k `E`s again, but it's still not the flag),  such as a `flags` directory with `flag0` to `flag499` files, each containing 20 lines like `cd21{im_very_indecisive_BPtIgu}`, the last part being random.

The most interesting is the `README` file:
> I hate coming up with flags, they always sound lame. So with this challenge I wanted to make the perfect flag. I may have gone a bit overboard though... Anyways I wrote all the flag candidates under /pi/flags/ folder in multiple files, so I can organize them, and select the best one. Sadly I now realize, that I accidentally overwrote the perfect flag, and I can't remember it. Luckily I can remember that I wrote it in the file "flag404" on the 5. line at exactly 1612346514 unix time. I must have overwritten it later, because I can't find it anymore. Can you help me?

Hmkay, I guess we can do that...

I ended up modding `jefferson-3` to ignore nodes not made at that time:
```diff
324a325,326
>                     if inode.mtime==1612346514:
>                         print(inode)
407c409
<                     print('writing S_ISDIR'.format(path))
---
>                     ##print('writing S_ISDIR'.format(path))
411c413
<                     print('writing S_ISLNK'.format(path))
---
>                     ##print('writing S_ISLNK'.format(path))
418,419c420,421
<                     print('writing S_ISREG'.format(path))
<                     if not os.path.isfile(target_path):
---
>                     ##print('writing S_ISREG'.format(path))
>                     if not os.path.isfile(target_path) and inode.mtime==1612346514:
428c430
<                     os.chmod(target_path, stat.S_IMODE(inode.mode))
---
>                     #os.chmod(target_path, stat.S_IMODE(inode.mode))
431c433
<                     print('writing S_ISBLK'.format(path))
---
>                     #print('writing S_ISBLK'.format(path))
434c436
<                     print('writing S_ISBLK'.format(path))
---
>                     #print('writing S_ISBLK'.format(path))
437c439,440
<                     print('skipping S_ISFIFO'.format(path))
---
>                     #print('skipping S_ISFIFO'.format(path))
>                     pass
439c442,443
<                     print('skipping S_ISSOCK {}'.format(path))
---
>                     #print('skipping S_ISSOCK {}'.format(path))
>                     pass
473a478
>     args.verbose = False
```

Extracted the files with it, and grabbed the flag...