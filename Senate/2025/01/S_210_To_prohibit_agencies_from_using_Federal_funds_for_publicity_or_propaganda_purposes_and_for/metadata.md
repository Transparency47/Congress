# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/210?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/210
- Title: SWAG Act
- Congress: 119
- Bill type: S
- Bill number: 210
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2025-12-05T22:02:50Z
- Update date including text: 2025-12-05T22:02:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/210",
    "number": "210",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "SWAG Act",
    "type": "S",
    "updateDate": "2025-12-05T22:02:50Z",
    "updateDateIncludingText": "2025-12-05T22:02:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T18:16:57Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "OK"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MT"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s210is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 210\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Ms. Ernst (for herself, Mr. Lankford , and Mr. Daines ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit agencies from using Federal funds for publicity or propaganda purposes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Wasteful Advertising by the Government Act or the SWAG Act .\n#### 2. Definitions\nIn this Act\u2014\n**(1)**\nthe term advertising means the placement of messages in media that are intended to inform or persuade an audience, including placement in television, radio, a magazine, a newspaper, digital media, direct mail, a tangible product, an exhibit, or a billboard;\n**(2)**\nthe term agency has the meaning given the term in section 551 of title 5, United States Code;\n**(3)**\nthe term mascot means an individual, animal, or object adopted by an agency as a symbolic figure to represent the agency, the mission of the agency, or a program within the agency, including a costumed character;\n**(4)**\nthe term public relations means communications by an agency that are directed to the public, including activities dedicated to maintaining the image of the governmental unit or maintaining or promoting understanding and favorable relations with the community or the public;\n**(5)**\nthe term return on investment means, with respect to the public relations and advertising spending by an agency, a positive return in achieving agency or program goals relative to the investment in advertising and marketing materials; and\n**(6)**\nthe term swag \u2014\n**(A)**\nmeans a tangible product or merchandise distributed at no cost with the sole purpose of advertising or promoting an agency, organization, or program;\n**(B)**\nincludes blankets, buttons, candy, clothing, coloring books, graphic novels, cups, fidget spinners, hats, holiday ornaments, jar grip openers, keychains, koozies, magnets, neckties, snuggies, stickers, stress balls, stuffed animals, thermoses, tote bags, trading cards, and writing utensils; and\n**(C)**\ndoes not include\u2014\n**(i)**\nan item presented as an honorary or informal recognition award related to the Armed Forces of the United States, such as a challenge coin or medal issued for sacrifice or meritorious service;\n**(ii)**\na brochure or pamphlet purchased or distributed for informational purposes; or\n**(iii)**\nan item distributed for diplomatic purposes, including a gift for a foreign leader.\n#### 3. Prohibitions; public relations and advertising spending\n##### (a) Prohibitions\nExcept as provided in subsection (c), and unless otherwise expressly authorized by law\u2014\n**(1)**\nan agency or other entity of the Federal Government may not use Federal funds to purchase or otherwise acquire or distribute swag; and\n**(2)**\nan agency or other entity of the Federal Government may not use Federal funds to manufacture or use a mascot to promote an agency, organization, program, or agenda.\n##### (b) Public relations and advertising spending\nEach agency shall, as part of the annual budget justification submitted to Congress, report on the public relations and advertising spending of the agency for the preceding fiscal year, which may include an estimate of the return on investment for the agency.\n##### (c) Exceptions\n**(1) Swag**\nSubsection (a)(1) shall not apply with respect to\u2014\n**(A)**\nan agency program that supports the mission and objectives of the agency that is initiating the public relations or advertising spending, provided that the spending generates a positive return on investment for the agency;\n**(B)**\nrecruitment relating to\u2014\n**(i)**\nenlistment or employment with the Armed Forces; or\n**(ii)**\nemployment with the Federal Government; or\n**(C)**\nan item distributed by the Bureau of the Census to assist the Bureau in conducting a census of the population of the United States.\n**(2) Mascots**\nSubsection (a)(2) shall not apply with respect to\u2014\n**(A)**\na mascot that is declared the property of the United States under a provision of law, including under section 2 of Public Law 93\u2013318 ( 16 U.S.C. 580p\u20131 ); or\n**(B)**\na mascot used\u2014\n**(i)**\nfor the purpose of recruitment of individuals to enlist in the Armed Forces of the United States; or\n**(ii)**\nin support of a military academy athletic team.\n##### (d) Regulations\nNot later than 180 days after the date of enactment of this Act, the Director of the Office of Management and Budget shall issue regulations to carry out this Act.",
      "versionDate": "2025-01-23",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-01-28",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "757",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SWAG Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-26T19:55:09Z"
          },
          {
            "name": "Marketing and advertising",
            "updateDate": "2025-03-26T19:54:59Z"
          },
          {
            "name": "Political advertising",
            "updateDate": "2025-03-26T19:55:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-03-20T21:26:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
    "originChamber": "Senate",
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
          "measure-id": "id119s210",
          "measure-number": "210",
          "measure-type": "s",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s210v00",
            "update-date": "2025-04-07"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Stop Wasteful Advertising by the Government Act or the SWAG Act</strong></p><p>This bill prohibits any federal agency or entity from using federal funds to purchase, acquire, or distribute swag (i.e., products distributed at no cost with the sole purpose of advertising or promoting an agency, organization, or program)\u00a0or to manufacture or use a mascot for promotional purposes. Exceptions to these prohibitions include (1) express authorization in law, (2) recruitment related to armed forces enlistment, and (3) military academy athletic team mascots.</p>"
        },
        "title": "SWAG Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s210.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Wasteful Advertising by the Government Act or the SWAG Act</strong></p><p>This bill prohibits any federal agency or entity from using federal funds to purchase, acquire, or distribute swag (i.e., products distributed at no cost with the sole purpose of advertising or promoting an agency, organization, or program)\u00a0or to manufacture or use a mascot for promotional purposes. Exceptions to these prohibitions include (1) express authorization in law, (2) recruitment related to armed forces enlistment, and (3) military academy athletic team mascots.</p>",
      "updateDate": "2025-04-07",
      "versionCode": "id119s210"
    },
    "title": "SWAG Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Wasteful Advertising by the Government Act or the SWAG Act</strong></p><p>This bill prohibits any federal agency or entity from using federal funds to purchase, acquire, or distribute swag (i.e., products distributed at no cost with the sole purpose of advertising or promoting an agency, organization, or program)\u00a0or to manufacture or use a mascot for promotional purposes. Exceptions to these prohibitions include (1) express authorization in law, (2) recruitment related to armed forces enlistment, and (3) military academy athletic team mascots.</p>",
      "updateDate": "2025-04-07",
      "versionCode": "id119s210"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s210is.xml"
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
      "title": "SWAG Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SWAG Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Wasteful Advertising by the Government Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit agencies from using Federal funds for publicity or propaganda purposes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:38Z"
    }
  ]
}
```
