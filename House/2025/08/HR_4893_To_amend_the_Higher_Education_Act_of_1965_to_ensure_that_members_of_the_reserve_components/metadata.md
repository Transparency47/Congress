# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4893?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4893
- Title: National Guard and Reserve Student Loan Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 4893
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2025-09-18T17:11:28Z
- Update date including text: 2025-09-18T17:11:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4893",
    "number": "4893",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001223",
        "district": "2",
        "firstName": "Seth",
        "fullName": "Rep. Magaziner, Seth [D-RI-2]",
        "lastName": "Magaziner",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "National Guard and Reserve Student Loan Fairness Act",
    "type": "HR",
    "updateDate": "2025-09-18T17:11:28Z",
    "updateDateIncludingText": "2025-09-18T17:11:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
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
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-05",
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
          "date": "2025-08-05T14:02:25Z",
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
      "bioguideId": "K000388",
      "district": "1",
      "firstName": "Trent",
      "fullName": "Rep. Kelly, Trent [R-MS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-08-05",
      "state": "MS"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "NC"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "IL"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4893ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4893\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Mr. Magaziner (for himself and Mr. Kelly of Mississippi ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to ensure that members of the reserve components of the Armed Forces receive appropriate credit toward public service loan forgiveness, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National Guard and Reserve Student Loan Fairness Act .\n#### 2. Special rule for members of the reserve components of the Armed Forces performing certain duty\nSection 455(m) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(m) ) is amended by adding at the end the following:\n(5) Special rule for members of the reserve components of the Armed Forces performing certain duty (A) Calculation of qualifying payments based on years of service creditable toward retired pay With respect to a borrower who is a member of a reserve component of an Armed Force, the Secretary shall\u2014 (i) in the case of a member who completed a full year of covered service, deem each month in such year to be a month for which a qualifying payment was made under paragraph (1) if\u2014 (I) for each such month the borrower made a corresponding monthly payment on an eligible Federal Direct Loan; and (II) such corresponding monthly payment\u2014 (aa) met the requirements of paragraph (1); or (bb) in the case of a borrower not employed full-time in a public service job at the time the payment was made, such payment would have met the requirements of paragraph (1) had the borrower been employed full-time in a public service job at the time of such payment. (ii) in the case of a member who completed a partial year of covered service, deem up to six months in such year to be a month for which a qualifying payment was made if\u2014 (I) for each such month the borrower made a corresponding monthly payment on an eligible Federal Direct Loan; and (II) such corresponding monthly payment\u2014 (aa) met the requirements of paragraph (1); or (bb) in the case of a borrower not employed full-time in a public service job at the time the payment was made, such payment would have met the requirements of paragraph (1) had the borrower been employed full-time in a public service job at the time of such payment. (B) Data matching required Not later than one year after the date of the enactment of this paragraph, and on an annual basis thereafter, the Secretary of Defense and the Secretary of Education shall jointly complete a data matching process\u2014 (i) to identify each individual who, while serving member of a reserve component of an Armed Force, made one or more student loan payments eligible to be counted under this paragraph; and (ii) without requiring further information or action from such individual\u2014 (I) to certify the total number of full or partial years of covered service of such individual; and (II) to count the total number of qualifying payments made by the individual during such years. (C) Definitions In this paragraph: (i) The term full year of covered service means any year for which a member of a reserve component of an Armed Force was credited at least 80 points toward eligibility for retired pay under section 12732(a)(2) of title 10, United States Code. (ii) The term partial year of covered service means any year for which a member of a reserve component of an Armed Force was credited at least 50 but less than 80 points toward eligibility for retired pay under section 12732(a)(2) of title 10, United States Code. (iii) The term Armed Force has the meaning given that term in section 101 of title 10, United States Code. .",
      "versionDate": "2025-08-05",
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
        "name": "Education",
        "updateDate": "2025-09-18T17:11:28Z"
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
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4893ih.xml"
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
      "title": "National Guard and Reserve Student Loan Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Guard and Reserve Student Loan Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to ensure that members of the reserve components of the Armed Forces receive appropriate credit toward public service loan forgiveness, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:27Z"
    }
  ]
}
```
