# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5736?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5736
- Title: PAVE Act
- Congress: 119
- Bill type: HR
- Bill number: 5736
- Origin chamber: House
- Introduced date: 2025-10-10
- Update date: 2026-05-08T08:06:57Z
- Update date including text: 2026-05-08T08:06:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-10: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-10-10: Introduced in House

## Actions

- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-10",
    "latestAction": {
      "actionDate": "2025-10-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5736",
    "number": "5736",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000568",
        "district": "9",
        "firstName": "H.",
        "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
        "lastName": "Griffith",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "PAVE Act",
    "type": "HR",
    "updateDate": "2026-05-08T08:06:57Z",
    "updateDateIncludingText": "2026-05-08T08:06:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-10",
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
      "actionDate": "2025-10-10",
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
      "actionDate": "2025-10-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-10",
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
          "date": "2025-10-10T16:32:45Z",
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
          "date": "2025-10-10T16:32:40Z",
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
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "CA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "IA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "WA"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "WA"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "MO"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "MA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "VA"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5736ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5736\nIN THE HOUSE OF REPRESENTATIVES\nOctober 10, 2025 Mr. Griffith (for himself, Mr. Bera , Mrs. Miller-Meeks , Ms. Schrier , Ms. DelBene , Mr. Onder , and Mr. Auchincloss ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to include penicillin allergy verification and evaluation as part of the initial preventive physical examination under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Penicillin Allergy Verification and Evaluation Act or the PAVE Act .\n#### 2. Findings\nCongress makes the following:\n**(1)**\nOn September 28, 1928, Alexander Fleming, a Scottish bacteriologist, discovered penicillin, forever changing healthcare by identifying an effective way to treat a wide range of infections which opened the door for numerous successful medical treatments.\n**(2)**\nMillions of patients believe they are allergic to penicillin, but information cited by the Centers for Disease Control and Prevention and recent medical journal articles in the Journal of the American Medical Association and the Journal of Allergy and Clinical Immunology, shows that more than 90 percent of patients who have a self-reported penicillin allergy in their electronic medical record can safely take penicillin after verification testing.\n**(3)**\nA 2020 medical research review found, penicillin allergy is estimated to affect approximately 10 percent of the population, and 15 percent of hospitalized patients are labeled with a penicillin allergy.\n**(4)**\nPenicillin allergy label is associated with poor patient outcomes including increased hospital length of stay, increased perioperative infections, and overall increased mortality according to the New England Journal of Medicine.\n**(5)**\nA 2018 paper in the Journal of Allergy and Clinical Immunology indicates that penicillin allergy evaluation by any means has been shown to be a cost-saving intervention.\n**(6)**\nDelabeling penicillin allergy is an important component of antibiotic stewardship and is endorsed by many professional organizations and public health bodies, including the American Academy of Allergy, Asthma & Immunology.\n**(7)**\nA 2023 study of adults 65 and older with a penicillin allergy label published in the Annals of Allergy, Asthma & Immunology found that 97 percent were disproved after verification testing.\n#### 3. Penicillin allergy verification and evaluation for seniors\n##### (a) Initial preventive physical examination\nSection 1861(ww) of the Social Security Act ( 42 U.S.C. 1395x(ww) ) is amended\u2014\n**(1)**\nIn paragraph (1)\u2014\n**(A)**\nby inserting penicillin allergy verification and evaluation (as defined in paragraph (5)), after (as defined in paragraph (4)), ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby redesignating subparagraph (O) as subparagraph (P); and\n**(B)**\nby inserting after subparagraph (N) the following new subparagraph:\n(O) Penicillin allergy verification and evaluation. ; and\n**(3)**\nby adding at the end the following new paragraph:\n(5) For purposes of paragraph (1), the term penicillin allergy verification and evaluation means\u2014 (A) identification of individuals reporting a history of penicillin allergy; (B) consideration of whether the reported reaction history is consistent with an allergy or hypersensitivity reaction or can be reevaluated; (C) the provision of information on the adverse individual and public health impact of a penicillin allergy label; and (D) a referral to an allergy or immunology specialist, as appropriate. .\n##### (b) Annual wellness visit\nSection 1861(hhh)(2) of the Social Security Act ( 42 U.S.C. 1395x(hhh)(2) ) is amended\u2014\n**(1)**\nby redesignating subparagraph (I) as subparagraph (J); and\n**(2)**\nby inserting after subparagraph (H) the following new subparagraph:\n(I) Penicillin allergy verification and evaluation (as defined in subsection (ww)(5)). .\n##### (c) Rule of construction\nNothing in the amendments made by subsection (a) or (b) shall be construed to prohibit separate payment for structured penicillin allergy validation and evaluation services furnished to an individual on the same day as an initial preventive physical examination or an annual wellness visit.\n##### (d) Effective date\nThe amendments made by this section shall apply to examinations and visits furnished on or after January 1, 2027.",
      "versionDate": "2025-10-10",
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
        "updateDate": "2025-12-09T17:30:03Z"
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
      "date": "2025-10-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5736ih.xml"
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
      "title": "PAVE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-18T03:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PAVE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-18T03:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Penicillin Allergy Verification and Evaluation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-18T03:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to include penicillin allergy verification and evaluation as part of the initial preventive physical examination under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-18T03:18:16Z"
    }
  ]
}
```
