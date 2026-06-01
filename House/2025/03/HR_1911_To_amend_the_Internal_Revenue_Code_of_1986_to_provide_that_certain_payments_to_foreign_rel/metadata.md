# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1911?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1911
- Title: To amend the Internal Revenue Code of 1986 to provide that certain payments to foreign related parties subject to sufficient foreign tax are not treated as base erosion payments.
- Congress: 119
- Bill type: HR
- Bill number: 1911
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-05-08T14:05:51Z
- Update date including text: 2025-05-08T14:05:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1911",
    "number": "1911",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001136",
        "district": "3",
        "firstName": "Herbert",
        "fullName": "Rep. Conaway, Herbert [D-NJ-3]",
        "lastName": "Conaway",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to provide that certain payments to foreign related parties subject to sufficient foreign tax are not treated as base erosion payments.",
    "type": "HR",
    "updateDate": "2025-05-08T14:05:51Z",
    "updateDateIncludingText": "2025-05-08T14:05:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
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
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:10:45Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1911ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1911\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Conaway (for himself, Mr. Suozzi , and Mr. Van Drew ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide that certain payments to foreign related parties subject to sufficient foreign tax are not treated as base erosion payments.\n#### 1. Certain payments to foreign related parties subject to sufficient foreign tax not treated as base erosion payments\n##### (a) In general\nSection 59A of the Internal Revenue Code of 1986 is amended by redesignating subsection (i) as subsection (j) and by inserting after subsection (h) the following new subsection:\n(i) Certain payments to foreign related parties subject to sufficient foreign tax not treated as base erosion payments (1) In general An amount shall not be treated as a base erosion payment if the taxpayer establishes to the satisfaction of the Secretary that\u2014 (A) the foreign person to whom such amount is paid or incurred is subject to an effective rate of foreign income tax of at least 15 percent, and (B) such amount is subject to an effective rate of foreign income tax of at least 15 percent. (2) Determination of effective rate on basis of applicable financial statements Except as otherwise provided by the Secretary, the effective rate of foreign income tax may be established on the basis of applicable financial statements (as defined in section 451(b)(3)) with appropriate adjustments (as determined by the Secretary) for excluded dividends, net tax expense, excluded equity gain or loss, included revaluation method gain or loss, gain or loss from intragroup transfers of assets and liabilities, asymmetric foreign currency gains or losses, bribes, illegal payments, large penalties, prior period errors and changes in accounting methods, accrued pension expenses, and such other items as the Secretary may provide. (3) Foreign income tax For purposes of this subsection, the term \u201cforeign income taxes\u201d means any income, war profits, or excess profits taxes paid or accrued to any foreign country or to any possession of the United States. .\n##### (b) Regulations\nSection 59A(j) of such Code, as redesignated by subsection (a), is amended by striking and at the end of paragraph (1), by striking the period at the end of paragraph (2) and inserting , and , and by adding at the end the following new paragraph:\n(3) for the application of subsection (i), including\u2014 (A) procedures for determining the effective rate of foreign income tax, and (B) rules to the prevent tax avoidance or abuse, including rules for recharacterizing a transaction or series of transactions among related parties. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-03-06",
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
        "updateDate": "2025-05-08T14:05:51Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1911ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide that certain payments to foreign related parties subject to sufficient foreign tax are not treated as base erosion payments.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:18:29Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to provide that certain payments to foreign related parties subject to sufficient foreign tax are not treated as base erosion payments.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-07T09:07:05Z"
    }
  ]
}
```
