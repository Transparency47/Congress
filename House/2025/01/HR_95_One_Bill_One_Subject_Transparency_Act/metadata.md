# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/95?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/95
- Title: One Bill, One Subject Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 95
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-06T21:45:15Z
- Update date including text: 2025-02-06T21:45:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/95",
    "number": "95",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
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
    "title": "One Bill, One Subject Transparency Act",
    "type": "HR",
    "updateDate": "2025-02-06T21:45:15Z",
    "updateDateIncludingText": "2025-02-06T21:45:15Z"
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
          "date": "2025-01-03T16:05:50Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr95ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 95\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require that each bill enacted by Congress be limited to only one subject, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the One Bill, One Subject Transparency Act .\n#### 2. One subject per bill\n##### (a) One subject\nEach bill or joint resolution shall embrace no more than one subject.\n##### (b) Subject in title\nThe subject of a bill or joint resolution shall be clearly and descriptively expressed in the title.\n##### (c) Appropriation bills\nAn appropriations bill shall not contain any general legislation or change of existing law provision which is not germane to the subject matter of the underlying bill. This subsection does not prohibit any provision imposing limitations upon the expenditure of appropriated funds.\n#### 3. Enforcement\n##### (a) Multiple subjects in title\nIf the title of an Act or joint resolution addresses two or more unrelated subjects, then the entire Act or joint resolution is void.\n##### (b) Provisions not expressed in title\nIf an Act or joint resolution contains provisions concerning a subject that is not clearly and descriptively expressed in its title, those provisions shall be void.\n##### (c) Appropriation provisions outside subcommittee jurisdiction\nIf an Act appropriating funds contains a provision outside of the jurisdiction of the relevant subcommittee of the Committees on Appropriations of the House and of the Senate, and therefore outside the subject of the bill, then such provision shall be void.\n##### (d) Provisions of appropriations bills not germane to subject matter\nIf an Act appropriating funds contains general legislation or change of existing law provision not germane to the subject matter of the underlying bill, then every such provision shall be void.\n##### (e) Commencement of an action\nAny person, including a Member of the House of Representatives or a Member of the Senate, aggrieved by the enforcement or threat of enforcement of Acts that do not comply with section 2 shall have a cause of action under sections 2201 and 2202 of title 28, United States Code, against the United States to seek appropriate relief, including an injunction against the enforcement of any law, the passage of which did not conform to section 2 or this section. The cause of action only applies to an Act or joint resolution signed into law on or after the date of enactment of this Act.\n##### (f) State of review\nIn any judicial action brought pursuant to subsection (e), the standard of review shall be de novo.",
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
            "name": "Appropriations",
            "updateDate": "2025-02-05T15:35:22Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-02-05T15:35:29Z"
          },
          {
            "name": "Government liability",
            "updateDate": "2025-02-05T15:35:39Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-02-05T15:35:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-03T15:27:53Z"
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
          "measure-id": "id119hr95",
          "measure-number": "95",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr95v00",
            "update-date": "2025-02-06"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>One Bill, One Subject Transparency Act</strong></p><p>This bill prohibits any bill or joint resolution from addressing more than one subject and establishes related enforcement mechanisms.</p><p>The bill requires bills and joint resolutions to address only one subject, which must be clearly and descriptively expressed in the bill or joint resolution's title. Appropriations bills may only contain provisions that are germane to the subject matter of the underlying bill.\u00a0However, appropriations bills may limit\u00a0the expenditure of appropriated funds.</p><p>The bill voids\u00a0<br/></p><ul><li>any act (i.e., law) or joint resolution with a title that addresses two or more unrelated subjects;</li><li>any provision of an act or joint resolution concerning a subject that is not clearly and descriptively expressed in the title;</li><li>any provision of an appropriations act that contains general legislation or change of existing law provision not germane to the subject matter of the underlying bill;</li><li>any provision of an appropriations act that addresses a subject outside of the jurisdiction of the relevant subcommittee of the Committees on Appropriations of the House and of the Senate.</li></ul><p>The bill also authorizes any person aggrieved by the enforcement or threat of enforcement of an act enacted after this bill that does not comply with the requirements of this bill\u00a0to sue the United States.</p>"
        },
        "title": "One Bill, One Subject Transparency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr95.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>One Bill, One Subject Transparency Act</strong></p><p>This bill prohibits any bill or joint resolution from addressing more than one subject and establishes related enforcement mechanisms.</p><p>The bill requires bills and joint resolutions to address only one subject, which must be clearly and descriptively expressed in the bill or joint resolution's title. Appropriations bills may only contain provisions that are germane to the subject matter of the underlying bill.\u00a0However, appropriations bills may limit\u00a0the expenditure of appropriated funds.</p><p>The bill voids\u00a0<br/></p><ul><li>any act (i.e., law) or joint resolution with a title that addresses two or more unrelated subjects;</li><li>any provision of an act or joint resolution concerning a subject that is not clearly and descriptively expressed in the title;</li><li>any provision of an appropriations act that contains general legislation or change of existing law provision not germane to the subject matter of the underlying bill;</li><li>any provision of an appropriations act that addresses a subject outside of the jurisdiction of the relevant subcommittee of the Committees on Appropriations of the House and of the Senate.</li></ul><p>The bill also authorizes any person aggrieved by the enforcement or threat of enforcement of an act enacted after this bill that does not comply with the requirements of this bill\u00a0to sue the United States.</p>",
      "updateDate": "2025-02-06",
      "versionCode": "id119hr95"
    },
    "title": "One Bill, One Subject Transparency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>One Bill, One Subject Transparency Act</strong></p><p>This bill prohibits any bill or joint resolution from addressing more than one subject and establishes related enforcement mechanisms.</p><p>The bill requires bills and joint resolutions to address only one subject, which must be clearly and descriptively expressed in the bill or joint resolution's title. Appropriations bills may only contain provisions that are germane to the subject matter of the underlying bill.\u00a0However, appropriations bills may limit\u00a0the expenditure of appropriated funds.</p><p>The bill voids\u00a0<br/></p><ul><li>any act (i.e., law) or joint resolution with a title that addresses two or more unrelated subjects;</li><li>any provision of an act or joint resolution concerning a subject that is not clearly and descriptively expressed in the title;</li><li>any provision of an appropriations act that contains general legislation or change of existing law provision not germane to the subject matter of the underlying bill;</li><li>any provision of an appropriations act that addresses a subject outside of the jurisdiction of the relevant subcommittee of the Committees on Appropriations of the House and of the Senate.</li></ul><p>The bill also authorizes any person aggrieved by the enforcement or threat of enforcement of an act enacted after this bill that does not comply with the requirements of this bill\u00a0to sue the United States.</p>",
      "updateDate": "2025-02-06",
      "versionCode": "id119hr95"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr95ih.xml"
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
      "title": "One Bill, One Subject Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T11:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "One Bill, One Subject Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T11:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require that each bill enacted by Congress be limited to only one subject, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T11:03:24Z"
    }
  ]
}
```
