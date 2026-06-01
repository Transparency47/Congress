# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6168?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6168
- Title: Airport TIFIA Financing Certainty Act
- Congress: 119
- Bill type: HR
- Bill number: 6168
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-04-17T08:06:59Z
- Update date including text: 2026-04-17T08:06:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-21 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-21 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6168",
    "number": "6168",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "H001100",
        "district": "3",
        "firstName": "Jeff",
        "fullName": "Rep. Hurd, Jeff [R-CO-3]",
        "lastName": "Hurd",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Airport TIFIA Financing Certainty Act",
    "type": "HR",
    "updateDate": "2026-04-17T08:06:59Z",
    "updateDateIncludingText": "2026-04-17T08:06:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-21",
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
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:10:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-21T18:24:43Z",
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
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "MP"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6168ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6168\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Hurd of Colorado (for himself and Mr. Garamendi ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo redefine the eligibility for airport-related TIFIA projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Airport TIFIA Financing Certainty Act .\n#### 2. Infrastructure finance\n##### (a) Eligible projects\nSection 601(a)(12)(G) of title 23, United States Code, is amended to read as follows:\n(G) any project that constructs new or improves existing aviation-related facilities, including equipment, regardless of revenue producing purposes or public accessibility, that facilitates, preserves, enhances, or expands\u2014 (i) air transportation; (ii) access to air transportation, including surface transportation, rental car, and parking facilities; (iii) the movement of passengers, baggage, or cargo; or (iv) the safety or security of airport users; and .\n##### (b) Determination of eligibility and project selection\nSection 602(a) of title 23, United States Code, is amended\u2014\n**(1)**\nin paragraph (3) by striking A project and inserting Except for a project described in section 601(a)(12)(G), a project ; and\n**(2)**\nin paragraph (5)(B)(iii) by striking eligible project costs and inserting a Federal credit instrument .\n##### (c) Applicability of waiver conditions\nSection 603(b)(6) of title 23, United States Code, is amended by adding at the end the following:\n(C) Applicability The conditions described in subparagraph (B)(i)(III) and subparagraph (6)(B)(ii)(I) shall not be required for a project described in section 601(a)(12)(G) to receive a waiver under this paragraph. .\n##### (d) Program administration\nSection 605(f)(1) of title 23, United States Code, is amended by striking eligible project costs that are reasonably anticipated not to equal or exceed $75,000,000 and inserting a TIFIA loan amount that is reasonably anticipated not to equal or exceed $100,000,000 .",
      "versionDate": "2025-11-20",
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
        "updateDate": "2025-12-05T14:20:33Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6168ih.xml"
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
      "title": "Airport TIFIA Financing Certainty Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T07:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Airport TIFIA Financing Certainty Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To redefine the eligibility for airport-related TIFIA projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T07:48:27Z"
    }
  ]
}
```
