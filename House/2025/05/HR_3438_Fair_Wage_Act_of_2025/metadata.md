# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3438?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3438
- Title: Fair Wage Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3438
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2025-08-30T08:05:17Z
- Update date including text: 2025-08-30T08:05:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3438",
    "number": "3438",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Fair Wage Act of 2025",
    "type": "HR",
    "updateDate": "2025-08-30T08:05:17Z",
    "updateDateIncludingText": "2025-08-30T08:05:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
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
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "WA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3438ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3438\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Fitzpatrick (for himself and Ms. Perez ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Fair Labor Standards Act of 1938 to provide for a Federal, cost-of-living based minimum wage, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Wage Act of 2025 .\n#### 2. Cost-of-living based minimum wage\n##### (a) In general\nSection 6(a)(1) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206(a)(1) ) is amended to read as follows:\n(1) except as otherwise provided in this section, not less than the amount determined by the Secretary under subsection (h) for the metropolitan statistical area or the nonmetropolitan portion in which the employer resides; .\n##### (b) Determination of regional minimum wage\nSection 6 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206 ) is amended by adding at the end the following:\n(h) Determination of minimum wage (1) (A) On the effective date of the Fair Wage Act of 2025 , the wage determined under this paragraph for a metropolitan statistical area or nonmetropolitan portion shall be equal to the result obtained\u2014 (i) by multiplying\u2014 (I) 40 percent of the national average hourly wage of private sector, non-supervisory workers (as reported by the Bureau of Labor Statistics of the Department of Labor for the most recent month for which data are available); by (II) the adjustment percentage specified in paragraph (2) for the area or portion; and (ii) by rounding the result obtained under clause (i) to the nearest tenth of a dollar. (B) Not later than 1 year after such effective date, subparagraph (A)(i)(I) shall be applied by substituting 45 percent for 40 percent . (C) Not later than 2 years after such effective date, subparagraph (A)(i)(I) shall be applied by substituting 50 percent for 40 percent . (D) Not later than 5 years after such effective date, and for each 3-year period thereafter, the wage determined under this paragraph for a metropolitan statistical area or nonmetropolitan portion shall be equal to the greater of\u2014 (i) the result obtained under subparagraph (C); or (ii) the wage determined under this paragraph for such area or portion for the preceding three-year period. (2) The adjustment percentage specified in this paragraph for a metropolitan statistical area or nonmetropolitan portion shall be\u2014 (A) 87.5 percent, for a metropolitan statistical area or nonmetropolitan portion with a regional price parity of less than 90; (B) 92.5 percent, for a metropolitan statistical area or nonmetropolitan portion with a regional price parity of less than 95, but not less than 90; (C) 100 percent, for a metropolitan statistical area or nonmetropolitan portion with a regional price parity of less than 105, but not less than 95; (D) 107.5 percent, for a metropolitan statistical area or nonmetropolitan portion with a regional price parity of less than 110, but not less than 105; and (E) 115 percent, for a metropolitan statistical area or nonmetropolitan portion with a regional price parity of not less than 110. (3) In this subsection: (A) The term metropolitan statistical area means a geographic area, defined by the Office of Management and Budget for statistical purposes, containing a large population nucleus and adjacent communities having a high degree of social and economic integration with that nucleus. (B) The term nonmetropolitan portion means any county (or portion thereof) which is not within a metropolitan statistical area. All nonmetropolitan portions of a State shall be treated, in aggregate, as a single nonmetropolitan portion for the State. (C) The term regional price parity means the regional price parity for a metropolitan statistical area or nonmetropolitan portion determined by the Bureau of Economic Analysis of the Department of Commerce for the most recent year for which data are available. In determining regional price parities for purposes of this subsection, the Bureau of Economic Analysis shall use the same methodology used to determine such parities for the most recent year for which such parities were reported by the Bureau before the date of the enactment of this subsection. .\n#### 3. Minimum cash wage for tipped employees\nClause (i) of section 3(m)(2)(A) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2)(A) ) is amended by striking the cash wage required to be paid such an employee on the date of the enactment of this paragraph and inserting an amount equal to 30 percent of the wage determined under section 6(a)(1) for the metropolitan statistical area or the nonmetropolitan portion in which the employer resides .\n#### 4. Minimum wage for newly hired employees who are 18 years old or younger\nSection 6(g) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206(g) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking a wage which is not less than $4.25 an hour and inserting a wage which is not less than 2/3 of the wage determined under subsection (a)(1) for the metropolitan statistical area or the nonmetropolitan portion in which the employer resides ; and\n**(2)**\nin paragraph (5)\u2014\n**(A)**\nby striking has not attained the age of 20 years and inserting is the age of 18 years or younger ; and\n**(B)**\nby striking 25 years and inserting 24 years or younger .\n#### 5. Effective date\nThe amendments and repeals made by this Act shall take effect on the first day of the third month that begins after the date of the enactment of this Act.",
      "versionDate": "2025-05-15",
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
        "name": "Labor and Employment",
        "updateDate": "2025-05-28T12:58:29Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3438ih.xml"
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
      "title": "Fair Wage Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-22T02:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Wage Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-22T02:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Fair Labor Standards Act of 1938 to provide for a Federal, cost-of-living based minimum wage, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-22T02:18:23Z"
    }
  ]
}
```
