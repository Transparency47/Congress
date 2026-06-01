# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/118?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/118
- Title: No Federal Funds for Political Prosecutions Act
- Congress: 119
- Bill type: HR
- Bill number: 118
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-06T15:18:08Z
- Update date including text: 2025-02-06T15:18:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/118",
    "number": "118",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
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
    "title": "No Federal Funds for Political Prosecutions Act",
    "type": "HR",
    "updateDate": "2025-02-06T15:18:08Z",
    "updateDateIncludingText": "2025-02-06T15:18:08Z"
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
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-01-03T16:17:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-03T16:17:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr118ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 118\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the use of forfeited funds made available to certain State or local law enforcement agencies pursuant to equitable sharing for certain purposes.\n#### 1. Short title\nThis Act may be cited as the No Federal Funds for Political Prosecutions Act .\n#### 2. Limitation on use of forfeited funds made available pursuant to equitable sharing\n##### (a) In general\nNo funds or property received pursuant to section 511(e) of the Controlled Substances Act ( 21 U.S.C. 811(e) ), section 981 of title 18, United States Code, or section 524 of title 28, United States Code, by a State or local law enforcement agency with the authority to prosecute a criminal case may be used to investigate or prosecute the President or Vice President, a former President or Vice President, or a candidate for the office of President.\n##### (b) Certification\nA State or local law enforcement agency referred to in subsection (a) shall certify to the Attorney General that the law enforcement agency will comply with subsection (a).\n##### (c) Disqualification\nIn the case of a State or local law enforcement agency that the Attorney General determines has failed to comply with this section, the Attorney General may not transfer, under section 511(e) of the Controlled Substances Act ( 21 U.S.C. 811(e) ), section 981 of title 18, United States Code, or section 524 of title 28, United States Code, any property seized by the Attorney General and forfeited to the United States, or any of the proceeds from the sale of such property to such State or local law enforcement agency.\n##### (d) Definition\nIn this section, the term candidate has the meaning given such term in section 301 of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101 ).",
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
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-02-06T15:17:58Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-02-06T15:18:03Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-02-06T15:17:51Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-06T15:18:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-03T15:06:02Z"
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
          "measure-id": "id119hr118",
          "measure-number": "118",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr118v00",
            "update-date": "2025-02-05"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Federal Funds for Political Prosecutions Act</strong></p><p>This bill specifies that no funds or property received through equitable sharing by a state or local law enforcement agency with the authority to prosecute a criminal case may be used to investigate or prosecute a current or former President or Vice President, or a candidate for the office of President.</p>"
        },
        "title": "No Federal Funds for Political Prosecutions Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr118.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Federal Funds for Political Prosecutions Act</strong></p><p>This bill specifies that no funds or property received through equitable sharing by a state or local law enforcement agency with the authority to prosecute a criminal case may be used to investigate or prosecute a current or former President or Vice President, or a candidate for the office of President.</p>",
      "updateDate": "2025-02-05",
      "versionCode": "id119hr118"
    },
    "title": "No Federal Funds for Political Prosecutions Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Federal Funds for Political Prosecutions Act</strong></p><p>This bill specifies that no funds or property received through equitable sharing by a state or local law enforcement agency with the authority to prosecute a criminal case may be used to investigate or prosecute a current or former President or Vice President, or a candidate for the office of President.</p>",
      "updateDate": "2025-02-05",
      "versionCode": "id119hr118"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr118ih.xml"
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
      "title": "No Federal Funds for Political Prosecutions Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T12:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Federal Funds for Political Prosecutions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T12:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of forfeited funds made available to certain State or local law enforcement agencies pursuant to equitable sharing for certain purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T12:48:25Z"
    }
  ]
}
```
