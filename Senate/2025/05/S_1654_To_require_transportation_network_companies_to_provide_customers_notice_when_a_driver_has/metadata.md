# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1654?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1654
- Title: Safe and Private Rides Act
- Congress: 119
- Bill type: S
- Bill number: 1654
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2025-05-27T12:57:58Z
- Update date including text: 2025-05-27T12:57:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1654",
    "number": "1654",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Safe and Private Rides Act",
    "type": "S",
    "updateDate": "2025-05-27T12:57:58Z",
    "updateDateIncludingText": "2025-05-27T12:57:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-05-07T21:02:19Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1654is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1654\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mrs. Blackburn (for herself and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require transportation network companies to provide customers notice when a driver has a camera in their motor vehicle and provide customers an opportunity to opt out of riding in motor vehicles with cameras, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe and Private Rides Act .\n#### 2. Requirements for transportation network companies pertaining to cameras in motor vehicles\n##### (a) Registering requirement, notice and opportunity To opt out of riding in cars with cameras, and restriction on use of passenger recording\nA transportation network company shall\u2014\n**(1)**\nfor the purpose of enabling the notification described in paragraph (2), require each driver affiliated with the transportation network company to register with such company any camera in the motor vehicle of the driver that records video images of passengers;\n**(2)**\nnotify each passenger of each camera registered with the transportation network company;\n**(3)**\ndevelop and implement a process to address any violation of the requirement under paragraph (1);\n**(4)**\nprovide any customer of the transportation network company with\u2014\n**(A)**\na clear and prominent notice on the application of the transportation network company when a driver affiliated with such company uses a motor vehicle that has a camera in the motor vehicle that records video images of passengers; and\n**(B)**\nsubject to the standards described in subsection (b), an opportunity on such application to opt out of riding in any motor vehicle that has a camera in the motor vehicle that records video images of passengers;\n**(5)**\nnot retain or transfer a recording of a passenger except as necessary to report criminal activity, for insurance purposes, or to determine compliance with the terms of service of a transportation network company; and\n**(6)**\nestablish a mechanism by which a passenger of the transportation network company may report instances of being\u2014\n**(A)**\nrecorded without being notified; or\n**(B)**\nconnected with a driver with a camera in the motor vehicle that records video images of passengers after such passenger opted out pursuant to paragraph (4)(B).\n##### (b) Standards for the opportunity To opt out\nFor purposes of the opportunity to opt out described in subsection (a)(2)(B), a transportation network company shall\u2014\n**(1)**\nallow any customer to revoke consent to ride in a motor vehicle that has a camera in such vehicle through an accessible and easily navigable mechanism;\n**(2)**\nprovide an option to opt out that is clearly displayed in the application settings or another easily accessible location in that application;\n**(3)**\nprovide to a customer an opportunity to opt out of riding in a motor vehicle that has a camera in such vehicle that is independent from the customer agreeing to the terms of service of the transportation network company; and\n**(4)**\nonly infer a customer's decision to opt out based on the customer taking a direct action that a reasonable person would constitute as an affirmative revocation of consent.\n##### (c) Limitation of liability\nNo transportation network company that has complied with subsections (a) and (b) shall be liable for the actions of a driver affiliated with such company who otherwise violates such subsections.\n##### (d) Enforcement by the Commission\n**(1) Unfair or deceptive act or practices**\nA violation of this Act shall be treated as an unfair or deceptive act or practice in violation of a rule promulgated under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section.\n**(B) Privileges and immunities**\nAny transportation network company that violates this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n##### (e) Effective date\nThe requirements established in this Act shall take effect on the date that is 180 days after the enactment of this Act.\n##### (f) Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Motor vehicle**\nThe term motor vehicle means any vehicle which is manufactured primarily for use on public streets, roads, and highways (not including a vehicle operated exclusively on a rail or rails) and which has at least 4 wheels.\n**(3) Transportation network company**\n**(A) In general**\nThe term transportation network company means any entity that uses a digital network to connect a customer to a driver affiliated with the company in order for the driver to provide transportation services using a motor vehicle to the customer.\n**(B) Exclusions**\nThe term transportation network company does not include\u2014\n**(i)**\na shared-expense carpool or vanpool arrangement that is not intended to generate a profit for the driver; or\n**(ii)**\nmicrotransit or other dedicated transportation services provided exclusively on behalf of a government entity, a nonprofit organization, or a third-party commercial enterprise.",
      "versionDate": "2025-05-07",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-05-27T12:57:58Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1654is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Safe and Private Rides Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safe and Private Rides Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require transportation network companies to provide customers notice when a driver has a camera in their motor vehicle and provide customers an opportunity to opt out of riding in motor vehicles with cameras, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:18:21Z"
    }
  ]
}
```
