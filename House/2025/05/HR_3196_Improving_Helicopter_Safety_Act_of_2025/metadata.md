# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3196?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3196
- Title: Improving Helicopter Safety Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3196
- Origin chamber: House
- Introduced date: 2025-05-05
- Update date: 2026-04-24T16:01:14Z
- Update date including text: 2026-04-24T16:01:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-05: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-05 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-05-05: Introduced in House

## Actions

- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-05 - Committee: Referred to the Subcommittee on Aviation.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3196",
    "number": "3196",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "N000002",
        "district": "12",
        "firstName": "Jerrold",
        "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
        "lastName": "Nadler",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Improving Helicopter Safety Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-24T16:01:14Z",
    "updateDateIncludingText": "2026-04-24T16:01:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-05",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-05",
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
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-05",
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
          "date": "2025-05-05T16:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-05T20:50:01Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NJ"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "NY"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NY"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NY"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NJ"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "NY"
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
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3196ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3196\nIN THE HOUSE OF REPRESENTATIVES\nMay 5, 2025 Mr. Nadler (for himself, Mr. Menendez , Ms. Malliotakis , Ms. Meng , Ms. Vel\u00e1zquez , and Mrs. McIver ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to prohibit helicopter flights near Statue of Liberty National Monument, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving Helicopter Safety Act of 2025 .\n#### 2. Prohibition on helicopter flights near Statue of Liberty National Monument\n##### (a) In general\nChapter 447 of title 49, United States Code, is amended by adding at the end the following:\n44749. Prohibition on helicopter flights near Statue of Liberty National Monument (a) In general Not later than 60 days after the date of enactment of this section, no person may operate a civil helicopter in covered airspace except as provided for under subsection (b). (b) Exceptions (1) Public health and safety The prohibition in subsection (a) shall not apply to a flight carried out for purposes of public health and safety, including\u2014 (A) law enforcement; (B) emergency response; (C) disaster response; (D) the provision of medical services; and (E) providing other services for the benefit of the general public, including flights carried out for research or for official purposes by a news organization. (2) Infrastructure maintenance The prohibition in subsection (a) shall not apply to a flight carried out for purposes heavy-lift operations in support of construction and infrastructure maintenance. (c) Covered airspace defined In this section, the term covered airspace means the airspace within a 20-mile radius of the Statue of Liberty National Monument. .\n##### (b) Conforming amendment\nThe table of sections for chapter 447 of title 49, United States Code, is amended by adding at the end the following:\n44749. Prohibition on helicopter flights near Statue of Liberty National Monument. .\n#### 3. Helicopter flight routes near Statue of Liberty National Monument\nNot later than 90 days after the date of enactment of this Act, the Administrator of the Federal Aviation Administration shall issue or update such regulations as are necessary to carry out the requirements of section 2.",
      "versionDate": "2025-05-05",
      "versionType": "Introduced in House"
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-22T16:10:07Z"
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
          "measure-id": "id119hr3196",
          "measure-number": "3196",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-05",
          "originChamber": "HOUSE",
          "update-date": "2026-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3196v00",
            "update-date": "2026-04-24"
          },
          "action-date": "2025-05-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Improving Helicopter Safety Act of 2025</strong></p><p>This bill generally prohibits the operation of a civil helicopter within a 20-mile radius of the Statue of Liberty National Monument in New York, New York.</p><p>The bill includes an exception for flights carried out for the purposes of (1) public health and safety (e.g., for law enforcement or the\u00a0provision of medical services), or (2) heavy-lift operations in support of construction and infrastructure maintenance.</p><p>The Federal Aviation Administration must issue or update regulations to carry out the requirements of this bill.</p>"
        },
        "title": "Improving Helicopter Safety Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3196.xml",
    "summary": {
      "actionDate": "2025-05-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improving Helicopter Safety Act of 2025</strong></p><p>This bill generally prohibits the operation of a civil helicopter within a 20-mile radius of the Statue of Liberty National Monument in New York, New York.</p><p>The bill includes an exception for flights carried out for the purposes of (1) public health and safety (e.g., for law enforcement or the\u00a0provision of medical services), or (2) heavy-lift operations in support of construction and infrastructure maintenance.</p><p>The Federal Aviation Administration must issue or update regulations to carry out the requirements of this bill.</p>",
      "updateDate": "2026-04-24",
      "versionCode": "id119hr3196"
    },
    "title": "Improving Helicopter Safety Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improving Helicopter Safety Act of 2025</strong></p><p>This bill generally prohibits the operation of a civil helicopter within a 20-mile radius of the Statue of Liberty National Monument in New York, New York.</p><p>The bill includes an exception for flights carried out for the purposes of (1) public health and safety (e.g., for law enforcement or the\u00a0provision of medical services), or (2) heavy-lift operations in support of construction and infrastructure maintenance.</p><p>The Federal Aviation Administration must issue or update regulations to carry out the requirements of this bill.</p>",
      "updateDate": "2026-04-24",
      "versionCode": "id119hr3196"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3196ih.xml"
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
      "title": "Improving Helicopter Safety Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improving Helicopter Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to prohibit helicopter flights near Statue of Liberty National Monument, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:48:41Z"
    }
  ]
}
```
