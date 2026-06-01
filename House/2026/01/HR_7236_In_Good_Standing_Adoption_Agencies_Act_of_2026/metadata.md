# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7236?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7236
- Title: In Good Standing Adoption Agencies Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7236
- Origin chamber: House
- Introduced date: 2026-01-23
- Update date: 2026-02-12T15:35:39Z
- Update date including text: 2026-02-12T15:35:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-23: Introduced in House
- 2026-01-23 - IntroReferral: Introduced in House
- 2026-01-23 - IntroReferral: Introduced in House
- 2026-01-23 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-01-23: Introduced in House

## Actions

- 2026-01-23 - IntroReferral: Introduced in House
- 2026-01-23 - IntroReferral: Introduced in House
- 2026-01-23 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-23",
    "latestAction": {
      "actionDate": "2026-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7236",
    "number": "7236",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "S001229",
        "district": "6",
        "firstName": "Jefferson",
        "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
        "lastName": "Shreve",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "In Good Standing Adoption Agencies Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-12T15:35:39Z",
    "updateDateIncludingText": "2026-02-12T15:35:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-23",
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
      "actionDate": "2026-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-23",
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
          "date": "2026-01-23T15:00:05Z",
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
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7236ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7236\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2026 Mr. Shreve introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo provide for the Secretary of Health and Human Services to maintain a national list of licensed private child placement agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the In Good Standing Adoption Agencies Act of 2026 .\n#### 2. National list of licensed child placement agencies\n##### (a) In general\nSection 474 of the Social Security Act ( 42 U.S.C. 674 ) is amended by adding at the end the following:\n(h) National list of licensed child placement agencies (1) State reporting (A) In general Not later than January 1 of each fiscal year, a State with a plan approved under this part for the fiscal year shall submit to the Secretary a list of private child placement agencies that, as of the end of the preceding fiscal year, were licensed or accredited by, and in good standing with, the State and exempt from Federal income tax by reason of section 501(c)(3) of the Internal Revenue Code of 1986. (B) Child placement agency In subparagraph (A), the term child placement agency means an agency that places children in prospective adoptive homes. (2) National list The Secretary, through the United States Children\u2019s Bureau, shall compile and maintain a publicly available list consisting of each list most recently submitted by a State under paragraph (1). (3) Annual reports to Congress Not later than the 2nd December 31 after the date of the enactment of this subsection, and annually thereafter, the Secretary shall submit to the Congress a written report that contains the list maintained under paragraph (2) and identifies any child placement agency that is licensed by a State and is not on the list, and a specification of any disciplinary actions that a State has taken against a private child placement agency. .\n##### (b) Loss of eligibility for adoption and legal guardianship incentive payments for failure of State To comply with list submission requirement\nSection 473A(b) of such Act ( 42 U.S.C. 673b(b) ) is amended\u2014\n**(1)**\nby striking and at the end of paragraph (3);\n**(2)**\nby striking the period at the end of paragraph (4) and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(5) the State has complied with section 474(h)(1) with respect to the preceding fiscal year. .",
      "versionDate": "2026-01-23",
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
        "actionDate": "2025-05-06",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1630",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "MOMS Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-07",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3235",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "MOMS Act",
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
        "name": "Families",
        "updateDate": "2026-02-12T15:35:39Z"
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
      "date": "2026-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7236ih.xml"
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
      "title": "In Good Standing Adoption Agencies Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "In Good Standing Adoption Agencies Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the Secretary of Health and Human Services to maintain a national list of licensed private child placement agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-06T03:18:26Z"
    }
  ]
}
```
