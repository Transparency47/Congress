# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4097?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4097
- Title: State-Based Education Loan Awareness Act
- Congress: 119
- Bill type: S
- Bill number: 4097
- Origin chamber: Senate
- Introduced date: 2026-03-16
- Update date: 2026-05-22T19:48:25Z
- Update date including text: 2026-05-22T19:48:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-16: Introduced in Senate
- 2026-03-16 - IntroReferral: Introduced in Senate
- 2026-03-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2026-03-16: Introduced in Senate

## Actions

- 2026-03-16 - IntroReferral: Introduced in Senate
- 2026-03-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-16",
    "latestAction": {
      "actionDate": "2026-03-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4097",
    "number": "4097",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001153",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Murkowski, Lisa [R-AK]",
        "lastName": "Murkowski",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "State-Based Education Loan Awareness Act",
    "type": "S",
    "updateDate": "2026-05-22T19:48:25Z",
    "updateDateIncludingText": "2026-05-22T19:48:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-16",
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
      "actionDate": "2026-03-16",
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
            "date": "2026-03-19T14:01:20Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-16T19:39:11Z",
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
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "RI"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "LA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "NH"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "AK"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "OK"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4097is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4097\nIN THE SENATE OF THE UNITED STATES\nMarch 16, 2026 Ms. Murkowski (for herself, Mr. Reed , Mr. Cassidy , and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish that a State-based education loan program is excluded from certain requirements relating to a preferred lender arrangement.\n#### 1. Short title\nThis Act may be cited as the State-Based Education Loan Awareness Act .\n#### 2. State-based education loan programs\nSection 151 of the Higher Education Act of 1965 ( 20 U.S.C. 1019 ) is amended\u2014\n**(1)**\nin paragraph (8)(B)\u2014\n**(A)**\nin clause (i), by striking or after the semicolon;\n**(B)**\nin clause (ii), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(iii) arrangements or agreements with respect to education loans made under a State-based education loan program. ; and\n**(2)**\nby adding at the end the following:\n(10) State-based education loan program The term State-based education loan program means an education loan program that\u2014 (A) is provided by a State agency, State authority, or nonprofit organization, separately or jointly; (B) makes loans that are not funded, insured, or guaranteed by the Federal Government; (C) is authorized, established, or chartered by State law, or otherwise approved by the State; (D) offers one or more loans for which the interest rate and fees, as calculated in accordance with sections 106 and 107 of the Truth in Lending Act ( 15 U.S.C. 1605 ; 1606), are at least as favorable as the interest rate and fees of the Direct PLUS loans authorized under part D of title IV at the time such loan is originated; and (E) is available only to a borrower who has been advised, such as in a financial aid offer, by an institution of higher education (as defined under section 102)\u2014 (i) that the borrower has the opportunity to exhaust eligibility for Federal education loans made under part D of title IV prior to accepting a private education loan; and (ii) of the interest rates, fees, and benefits of such Federal education loans, including income-driven repayment options, opportunities for loan forgiveness, forbearance or deferment options, interest subsidies, and tax benefits. .",
      "versionDate": "2026-03-16",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2026-04-02T17:18:23Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2026-04-02T17:18:23Z"
          },
          {
            "name": "Interest, dividends, interest rates",
            "updateDate": "2026-04-02T17:18:23Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-04-02T17:18:23Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2026-04-02T17:18:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2026-04-01T19:59:28Z"
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
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4097is.xml"
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
      "title": "State-Based Education Loan Awareness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T19:48:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish that a State-based education loan program is excluded from certain requirements relating to a preferred lender arrangement.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "State-Based Education Loan Awareness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:18Z"
    }
  ]
}
```
