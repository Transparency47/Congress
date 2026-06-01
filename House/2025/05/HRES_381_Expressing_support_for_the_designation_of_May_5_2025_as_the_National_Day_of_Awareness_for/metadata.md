# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/381?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/381
- Title: Expressing support for the designation of May 5, 2025, as the "National Day of Awareness for Missing and Murdered Indigenous Women and Girls".
- Congress: 119
- Bill type: HRES
- Bill number: 381
- Origin chamber: House
- Introduced date: 2025-05-05
- Update date: 2026-05-07T02:27:57Z
- Update date including text: 2026-05-07T02:27:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-05: Introduced in House
- 2025-05-05 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-05 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-05 - IntroReferral: Submitted in House
- 2025-05-05 - IntroReferral: Submitted in House
- Latest action: 2025-05-05: Submitted in House

## Actions

- 2025-05-05 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-05 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-05 - IntroReferral: Submitted in House
- 2025-05-05 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-05",
    "latestAction": {
      "actionDate": "2025-05-05",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/381",
    "number": "381",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "N000189",
        "district": "4",
        "firstName": "Dan",
        "fullName": "Rep. Newhouse, Dan [R-WA-4]",
        "lastName": "Newhouse",
        "party": "R",
        "state": "WA"
      }
    ],
    "title": "Expressing support for the designation of May 5, 2025, as the \"National Day of Awareness for Missing and Murdered Indigenous Women and Girls\".",
    "type": "HRES",
    "updateDate": "2026-05-07T02:27:57Z",
    "updateDateIncludingText": "2026-05-07T02:27:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-05",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-05",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-05",
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
          "date": "2025-05-05T16:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-05T16:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NM"
    },
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "OK"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "CA"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "SD"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "HI"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "FL"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "AZ"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "OK"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "OR"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "NE"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "ME"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "WI"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "WA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "CA"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NJ"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres381ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 381\nIN THE HOUSE OF REPRESENTATIVES\nMay 5, 2025 Mr. Newhouse (for himself, Ms. Leger Fernandez , Mr. Cole , Mr. Huffman , Mr. Johnson of South Dakota , Mr. Case , Ms. Salazar , Mr. Stanton , Mrs. Bice , Ms. Bonamici , Mr. Smith of Nebraska , Ms. Pingree , Mr. Pocan , and Ms. Schrier ) submitted the following resolution; which was referred to the Committee on Natural Resources , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nExpressing support for the designation of May 5, 2025, as the National Day of Awareness for Missing and Murdered Indigenous Women and Girls .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of a National Day of Awareness for Missing and Murdered Indigenous Women and Girls ;\n**(2)**\ncalls on the people of the United States and interested groups to\u2014\n**(A)**\ncommemorate the lives of missing and murdered Indigenous women and girls whose cases are documented and undocumented in public records and the media; and\n**(B)**\ndemonstrate solidarity with the families of victims in light of those tragedies;\n**(3)**\nrecommends that the Department of Justice\u2019s National Institute of Justice commission a new study with focused data on missing and murdered Indigenous women and girls to ensure up-to-date statistics are made public regarding the current state of the missing and murdered Indigenous women and girls crisis given 9 years have passed since their 2016 study was published; and\n**(4)**\nrecognizes that, despite the positive efforts made, there is more work to be done to address this nationwide crisis.",
      "versionDate": "2025-05-05",
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
        "actionDate": "2026-05-04",
        "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1257",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for the designation of May 5, 2026, as the \"National Day of Awareness for Missing and Murdered Indigenous Women and Girls\".",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-05",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2753; text: CR S2758)"
      },
      "number": "200",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution expressing support for the designation of May 5, 2025, as the \"National Day of Awareness for Missing and Murdered Indigenous Women and Girls\".",
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
            "name": "Alaska Natives and Hawaiians",
            "updateDate": "2025-06-04T13:40:39Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-06-04T13:40:39Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-06-04T13:40:39Z"
          },
          {
            "name": "Crimes against women",
            "updateDate": "2025-06-04T13:40:39Z"
          },
          {
            "name": "Missing persons",
            "updateDate": "2025-06-04T13:40:39Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2025-06-04T13:40:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-06-03T18:22:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-05",
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
          "measure-id": "id119hres381",
          "measure-number": "381",
          "measure-type": "hres",
          "orig-publish-date": "2025-05-05",
          "originChamber": "HOUSE",
          "update-date": "2025-08-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres381v00",
            "update-date": "2025-08-04"
          },
          "action-date": "2025-05-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses support for the designation of a National Day of Awareness for Missing and Murdered Indigenous Women and Girls.</p>"
        },
        "title": "Expressing support for the designation of May 5, 2025, as the \"National Day of Awareness for Missing and Murdered Indigenous Women and Girls\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres381.xml",
    "summary": {
      "actionDate": "2025-05-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of a National Day of Awareness for Missing and Murdered Indigenous Women and Girls.</p>",
      "updateDate": "2025-08-04",
      "versionCode": "id119hres381"
    },
    "title": "Expressing support for the designation of May 5, 2025, as the \"National Day of Awareness for Missing and Murdered Indigenous Women and Girls\"."
  },
  "summaries": [
    {
      "actionDate": "2025-05-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of a National Day of Awareness for Missing and Murdered Indigenous Women and Girls.</p>",
      "updateDate": "2025-08-04",
      "versionCode": "id119hres381"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres381ih.xml"
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
      "title": "Expressing support for the designation of May 5, 2025, as the \"National Day of Awareness for Missing and Murdered Indigenous Women and Girls\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-06T10:18:20Z"
    },
    {
      "title": "Expressing support for the designation of May 5, 2025, as the \"National Day of Awareness for Missing and Murdered Indigenous Women and Girls\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-06T08:05:28Z"
    }
  ]
}
```
