# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3618?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3618
- Title: No Fentanyl on Social Media Act
- Congress: 119
- Bill type: S
- Bill number: 3618
- Origin chamber: Senate
- Introduced date: 2026-01-13
- Update date: 2026-04-29T11:03:33Z
- Update date including text: 2026-04-29T11:03:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-13: Introduced in Senate
- 2026-01-13 - IntroReferral: Introduced in Senate
- 2026-01-13 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-04-14 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with amendments favorably.
- Latest action: 2026-01-13: Introduced in Senate

## Actions

- 2026-01-13 - IntroReferral: Introduced in Senate
- 2026-01-13 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-04-14 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with amendments favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-13",
    "latestAction": {
      "actionDate": "2026-01-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3618",
    "number": "3618",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "No Fentanyl on Social Media Act",
    "type": "S",
    "updateDate": "2026-04-29T11:03:33Z",
    "updateDateIncludingText": "2026-04-29T11:03:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-14",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with amendments favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-13",
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
            "date": "2026-04-14T14:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-13T16:46:44Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sponsorshipDate": "2026-01-13",
      "state": "MN"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "DE"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "LA"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "OH"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3618is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3618\nIN THE SENATE OF THE UNITED STATES\nJanuary 13, 2026 Mr. Husted (for himself, Ms. Klobuchar , Ms. Blunt Rochester , and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Federal Trade Commission to submit to Congress a report on the ability of minors to access fentanyl through social media platforms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Fentanyl on Social Media Act .\n#### 2. Report on the ability of minors to access fentanyl through social media platforms\n##### (a) Report required\nNot later than 1 year after the date of the enactment of this Act, the Commission, in coordination with the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, and the Administrator of the Drug Enforcement Administration, shall submit to the relevant congressional committees and make publicly available on the website of the Commission a report on the ability of minors to access fentanyl, including through pressed pills, on social media platforms that includes the following:\n**(1)**\nThe prevalence and ability for minors to access fentanyl from drug sellers on social media platforms.\n**(2)**\nThe impact of such prevalence and access on minors, including health risks and risks to physical safety.\n**(3)**\nHow drug sellers use social media platforms to market, sell, deliver, distribute, dispense, and engage in other transactions related to the provision of fentanyl to minors.\n**(4)**\nHow design features and other characteristics of social media platforms affect the ability of minors to access fentanyl.\n**(5)**\nPractices, policies, and other measures taken by social media platforms to address the ability of drug sellers to use social media platforms and the effectiveness of those practices, policies, and measures.\n**(6)**\nOther measures taken by law enforcement, the medical community, and others to address the issues described in paragraphs (1) through (4).\n**(7)**\nRecommendations for Congress to eliminate the prevalence and ability for minors to access fentanyl on social media platforms.\n##### (b) Consultation required\nIn developing the report required under subsection (a), the Commission shall consult with stakeholders including parents, social media platforms, law enforcement, medical professionals, and other relevant experts.\n##### (c) Redaction permitted\nIn publishing the report required under subsection (a), the Commission, in consultation with the Attorney General, may redact any information relating to paragraphs (3) and (6) of such subsection that may compromise any law enforcement tactic, strategy, or technique.\n##### (d) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Fentanyl**\nThe term fentanyl includes any fentanyl analogue and fentanyl-related substance.\n**(3) Fentanyl-related substance**\nThe term fentanyl-related substance has the meaning given that term in subsection (e) of schedule I of section 202(c) of the Controlled Substances Act ( 21 U.S.C. 812(c) ).\n**(4) Minor**\nThe term minor means an individual who is under the age of 18.\n**(5) Relevant congressional committees**\nThe term relevant congressional committees means the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate.\n**(6) Social Media Platform**\nThe term social media platform \u2014\n**(A)**\nmeans a public-facing website, internet application, or mobile internet application, including a social network or video sharing service that\u2014\n**(i)**\nserves the public; and\n**(ii)**\nprimarily provides a forum for user-generated content, including messages, videos, images, games, and audio files; and\n**(B)**\ndoes not include\u2014\n**(i)**\na provider of broadband internet access service (as described in section 8.1(b) of title 47, Code of Federal Regulations, or successor regulation); or\n**(ii)**\nelectronic mail.",
      "versionDate": "2026-01-13",
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
        "actionDate": "2025-12-11",
        "text": "Forwarded by Subcommittee to Full Committee by Voice Vote."
      },
      "number": "6259",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No Fentanyl on Social Media Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Child safety and welfare",
            "updateDate": "2026-04-16T13:21:05Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-16T13:21:05Z"
          },
          {
            "name": "Drug trafficking and controlled substances",
            "updateDate": "2026-04-16T13:21:05Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2026-04-16T13:21:05Z"
          },
          {
            "name": "Federal Trade Commission (FTC)",
            "updateDate": "2026-04-16T13:21:05Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-16T13:21:05Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-04-16T13:21:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2026-04-02T15:49:07Z"
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
      "date": "2026-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3618is.xml"
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
      "title": "No Fentanyl on Social Media Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Fentanyl on Social Media Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-04T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Federal Trade Commission to submit to Congress a report on the ability of minors to access fentanyl through social media platforms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-04T04:18:18Z"
    }
  ]
}
```
