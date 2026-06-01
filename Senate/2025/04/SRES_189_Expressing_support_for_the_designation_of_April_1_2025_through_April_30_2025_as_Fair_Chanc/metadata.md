# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/189?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/189
- Title: A resolution expressing support for the designation of April 1, 2025, through April 30, 2025, as "Fair Chance Jobs Month".
- Congress: 119
- Bill type: SRES
- Bill number: 189
- Origin chamber: Senate
- Introduced date: 2025-04-30
- Update date: 2026-05-18T18:51:34Z
- Update date including text: 2026-05-18T18:51:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in Senate
- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2717-2718)
- Latest action: 2025-04-30: Introduced in Senate

## Actions

- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2717-2718)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/189",
    "number": "189",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "A resolution expressing support for the designation of April 1, 2025, through April 30, 2025, as \"Fair Chance Jobs Month\".",
    "type": "SRES",
    "updateDate": "2026-05-18T18:51:34Z",
    "updateDateIncludingText": "2026-05-18T18:51:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2717-2718)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T19:33:57Z",
          "name": "Referred To"
        }
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "MN"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NJ"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "IL"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "IL"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "VT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "MN"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres189is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 189\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Mr. Markey (for himself, Ms. Klobuchar , Mr. Booker , Mr. Durbin , Ms. Duckworth , Mr. Padilla , Ms. Warren , Mr. Welch , Ms. Smith , and Mr. Kim ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nExpressing support for the designation of April 1, 2025, through April 30, 2025, as \u201cFair Chance Jobs Month\u201d.\nThat the Senate\u2014\n**(1)**\nexpresses support for the designation of April 1, 2025, through April 30, 2025, as Fair Chance Jobs Month ; and\n**(2)**\nsupports efforts to\u2014\n**(A)**\nensure that people directly impacted by incarceration obtain stable and high-quality employment, housing, healthcare, and nutrition;\n**(B)**\ndismantle structural barriers to fair-chance hiring and employment, such as licensing restrictions, employer liability, and insurance restrictions;\n**(C)**\nexpand workforce development programs for returning citizens, formerly incarcerated individuals, and others directly impacted by incarceration, including\u2014\n**(i)**\npre-apprenticeship programs;\n**(ii)**\nregistered apprenticeship programs;\n**(iii)**\ncareer coaching, r\u00e9sum\u00e9-building, technology literacy, and other skillset development programs; and\n**(iv)**\nprograms that educate employers on best practices for, and the benefits of, fair-chance hiring;\n**(D)**\nmatch jobs providers with returning citizens and formerly incarcerated individuals seeking jobs;\n**(E)**\nsupport efforts from labor unions and worker organizations to engage returning citizens and formerly incarcerated individuals who are seeking jobs;\n**(F)**\npublicize work opportunities that are open to applicants with prior arrest or conviction records; and\n**(G)**\nfoster greater collaboration and dialogue between Federal, State, and local government agencies, community-based organizations, advocacy groups, employers, labor unions, currently and formerly incarcerated individuals, and others directly impacted by incarceration to enhance fair-chance hiring and employment and help to heal communities impacted by mass incarceration.",
      "versionDate": "2025-04-30",
      "versionType": "IS"
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
        "actionDate": "2026-04-29",
        "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2134)"
      },
      "number": "700",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution expressing support for the designation of April 1, 2026, through April 30, 2026, as \"Fair Chance Jobs Month\".",
      "type": "SRES"
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
        "updateDate": "2025-05-20T12:17:08Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres189is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution expressing support for the designation of April 1, 2025, through April 30, 2025, as \"Fair Chance Jobs Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T02:18:26Z"
    },
    {
      "title": "A resolution expressing support for the designation of April 1, 2025, through April 30, 2025, as \"Fair Chance Jobs Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-01T10:56:24Z"
    }
  ]
}
```
