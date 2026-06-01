# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/58?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/58
- Title: Voter Integrity Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 58
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-11-21T12:04:23Z
- Update date including text: 2025-11-21T12:04:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/58",
    "number": "58",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Voter Integrity Protection Act",
    "type": "HR",
    "updateDate": "2025-11-21T12:04:23Z",
    "updateDateIncludingText": "2025-11-21T12:04:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:07:05Z",
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
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "SC"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr58ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 58\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself and Ms. Mace ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to make voting in a Federal election by an unlawfully present alien an aggravated felony, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Voter Integrity Protection Act .\n#### 2. Unlawful voting\n##### (a) Aggravated felony\nSection 101(a)(43) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(43) ) is amended\u2014\n**(1)**\nin subparagraph (T), by striking and at the end;\n**(2)**\nin subparagraph (U), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(V) an offense described in section 611 of title 18, United States Code, committed by an alien who is unlawfully present in the United States. .\n##### (b) Deportable offense\nSection 237(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(2) ) is amended by adding at the end the following:\n(G) Voting offenses Any alien who is unlawfully present in the United States and who knowingly commits a violation of section 611 of title 18, United States Code, is deportable. .",
      "versionDate": "2025-01-03",
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
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-06-10T16:03:39Z"
          },
          {
            "name": "Congressional elections",
            "updateDate": "2025-06-10T16:03:39Z"
          },
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-06-10T16:03:39Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-06-10T16:03:39Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-06-10T16:03:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-02-03T14:51:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr58",
          "measure-number": "58",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr58v00",
            "update-date": "2025-02-07"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Voter Integrity Protection Act</b></p> <p>This bill imposes additional immigration-related penalties for non-U.S. nationals (<i>aliens</i> under federal law) who vote in an election for federal office.</p> <p> It shall be an aggravated felony for a non-U.S. national who is unlawfully present to violate an existing prohibition against a non-U.S. national voting in a federal election. (An aggravated felony conviction carries various immigration consequences, such as rendering the non-U.S. national inadmissible, deportable, and barred from establishing good moral character for naturalization.)</p> <p>A non-U.S. national who is unlawfully present and who knowingly violates the prohibition against voting in a federal election shall be deportable.</p>"
        },
        "title": "Voter Integrity Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr58.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Voter Integrity Protection Act</b></p> <p>This bill imposes additional immigration-related penalties for non-U.S. nationals (<i>aliens</i> under federal law) who vote in an election for federal office.</p> <p> It shall be an aggravated felony for a non-U.S. national who is unlawfully present to violate an existing prohibition against a non-U.S. national voting in a federal election. (An aggravated felony conviction carries various immigration consequences, such as rendering the non-U.S. national inadmissible, deportable, and barred from establishing good moral character for naturalization.)</p> <p>A non-U.S. national who is unlawfully present and who knowingly violates the prohibition against voting in a federal election shall be deportable.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hr58"
    },
    "title": "Voter Integrity Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Voter Integrity Protection Act</b></p> <p>This bill imposes additional immigration-related penalties for non-U.S. nationals (<i>aliens</i> under federal law) who vote in an election for federal office.</p> <p> It shall be an aggravated felony for a non-U.S. national who is unlawfully present to violate an existing prohibition against a non-U.S. national voting in a federal election. (An aggravated felony conviction carries various immigration consequences, such as rendering the non-U.S. national inadmissible, deportable, and barred from establishing good moral character for naturalization.)</p> <p>A non-U.S. national who is unlawfully present and who knowingly violates the prohibition against voting in a federal election shall be deportable.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hr58"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr58ih.xml"
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
      "title": "Voter Integrity Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T11:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Voter Integrity Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to make voting in a Federal election by an unlawfully present alien an aggravated felony, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T11:18:27Z"
    }
  ]
}
```
