# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/653?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/653
- Title: A bill to amend the Internal Revenue Code of 1986 to treat membership in a health care sharing ministry as a medical expense, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 653
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2026-01-10T07:25:22Z
- Update date including text: 2026-01-10T07:25:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/653",
    "number": "653",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "A bill to amend the Internal Revenue Code of 1986 to treat membership in a health care sharing ministry as a medical expense, and for other purposes.",
    "type": "S",
    "updateDate": "2026-01-10T07:25:22Z",
    "updateDateIncludingText": "2026-01-10T07:25:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-20",
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
          "date": "2025-02-20T18:13:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s653is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 653\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Budd introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to treat membership in a health care sharing ministry as a medical expense, and for other purposes.\n#### 1. Treatment of health care sharing ministries as a medical expense and not as insurance\n##### (a) Treatment as a medical expense\nSection 213(d)(1) of the Internal Revenue Code of 1986 is amended by striking or at the end of subparagraph (C), by striking the period at the end of subparagraph (D) and inserting , or , and by adding at the end the following new subparagraph:\n(E) for membership in a health care sharing ministry (as defined in section 5000A(d)(2)(B)(ii) without regard to subclause (IV) thereof), including\u2014 (i) the sharing of medical expenses with respect to such ministry, and (ii) the payment of administrative fees of such ministry. .\n##### (b) Health care sharing ministry not treated as a health plan or insurance\n**(1) In general**\nChapter 79 of the Internal Revenue Code of 1986 is amended by inserting after section 7702B the following new section:\n7702C. Treatment of health care sharing ministries For purposes of this title, a health care sharing ministry (as defined in section 5000A(d)(2)(B)(ii) without regard to subclause (IV) thereof) shall not be treated as a health plan or as insurance. .\n**(2) Clerical amendment**\nThe table of sections for chapter 79 of such Code is amended by inserting after the item relating to section 7702B the following new item:\nSec. 7702C. Treatment of health care sharing ministries. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-02-20",
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
        "actionDate": "2025-03-11",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2062",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To amend the Internal Revenue Code of 1986 to treat membership in a health care sharing ministry as a medical expense, and for other purposes.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-05-06T14:23:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-20",
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
          "measure-id": "id119s653",
          "measure-number": "653",
          "measure-type": "s",
          "orig-publish-date": "2025-02-20",
          "originChamber": "SENATE",
          "update-date": "2025-09-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s653v00",
            "update-date": "2025-09-23"
          },
          "action-date": "2025-02-20",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill provides that amounts paid for membership in a health care sharing ministry, including amounts paid for the sharing of medical expenses and administrative fees, are a tax-deductible medical expense. (Health care sharing ministries are faith-based organizations with members who share a common set of ethical or religious beliefs and who contribute regular payments to cover the medical expenses of other members.)</p>"
        },
        "title": "A bill to amend the Internal Revenue Code of 1986 to treat membership in a health care sharing ministry as a medical expense, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s653.xml",
    "summary": {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill provides that amounts paid for membership in a health care sharing ministry, including amounts paid for the sharing of medical expenses and administrative fees, are a tax-deductible medical expense. (Health care sharing ministries are faith-based organizations with members who share a common set of ethical or religious beliefs and who contribute regular payments to cover the medical expenses of other members.)</p>",
      "updateDate": "2025-09-23",
      "versionCode": "id119s653"
    },
    "title": "A bill to amend the Internal Revenue Code of 1986 to treat membership in a health care sharing ministry as a medical expense, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill provides that amounts paid for membership in a health care sharing ministry, including amounts paid for the sharing of medical expenses and administrative fees, are a tax-deductible medical expense. (Health care sharing ministries are faith-based organizations with members who share a common set of ethical or religious beliefs and who contribute regular payments to cover the medical expenses of other members.)</p>",
      "updateDate": "2025-09-23",
      "versionCode": "id119s653"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s653is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to treat membership in a health care sharing ministry as a medical expense, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:44Z"
    },
    {
      "title": "A bill to amend the Internal Revenue Code of 1986 to treat membership in a health care sharing ministry as a medical expense, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T11:56:29Z"
    }
  ]
}
```
