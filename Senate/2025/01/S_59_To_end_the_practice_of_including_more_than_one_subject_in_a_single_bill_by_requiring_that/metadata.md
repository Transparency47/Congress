# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/59?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/59
- Title: One Subject at a Time Act
- Congress: 119
- Bill type: S
- Bill number: 59
- Origin chamber: Senate
- Introduced date: 2025-01-09
- Update date: 2025-12-06T06:31:28Z
- Update date including text: 2025-12-06T06:31:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in Senate
- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2025-01-09: Introduced in Senate

## Actions

- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/59",
    "number": "59",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "One Subject at a Time Act",
    "type": "S",
    "updateDate": "2025-12-06T06:31:28Z",
    "updateDateIncludingText": "2025-12-06T06:31:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Rules and Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T20:19:12Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s59is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 59\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Mr. Paul introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo end the practice of including more than one subject in a single bill by requiring that each bill enacted by Congress be limited to only one subject, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the One Subject at a Time Act .\n#### 2. One subject at a time\n##### (a) One subject\nEach bill or joint resolution shall embrace no more than one subject.\n##### (b) Subject in title\nThe subject of a bill or joint resolution shall be clearly and descriptively expressed in the title.\n##### (c) Appropriation bills\nAn appropriations bill shall not contain any general legislation or change to a provision of existing law, the subject of which is not germane to the subject matter of each such appropriations bill. This section shall not be construed to prohibit any provision imposing limitations upon the expenditure of funds so appropriated.\n#### 3. Enforcement\n##### (a) Multiple subjects in title\nIf the title of an Act or joint resolution addresses two or more unrelated subjects, the entire Act or joint resolution is void.\n##### (b) Provisions not expressed in title\nIf the title of an Act or joint resolution addresses a single subject, but the Act contains one or more provisions concerning a subject that is not clearly and descriptively expressed in its title, only such provision or provisions concerning the subject not clearly and descriptively expressed in the title shall be void.\n##### (c) Appropriation provisions outside subcommittee jurisdiction\nIf an Act appropriating funds contains a provision outside of the jurisdiction of the relevant subcommittee of the Committees on Appropriations of the House of Representatives and of the Senate, and therefore outside the subject of the bill, such provision shall be void.\n##### (d) Provisions of appropriation bills not germane to subject matter\nIf an Act appropriating funds contains a provision of general legislation or a change of a provision of existing law not germane to the subject matter of such bill, such provision shall be void.\n##### (e) Commencement of an action\nAny person aggrieved by the enforcement of, or attempt or threat of enforcement of, an Act passed without having complied with section 2 or this section, or any Member of Congress aggrieved by the failure of the House of Congress of which that individual is a member to comply with any requirement of those sections, shall, regardless of the amount in controversy, have a cause of action under sections 2201 and 2202 of title 28, United States Code, against the United States to seek appropriate relief, including an injunction against the enforcement of any law, the passage of which did not conform to section 2 or this section.\n##### (f) State of review\nIn any judicial action brought pursuant to subsection (e), the standard of review shall be de novo.",
      "versionDate": "2025-01-09",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-10",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4324",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "One Subject at a Time Act",
      "type": "HR"
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
            "updateDate": "2025-03-03T16:36:46Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-03-03T16:36:46Z"
          },
          {
            "name": "Government liability",
            "updateDate": "2025-03-03T16:36:46Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-03-03T16:36:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-28T14:55:48Z"
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
          "measure-id": "id119s59",
          "measure-number": "59",
          "measure-type": "s",
          "orig-publish-date": "2025-01-09",
          "originChamber": "SENATE",
          "update-date": "2025-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s59v00",
            "update-date": "2025-03-11"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>One Subject at a Time Act</strong></p><p>This bill requires each bill or joint resolution to include no more than one subject and the subject to be clearly and descriptively expressed in the measure's title.</p><p>Further, an appropriations bill may not contain any general legislation or change to existing law that is not germane to the subject of such bill.</p><p>The bill voids an entire law or joint resolution that has a title which addresses two or more unrelated subjects.\u00a0For noncompliant provisions of a law or joint resolution, the bill voids the specific noncompliant provisions.\u00a0For example, this includes appropriation provisions that are outside of\u00a0the relevant subcommittee's jurisdiction.\u00a0</p><p>Additionally, a person (individual or entity) who is aggrieved by the enforcement, or the attempted enforcement, of a law that passed without complying with this bill's requirements may sue the United States for appropriate relief.</p>"
        },
        "title": "One Subject at a Time Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s59.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>One Subject at a Time Act</strong></p><p>This bill requires each bill or joint resolution to include no more than one subject and the subject to be clearly and descriptively expressed in the measure's title.</p><p>Further, an appropriations bill may not contain any general legislation or change to existing law that is not germane to the subject of such bill.</p><p>The bill voids an entire law or joint resolution that has a title which addresses two or more unrelated subjects.\u00a0For noncompliant provisions of a law or joint resolution, the bill voids the specific noncompliant provisions.\u00a0For example, this includes appropriation provisions that are outside of\u00a0the relevant subcommittee's jurisdiction.\u00a0</p><p>Additionally, a person (individual or entity) who is aggrieved by the enforcement, or the attempted enforcement, of a law that passed without complying with this bill's requirements may sue the United States for appropriate relief.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119s59"
    },
    "title": "One Subject at a Time Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>One Subject at a Time Act</strong></p><p>This bill requires each bill or joint resolution to include no more than one subject and the subject to be clearly and descriptively expressed in the measure's title.</p><p>Further, an appropriations bill may not contain any general legislation or change to existing law that is not germane to the subject of such bill.</p><p>The bill voids an entire law or joint resolution that has a title which addresses two or more unrelated subjects.\u00a0For noncompliant provisions of a law or joint resolution, the bill voids the specific noncompliant provisions.\u00a0For example, this includes appropriation provisions that are outside of\u00a0the relevant subcommittee's jurisdiction.\u00a0</p><p>Additionally, a person (individual or entity) who is aggrieved by the enforcement, or the attempted enforcement, of a law that passed without complying with this bill's requirements may sue the United States for appropriate relief.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119s59"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s59is.xml"
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
      "title": "One Subject at a Time Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T01:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "One Subject at a Time Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T01:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to end the practice of including more than one subject in a single bill by requiring that each bill enacted by Congress be limited to only one subject, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T01:03:23Z"
    }
  ]
}
```
