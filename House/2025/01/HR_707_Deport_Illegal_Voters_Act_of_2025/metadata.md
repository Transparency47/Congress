# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/707?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/707
- Title: Deport Illegal Voters Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 707
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-05-07T23:29:04Z
- Update date including text: 2025-05-07T23:29:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on the Judiciary.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/707",
    "number": "707",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
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
    "title": "Deport Illegal Voters Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-07T23:29:04Z",
    "updateDateIncludingText": "2025-05-07T23:29:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:03:30Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr707ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 707\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Strong introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to make unlawful voting an aggravated felony.\n#### 1. Short title\nThis Act may be cited as the Deport Illegal Voters Act of 2025 .\n#### 2. Expanding the definition of aggravated felonies under the Immigration and Nationality Act\n##### (a) In general\nSection 101(a)(43) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(43) ) is amended\u2014\n**(1)**\nin subparagraph (T), by striking and at the end;\n**(2)**\nby redesignating subparagraph (U) as subparagraph (V); and\n**(3)**\nby inserting after subparagraph (T) the following:\n(U) voting in violation of any Federal, State, or local constitutional provision, statute, ordinance, or regulation; and .\n##### (b) Conforming amendment\n**(1) Inadmissibility**\nSection 212(a)(10)(D) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(10)(D) ) is amended to read as follows:\n(D) Unlawful voters Any alien who has voted in violation of any Federal, State, or local constitutional provision, statute, ordinance, or regulation is inadmissible. .\n**(2) Deportability**\nSection 237(a) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a) ) is amended by striking paragraph (6).",
      "versionDate": "2025-01-23",
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
        "updateDate": "2025-02-24T15:48:46Z"
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
          "measure-id": "id119hr707",
          "measure-number": "707",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr707v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Deport Illegal Voters Act of 2025</strong></p><p>This bill increases immigration restrictions for\u00a0non-U.S. nationals (<em>aliens </em>under federal law) who vote in violation of a federal, state, or local constitutional provision, statute, ordinance, or regulation. Specifically, the bill adds such an act to the list of aggravated felonies that are grounds for deportation and inadmissibility.</p><p>Under current law, this act is generally grounds for deportation and inadmissibility. However, an exception exists for individuals who, in addition to other requirements, reasonably believed at the time of such act that they were citizens.</p>"
        },
        "title": "Deport Illegal Voters Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr707.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Deport Illegal Voters Act of 2025</strong></p><p>This bill increases immigration restrictions for\u00a0non-U.S. nationals (<em>aliens </em>under federal law) who vote in violation of a federal, state, or local constitutional provision, statute, ordinance, or regulation. Specifically, the bill adds such an act to the list of aggravated felonies that are grounds for deportation and inadmissibility.</p><p>Under current law, this act is generally grounds for deportation and inadmissibility. However, an exception exists for individuals who, in addition to other requirements, reasonably believed at the time of such act that they were citizens.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr707"
    },
    "title": "Deport Illegal Voters Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Deport Illegal Voters Act of 2025</strong></p><p>This bill increases immigration restrictions for\u00a0non-U.S. nationals (<em>aliens </em>under federal law) who vote in violation of a federal, state, or local constitutional provision, statute, ordinance, or regulation. Specifically, the bill adds such an act to the list of aggravated felonies that are grounds for deportation and inadmissibility.</p><p>Under current law, this act is generally grounds for deportation and inadmissibility. However, an exception exists for individuals who, in addition to other requirements, reasonably believed at the time of such act that they were citizens.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr707"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr707ih.xml"
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
      "title": "Deport Illegal Voters Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T08:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Deport Illegal Voters Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T08:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to make unlawful voting an aggravated felony.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T08:03:48Z"
    }
  ]
}
```
