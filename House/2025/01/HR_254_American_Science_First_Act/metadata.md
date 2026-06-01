# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/254?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/254
- Title: American Science First Act
- Congress: 119
- Bill type: HR
- Bill number: 254
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-02-11T21:14:20Z
- Update date including text: 2025-02-11T21:14:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/254",
    "number": "254",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "A000372",
        "district": "12",
        "firstName": "Rick",
        "fullName": "Rep. Allen, Rick W. [R-GA-12]",
        "lastName": "Allen",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "American Science First Act",
    "type": "HR",
    "updateDate": "2025-02-11T21:14:20Z",
    "updateDateIncludingText": "2025-02-11T21:14:20Z"
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
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
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
          "date": "2025-01-09T14:32:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr254ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 254\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Allen introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo prohibit the Director of the National Science Foundation from awarding grants and other forms of assistance to Chinese communist military companies and their affiliates, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Science First Act .\n#### 2. Restriction on National Science Foundation grants and other forms of assistance to Chinese communist military companies and their affiliates\n##### (a) In general\nNotwithstanding any other provision of law, the Director of the National Science Foundation may not provide grants or other forms of assistance to any individual or entity that is affiliated or otherwise has a relationship, including but not limited to a research partnership, joint venture, or contract with\u2014\n**(1)**\nan entity included on the list maintained and set forth in Supplement No. 4 to part 744 of the Export Administration Regulations;\n**(2)**\na company on the list required by section 1237 of the Strom Thurmond National Defense Authorization Act for Fiscal Year 1999 ( Public Law 105\u2013261 ; 50 U.S.C. 1701 note), or required by section 1260H of the Mac Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ), or any successor list; or\n**(3)**\nany parent, subsidiary, affiliate of, or entity owned by or controlled by, an entity described in paragraph (1) or (2).\n##### (b) Export administration regulations defined\nIn this section, the term Export Administration Regulations means the regulations set forth in subchapter C of chapter VII of title 15, Code of Federal Regulations, or successor regulations.",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-02-06T21:05:01Z"
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
          "measure-id": "id119hr254",
          "measure-number": "254",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr254v00",
            "update-date": "2025-02-11"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>American Science First Act</strong></p> <p>This bill prohibits the National Science Foundation (NSF) from providing grants or other forms of assistance to certain foreign individuals and entities. Specifically, the NSF may not support any individual or entity that is affiliated or otherwise has a relationship, including but not limited to a research partnership, joint venture, or contract, with</p> <ul> <li>an entity included on the entity list under the Export Administration Regulations, which identifies foreign entities subject to license requirements for the export, reexport, or transfer of certain items;</li> <li>a Chinese military company operating in the United States or any of its territories or possessions on the list required under the Strom Thurmond National Defense Authorization Act for Fiscal Year 1999, or required under the Mac Thornberry National Defense Authorization Act for Fiscal Year 2021, or any successor list; or</li> <li>any parent, subsidiary, affiliate of, or entity owned by or controlled by any such entity.</li> </ul>"
        },
        "title": "American Science First Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr254.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Science First Act</strong></p> <p>This bill prohibits the National Science Foundation (NSF) from providing grants or other forms of assistance to certain foreign individuals and entities. Specifically, the NSF may not support any individual or entity that is affiliated or otherwise has a relationship, including but not limited to a research partnership, joint venture, or contract, with</p> <ul> <li>an entity included on the entity list under the Export Administration Regulations, which identifies foreign entities subject to license requirements for the export, reexport, or transfer of certain items;</li> <li>a Chinese military company operating in the United States or any of its territories or possessions on the list required under the Strom Thurmond National Defense Authorization Act for Fiscal Year 1999, or required under the Mac Thornberry National Defense Authorization Act for Fiscal Year 2021, or any successor list; or</li> <li>any parent, subsidiary, affiliate of, or entity owned by or controlled by any such entity.</li> </ul>",
      "updateDate": "2025-02-11",
      "versionCode": "id119hr254"
    },
    "title": "American Science First Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Science First Act</strong></p> <p>This bill prohibits the National Science Foundation (NSF) from providing grants or other forms of assistance to certain foreign individuals and entities. Specifically, the NSF may not support any individual or entity that is affiliated or otherwise has a relationship, including but not limited to a research partnership, joint venture, or contract, with</p> <ul> <li>an entity included on the entity list under the Export Administration Regulations, which identifies foreign entities subject to license requirements for the export, reexport, or transfer of certain items;</li> <li>a Chinese military company operating in the United States or any of its territories or possessions on the list required under the Strom Thurmond National Defense Authorization Act for Fiscal Year 1999, or required under the Mac Thornberry National Defense Authorization Act for Fiscal Year 2021, or any successor list; or</li> <li>any parent, subsidiary, affiliate of, or entity owned by or controlled by any such entity.</li> </ul>",
      "updateDate": "2025-02-11",
      "versionCode": "id119hr254"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr254ih.xml"
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
      "title": "American Science First Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T02:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Science First Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T02:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Director of the National Science Foundation from awarding grants and other forms of assistance to Chinese communist military companies and their affiliates, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T02:18:30Z"
    }
  ]
}
```
