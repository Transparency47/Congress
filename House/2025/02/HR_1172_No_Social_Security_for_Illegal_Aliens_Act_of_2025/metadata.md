# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1172?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1172
- Title: No Social Security for Illegal Aliens Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1172
- Origin chamber: House
- Introduced date: 2025-02-10
- Update date: 2025-11-20T09:06:35Z
- Update date including text: 2025-11-20T09:06:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-10: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-10: Introduced in House

## Actions

- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1172",
    "number": "1172",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "M001194",
        "district": "2",
        "firstName": "John",
        "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
        "lastName": "Moolenaar",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "No Social Security for Illegal Aliens Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-20T09:06:35Z",
    "updateDateIncludingText": "2025-11-20T09:06:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-10",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-10",
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
          "date": "2025-02-10T17:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "OH"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "TN"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "SC"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NJ"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "AZ"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "False",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "NE"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "PA"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "TX"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "CA"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1172ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1172\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2025 Mr. Moolenaar (for himself, Mr. Webster of Florida , Mr. Weber of Texas , Mr. Haridopolos , Mr. Rulli , and Mrs. Harshbarger ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title II of the Social Security Act to exclude from creditable wages and self-employment income wages earned for services by aliens illegally performed in the United States and self-employment income derived from a trade or business illegally conducted in the United States.\n#### 1. Short title\nThis Act may be cited as the No Social Security for Illegal Aliens Act of 2025 .\n#### 2. Exclusion of unauthorized employment from employment upon which creditable wages may be based\nSection 210(a)(19) of the Social Security Act ( 42 U.S.C. 410(a)(19) ) is amended by striking (19) Service and inserting the following:\n(19) (A) Service performed by an alien while employed in the United States for any period during which the alien is not authorized to be so employed; (B) Service .\n#### 3. Exclusion of unauthorized functions and services from trade or business from which creditable self-employment income may be derived\nSection 211(c) of the Social Security Act ( 42 U.S.C. 411(c) ) is amended\u2014\n**(1)**\nin paragraph (5), by striking or at the end;\n**(2)**\nin paragraph (6), by striking him. and inserting him; or ; and\n**(3)**\nby inserting after paragraph (6) the following new paragraph:\n(7) The performance of a function or service in the United States by an alien during any period for which the alien is not authorized to perform such function or service in the United States. .\n#### 4. Effective date\nThe amendments made by this Act shall apply with respect to wages earned, and self-employment income derived, before, on, or after the date of the enactment of this Act. Notwithstanding section 215(f)(1) of the Social Security Act ( 42 U.S.C. 415(f)(1) ), as soon as practicable after the date of the enactment of this Act, the Commissioner of Social Security shall recompute all primary insurance amounts to the extent necessary to carry out such amendments. Such amendments shall affect benefits only for months after the date of the enactment of this Act.",
      "versionDate": "2025-02-10",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-04-24T16:21:42Z"
          },
          {
            "name": "Foreign labor",
            "updateDate": "2025-04-24T16:21:42Z"
          },
          {
            "name": "Social security and elderly assistance",
            "updateDate": "2025-04-24T16:21:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-03-17T14:33:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-10",
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
          "measure-id": "id119hr1172",
          "measure-number": "1172",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-10",
          "originChamber": "HOUSE",
          "update-date": "2025-04-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1172v00",
            "update-date": "2025-04-29"
          },
          "action-date": "2025-02-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Social Security for Illegal Aliens Act of 2025</strong></p><p>This bill excludes wages and self-employment income earned by non-U.S. nationals (<em>aliens</em> under federal law) who are not authorized to work in the United States\u00a0from consideration for purposes of Social Security eligibility and benefits.</p><p>This exclusion applies with respect to all such wages and self-employment income earned both before and after the bill\u2019s enactment. However, any change to the amount of an individual\u2019s Social Security benefits as a result of these provisions may only apply to benefits for months after the bill\u2019s enactment. \u00a0\u00a0</p>"
        },
        "title": "No Social Security for Illegal Aliens Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1172.xml",
    "summary": {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Social Security for Illegal Aliens Act of 2025</strong></p><p>This bill excludes wages and self-employment income earned by non-U.S. nationals (<em>aliens</em> under federal law) who are not authorized to work in the United States\u00a0from consideration for purposes of Social Security eligibility and benefits.</p><p>This exclusion applies with respect to all such wages and self-employment income earned both before and after the bill\u2019s enactment. However, any change to the amount of an individual\u2019s Social Security benefits as a result of these provisions may only apply to benefits for months after the bill\u2019s enactment. \u00a0\u00a0</p>",
      "updateDate": "2025-04-29",
      "versionCode": "id119hr1172"
    },
    "title": "No Social Security for Illegal Aliens Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Social Security for Illegal Aliens Act of 2025</strong></p><p>This bill excludes wages and self-employment income earned by non-U.S. nationals (<em>aliens</em> under federal law) who are not authorized to work in the United States\u00a0from consideration for purposes of Social Security eligibility and benefits.</p><p>This exclusion applies with respect to all such wages and self-employment income earned both before and after the bill\u2019s enactment. However, any change to the amount of an individual\u2019s Social Security benefits as a result of these provisions may only apply to benefits for months after the bill\u2019s enactment. \u00a0\u00a0</p>",
      "updateDate": "2025-04-29",
      "versionCode": "id119hr1172"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1172ih.xml"
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
      "title": "No Social Security for Illegal Aliens Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Social Security for Illegal Aliens Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T06:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title II of the Social Security Act to exclude from creditable wages and self-employment income wages earned for services by aliens illegally performed in the United States and self-employment income derived from a trade or business illegally conducted in the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T06:33:46Z"
    }
  ]
}
```
