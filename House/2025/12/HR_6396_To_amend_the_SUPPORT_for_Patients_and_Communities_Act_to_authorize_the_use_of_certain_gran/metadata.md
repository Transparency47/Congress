# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6396?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6396
- Title: Kid PROOF Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6396
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-05-22T08:08:35Z
- Update date including text: 2026-05-22T08:08:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-03 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-03 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6396",
    "number": "6396",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000307",
        "district": "10",
        "firstName": "John",
        "fullName": "Rep. James, John [R-MI-10]",
        "lastName": "James",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Kid PROOF Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:35Z",
    "updateDateIncludingText": "2026-05-22T08:08:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-03T15:03:45Z",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MI"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "FL"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "NY"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6396ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6396\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mr. James (for himself, Mrs. Dingell , Ms. Salazar , and Ms. Craig ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the SUPPORT for Patients and Communities Act to authorize the use of certain grants to prevent suicide or overdose by children, adolescents, and young adults, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Kid Providing Resources for Optimal Outcomes against Fatalities Act of 2025 or the Kid PROOF Act of 2025 .\n#### 2. Substance abuse treatment services for children, adolescents, and young adults\nSection 7102(c) of the SUPPORT for Patients and Communities Act (42 U.S.C. 290bb\u20137a(c)) is amended\u2014\n**(1)**\nin paragraph (1), by inserting and suicide before for children ;\n**(2)**\nin paragraph (2)(A)\u2014\n**(A)**\nin clause (vi), by striking or at the end;\n**(B)**\nin clause (vii), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(viii) a health care agency, health care site, facility, nonprofit entity, or provider treating children and adolescents (including any such agency, site, facility, or provider specializing in pediatrics and family medicine), a child and adolescent mental and behavioral health specialist, a children\u2019s hospital, a hospital emergency department, or a health facility or program operated by or in accordance with a contract with or grant from the Indian Health Service. ;\n**(3)**\nin paragraph (4)\u2014\n**(A)**\nin subparagraph (B), by striking or at the end;\n**(B)**\nin subparagraph (C), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(D) in the case of an eligible entity described in paragraph (2)(A)(viii), or in the case of an eligible entity that is an Indian tribe or a tribal organization, interventions, with the consent of parents or legal guardians of minors, to support the prevention of, treatment of, and recovery from suicide or overdose by children, adolescents, and young adults, by\u2014 (i) providing counseling to parents or legal guardians on best practices to prevent overdose and suicide; and (ii) furnishing supplies to parents or legal guardians to prevent the misuse of lethal means commonly used in overdose or suicide. ; and\n**(4)**\nin paragraph (9)\u2014\n**(A)**\nby striking 2019 through 2023 and inserting 2026 through 2030 ;\n**(B)**\nby striking There is authorized and inserting the following:\n(A) In general There is authorized ; and\n**(C)**\nby adding at the end the following:\n(B) Allocation of amounts Of the amount appropriated under subparagraph (A) for a fiscal year, not less than $2,000,000 shall be allocated to awarding grants pursuant to subparagraphs (A), (B), and (C) of paragraph (4). .",
      "versionDate": "2025-12-03",
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
        "updateDate": "2025-12-05T15:13:32Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6396ih.xml"
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
      "title": "Kid PROOF Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T09:23:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Kid PROOF Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T09:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Kid Providing Resources for Optimal Outcomes against Fatalities Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T09:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the SUPPORT for Patients and Communities Act to authorize the use of certain grants to prevent suicide or overdose by children, adolescents, and young adults, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T09:18:31Z"
    }
  ]
}
```
