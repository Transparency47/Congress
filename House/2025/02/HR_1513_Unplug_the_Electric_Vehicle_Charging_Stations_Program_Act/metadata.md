# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1513?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1513
- Title: Unplug the Electric Vehicle Charging Stations Program Act
- Congress: 119
- Bill type: HR
- Bill number: 1513
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2026-03-19T10:49:16Z
- Update date including text: 2026-03-19T10:49:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-21 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-21 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-21 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-21 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1513",
    "number": "1513",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "W000829",
        "district": "8",
        "firstName": "Tony",
        "fullName": "Rep. Wied, Tony [R-WI-8]",
        "lastName": "Wied",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Unplug the Electric Vehicle Charging Stations Program Act",
    "type": "HR",
    "updateDate": "2026-03-19T10:49:16Z",
    "updateDateIncludingText": "2026-03-19T10:49:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-21",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:34:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-21T22:26:24Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-21T20:34:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "TX"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "TX"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "WI"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "WI"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "TX"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "CO"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "GA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "NY"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "MN"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1513ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1513\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Wied (for himself, Mr. Weber of Texas , Mr. Sessions , Mr. Tiffany , Mr. Grothman , Mr. Williams of Texas , Mr. Crank , Mr. Collins , Ms. Tenney , Mr. Finstad , and Mr. Rutherford ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo repeal programs relating to funding for electric vehicle charging infrastructure, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Unplug the Electric Vehicle Charging Stations Program Act .\n#### 2. Repeal of charging and fueling infrastructure grants\n##### (a) Authorization of appropriations\nSection 11101(b) of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ; 135 Stat. 444) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking subparagraph (C); and\n**(B)**\nby redesignating subparagraphs (D) through (G) as subparagraphs (C) through (F), respectively; and\n**(2)**\nin paragraph (2)(B), by striking paragraph (1)(G) and inserting paragraph (1)(F) .\n##### (b) Grant program\nSection 151 of title 23, United States Code, is amended\u2014\n**(1)**\nin subsection (e)(2), by striking , including through funds awarded through the grant program under subsection (f), ; and\n**(2)**\nby striking subsection (f).\n#### 3. Repeal of National Electric Vehicle Infrastructure Formula Program\n##### (a) Rescission\nThe unobligated amounts made available under paragraph (2) in the matter under the heading highway infrastructure programs under the heading Federal Highway Administration under the heading Department of Transportation in title VIII of division J of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ; 135 Stat. 1419) are rescinded.\n##### (b) Termination\nNotwithstanding any other provision of law, beginning on the date of enactment of this Act\u2014\n**(1)**\nthe program under paragraph (2) in the matter under the heading highway infrastructure programs under the heading Federal Highway Administration under the heading Department of Transportation in title VIII of division J of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ; 135 Stat. 1419) is terminated; and\n**(2)**\nno funds may used to carry out that program.",
      "versionDate": "2025-02-21",
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
        "actionDate": "2025-02-20",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "651",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Unplug the Electric Vehicle Charging Stations Programs Act",
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
        "name": "Energy",
        "updateDate": "2025-03-18T12:54:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
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
          "measure-id": "id119hr1513",
          "measure-number": "1513",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2026-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1513v00",
            "update-date": "2026-03-19"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Unplug the Electric Vehicle Charging Stations Program Act</strong></p><p>This bill repeals grant programs that provide funding for electric vehicle charging infrastructure and alternative fueling infrastructure.</p><p>Specifically, the bill repeals the\u00a0Charging and Fueling Infrastructure Grant Program under which the Department of Transportation provides grants for acquiring and installing publicly accessible electric vehicle charging infrastructure, hydrogen fueling infrastructure, propane fueling infrastructure, or natural gas fueling infrastructure that is directly related to the charging or fueling of a vehicle.</p><p>It also repeals the National Electric Vehicle Infrastructure Formula Program under which the Federal Highway Administration (FHWA) provides grants for deploying electric vehicle charging infrastructure and establishing a network to facilitate data collection, access, and reliability. In addition, the bill rescinds unobligated funds\u00a0that were provided to the FHWA for the program and prohibits funds from being used to carry out the program.\u00a0</p>"
        },
        "title": "Unplug the Electric Vehicle Charging Stations Program Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1513.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Unplug the Electric Vehicle Charging Stations Program Act</strong></p><p>This bill repeals grant programs that provide funding for electric vehicle charging infrastructure and alternative fueling infrastructure.</p><p>Specifically, the bill repeals the\u00a0Charging and Fueling Infrastructure Grant Program under which the Department of Transportation provides grants for acquiring and installing publicly accessible electric vehicle charging infrastructure, hydrogen fueling infrastructure, propane fueling infrastructure, or natural gas fueling infrastructure that is directly related to the charging or fueling of a vehicle.</p><p>It also repeals the National Electric Vehicle Infrastructure Formula Program under which the Federal Highway Administration (FHWA) provides grants for deploying electric vehicle charging infrastructure and establishing a network to facilitate data collection, access, and reliability. In addition, the bill rescinds unobligated funds\u00a0that were provided to the FHWA for the program and prohibits funds from being used to carry out the program.\u00a0</p>",
      "updateDate": "2026-03-19",
      "versionCode": "id119hr1513"
    },
    "title": "Unplug the Electric Vehicle Charging Stations Program Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Unplug the Electric Vehicle Charging Stations Program Act</strong></p><p>This bill repeals grant programs that provide funding for electric vehicle charging infrastructure and alternative fueling infrastructure.</p><p>Specifically, the bill repeals the\u00a0Charging and Fueling Infrastructure Grant Program under which the Department of Transportation provides grants for acquiring and installing publicly accessible electric vehicle charging infrastructure, hydrogen fueling infrastructure, propane fueling infrastructure, or natural gas fueling infrastructure that is directly related to the charging or fueling of a vehicle.</p><p>It also repeals the National Electric Vehicle Infrastructure Formula Program under which the Federal Highway Administration (FHWA) provides grants for deploying electric vehicle charging infrastructure and establishing a network to facilitate data collection, access, and reliability. In addition, the bill rescinds unobligated funds\u00a0that were provided to the FHWA for the program and prohibits funds from being used to carry out the program.\u00a0</p>",
      "updateDate": "2026-03-19",
      "versionCode": "id119hr1513"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1513ih.xml"
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
      "title": "Unplug the Electric Vehicle Charging Stations Program Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Unplug the Electric Vehicle Charging Stations Program Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal programs relating to funding for electric vehicle charging infrastructure, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:22Z"
    }
  ]
}
```
