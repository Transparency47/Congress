# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8049?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8049
- Title: End Special Treatment for Congress at Airports Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8049
- Origin chamber: House
- Introduced date: 2026-03-24
- Update date: 2026-05-16T08:07:47Z
- Update date including text: 2026-05-16T08:07:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-24: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-03-25 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.
- Latest action: 2026-03-24: Introduced in House

## Actions

- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-03-25 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-24",
    "latestAction": {
      "actionDate": "2026-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8049",
    "number": "8049",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "H001091",
        "district": "2",
        "firstName": "Ashley",
        "fullName": "Rep. Hinson, Ashley [R-IA-2]",
        "lastName": "Hinson",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "End Special Treatment for Congress at Airports Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:47Z",
    "updateDateIncludingText": "2026-05-16T08:07:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Transportation and Maritime Security.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-24",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-24",
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
          "date": "2026-03-24T16:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-25T19:50:55Z",
              "name": "Referred to"
            }
          },
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "TN"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8049ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8049\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2026 Mrs. Hinson (for herself and Mrs. Harshbarger ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo prohibit preferential screening for Members of Congress at airports, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End Special Treatment for Congress at Airports Act of 2026 .\n#### 2. Definitions\nIn this Act\u2014\n**(1) Administrator**\nThe term Administrator means the Administrator of the Transportation Security Administration.\n**(2) Member of Congress**\nThe term Member of Congress has the meaning given that term in section 13101 of title 5, United States Code.\n**(3) Screening location**\nThe term screening location has the meaning given that term in section 1540.5 of title 49, Code of Federal Regulations.\n**(4) Trusted Traveler Program**\nThe term Trusted Traveler Program means any of the following:\n**(A)**\nGlobal Entry.\n**(B)**\nThe PreCheck Program.\n**(C)**\nSENTRI.\n**(D)**\nNEXUS.\n**(E)**\nAny other United States Government program that issues a unique identifier, such as a known traveler number, that the Transportation Security Administration accepts as validating that the individual holding such identifier is a member of a known low-risk population.\n**(F)**\nAny other program implemented by the Transportation Security Administration under section 109(a)(3) of the Aviation and Transportation Security Act ( 49 U.S.C. 114 note; Public Law 107\u201371 ).\n#### 3. Requirement for standard security screening\n##### (a) In general\nNone of the funds appropriated or otherwise made available to the Transportation Security Administration shall be used to provide or facilitate the provision of a Member of Congress with expedited or preferential access to or through security screenings required pursuant to section 44901 of title 49, United States Code.\n##### (b) No expedited access\nA Member of Congress shall not\u2014\n**(1)**\nbe exempt from Federal passenger and baggage screening procedures of the Transportation Security Administration; or\n**(2)**\nreceive priority or expedited access to a screening location on the basis of the official position of such Member of Congress.\n#### 4. Rule of construction\nNothing in this Act shall be construed\u2014\n**(1)**\nto limit the authority of the Transportation Security Administration to implement risk-based security programs available to the general public; or\n**(2)**\nto prohibit Members of Congress from participating in a publicly available Trusted Traveler Program, provided such participation is not based on the official positions of such Members of Congress.\n#### 5. Enforcement\n##### (a) Policy Implementation\nThe Administrator shall update policies and procedures as necessary to ensure compliance with this Act.\n##### (b) Report\nNot later than 180 days after the date of the enactment of this Act, the Administrator shall submit to Congress a report on the implementation of, and compliance with, this Act.",
      "versionDate": "2026-03-24",
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
        "actionDate": "2026-03-24",
        "actionTime": "14:11:54",
        "text": "Held at the desk."
      },
      "number": "4123",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "End Special Treatment for Congress at Airports Act of 2026",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-04-09T20:02:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-24",
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
          "measure-id": "id119hr8049",
          "measure-number": "8049",
          "measure-type": "hr",
          "orig-publish-date": "2026-03-24",
          "originChamber": "HOUSE",
          "update-date": "2026-04-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr8049v00",
            "update-date": "2026-04-21"
          },
          "action-date": "2026-03-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>End Special Treatment for Congress at Airports Act of 2026</strong></p><p>This bill prohibits the Transportation Security Administration (TSA) from providing a Member of Congress with expedited or preferential access to or through airport security screenings.</p><p>Specifically, TSA funds may not be used to\u00a0</p><ul><li>exempt a Member of Congress from\u00a0TSA passenger and baggage screening, or</li><li>provide a Member of Congress with priority or expedited access to a screening location based on their position.</li></ul><p>TSA must update its policies and procedures to ensure compliance with this\u00a0bill.</p>"
        },
        "title": "End Special Treatment for Congress at Airports Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr8049.xml",
    "summary": {
      "actionDate": "2026-03-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>End Special Treatment for Congress at Airports Act of 2026</strong></p><p>This bill prohibits the Transportation Security Administration (TSA) from providing a Member of Congress with expedited or preferential access to or through airport security screenings.</p><p>Specifically, TSA funds may not be used to\u00a0</p><ul><li>exempt a Member of Congress from\u00a0TSA passenger and baggage screening, or</li><li>provide a Member of Congress with priority or expedited access to a screening location based on their position.</li></ul><p>TSA must update its policies and procedures to ensure compliance with this\u00a0bill.</p>",
      "updateDate": "2026-04-21",
      "versionCode": "id119hr8049"
    },
    "title": "End Special Treatment for Congress at Airports Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-03-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>End Special Treatment for Congress at Airports Act of 2026</strong></p><p>This bill prohibits the Transportation Security Administration (TSA) from providing a Member of Congress with expedited or preferential access to or through airport security screenings.</p><p>Specifically, TSA funds may not be used to\u00a0</p><ul><li>exempt a Member of Congress from\u00a0TSA passenger and baggage screening, or</li><li>provide a Member of Congress with priority or expedited access to a screening location based on their position.</li></ul><p>TSA must update its policies and procedures to ensure compliance with this\u00a0bill.</p>",
      "updateDate": "2026-04-21",
      "versionCode": "id119hr8049"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8049ih.xml"
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
      "title": "End Special Treatment for Congress at Airports Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-07T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "End Special Treatment for Congress at Airports Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-07T05:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit preferential screening for Members of Congress at airports, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-07T05:48:29Z"
    }
  ]
}
```
