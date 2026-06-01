# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3403?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3403
- Title: SEAT Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3403
- Origin chamber: House
- Introduced date: 2025-05-14
- Update date: 2025-11-08T09:05:53Z
- Update date including text: 2025-11-08T09:05:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-05-14: Introduced in House

## Actions

- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3403",
    "number": "3403",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "SEAT Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-08T09:05:53Z",
    "updateDateIncludingText": "2025-11-08T09:05:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T14:05:20Z",
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
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "LA"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3403ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3403\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Ms. Mace introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit third-party restaurant reservation services from offering or arranging unauthorized reservations for food service establishments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Equal Access to Tables Act of 2025 or the SEAT Act of 2025 .\n#### 2. Limitation on third-party restaurant reservation services\n##### (a) Requirement\nA provider of a third-party restaurant reservation service may only list, promote, sell, or otherwise advertise or make available a reservation for a food service establishment if there is a written agreement between such service and such establishment, or a contractual designee of such establishment who obtained reservation distribution rights directly from the establishment, that permits such service to list, promote, sell, or otherwise advertise or make available such reservation.\n##### (b) Enforcement by commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this section shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of commission**\nThe Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section. Any person who violates this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n##### (c) Applicability\nThis section shall apply to a provider of a third-party restaurant reservation service beginning on the date that is 180 days after the date of the enactment of this Act.\n##### (d) Indemnification provisions\nAn agreement entered into pursuant to subsection (a) may not include a provision that requires a food service establishment to indemnify a third-party restaurant reservation service, any independent contractor acting on behalf of such third-party restaurant reservation service, or any registered agent of such third-party restaurant reservation service for any damages or harm by an act or omission initiated by the third-party restaurant reservation service. If an agreement entered into pursuant to subsection (a) contains such a provision, such provision shall be deemed void and unenforceable.\n##### (e) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Food service establishment**\nThe term food service establishment \u2014\n**(A)**\nmeans a restaurant, food stand, food truck, food cart, saloon, inn, tavern, bar, lounge, brewpub, tasting room, taproom, licensed facility or premise of a beverage alcohol producer where the public may taste, sample, or purchase products, or other similar place of business in or at which the public or patrons assemble for the primary purpose of being served food or drink; and\n**(B)**\nincludes an entity described in subparagraph (A) that is located in a larger establishment or complex, including an airport terminal or other transportation facility, amusement park, sports stadium, entertainment venue, hotel or hotel complex, or retail store or retail complex.\n**(3) Third-party restaurant reservation service**\nThe term third-party restaurant reservation service means any website, mobile application, or other internet-based service that\u2014\n**(A)**\nlists, promotes, sells, or otherwise advertises or makes available reservations for on-premises service for a customer at a food service establishment; and\n**(B)**\nis provided by a person other than the person who provides such food service establishment.",
      "versionDate": "2025-05-14",
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
        "name": "Commerce",
        "updateDate": "2025-05-28T12:33:56Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3403ih.xml"
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
      "title": "SEAT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-22T02:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SEAT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-22T02:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Equal Access to Tables Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-22T02:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit third-party restaurant reservation services from offering or arranging unauthorized reservations for food service establishments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-22T02:18:35Z"
    }
  ]
}
```
