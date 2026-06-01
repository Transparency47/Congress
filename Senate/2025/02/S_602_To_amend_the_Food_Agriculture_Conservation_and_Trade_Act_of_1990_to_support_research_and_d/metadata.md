# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/602?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/602
- Title: Wildfire Resilience Through Grazing Research Act
- Congress: 119
- Bill type: S
- Bill number: 602
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2025-09-17T11:03:17Z
- Update date including text: 2025-09-17T11:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/602",
    "number": "602",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Wildfire Resilience Through Grazing Research Act",
    "type": "S",
    "updateDate": "2025-09-17T11:03:17Z",
    "updateDateIncludingText": "2025-09-17T11:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-02-13T20:39:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "HI"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "KS"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "OK"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "NV"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CO"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s602is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 602\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Padilla (for himself, Ms. Hirono , Mr. Moran , and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food, Agriculture, Conservation, and Trade Act of 1990 to support research and development of ungulate grazing land management techniques for purposes of wildfire mitigation, fuel reduction, and post-fire recovery.\n#### 1. Short title\nThis Act may be cited as the Wildfire Resilience Through Grazing Research Act .\n#### 2. Grazing for wildfire mitigation research and development\nSection 1672(d) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5925(d) ) is amended by adding at the end the following:\n(21) Grazing for wildfire mitigation initiative (A) Definitions In this paragraph: (i) Land-grant institution The term land-grant institution means an 1862 Institution, 1890 Institution, or 1994 Institution (as those terms are defined in section 2 of the Agricultural Research, Extension, and Education Reform Act of 1998 ( 7 U.S.C. 7601 )). (ii) Ungulate The term ungulate means a hooved grazing mammal. (B) Initiative Research and extension grants may be made under this section at land-grant institutions for the purposes of\u2014 (i) supporting research and development of ungulate grazing land management techniques that\u2014 (I) promote wildfire mitigation, fuel reduction, and post-fire recovery on public land and private land, including research and development relating to understanding the economic benefits of, and increasing social support for, such activities; (II) are compatible with activities that protect against adverse environmental effects, including the spread of invasive plant species and disease, soil erosion, water quality degradation, and watershed degradation, such as\u2014 (aa) rotational grazing; (bb) managed stocking rates; (cc) riparian buffer zones; (dd) cover crops; (ee) fencing, including virtual fencing; (ff) manipulation of wild ungulate populations through targeted wildlife management; and (gg) water point management techniques; and (III) improve soil health; and (ii) disseminating information to public and private landowners, land managers, and livestock owners, including through providing educational materials and conducting outreach programs, regarding\u2014 (I) ungulate grazing land management techniques that promote wildfire mitigation, fuel reduction, and post-fire recovery; and (II) compatible activities described in clause (i). .",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-03-20T19:46:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s602",
          "measure-number": "602",
          "measure-type": "s",
          "orig-publish-date": "2025-02-13",
          "originChamber": "SENATE",
          "update-date": "2025-06-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s602v00",
            "update-date": "2025-06-23"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Wildfire Resilience Through Grazing Research Act</strong></p><p>This bill expands the high-priority research and extension areas\u00a0at the Department of Agriculture (USDA) to include\u00a0the research and development of ungulate grazing land management techniques to promote wildfire mitigation, fuel reduction, and post-fire recovery. (An\u00a0<em>ungulate</em> is a hooved grazing mammal.)\u00a0</p><p>Specifically, the bill allows USDA to provide grants to land-grant institutions for supporting the\u00a0research and development of wildfire-related ungulate grazing land management techniques that improve soil health and are compatible with activities that protect against adverse environmental effects. This includes compatibility with activities that\u00a0protect against the spread of invasive plant species and disease, soil erosion, water quality degradation, and watershed degradation.</p><p>The grants to land-grant universities may also be used to disseminate information to public and private landowners, land managers, and livestock owners regarding these wildfire-related\u00a0grazing land management techniques and compatible activities.\u00a0</p>"
        },
        "title": "Wildfire Resilience Through Grazing Research Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s602.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Wildfire Resilience Through Grazing Research Act</strong></p><p>This bill expands the high-priority research and extension areas\u00a0at the Department of Agriculture (USDA) to include\u00a0the research and development of ungulate grazing land management techniques to promote wildfire mitigation, fuel reduction, and post-fire recovery. (An\u00a0<em>ungulate</em> is a hooved grazing mammal.)\u00a0</p><p>Specifically, the bill allows USDA to provide grants to land-grant institutions for supporting the\u00a0research and development of wildfire-related ungulate grazing land management techniques that improve soil health and are compatible with activities that protect against adverse environmental effects. This includes compatibility with activities that\u00a0protect against the spread of invasive plant species and disease, soil erosion, water quality degradation, and watershed degradation.</p><p>The grants to land-grant universities may also be used to disseminate information to public and private landowners, land managers, and livestock owners regarding these wildfire-related\u00a0grazing land management techniques and compatible activities.\u00a0</p>",
      "updateDate": "2025-06-23",
      "versionCode": "id119s602"
    },
    "title": "Wildfire Resilience Through Grazing Research Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Wildfire Resilience Through Grazing Research Act</strong></p><p>This bill expands the high-priority research and extension areas\u00a0at the Department of Agriculture (USDA) to include\u00a0the research and development of ungulate grazing land management techniques to promote wildfire mitigation, fuel reduction, and post-fire recovery. (An\u00a0<em>ungulate</em> is a hooved grazing mammal.)\u00a0</p><p>Specifically, the bill allows USDA to provide grants to land-grant institutions for supporting the\u00a0research and development of wildfire-related ungulate grazing land management techniques that improve soil health and are compatible with activities that protect against adverse environmental effects. This includes compatibility with activities that\u00a0protect against the spread of invasive plant species and disease, soil erosion, water quality degradation, and watershed degradation.</p><p>The grants to land-grant universities may also be used to disseminate information to public and private landowners, land managers, and livestock owners regarding these wildfire-related\u00a0grazing land management techniques and compatible activities.\u00a0</p>",
      "updateDate": "2025-06-23",
      "versionCode": "id119s602"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s602is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Wildfire Resilience Through Grazing Research Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-17T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Wildfire Resilience Through Grazing Research Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food, Agriculture, Conservation, and Trade Act of 1990 to support research and development of ungulate grazing land management techniques for purposes of wildfire mitigation, fuel reduction, and post-fire recovery.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:33:41Z"
    }
  ]
}
```
