# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/320?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/320
- Title: Make Marriage Great Again Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 320
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-08-12T16:45:34Z
- Update date including text: 2025-08-12T16:45:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Ways and Means.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/320",
    "number": "320",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Make Marriage Great Again Act of 2025",
    "type": "HR",
    "updateDate": "2025-08-12T16:45:34Z",
    "updateDateIncludingText": "2025-08-12T16:45:34Z"
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
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
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
          "date": "2025-01-09T14:38:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr320ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 320\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Steube introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to eliminate the marriage penalty in the income tax rate brackets.\n#### 1. Short title\nThis Act may be cited as the Make Marriage Great Again Act of 2025 .\n#### 2. Elimination of marriage penalty in income tax rate brackets\n##### (a) In general\nSection 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(k) Elimination of marriage penalty In the case of any taxable year beginning after December 31, 2024\u2014 (1) in lieu of the table which would otherwise apply under subsection (a) or (j)(2)(A) for such taxable year, the table which applies under subsection (c) or (j)(2)(C), respectively, shall apply determined by substituting for each dollar amount contained therein a dollar amount which is twice such dollar amount (as otherwise in effect for such taxable year), (2) subsection (c) shall be applied without regard to the phrase who is not a married individual (as defined in section 7703) , and (3) subsections (d) and (j)(2)(D) shall not apply. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2024.",
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
        "name": "Taxation",
        "updateDate": "2025-02-14T16:48:32Z"
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
          "measure-id": "id119hr320",
          "measure-number": "320",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-08-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr320v00",
            "update-date": "2025-08-12"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Make Marriage Great Again Act of 2025</strong></p><p>This bill modifies the federal income tax rate brackets for married individuals filing joint federal income tax returns so that they are twice the amount of the federal income tax rate brackets for unmarried individuals filing federal income tax returns (thus eliminating the tax effect commonly known as the marriage penalty). Further, the bill eliminates the federal income tax rate brackets for married individuals filing separate federal income tax returns for tax years beginning after December 31, 2024. (An income tax rate bracket is a range of income that is taxed at a specific percentage to determine an individual\u2019s income tax liability.)</p><p>Thus, under the bill, the federal income tax rate bracket amounts that apply to a married individual are either (1) the individual federal income tax rate bracket amounts if such individual files an individual federal income tax return, or (2) twice such amounts if the individual files a joint federal income tax return with their spouse.</p>"
        },
        "title": "Make Marriage Great Again Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr320.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Make Marriage Great Again Act of 2025</strong></p><p>This bill modifies the federal income tax rate brackets for married individuals filing joint federal income tax returns so that they are twice the amount of the federal income tax rate brackets for unmarried individuals filing federal income tax returns (thus eliminating the tax effect commonly known as the marriage penalty). Further, the bill eliminates the federal income tax rate brackets for married individuals filing separate federal income tax returns for tax years beginning after December 31, 2024. (An income tax rate bracket is a range of income that is taxed at a specific percentage to determine an individual\u2019s income tax liability.)</p><p>Thus, under the bill, the federal income tax rate bracket amounts that apply to a married individual are either (1) the individual federal income tax rate bracket amounts if such individual files an individual federal income tax return, or (2) twice such amounts if the individual files a joint federal income tax return with their spouse.</p>",
      "updateDate": "2025-08-12",
      "versionCode": "id119hr320"
    },
    "title": "Make Marriage Great Again Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Make Marriage Great Again Act of 2025</strong></p><p>This bill modifies the federal income tax rate brackets for married individuals filing joint federal income tax returns so that they are twice the amount of the federal income tax rate brackets for unmarried individuals filing federal income tax returns (thus eliminating the tax effect commonly known as the marriage penalty). Further, the bill eliminates the federal income tax rate brackets for married individuals filing separate federal income tax returns for tax years beginning after December 31, 2024. (An income tax rate bracket is a range of income that is taxed at a specific percentage to determine an individual\u2019s income tax liability.)</p><p>Thus, under the bill, the federal income tax rate bracket amounts that apply to a married individual are either (1) the individual federal income tax rate bracket amounts if such individual files an individual federal income tax return, or (2) twice such amounts if the individual files a joint federal income tax return with their spouse.</p>",
      "updateDate": "2025-08-12",
      "versionCode": "id119hr320"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr320ih.xml"
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
      "title": "Make Marriage Great Again Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T09:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Make Marriage Great Again Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T09:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to eliminate the marriage penalty in the income tax rate brackets.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T09:03:22Z"
    }
  ]
}
```
