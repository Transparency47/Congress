# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/645?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/645
- Title: A resolution recognizing 2026 as the "International Year of Rangelands and Pastoralists".
- Congress: 119
- Bill type: SRES
- Bill number: 645
- Origin chamber: Senate
- Introduced date: 2026-03-17
- Update date: 2026-04-06T14:27:56Z
- Update date including text: 2026-04-06T14:27:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-17: Introduced in Senate
- 2026-03-17 - IntroReferral: Referred to the Committee on Energy and Natural Resources. (text: CR S1093-1094)
- 2026-03-17 - IntroReferral: Submitted in Senate
- Latest action: 2026-03-17: Submitted in Senate

## Actions

- 2026-03-17 - IntroReferral: Referred to the Committee on Energy and Natural Resources. (text: CR S1093-1094)
- 2026-03-17 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/645",
    "number": "645",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "A resolution recognizing 2026 as the \"International Year of Rangelands and Pastoralists\".",
    "type": "SRES",
    "updateDate": "2026-04-06T14:27:56Z",
    "updateDateIncludingText": "2026-04-06T14:27:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Energy and Natural Resources. (text: CR S1093-1094)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
          "date": "2026-03-17T20:04:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "NM"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "SD"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "NE"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "TN"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "MT"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "KS"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "MS"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "UT"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "ID"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "CO"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "NV"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "NV"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres645is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 645\nIN THE SENATE OF THE UNITED STATES\nMarch 17, 2026 Ms. Lummis (for herself, Mr. Luj\u00e1n , Mr. Rounds , Mr. Ricketts , Mrs. Blackburn , Mr. Daines , Mr. Moran , Mrs. Hyde-Smith , Mr. Curtis , Mr. Crapo , Mr. Hickenlooper , Ms. Rosen , and Ms. Cortez Masto ) submitted the following resolution; which was referred to the Committee on Energy and Natural Resources\nRESOLUTION\nRecognizing 2026 as the International Year of Rangelands and Pastoralists.\nThat the Senate\u2014\n**(1)**\nrecognizes 2026 as the International Year of Rangelands and Pastoralists ;\n**(2)**\nrecognizes the economic, social, and ecological importance of rangelands and the ranchers, farmers, land managers, pastoralists, and partners who have been caretakers of the American rangelands for generations; and\n**(3)**\nencourages Federal agencies, universities, and organizations across the country to engage in activities that promote education, research, and outreach related to rangeland management.",
      "versionDate": "2026-03-17",
      "versionType": "IS"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-27",
        "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1144",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Supporting recognition of 2026 as the \"International Year of Rangelands and Pastoralists\".",
      "type": "HRES"
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
        "updateDate": "2026-03-20T19:11:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-17",
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
          "measure-id": "id119sres645",
          "measure-number": "645",
          "measure-type": "sres",
          "orig-publish-date": "2026-03-17",
          "originChamber": "SENATE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres645v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2026-03-17",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution recognizes 2026 as the International Year of Rangelands and Pastoralists. It also\u00a0encourages federal agencies, universities, and organizations across the country to promote education, research, and outreach related to rangeland management.</p>"
        },
        "title": "A resolution recognizing 2026 as the \"International Year of Rangelands and Pastoralists\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres645.xml",
    "summary": {
      "actionDate": "2026-03-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution recognizes 2026 as the International Year of Rangelands and Pastoralists. It also\u00a0encourages federal agencies, universities, and organizations across the country to promote education, research, and outreach related to rangeland management.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119sres645"
    },
    "title": "A resolution recognizing 2026 as the \"International Year of Rangelands and Pastoralists\"."
  },
  "summaries": [
    {
      "actionDate": "2026-03-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution recognizes 2026 as the International Year of Rangelands and Pastoralists. It also\u00a0encourages federal agencies, universities, and organizations across the country to promote education, research, and outreach related to rangeland management.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119sres645"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres645is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution recognizing 2026 as the \"International Year of Rangelands and Pastoralists\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:48:40Z"
    },
    {
      "title": "A resolution recognizing 2026 as the \"International Year of Rangelands and Pastoralists\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T10:56:22Z"
    }
  ]
}
```
