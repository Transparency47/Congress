# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1852?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1852
- Title: IHE Nonprofit Clarity Act
- Congress: 119
- Bill type: HR
- Bill number: 1852
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-02-17T20:11:07Z
- Update date including text: 2026-02-17T20:11:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1852",
    "number": "1852",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
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
    "title": "IHE Nonprofit Clarity Act",
    "type": "HR",
    "updateDate": "2026-02-17T20:11:07Z",
    "updateDateIncludingText": "2026-02-17T20:11:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:04:10Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1852ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1852\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to require that any institution of higher education that is a nonprofit organization under section 501(c)(3) of the Internal Revenue Code be deemed a nonprofit institution of higher education for purposes of such Act.\n#### 1. Short title\nThis Act may be cited as the IHE Nonprofit Clarity Act .\n#### 2. Definition of nonprofit institution of higher education\nSection 103(13) of the Higher Education Act of 1965 ( 20 U.S.C. 1003(13) ) is amended by inserting at the end the following: Notwithstanding the preceding sentence, in the case of an institution of higher education that is an organization described in section 501(c)(3) of the Internal Revenue Code and exempt from taxation under section 501(a) of such Code, such institution of higher education shall be deemed to be a nonprofit institution of higher education for purposes of this Act. .",
      "versionDate": "2025-03-05",
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
            "name": "Higher education",
            "updateDate": "2026-02-17T20:11:02Z"
          },
          {
            "name": "Tax-exempt organizations",
            "updateDate": "2026-02-17T20:11:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-21T16:57:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
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
          "measure-id": "id119hr1852",
          "measure-number": "1852",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-05",
          "originChamber": "HOUSE",
          "update-date": "2025-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1852v00",
            "update-date": "2025-05-13"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>IHE Nonprofit Clarity Act</strong></p><p>This bill specifies that an institution of higher education (IHE) that is recognized as a tax-exempt nonprofit organization under Section 501(c)(3) of the Internal Revenue Code of 1986 must also be deemed as a nonprofit\u00a0IHE for purposes of the Higher Education Act of 1965. Thus, if the Internal Revenue Service recognizes an IHE as a tax-exempt nonprofit organization,\u00a0then the Department of Education must also recognize the\u00a0IHE as a nonprofit IHE.</p>"
        },
        "title": "IHE Nonprofit Clarity Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1852.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>IHE Nonprofit Clarity Act</strong></p><p>This bill specifies that an institution of higher education (IHE) that is recognized as a tax-exempt nonprofit organization under Section 501(c)(3) of the Internal Revenue Code of 1986 must also be deemed as a nonprofit\u00a0IHE for purposes of the Higher Education Act of 1965. Thus, if the Internal Revenue Service recognizes an IHE as a tax-exempt nonprofit organization,\u00a0then the Department of Education must also recognize the\u00a0IHE as a nonprofit IHE.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119hr1852"
    },
    "title": "IHE Nonprofit Clarity Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>IHE Nonprofit Clarity Act</strong></p><p>This bill specifies that an institution of higher education (IHE) that is recognized as a tax-exempt nonprofit organization under Section 501(c)(3) of the Internal Revenue Code of 1986 must also be deemed as a nonprofit\u00a0IHE for purposes of the Higher Education Act of 1965. Thus, if the Internal Revenue Service recognizes an IHE as a tax-exempt nonprofit organization,\u00a0then the Department of Education must also recognize the\u00a0IHE as a nonprofit IHE.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119hr1852"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1852ih.xml"
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
      "title": "IHE Nonprofit Clarity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "IHE Nonprofit Clarity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to require that any institution of higher education that is a nonprofit organization under section 501(c)(3) of the Internal Revenue Code be deemed a nonprofit institution of higher education for purposes of such Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:06Z"
    }
  ]
}
```
