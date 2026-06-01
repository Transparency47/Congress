# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/370?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/370
- Title: Voluntary School Prayer Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 370
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/370",
    "number": "370",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "R000603",
        "district": "7",
        "firstName": "David",
        "fullName": "Rep. Rouzer, David [R-NC-7]",
        "lastName": "Rouzer",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Voluntary School Prayer Protection Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr370ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 370\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Mr. Rouzer introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo prohibit the provision of Federal funds to any State or local educational agency that denies or prevents participation in constitutionally protected prayer in schools, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Voluntary School Prayer Protection Act of 2025 .\n#### 2. Funding contingent on respect for constitutionally protected school prayer\n##### (a) In general\nNotwithstanding any other provision of law, no funds made available through the Department of Education shall be provided to any State or local educational agency that has a policy of denying, or that effectively prevents participation in, constitutionally protected prayer in public schools by individuals on a voluntary basis.\n##### (b) Limitation\nNo person shall be required to participate in prayer or influence the form or content of any constitutionally protected prayer in public schools.",
      "versionDate": "2025-01-13",
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
            "name": "Education programs funding",
            "updateDate": "2025-02-13T15:00:35Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-02-13T15:00:35Z"
          },
          {
            "name": "Religion",
            "updateDate": "2025-02-13T15:00:35Z"
          },
          {
            "name": "School administration",
            "updateDate": "2025-02-13T15:00:35Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-13T15:00:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-02-13T14:22:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hr370",
          "measure-number": "370",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-03-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr370v00",
            "update-date": "2025-03-18"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Voluntary School Prayer Protection Act of 2025</strong></p><p>This bill prohibits the Department of Education (ED) from providing funding for public schools that restrict voluntary school prayer.</p><p>Specifically, the bill prohibits ED from providing funds to state or local educational agencies with policies that deny, or effectively prevent, individuals from voluntarily participating in public school prayer that is constitutionally protected.</p>"
        },
        "title": "Voluntary School Prayer Protection Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr370.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Voluntary School Prayer Protection Act of 2025</strong></p><p>This bill prohibits the Department of Education (ED) from providing funding for public schools that restrict voluntary school prayer.</p><p>Specifically, the bill prohibits ED from providing funds to state or local educational agencies with policies that deny, or effectively prevent, individuals from voluntarily participating in public school prayer that is constitutionally protected.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr370"
    },
    "title": "Voluntary School Prayer Protection Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Voluntary School Prayer Protection Act of 2025</strong></p><p>This bill prohibits the Department of Education (ED) from providing funding for public schools that restrict voluntary school prayer.</p><p>Specifically, the bill prohibits ED from providing funds to state or local educational agencies with policies that deny, or effectively prevent, individuals from voluntarily participating in public school prayer that is constitutionally protected.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr370"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr370ih.xml"
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
      "title": "Voluntary School Prayer Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T12:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Voluntary School Prayer Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T12:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the provision of Federal funds to any State or local educational agency that denies or prevents participation in constitutionally protected prayer in schools, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T12:48:19Z"
    }
  ]
}
```
