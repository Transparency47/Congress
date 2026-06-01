# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/314?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/314
- Title: Empowering Nonprofits Act
- Congress: 119
- Bill type: HR
- Bill number: 314
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-02-27T15:41:46Z
- Update date including text: 2025-02-27T15:41:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/314",
    "number": "314",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "R000600",
        "district": "",
        "firstName": "Aumua Amata",
        "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS]",
        "lastName": "Radewagen",
        "party": "R",
        "state": "AS"
      }
    ],
    "title": "Empowering Nonprofits Act",
    "type": "HR",
    "updateDate": "2025-02-27T15:41:46Z",
    "updateDateIncludingText": "2025-02-27T15:41:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:36:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr314ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 314\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mrs. Radewagen introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require executive agencies to reduce cost-sharing requirements for certain grants with certain nonprofit organizations 25 percent, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Empowering Nonprofits Act .\n#### 2. Reduction of cost-sharing requirements for grants\n##### (a) Reduction of cost-Sharing requirement\nBeginning on the date of the enactment of this Act and ending 5 years thereafter, the head of an executive agency shall reduce any cost-sharing requirement 25 percent for an eligible nonprofit organization for grants made directly to that organization.\n##### (b) Definitions\nIn this section:\n**(1) Eligible nonprofit organization**\nThe term eligible nonprofit organization means a nonprofit organization that is located in a State with more than 20 percent of individuals living below the Federal poverty line.\n**(2) Executive agency**\nThe term executive agency has the meaning given in section 133 of title 41, United States Code.\n**(3) Nonprofit organization**\nThe term nonprofit organization means an organization that is described in section 501(c)(3) of the Internal Revenue Code of 1968 and exempt from taxation under section 501(a) of such Code.\n**(4) State**\nThe term State means each of the several States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Tribe.",
      "versionDate": "2025-01-09",
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
            "name": "Executive agency funding and structure",
            "updateDate": "2025-02-24T19:25:49Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2025-02-24T19:25:49Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-02-24T19:25:49Z"
          },
          {
            "name": "Tax-exempt organizations",
            "updateDate": "2025-02-24T19:25:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-21T12:01:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr314",
          "measure-number": "314",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr314v00",
            "update-date": "2025-02-27"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Empowering Nonprofits Act</strong></p><p>This bill reduces cost-sharing requirements for grants directly awarded to certain nonprofit organizations for the five years following the bill's enactment. Eligible nonprofit organizations are those located in a U.S. state (including the District of Columbia or a U.S. commonwealth, territory, or possession) or federally recognized Indian tribe that has more than 20% of individuals living below the poverty line.</p><p>Specifically, the bill requires an executive agency, during that time frame, to reduce any cost-sharing requirement by 25% for grants made directly to an eligible nonprofit.</p>"
        },
        "title": "Empowering Nonprofits Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr314.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Empowering Nonprofits Act</strong></p><p>This bill reduces cost-sharing requirements for grants directly awarded to certain nonprofit organizations for the five years following the bill's enactment. Eligible nonprofit organizations are those located in a U.S. state (including the District of Columbia or a U.S. commonwealth, territory, or possession) or federally recognized Indian tribe that has more than 20% of individuals living below the poverty line.</p><p>Specifically, the bill requires an executive agency, during that time frame, to reduce any cost-sharing requirement by 25% for grants made directly to an eligible nonprofit.</p>",
      "updateDate": "2025-02-27",
      "versionCode": "id119hr314"
    },
    "title": "Empowering Nonprofits Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Empowering Nonprofits Act</strong></p><p>This bill reduces cost-sharing requirements for grants directly awarded to certain nonprofit organizations for the five years following the bill's enactment. Eligible nonprofit organizations are those located in a U.S. state (including the District of Columbia or a U.S. commonwealth, territory, or possession) or federally recognized Indian tribe that has more than 20% of individuals living below the poverty line.</p><p>Specifically, the bill requires an executive agency, during that time frame, to reduce any cost-sharing requirement by 25% for grants made directly to an eligible nonprofit.</p>",
      "updateDate": "2025-02-27",
      "versionCode": "id119hr314"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr314ih.xml"
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
      "title": "Empowering Nonprofits Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-07T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Empowering Nonprofits Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-07T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require executive agencies to reduce cost-sharing requirements for certain grants with certain nonprofit organizations 25 percent, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-07T04:18:19Z"
    }
  ]
}
```
