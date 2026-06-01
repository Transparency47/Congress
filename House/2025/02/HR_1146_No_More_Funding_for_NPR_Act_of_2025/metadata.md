# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1146?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1146
- Title: No More Funding for NPR Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1146
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2025-08-16T08:05:51Z
- Update date including text: 2025-08-16T08:05:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-07: Introduced in House

## Actions

- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1146",
    "number": "1146",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "S001220",
        "district": "5",
        "firstName": "Dale",
        "fullName": "Rep. Strong, Dale W. [R-AL-5]",
        "lastName": "Strong",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "No More Funding for NPR Act of 2025",
    "type": "HR",
    "updateDate": "2025-08-16T08:05:51Z",
    "updateDateIncludingText": "2025-08-16T08:05:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
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
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-07",
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
          "date": "2025-02-07T14:01:30Z",
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
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "GA"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1146ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1146\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mr. Strong introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit Federal funding for National Public Radio, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No More Funding for NPR Act of 2025 .\n#### 2. Prohibition on Federal funding for National Public Radio\n##### (a) Prohibition\nAfter the date of the enactment of this Act, no Federal funds may, directly or indirectly, be made available to or used to support an organization described in subsection (d), including through the payment of dues to or the purchase of programming from such organization by a public broadcast station using Federal funds received by such station.\n##### (b) Rescission\nThe unobligated balances of any Federal amounts that otherwise would have been allocated to the organization described in subsection (d)(1) for fiscal year 2025 or 2026 are hereby permanently rescinded.\n##### (c) Limitation\nSubsections (a) and (b) do not apply to Federal funds made available to an organization described in subsection (d)\u2014\n**(1)**\nduring a period that the Federal Emergency Management Agency is actively engaged in disaster response activities; and\n**(2)**\nfor the sole purpose of disseminating to the public urgent information necessary to protect public safety.\n##### (d) Organizations described\nThe organizations described in this subsection are\u2014\n**(1)**\nthe organization known, as of the date of the enactment of this Act, as National Public Radio ; and\n**(2)**\nany successor organization to the organization described in paragraph (1).",
      "versionDate": "2025-02-07",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-14T17:54:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-07",
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
          "measure-id": "id119hr1146",
          "measure-number": "1146",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-07",
          "originChamber": "HOUSE",
          "update-date": "2025-06-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1146v00",
            "update-date": "2025-06-05"
          },
          "action-date": "2025-02-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No More Funding for NPR Act of 2025</strong></p><p>This bill prohibits federal funding of National Public Radio (NPR) or any successor organization and rescinds certain funds that were provided to NPR.</p><p>The prohibition includes the payment of dues to or the purchase of programming from NPR by a public broadcast station using federal funds. The prohibition does not include funds made available to NPR during certain periods of disaster response and for the sole purpose of disseminating urgent information to protect public safety.</p>"
        },
        "title": "No More Funding for NPR Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1146.xml",
    "summary": {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No More Funding for NPR Act of 2025</strong></p><p>This bill prohibits federal funding of National Public Radio (NPR) or any successor organization and rescinds certain funds that were provided to NPR.</p><p>The prohibition includes the payment of dues to or the purchase of programming from NPR by a public broadcast station using federal funds. The prohibition does not include funds made available to NPR during certain periods of disaster response and for the sole purpose of disseminating urgent information to protect public safety.</p>",
      "updateDate": "2025-06-05",
      "versionCode": "id119hr1146"
    },
    "title": "No More Funding for NPR Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No More Funding for NPR Act of 2025</strong></p><p>This bill prohibits federal funding of National Public Radio (NPR) or any successor organization and rescinds certain funds that were provided to NPR.</p><p>The prohibition includes the payment of dues to or the purchase of programming from NPR by a public broadcast station using federal funds. The prohibition does not include funds made available to NPR during certain periods of disaster response and for the sole purpose of disseminating urgent information to protect public safety.</p>",
      "updateDate": "2025-06-05",
      "versionCode": "id119hr1146"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1146ih.xml"
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
      "title": "No More Funding for NPR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-10T12:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No More Funding for NPR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-10T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit Federal funding for National Public Radio, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-10T12:33:31Z"
    }
  ]
}
```
