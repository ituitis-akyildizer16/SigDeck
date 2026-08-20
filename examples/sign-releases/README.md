# Signing releases

```
sd sign app-v1.2.tar.gz --key release.key
```

Ship the `.sig` next to the artifact and the `release.pub` on your site.
Users verify with:

```
sd verify app-v1.2.tar.gz --sig app-v1.2.tar.gz.sig --pub release.pub
```

Batch: `sigdeck/batch.py` signs every file in a directory in one pass.
