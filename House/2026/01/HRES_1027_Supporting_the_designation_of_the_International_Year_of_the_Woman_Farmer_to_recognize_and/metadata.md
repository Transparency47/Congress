# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1027?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1027
- Title: Supporting the designation of the "International Year of the Woman Farmer" to recognize and honor the critical role of women in agriculture.
- Congress: 119
- Bill type: HRES
- Bill number: 1027
- Origin chamber: House
- Introduced date: 2026-01-30
- Update date: 2026-03-12T12:32:43Z
- Update date including text: 2026-03-12T12:32:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-01-30: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-30 - IntroReferral: Submitted in House
- 2026-01-30 - IntroReferral: Submitted in House
- Latest action: 2026-01-30: Submitted in House

## Actions

- 2026-01-30 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-30 - IntroReferral: Submitted in House
- 2026-01-30 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-30",
    "latestAction": {
      "actionDate": "2026-01-30",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1027",
    "number": "1027",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "P000597",
        "district": "1",
        "firstName": "Chellie",
        "fullName": "Rep. Pingree, Chellie [D-ME-1]",
        "lastName": "Pingree",
        "party": "D",
        "state": "ME"
      }
    ],
    "title": "Supporting the designation of the \"International Year of the Woman Farmer\" to recognize and honor the critical role of women in agriculture.",
    "type": "HRES",
    "updateDate": "2026-03-12T12:32:43Z",
    "updateDateIncludingText": "2026-03-12T12:32:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-30",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-01-30T15:31:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "IA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "MN"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "WA"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "OH"
    },
    {
      "bioguideId": "L000491",
      "district": "3",
      "firstName": "Frank",
      "fullName": "Rep. Lucas, Frank D. [R-OK-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lucas",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "OK"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "CA"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "IL"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "HI"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "FL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "NC"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "KS"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "IL"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "TN"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "GA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "OR"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "OH"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "CT"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "MD"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "CA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "KS"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1027ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1027\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 30, 2026 Ms. Pingree (for herself, Mrs. Hinson , Ms. Craig , Mr. Newhouse , Ms. Brown , Mr. Lucas , Mr. Gray , Mr. Bost , Ms. Tokuda , Mrs. Cammack , Mr. Davis of North Carolina , Mr. Mann , Ms. Budzinski , Mr. Rose , Mr. Bishop , Ms. Salinas , Ms. Kaptur , Mrs. Hayes , Mrs. McClain Delaney , and Mr. Costa ) submitted the following resolution; which was referred to the Committee on Agriculture\nRESOLUTION\nSupporting the designation of the International Year of the Woman Farmer to recognize and honor the critical role of women in agriculture.\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of the International Year of the Woman Farmer ;\n**(2)**\nrecognizes the critical role of women in agriculture; and\n**(3)**\nencourages all citizens to\u2014\n**(A)**\nhonor and recognize the contributions of women working in agriculture; and\n**(B)**\ncelebrate the positive impact these women have on the food systems and agricultural workforce of the United States by encouraging and empowering women to\u2014\n**(i)**\npursue careers in agriculture, a high-demand and essential field;\n**(ii)**\ncultivate leadership opportunities; and\n**(iii)**\nhelp feed a growing and hungry world.",
      "versionDate": "2026-01-30",
      "versionType": "IH"
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
        "actionDate": "2026-01-29",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S397; text: CR S381)"
      },
      "number": "592",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution supporting the designation of 2026 as the \"International Year of the Woman Farmer\" to recognize and honor the critical role of women in agriculture.",
      "type": "SRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Food supply, safety, and labeling",
            "updateDate": "2026-02-06T18:00:12Z"
          },
          {
            "name": "Women in business",
            "updateDate": "2026-02-06T18:00:12Z"
          },
          {
            "name": "Women's employment",
            "updateDate": "2026-02-06T18:00:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2026-02-03T20:57:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-30",
    "originChamber": "House",
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
          "measure-id": "id119hres1027",
          "measure-number": "1027",
          "measure-type": "hres",
          "orig-publish-date": "2026-01-30",
          "originChamber": "HOUSE",
          "update-date": "2026-03-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1027v00",
            "update-date": "2026-03-12"
          },
          "action-date": "2026-01-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of the International Year of the Woman Farmer and recognizes the critical role of women in agriculture.</p><p>The resolution also encourages citizens to celebrate the impact these women have on the\u00a0food systems and agricultural workforce of the United States by encouraging and empowering women to pursue careers in agriculture and cultivate leadership opportunities.</p>"
        },
        "title": "Supporting the designation of the \"International Year of the Woman Farmer\" to recognize and honor the critical role of women in agriculture."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1027.xml",
    "summary": {
      "actionDate": "2026-01-30",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of the International Year of the Woman Farmer and recognizes the critical role of women in agriculture.</p><p>The resolution also encourages citizens to celebrate the impact these women have on the\u00a0food systems and agricultural workforce of the United States by encouraging and empowering women to pursue careers in agriculture and cultivate leadership opportunities.</p>",
      "updateDate": "2026-03-12",
      "versionCode": "id119hres1027"
    },
    "title": "Supporting the designation of the \"International Year of the Woman Farmer\" to recognize and honor the critical role of women in agriculture."
  },
  "summaries": [
    {
      "actionDate": "2026-01-30",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of the International Year of the Woman Farmer and recognizes the critical role of women in agriculture.</p><p>The resolution also encourages citizens to celebrate the impact these women have on the\u00a0food systems and agricultural workforce of the United States by encouraging and empowering women to pursue careers in agriculture and cultivate leadership opportunities.</p>",
      "updateDate": "2026-03-12",
      "versionCode": "id119hres1027"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1027ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting the designation of the \"International Year of the Woman Farmer\" to recognize and honor the critical role of women in agriculture.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-31T09:18:22Z"
    },
    {
      "title": "Supporting the designation of the \"International Year of the Woman Farmer\" to recognize and honor the critical role of women in agriculture.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-31T09:05:49Z"
    }
  ]
}
```
