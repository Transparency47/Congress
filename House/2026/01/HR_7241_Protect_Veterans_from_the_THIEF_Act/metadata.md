# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7241?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7241
- Title: Protect Veterans from the THIEF Act
- Congress: 119
- Bill type: HR
- Bill number: 7241
- Origin chamber: House
- Introduced date: 2026-01-27
- Update date: 2026-02-25T20:11:23Z
- Update date including text: 2026-02-25T20:11:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-02-12 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- Latest action: 2026-01-27: Introduced in House

## Actions

- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-02-12 - Committee: Referred to the Subcommittee on Oversight and Investigations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7241",
    "number": "7241",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001315",
        "district": "13",
        "firstName": "Nikki",
        "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
        "lastName": "Budzinski",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Protect Veterans from the THIEF Act",
    "type": "HR",
    "updateDate": "2026-02-25T20:11:23Z",
    "updateDateIncludingText": "2026-02-25T20:11:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight and Investigations.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-27",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T17:33:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-12T19:40:01Z",
              "name": "Referred to"
            }
          },
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7241ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7241\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Ms. Budzinski (for herself and Mr. Barrett ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to prohibit the Secretary of Veterans Affairs from entering into a contract pursuant to which the contractor may sell sensitive personal information maintained by the Secretary and to ensure the protection of personal information in certain contracts of the Department.\n#### 1. Short title\nThis Act may be cited as the Protect Veterans from the Theft of Health and Identifying Information in Electronic Forms Act or the Protect Veterans from the THIEF Act .\n#### 2. Prohibition of the sale of sensitive personal information maintained by the Secretary of Veterans Affairs\nSection 5725 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(d) Prohibition of sale of sensitive personal information The Secretary may not enter into a contract that permits the contractor to sell (or otherwise disclose for consideration) sensitive personal information to another entity. .\n#### 3. Protection of personal information in contracts of the Department of Veterans Affairs\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall\u2014\n**(1)**\nensure that each covered contract includes, or is modified to include, a clause prohibiting covered information from being monetized, sold, or otherwise misused by any contractor, including any subcontractor or affiliate thereof, or other non-Department of Veterans Affairs entity; and\n**(2)**\nissue a directive or other policy providing guidance to employees and contractors of the Department on how to identify the monetization, sale, or misuse of covered information in order to ensure contractors are in compliance with clauses in covered contracts included pursuant to paragraph (1).\n##### (b) Report\nNot later than one year after the date of the enactment of this Act, the Secretary shall submit to the appropriate congressional committees a report that includes\u2014\n**(1)**\na copy of the contract clause required by subsection (a)(1);\n**(2)**\nthe guidance required by subsection (a)(2); and\n**(3)**\na summary of any other actions taken to comply with subsection (a).\n##### (c) Definitions\nIn this section:\n**(1)**\nThe term appropriate congressional committees means the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate.\n**(2)**\nThe term covered contract means a contract of the Department of Veterans Affairs that provides for the handling of covered information and is entered into\u2014\n**(A)**\nafter the date of the enactment of this Act; or\n**(B)**\nbefore the date of the enactment of this Act and does not expire before the date of the enactment of this Act.\n**(3)**\nThe term covered information \u2014\n**(A)**\nmeans protected health information or personally identifiable information, including such information that has been anonymized; and\n**(B)**\nincludes information protected under\u2014\n**(i)**\nsection 552a of title 5, United States Code;\n**(ii)**\nsection 5701 or 7332 of title 38 United States Code;\n**(iii)**\nparts 160, 161, and 164 of title 45, Code of Federal Regulations; and\n**(iv)**\nany other provision of law, as determined by the Secretary.",
      "versionDate": "2026-01-27",
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
        "actionDate": "2026-01-30",
        "text": "Referred to the House Committee on Veterans' Affairs."
      },
      "number": "7280",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Veteran DATA Act",
      "type": "HR"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-02-09T19:19:43Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7241ih.xml"
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
      "title": "Protect Veterans from the THIEF Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Veterans from the THIEF Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Veterans from the Theft of Health and Identifying Information in Electronic Forms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to prohibit the Secretary of Veterans Affairs from entering into a contract pursuant to which the contractor may sell sensitive personal information maintained by the Secretary and to ensure the protection of personal information in certain contracts of the Department.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-06T03:18:31Z"
    }
  ]
}
```
