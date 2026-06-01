# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3155?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3155
- Title: COACH Act
- Congress: 119
- Bill type: S
- Bill number: 3155
- Origin chamber: Senate
- Introduced date: 2025-11-07
- Update date: 2026-04-21T18:02:24Z
- Update date including text: 2026-04-21T18:02:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in Senate
- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- Latest action: 2025-11-07: Introduced in Senate

## Actions

- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3155",
    "number": "3155",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "COACH Act",
    "type": "S",
    "updateDate": "2026-04-21T18:02:24Z",
    "updateDateIncludingText": "2026-04-21T18:02:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T18:23:57Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3155is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3155\nIN THE SENATE OF THE UNITED STATES\nNovember 7, 2025 Ms. Klobuchar (for herself and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo amend the Small Business Act to require the Administrator of the Small Business Administration to publish or update a resource guide for small business concerns operating as child care providers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Convening Operations Assistance for Childcare Heroes Act or the COACH Act .\n#### 2. Child care resource guide\nThe Small Business Act ( 15 U.S.C. 631 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 49 as section 50; and\n**(2)**\nby inserting after section 48 the following new section:\n49. Child care resource guide (a) In general Not later than 1 year after the date of enactment of the COACH Act, and not less frequently than every 5 years thereafter, the Administrator shall publish or update a resource guide, applicable to various business models as determined by the Administrator, for small business concerns operating as child care providers. (b) Guidance on small business concern matters The resource guide required under subsection (a) shall include guidance for small business concerns operating as child care providers related to\u2014 (1) operations (including marketing and management planning); (2) finances (including financial planning, financing, payroll, and insurance); (3) compliance with relevant laws (including the Internal Revenue Code of 1986 and this Act); (4) training and safety (including equipment and materials); (5) quality (including eligibility for funding as an eligible child care provider under the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9857 et seq. )); and (6) any other matters the Administrator determines appropriate. (c) Consultation required Before publishing or updating the resource guide required under subsection (a), the Administrator shall consult with\u2014 (1) the Secretary of Health and Human Services; (2) representatives from lead agencies designated under section 658D(a) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858b(a) ); (3) representatives from local or regional child care resource and referral organizations described in section 658E(c)(3)(B)(iii)(I) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858c(c)(3)(B)(iii)(I) ); and (4) any other relevant entities, as determined by the Administrator. (d) Publication and dissemination required (1) Publication The Administrator shall publish the resource guide required under subsection (a) on a publicly accessible website of the Administration\u2014 (A) in English; and (B) in the 10 most commonly spoken languages in the United States, other than English, which shall include Mandarin, Cantonese, Japanese, and Korean. (2) Distribution (A) Administrator The Administrator shall distribute the resource guide required under subsection (a) to offices within the Administration, including district offices, and to persons and entities consulted under subsection (c). (B) Other entities Women\u2019s business centers (as described in section 29), small business development centers, chapters of the Service Corps of Retired Executives (established under section 8(b)(1)(B)), and Veteran Business Outreach Centers (as described in section 32) shall distribute to small business concerns operating as child care providers, sole proprietors operating as child care providers, and child care providers that have limited administrative capacity, as determined by the Administrator\u2014 (i) the resource guide required under subsection (a); and (ii) other available resources that the Administrator determines to be relevant. .",
      "versionDate": "2025-11-07",
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
        "actionDate": "2025-11-13",
        "text": "Referred to the House Committee on Small Business."
      },
      "number": "6045",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "COACH Act",
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
        "name": "Commerce",
        "updateDate": "2025-11-19T14:59:35Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3155is.xml"
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
      "title": "COACH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T12:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "COACH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Convening Operations Assistance for Childcare Heroes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Small Business Act to require the Administrator of the Small Business Administration to publish or update a resource guide for small business concerns operating as child care providers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T12:03:32Z"
    }
  ]
}
```
