# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6079?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6079
- Title: Social Security Guarantee Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6079
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2026-04-01T21:42:52Z
- Update date including text: 2026-04-01T21:42:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6079",
    "number": "6079",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "B001309",
        "district": "2",
        "firstName": "Tim",
        "fullName": "Rep. Burchett, Tim [R-TN-2]",
        "lastName": "Burchett",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Social Security Guarantee Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-01T21:42:52Z",
    "updateDateIncludingText": "2026-04-01T21:42:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
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
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T15:03:30Z",
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
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "NJ"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6079ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6079\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Mr. Burchett introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo guarantee the right of individuals to receive Social Security benefits under title II of the Social Security Act in full with an accurate annual cost-of-living adjustment.\n#### 1. Short title\nThis Act may be cited as the Social Security Guarantee Act of 2025 .\n#### 2. Guarantee of full Social Security benefits with accurate annual cost-of-living adjustment\n##### (a) In General\nOn a date not later than 90 days after the date of the enactment of this Act, the Secretary of the Treasury shall issue a benefit guarantee certificate to each individual who is determined by the Commissioner of Social Security as of such date to be entitled to benefits under title II of the Social Security Act ( 42 U.S.C. 401 et seq. ). The Secretary shall also issue such a certificate to any individual on the date such individual is determined thereafter to be entitled to benefits under such title.\n##### (b) Benefit Guarantee Certificate\nThe benefit guarantee certificate issued pursuant to subsection (a) shall represent a legally enforceable guarantee\u2014\n**(1)**\nof the monthly amount of benefits to which the individual is entitled under title II of the Social Security Act (as in effect on the date of the issuance of the certificate); and\n**(2)**\nthat the benefits will be adjusted\u2014\n**(A)**\nnot less frequently than annually on the basis of an accurate determination of the increase in the cost-of-living of the individual; and\n**(B)**\nin accordance with such title (as so in effect), to reflect any future changes in the eligibility status of the individual under such title.\n##### (c) Entitlement\nAny certificate issued under the authority of this section constitutes budget authority in advance of appropriations Acts and represents the obligation of the Federal Government to provide for the payment to the individual to whom the certificate is issued benefits under title II of the Social Security Act ( 42 U.S.C. 401 et seq. ) in the amounts set forth in the certificate and adjusted thereafter as described in subsection (b)(2).",
      "versionDate": "2025-11-18",
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
        "name": "Social Welfare",
        "updateDate": "2025-12-01T16:24:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-18",
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
          "measure-id": "id119hr6079",
          "measure-number": "6079",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-18",
          "originChamber": "HOUSE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6079v00",
            "update-date": "2026-04-01"
          },
          "action-date": "2025-11-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Social Security Guarantee Act of 2025</strong></p><p>This bill requires the Department of the Treasury to issue certificates to Social Security beneficiaries that guarantee them the full monthly benefit amount to which they are entitled and at least an annual cost-of-living increase to their benefits. It also provides additional mandatory funding for those benefits.</p><p>Currently, Social Security beneficiaries are entitled to their benefits, but benefits are primarily funded through a payroll tax (including assets derived from the tax held in reserve). Actuarial projections reported by the Social Security Board of Trustees indicate that in 2035 there will be insufficient tax revenue and reserved assets to cover the full amount of benefit payments.</p>"
        },
        "title": "Social Security Guarantee Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6079.xml",
    "summary": {
      "actionDate": "2025-11-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Social Security Guarantee Act of 2025</strong></p><p>This bill requires the Department of the Treasury to issue certificates to Social Security beneficiaries that guarantee them the full monthly benefit amount to which they are entitled and at least an annual cost-of-living increase to their benefits. It also provides additional mandatory funding for those benefits.</p><p>Currently, Social Security beneficiaries are entitled to their benefits, but benefits are primarily funded through a payroll tax (including assets derived from the tax held in reserve). Actuarial projections reported by the Social Security Board of Trustees indicate that in 2035 there will be insufficient tax revenue and reserved assets to cover the full amount of benefit payments.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hr6079"
    },
    "title": "Social Security Guarantee Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-11-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Social Security Guarantee Act of 2025</strong></p><p>This bill requires the Department of the Treasury to issue certificates to Social Security beneficiaries that guarantee them the full monthly benefit amount to which they are entitled and at least an annual cost-of-living increase to their benefits. It also provides additional mandatory funding for those benefits.</p><p>Currently, Social Security beneficiaries are entitled to their benefits, but benefits are primarily funded through a payroll tax (including assets derived from the tax held in reserve). Actuarial projections reported by the Social Security Board of Trustees indicate that in 2035 there will be insufficient tax revenue and reserved assets to cover the full amount of benefit payments.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hr6079"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6079ih.xml"
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
      "title": "Social Security Guarantee Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-29T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Social Security Guarantee Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-29T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To guarantee the right of individuals to receive Social Security benefits under title II of the Social Security Act in full with an accurate annual cost-of-living adjustment.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-29T05:48:38Z"
    }
  ]
}
```
