# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2738?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2738
- Title: ESP, Paraprofessional, and Education Support Staff Family Leave Act
- Congress: 119
- Bill type: S
- Bill number: 2738
- Origin chamber: Senate
- Introduced date: 2025-09-09
- Update date: 2026-01-13T12:03:23Z
- Update date including text: 2026-01-13T12:03:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-09: Introduced in Senate
- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-09-09: Introduced in Senate

## Actions

- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-09",
    "latestAction": {
      "actionDate": "2025-09-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2738",
    "number": "2738",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "ESP, Paraprofessional, and Education Support Staff Family Leave Act",
    "type": "S",
    "updateDate": "2026-01-13T12:03:23Z",
    "updateDateIncludingText": "2026-01-13T12:03:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-09",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-09",
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
        "item": [
          {
            "date": "2025-09-09T18:43:59Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-09T18:43:59Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "IL"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "MA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "DE"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "NY"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "MN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NM"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NJ"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-01-05",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2738is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2738\nIN THE SENATE OF THE UNITED STATES\nSeptember 9, 2025 Ms. Duckworth (for herself, Mr. Durbin , Mr. Markey , Mr. Coons , Mrs. Gillibrand , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish eligibility requirements for covered educational employees under the Family and Medical Leave Act of 1993, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the ESP, Paraprofessional, and Education Support Staff Family Leave Act .\n#### 2. Eligibility for education support professionals and school support staff\nSection 101(2) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611(2) ) is amended by adding at the end the following:\n(F) Paraprofessionals and education support staff (i) Determination For purposes of determining whether a covered educational employee meets the hours of service requirement specified in subparagraph (A)(ii), the covered educational employee will be considered to meet the requirement if the employee has worked a number of hours equal to not less than 60 percent of the applicable total monthly hours expected for the employee\u2019s job description and duties, as assigned for the previous school year. (ii) File Each employer of a covered educational employee shall maintain on file with the Secretary (in accordance with such regulations as the Secretary may prescribe) information specifying the total monthly hours expected for the employee\u2019s job description and duties for each school year. (iii) Definitions In this subparagraph: (I) Covered educational employee The term covered educational employee means a paraprofessional or an education support staff member employed by an educational agency or institution. (II) Paraprofessional The term paraprofessional has the meaning given the term in section 8101(37) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801(37) ). (III) Education support staff The term education support staff member (also known as a classified school employee , education support professional , or ESP ) means an employee of an educational agency or institution who provides clerical and administrative services, transportation services, food and nutrition services, custodial and maintenance services, health and student services, technical services, or services related to skilled trades. (IV) Educational agency or institution The term educational agency or institution has the meaning given the term in section 444(a)(3) of the General Education Provisions Act ( 20 U.S.C. 1232g(a)(3) ). .\n#### 3. Entitlement to leave\nSection 102(a) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2612(a) ) is amended by adding at the end the following:\n(6) Calculation of leave for covered educational employees The Secretary shall provide methods for calculating the leave described in paragraph (1) with respect to covered educational employees, in accordance with section 108, as applicable. .",
      "versionDate": "2025-09-09",
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
        "actionDate": "2025-09-09",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committees on Oversight and Government Reform, and House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5222",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ESP, Paraprofessional, and Education Support Staff Family Leave Act",
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
        "name": "Labor and Employment",
        "updateDate": "2025-09-23T15:38:07Z"
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
      "date": "2025-09-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2738is.xml"
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
      "title": "ESP, Paraprofessional, and Education Support Staff Family Leave Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-13T12:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ESP, Paraprofessional, and Education Support Staff Family Leave Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-17T02:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish eligibility requirements for covered educational employees under the Family and Medical Leave Act of 1993, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-17T02:48:23Z"
    }
  ]
}
```
