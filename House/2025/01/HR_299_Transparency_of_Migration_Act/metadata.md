# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/299?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/299
- Title: Transparency of Migration Act
- Congress: 119
- Bill type: HR
- Bill number: 299
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-02-27T19:56:51Z
- Update date including text: 2025-02-27T19:56:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/299",
    "number": "299",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Transparency of Migration Act",
    "type": "HR",
    "updateDate": "2025-02-27T19:56:51Z",
    "updateDateIncludingText": "2025-02-27T19:56:51Z"
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
          "date": "2025-01-09T14:38:40Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr299ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 299\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Ms. Malliotakis introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require the Secretary of Homeland Security and the Secretary of Health and Human Services to make available to the public on the websites of their respective departments certain information relating to individuals processed through U.S. Customs and Border Protection or Department of Health and Human Services facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transparency of Migration Act .\n#### 2. Public availability of information relating to individuals processed through U.S. Customs and Border Protection or Department of Health and Human Services facilities\n##### (a) In general\nThe Secretary of Homeland Security and the Secretary of Health and Human Services shall make available to the public on the websites of their respective departments\u2019 information described in subsection (b) relating to individuals unlawfully present in the United States who are\u2014\n**(1)**\napprehended by U.S. Customs and Border Protection and sent to a federally owned or run detention center or released into the United States; or\n**(2)**\nprocessed through a Department of Health and Human Services facility.\n##### (b) Information described\nInformation described in this subsection is information relating to the following:\n**(1)**\nThe daily number of individuals described in subsection (a).\n**(2)**\nThe countries of origins of such individuals.\n**(3)**\nThe ages and genders of such individuals.\n**(4)**\nThe States to which such individuals have been either released or sent.\n**(5)**\nThe number and types of criminal convictions, if any, such individuals possess.\n##### (c) Updates\nInformation under this section shall be updated weekly.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-02-19T18:00:02Z"
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
          "measure-id": "id119hr299",
          "measure-number": "299",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr299v00",
            "update-date": "2025-02-27"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Transparency of Migration Act</strong></p> <p>This bill requires the Department of Homeland Security and the Department of Health and Human Services (HHS) to make publicly available online certain information about individuals unlawfully present in the United States who are (1) apprehended by U.S. Customs and Border Protection and sent to a federal detention center or released into the United States, or (2) processed through an HHS facility.</p> <p>This information must be updated weekly and must include daily numbers, the country of origin of such individuals, and other details. </p>"
        },
        "title": "Transparency of Migration Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr299.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Transparency of Migration Act</strong></p> <p>This bill requires the Department of Homeland Security and the Department of Health and Human Services (HHS) to make publicly available online certain information about individuals unlawfully present in the United States who are (1) apprehended by U.S. Customs and Border Protection and sent to a federal detention center or released into the United States, or (2) processed through an HHS facility.</p> <p>This information must be updated weekly and must include daily numbers, the country of origin of such individuals, and other details. </p>",
      "updateDate": "2025-02-27",
      "versionCode": "id119hr299"
    },
    "title": "Transparency of Migration Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Transparency of Migration Act</strong></p> <p>This bill requires the Department of Homeland Security and the Department of Health and Human Services (HHS) to make publicly available online certain information about individuals unlawfully present in the United States who are (1) apprehended by U.S. Customs and Border Protection and sent to a federal detention center or released into the United States, or (2) processed through an HHS facility.</p> <p>This information must be updated weekly and must include daily numbers, the country of origin of such individuals, and other details. </p>",
      "updateDate": "2025-02-27",
      "versionCode": "id119hr299"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr299ih.xml"
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
      "title": "Transparency of Migration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transparency of Migration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Homeland Security and the Secretary of Health and Human Services to make available to the public on the websites of their respective departments certain information relating to individuals processed through U.S. Customs and Border Protection or Department of Health and Human Services facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T03:03:33Z"
    }
  ]
}
```
