# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/174?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/174
- Title: Amtrak Transparency Act
- Congress: 119
- Bill type: S
- Bill number: 174
- Origin chamber: Senate
- Introduced date: 2025-01-21
- Update date: 2025-03-19T13:52:03Z
- Update date including text: 2025-03-19T13:52:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in Senate
- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-01-21: Introduced in Senate

## Actions

- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/174",
    "number": "174",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Amtrak Transparency Act",
    "type": "S",
    "updateDate": "2025-03-19T13:52:03Z",
    "updateDateIncludingText": "2025-03-19T13:52:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-21",
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
      "actionDate": "2025-01-21",
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
          "date": "2025-01-21T22:47:40Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s174is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 174\nIN THE SENATE OF THE UNITED STATES\nJanuary 21, 2025 Mrs. Fischer introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo improve the transparency of Amtrak operations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Amtrak Transparency Act .\n#### 2. Board of Directors meetings\nSection 24302 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(6), by striking in an open meeting ; and\n**(2)**\nby amending subsection (e) to read as follows:\n(e) Meetings (1) Quorum A majority of the members serving on the Board who are eligible to vote shall constitute a quorum for doing business. (2) Notice; open meetings (A) Notice Not later than 30 days before convening any meeting of the Board, the Board shall post, on a publicly accessible website, an announcement of the meeting that includes the anticipated agenda for the meeting. (B) Open meetings All meetings of the Board shall comply with the requirements set forth in section 552b of title 5. (3) Annual meeting with States Not less frequently than annually, the Board shall convene a meeting to which the head of the Department of Transportation of each State traversed by a long-distance route or State-supported route, or the designee of such State official, shall be invited to participate. .\n#### 3. Discretionary bonus disclosure requirement\nSection 24303(b) of title 49, United States Code, is amended by striking The preceding sentence and inserting Amtrak shall publicly disclose the amount of each discretionary bonus paid to any officer or non-bargaining unit employee. The 2 preceding sentences .\n#### 4. Disclosure of vendor agreements\nSection 24315(h) of title 49, United States Code, is amended by adding at the end the following: Upon request, Amtrak shall disclose to a State or the State-Amtrak Intercity Passenger Rail Committee, any vendor agreement valued at not less than $250,000 for services procured to implement a service on a State-supported route. .",
      "versionDate": "2025-01-21",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-02-24T16:03:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
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
          "measure-id": "id119s174",
          "measure-number": "174",
          "measure-type": "s",
          "orig-publish-date": "2025-01-21",
          "originChamber": "SENATE",
          "update-date": "2025-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s174v00",
            "update-date": "2025-03-19"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Amtrak Transparency Act</strong></p><p>This bill increases Amtrak's open meeting and public disclosure requirements.</p><p>Specifically, the Amtrak Board of Directors must comply with federal open meeting requirements under the Government in the Sunshine Act.</p><p>In addition, at least 30 days prior to the board convening, the board must publicly post an announcement of the meeting and the anticipated meeting agenda.</p><p>The board must also annually convene a meeting to which state departments of transportation\u00a0with long-distance routes or state-supported routes are\u00a0invited to participate.</p><p>Further, Amtrak must publicly disclose the discretionary bonus compensation paid to an Amtrak officer or non-bargaining unit employee.</p><p>Upon request,\u00a0Amtrak must also disclose to a state or the State-Amtrak Intercity Passenger Rail Committee vendor agreements of $250,000 or more for certain services on state-supported routes.</p>"
        },
        "title": "Amtrak Transparency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s174.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Amtrak Transparency Act</strong></p><p>This bill increases Amtrak's open meeting and public disclosure requirements.</p><p>Specifically, the Amtrak Board of Directors must comply with federal open meeting requirements under the Government in the Sunshine Act.</p><p>In addition, at least 30 days prior to the board convening, the board must publicly post an announcement of the meeting and the anticipated meeting agenda.</p><p>The board must also annually convene a meeting to which state departments of transportation\u00a0with long-distance routes or state-supported routes are\u00a0invited to participate.</p><p>Further, Amtrak must publicly disclose the discretionary bonus compensation paid to an Amtrak officer or non-bargaining unit employee.</p><p>Upon request,\u00a0Amtrak must also disclose to a state or the State-Amtrak Intercity Passenger Rail Committee vendor agreements of $250,000 or more for certain services on state-supported routes.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119s174"
    },
    "title": "Amtrak Transparency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Amtrak Transparency Act</strong></p><p>This bill increases Amtrak's open meeting and public disclosure requirements.</p><p>Specifically, the Amtrak Board of Directors must comply with federal open meeting requirements under the Government in the Sunshine Act.</p><p>In addition, at least 30 days prior to the board convening, the board must publicly post an announcement of the meeting and the anticipated meeting agenda.</p><p>The board must also annually convene a meeting to which state departments of transportation\u00a0with long-distance routes or state-supported routes are\u00a0invited to participate.</p><p>Further, Amtrak must publicly disclose the discretionary bonus compensation paid to an Amtrak officer or non-bargaining unit employee.</p><p>Upon request,\u00a0Amtrak must also disclose to a state or the State-Amtrak Intercity Passenger Rail Committee vendor agreements of $250,000 or more for certain services on state-supported routes.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119s174"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s174is.xml"
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
      "title": "Amtrak Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Amtrak Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve the transparency of Amtrak operations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:21Z"
    }
  ]
}
```
