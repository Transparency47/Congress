# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/288?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/288
- Title: Long Island Sound Restoration and Stewardship Reauthorization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 288
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-12-05T21:57:43Z
- Update date including text: 2025-12-05T21:57:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-09 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-10 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-09 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-10 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/288",
    "number": "288",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "L000598",
        "district": "1",
        "firstName": "Nick",
        "fullName": "Rep. LaLota, Nick [R-NY-1]",
        "lastName": "LaLota",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Long Island Sound Restoration and Stewardship Reauthorization Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:57:43Z",
    "updateDateIncludingText": "2025-12-05T21:57:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-10",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-01-09T14:34:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-10T15:29:30Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-09T14:34:05Z",
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
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CT"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "CT"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "RI"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NY"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "NY"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NY"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr288ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 288\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. LaLota (for himself and Mr. Courtney ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo reauthorize Long Island Sound programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Long Island Sound Restoration and Stewardship Reauthorization Act of 2025 .\n#### 2. Reauthorization of Long Island Sound programs\n##### (a) Long island sound grants\nSection 119(h) of the Federal Water Pollution Control Act ( 33 U.S.C. 1269(h) ) is amended by striking 2019 through 2023 and inserting 2025 through 2029 .\n##### (b) Long island sound stewardship grants\nSection 11(a) of the Long Island Sound Stewardship Act of 2006 ( 33 U.S.C. 1269 note; Public Law 109\u2013359 ) is amended, in the matter preceding paragraph (1), by striking 2019 through 2023 and inserting 2025 through 2029 .\n##### (c) Technical amendment\nSection 119(g) of the Federal Water Pollution Control Act ( 33 U.S.C. 1269(g) ) is amended by redesignating paragraph (4) as paragraph (3).",
      "versionDate": "2025-01-09",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-02-27",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "781",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Long Island Sound Restoration and Stewardship Reauthorization Act of 2025",
      "type": "S"
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
        "name": "Environmental Protection",
        "updateDate": "2025-02-08T13:34:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr288",
          "measure-number": "288",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr288v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Long Island Sound Restoration and Stewardship Reauthorization Act of 2025</strong></p><p>This bill reauthorizes the Environmental Protection Agency's Long Island Sound programs through FY2029. The programs, which include\u00a0a stewardship grant program, focus on conserving and restoring the estuary off the coast of New York and Connecticut.</p>"
        },
        "title": "Long Island Sound Restoration and Stewardship Reauthorization Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr288.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Long Island Sound Restoration and Stewardship Reauthorization Act of 2025</strong></p><p>This bill reauthorizes the Environmental Protection Agency's Long Island Sound programs through FY2029. The programs, which include\u00a0a stewardship grant program, focus on conserving and restoring the estuary off the coast of New York and Connecticut.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr288"
    },
    "title": "Long Island Sound Restoration and Stewardship Reauthorization Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Long Island Sound Restoration and Stewardship Reauthorization Act of 2025</strong></p><p>This bill reauthorizes the Environmental Protection Agency's Long Island Sound programs through FY2029. The programs, which include\u00a0a stewardship grant program, focus on conserving and restoring the estuary off the coast of New York and Connecticut.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr288"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr288ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Long Island Sound Restoration and Stewardship Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Long Island Sound Restoration and Stewardship Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T03:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize Long Island Sound programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T03:03:27Z"
    }
  ]
}
```
