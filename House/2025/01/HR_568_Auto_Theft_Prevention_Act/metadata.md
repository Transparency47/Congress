# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/568?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/568
- Title: Auto Theft Prevention Act
- Congress: 119
- Bill type: HR
- Bill number: 568
- Origin chamber: House
- Introduced date: 2025-01-20
- Update date: 2026-04-09T15:42:24Z
- Update date including text: 2026-04-09T15:42:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-20: Introduced in House
- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-20: Introduced in House

## Actions

- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-20",
    "latestAction": {
      "actionDate": "2025-01-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/568",
    "number": "568",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001207",
        "district": "11",
        "firstName": "Mikie",
        "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
        "lastName": "Sherrill",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Auto Theft Prevention Act",
    "type": "HR",
    "updateDate": "2026-04-09T15:42:24Z",
    "updateDateIncludingText": "2026-04-09T15:42:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-20",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-20",
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
          "date": "2025-01-20T15:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-01-20",
      "state": "NE"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr568ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 568\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 20, 2025 Ms. Sherrill (for herself and Mr. Bacon ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide funding to State and local law enforcement agencies to combat auto theft and stolen automobile trafficking, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Auto Theft Prevention Act .\n#### 2. Auto theft prevention grant program\n##### (a) Establishment\nNot later than 60 days after the date of the enactment of this Act, the Director of the Office of Community Oriented Policing Services of the Department of Justice shall establish an auto theft prevention grant program (in this Act referred to as the Program ) to provide funding to State law enforcement agencies and local law enforcement agencies to combat auto theft and stolen vehicle trafficking.\n##### (b) Eligible recipient\nThe Director shall make grants under the Program to the Attorney General of each State, with the amount awarded proportional to the overall level of auto thefts within each State in the year prior to the date of the disbursement of the grant.\n##### (c) Distribution of funds\n**(1) Local law enforcement agencies**\nThe Attorney General of a State shall make at least 50 percent of a grant awarded under the Program available as competitive subgrants to local law enforcement agencies to combat auto theft, with the amount awarded determined by prioritizing localities with a higher overall level of auto thefts in the year prior to the date of the disbursement of the grant.\n**(2) State law enforcement agencies**\nThe Attorney General of a State shall make at least 25 percent of a grant awarded under the Program available to State law enforcement agencies to combat auto theft.\n**(3) Other amounts**\nThe Attorney General of a State shall make any proportion of the grant awarded under the Program not allocated under paragraph (1) or (2) available as competitive subgrants to local law enforcement agencies or to State law enforcement agencies. Any subgrant made under this paragraph to a local law enforcement agency shall follow the prioritization under paragraph (1).\n##### (d) Eligible activities\nAmounts from a grant awarded under the Program may only be used for the purpose of combating auto theft and combating stolen automobile trafficking, including\u2014\n**(1)**\npurchasing equipment used to combat auto theft, such as law enforcement vehicles and license plate readers, and funding costs associated with that equipment, such as subscription fees and data storage fees for license plate readers;\n**(2)**\nhiring additional law enforcement officers and support staff to combat auto theft;\n**(3)**\nfunding overtime costs and additional compensation for law enforcement officers and support staff involved in combating auto theft;\n**(4)**\nproviding training for law enforcement officers and support staff to combat auto theft;\n**(5)**\nproviding resources for joint task forces established to combat auto theft;\n**(6)**\nfunding law enforcement data collection, data storage, and research activities related to combating auto theft; and\n**(7)**\nfunding for the administrative costs of applying for and implementing the grant, up to a maximum of 5 percent of the grant amount.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated $30,000,000 for each of fiscal years 2026 through 2030 to carry out the Program.\n#### 3. Additional authorized uses of cops grant program funds\nSection 1701(b) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381(b) ) is amended\u2014\n**(1)**\nby redesignating paragraph (24) as paragraph (25);\n**(2)**\nin paragraph (23)\u2014\n**(A)**\nby striking (22) and inserting (23) ; and\n**(B)**\nby redesignating paragraph (23) as paragraph (24); and\n**(3)**\nby inserting after paragraph (22), the following:\n(23) to combat auto thefts and stolen automobile trafficking by purchasing equipment, hiring law enforcement officers and support staff, covering overtime and officer compensation costs, expanding access to training initiatives, funding joint task forces, and funding law enforcement data collection and research activities related to auto thefts; .\n#### 4. Definitions\nIn this Act:\n**(1) Local law enforcement agency**\nThe term local law enforcement agency means any entity administered by a locality that exists primarily to prevent and detect crime and enforce criminal laws.\n**(2) Locality**\nThe term locality means any city, county, township, town, borough, parish, village, or other general purpose political subdivision of a State.\n**(3) State**\nThe term State means any State of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands.\n**(4) State law enforcement agency**\nThe term State law enforcement agency means any State entity that exists primarily to prevent and detect crime and enforce criminal laws.",
      "versionDate": "2025-01-20",
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
            "name": "Crimes against property",
            "updateDate": "2025-03-03T17:36:40Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-09T15:42:24Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-03-03T17:36:40Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2025-03-03T17:36:40Z"
          },
          {
            "name": "Smuggling and trafficking",
            "updateDate": "2025-03-03T17:36:40Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-03T17:36:40Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-19T13:03:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-20",
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
          "measure-id": "id119hr568",
          "measure-number": "568",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-20",
          "originChamber": "HOUSE",
          "update-date": "2025-07-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr568v00",
            "update-date": "2025-07-21"
          },
          "action-date": "2025-01-20",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Auto Theft Prevention Act</strong></p><p>This bill establishes a grant program to combat auto theft and stolen automobile trafficking.</p><p>Specifically, the bill directs the Office of Community Oriented Policing Services\u00a0within the Department of Justice to award grants for state and local law enforcement agencies to combat auto theft and stolen vehicle trafficking. </p><p>The bill also allows funds under the Community Oriented Policing Services grant program to be used to combat auto thefts and stolen automobile trafficking.</p>"
        },
        "title": "Auto Theft Prevention Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr568.xml",
    "summary": {
      "actionDate": "2025-01-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Auto Theft Prevention Act</strong></p><p>This bill establishes a grant program to combat auto theft and stolen automobile trafficking.</p><p>Specifically, the bill directs the Office of Community Oriented Policing Services\u00a0within the Department of Justice to award grants for state and local law enforcement agencies to combat auto theft and stolen vehicle trafficking. </p><p>The bill also allows funds under the Community Oriented Policing Services grant program to be used to combat auto thefts and stolen automobile trafficking.</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119hr568"
    },
    "title": "Auto Theft Prevention Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Auto Theft Prevention Act</strong></p><p>This bill establishes a grant program to combat auto theft and stolen automobile trafficking.</p><p>Specifically, the bill directs the Office of Community Oriented Policing Services\u00a0within the Department of Justice to award grants for state and local law enforcement agencies to combat auto theft and stolen vehicle trafficking. </p><p>The bill also allows funds under the Community Oriented Policing Services grant program to be used to combat auto thefts and stolen automobile trafficking.</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119hr568"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr568ih.xml"
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
      "title": "Auto Theft Prevention Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-19T07:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Auto Theft Prevention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T07:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide funding to State and local law enforcement agencies to combat auto theft and stolen automobile trafficking, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T07:48:32Z"
    }
  ]
}
```
