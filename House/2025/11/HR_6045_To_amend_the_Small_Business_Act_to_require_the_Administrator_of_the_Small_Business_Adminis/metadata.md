# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6045?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6045
- Title: COACH Act
- Congress: 119
- Bill type: HR
- Bill number: 6045
- Origin chamber: House
- Introduced date: 2025-11-13
- Update date: 2026-04-21T18:02:24Z
- Update date including text: 2026-04-21T18:02:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-13: Introduced in House
- 2025-11-13 - IntroReferral: Introduced in House
- 2025-11-13 - IntroReferral: Introduced in House
- 2025-11-13 - IntroReferral: Referred to the House Committee on Small Business.
- Latest action: 2025-11-13: Introduced in House

## Actions

- 2025-11-13 - IntroReferral: Introduced in House
- 2025-11-13 - IntroReferral: Introduced in House
- 2025-11-13 - IntroReferral: Referred to the House Committee on Small Business.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-13",
    "latestAction": {
      "actionDate": "2025-11-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6045",
    "number": "6045",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "COACH Act",
    "type": "HR",
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
      "actionCode": "H11100",
      "actionDate": "2025-11-13",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-13",
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
          "date": "2025-11-13T14:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-11-13",
      "state": "MN"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-11-13",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6045ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6045\nIN THE HOUSE OF REPRESENTATIVES\nNovember 13, 2025 Ms. Williams of Georgia (for herself, Mr. Stauber , and Ms. Chu ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo amend the Small Business Act to require the Administrator of the Small Business Administration to publish or update a resource guide for small business concerns operating as child care providers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Convening Operations Assistance for Childcare Heroes Act or the COACH Act .\n#### 2. Child care resource guide\nThe Small Business Act ( 15 U.S.C. 631 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 49 as section 50; and\n**(2)**\nby inserting after section 48 the following new section:\n49. Child care resource guide (a) In general Not later than 1 year after the date of the enactment of this section and not less frequently than every 5 years thereafter, the Administrator shall publish or update a resource guide, applicable to various business models as determined by the Administrator, for small business concerns operating as child care providers. (b) Guidance on small business concern matters The resource guide required under subsection (a) shall include guidance for such small business concerns related to\u2014 (1) operations (including marketing and management planning); (2) finances (including financial planning, financing, payroll, and insurance); (3) compliance with relevant laws (including the Internal Revenue Code of 1986 and this Act); (4) training and safety (including equipment and materials); (5) quality (including eligibility for funding under the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9857 et seq. ) as an eligible child care provider); and (6) any other matters the Administrator determines appropriate. (c) Consultation required Before publication or update of the resource guide required under subsection (a), the Administrator shall consult with the following: (1) The Secretary of Health and Human Services. (2) Representatives from lead agencies designated under section 658D of the Child Care and Development Block Grant Act of 1990. (3) Representatives from local or regional child care resource and referral organizations described in section 658E(c)(3)(B)(iii)(I) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858c(c)(3)(B)(iii)(I) ). (4) Any other relevant entities as determined by the Administrator. (d) Publication and dissemination required (1) Publication The Administrator shall publish the resource guide required under subsection (a) in English and in the 10 most commonly spoken languages, other than English, in the United States, which shall include Mandarin, Cantonese, Japanese, and Korean. The Administrator shall make each translation of the resource guide available on a publicly accessible website of the Administration. (2) Distribution (A) Administrator The Administrator shall distribute the resource guide required under subsection (a) to offices within the Administration, including district offices, and to the persons consulted under subsection (c). (B) Other entities Women\u2019s business centers (as described under section 29), small business development centers, chapters of the Service Corps of Retired Executives (established under section 8(b)(1)(B)), and Veteran Business Outreach Centers (as described under section 32) shall distribute to small business concerns operating as child care providers, sole proprietors operating as child care providers, and child care providers that have limited administrative capacity, as determined by the Administrator\u2014 (i) the resource guide required under subsection (a); and (ii) other resources available that the Administrator determines to be relevant. .",
      "versionDate": "2025-11-13",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-11-07",
        "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship."
      },
      "number": "3155",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "COACH Act",
      "type": "S"
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
        "updateDate": "2025-11-19T13:57:58Z"
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
      "date": "2025-11-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6045ih.xml"
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
      "title": "COACH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-18T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "COACH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-18T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Convening Operations Assistance for Childcare Heroes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-18T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Small Business Act to require the Administrator of the Small Business Administration to publish or update a resource guide for small business concerns operating as child care providers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-18T09:18:21Z"
    }
  ]
}
```
