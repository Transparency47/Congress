# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8143?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8143
- Title: Ensuring Access to Lower-Cost Medicines for Seniors Act of 2026.
- Congress: 119
- Bill type: HR
- Bill number: 8143
- Origin chamber: House
- Introduced date: 2026-03-27
- Update date: 2026-04-13T14:34:23Z
- Update date including text: 2026-04-13T14:34:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-27: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-27 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-27: Introduced in House

## Actions

- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-27 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-27",
    "latestAction": {
      "actionDate": "2026-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8143",
    "number": "8143",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001163",
        "district": "7",
        "firstName": "Doris",
        "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
        "lastName": "Matsui",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Ensuring Access to Lower-Cost Medicines for Seniors Act of 2026.",
    "type": "HR",
    "updateDate": "2026-04-13T14:34:23Z",
    "updateDateIncludingText": "2026-04-13T14:34:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-27",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-27",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-27",
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
          "date": "2026-03-28T01:31:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-28T01:31:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "IA"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8143ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8143\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2026 Ms. Matsui (for herself, Mrs. Miller-Meeks , and Mr. Auchincloss ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to require PDP sponsors of a prescription drug plan under part D of the Medicare program that use a formulary to include certain generic drugs and biosimilar biological products on such formulary, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ensuring Access to Lower-Cost Medicines for Seniors Act of 2026.\n#### 2. Requirements for pdp sponsors of prescription drug plans under part d of the medicare program that use formularies\nSection 1860D\u20134(b)(3) of the Social Security Act ( 42 U.S.C. 1395w\u2013104(b)(3) ) is amended by adding at the end the following new subparagraph:\n(J) Required inclusion of certain generic drugs and biosimilar biological products (i) In general With respect to a plan year beginning on or after January 1, 2027, the formulary shall include in a preferred position relative to the reference drug\u2014 (I) each covered generic drug for which the wholesale acquisition cost is less than the wholesale acquisition cost of the reference drug of such covered generic drug; and (II) at least two covered bio-similar biological products for which the wholesale acquisition cost is less than the wholesale acquisition cost of the reference biological product of such covered biosimilar biological product. (ii) Prohibition on certain lim-its on access The PDP sponsor offering the prescription drug plan may not impose limits on access to a covered generic drug required to be included on the formulary under clause (i)(I) or a covered biosimilar biological product required to be included on the formulary under clause (i)(II), including through utilization management techniques such as prior authorization, or step therapy, that are more restrictive than any such limits imposed on access to the reference drug of such covered generic drug or reference biological product of such covered biosimilar biological product, respectively, or that otherwise have the effect of limiting the availability to enrollees of such covered generic drug or covered biosimilar biological product relative to such reference drug or reference biological product over such covered generic drug or covered biosimilar biological product, respectively. (iii) Definitions In this subparagraph and subparagraph (J): (I) Covered biosimilar biological product The term covered biosimilar biological product means a covered part D drug that is a biosimilar biological product (as defined in section 1847A(c)(6)(H)). (II) Covered generic drug The term covered generic drug means a covered part D drug that is a drug described in section 1860D\u20132(e)(1)(A) and approved under section 505(j) of the Federal Food, Drug, and Cosmetic Act. (III) Preferred position The term preferred position means a product is placed on a more favorable formulary tier and has lower patient out-of-pocket costs than the corresponding reference drug or reference biological product. (IV) Reference biological product The term reference biological product has the meaning given such term in section 1847A(c)(6)(I). (V) Reference drug The term reference drug means, with respect to a covered generic drug, the listed drug (as described in clause (i) of section 505(j)(2)(A) of the Federal Food, Drug, and Cosmetic Act) that is referred to in the abbreviated application for such covered generic drug under such section. (VI) Wholesale acquisition cost The term wholesale acquisition cost has the meaning given such term in section 1847A(c)(6)(B). .",
      "versionDate": "2026-03-27",
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
        "name": "Health",
        "updateDate": "2026-04-13T14:34:23Z"
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
      "date": "2026-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8143ih.xml"
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
      "title": "Ensuring Access to Lower-Cost Medicines for Seniors Act of 2026.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ensuring Access to Lower-Cost Medicines for Seniors Act of 2026.",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to require PDP sponsors of a prescription drug plan under part D of the Medicare program that use a formulary to include certain generic drugs and biosimilar biological products on such formulary, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:23Z"
    }
  ]
}
```
