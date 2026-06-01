# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3108?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3108
- Title: AI-Related Job Impacts Clarity Act
- Congress: 119
- Bill type: S
- Bill number: 3108
- Origin chamber: Senate
- Introduced date: 2025-11-05
- Update date: 2026-03-20T11:03:19Z
- Update date including text: 2026-03-20T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-05: Introduced in Senate
- 2025-11-05 - IntroReferral: Introduced in Senate
- 2025-11-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-11-05: Introduced in Senate

## Actions

- 2025-11-05 - IntroReferral: Introduced in Senate
- 2025-11-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-05",
    "latestAction": {
      "actionDate": "2025-11-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3108",
    "number": "3108",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "AI-Related Job Impacts Clarity Act",
    "type": "S",
    "updateDate": "2026-03-20T11:03:19Z",
    "updateDateIncludingText": "2026-03-20T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-05",
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
      "actionDate": "2025-11-05",
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
            "date": "2025-11-05T19:37:30Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-05T19:37:30Z",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "VA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "VA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3108is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3108\nIN THE SENATE OF THE UNITED STATES\nNovember 5, 2025 Mr. Hawley (for himself and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo require reports regarding artificial intelligence-related job impacts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AI-Related Job Impacts Clarity Act .\n#### 2. Disclosures and reports regarding artificial intelligence-related job impacts\n##### (a) Covered entity disclosures\n**(1) In general**\nNot more than 30 days after the last day of each quarter, a covered entity shall, with respect to such quarter, disclose to the Secretary any artificial intelligence-related job impact experienced by the entity in the United States (including any territory or possession of the United States), including\u2014\n**(A)**\nthe number of individuals laid off by the covered entity in the United States (including any territory or possession of the United States) during the quarter that are substantially due to the replacement or automation by artificial intelligence of the functions performed by such individuals;\n**(B)**\nthe number of individuals hired by the covered entity in the United States (including any territory or possession of the United States) during the quarter that are substantially due to the incorporation of artificial intelligence;\n**(C)**\nthe number of positions of the covered entity in the United States (including any territory or possession of the United States) that were occupied at any point during the prior quarter for which the covered entity has decided not to fill based on a reason that is substantially due to the replacement or automation by artificial intelligence of the functions of such positions;\n**(D)**\nthe number of individuals in the United States (including any territory or possession of the United States) whom the covered entity is retraining, or assisting in retraining, based on a reason that is substantially due to artificial intelligence; and\n**(E)**\nany other information related to artificial intelligence-related job impacts, as determined appropriate by the Secretary.\n**(2) NAICS codes**\nWith respect to each artificial intelligence-related job impact disclosure under paragraph (1), the covered entity shall provide in such disclosure the corresponding North American Industry Classification System codes.\n**(3) Surveys**\n**(A) In general**\nAs determined appropriate by the Secretary, the Secretary may\u2014\n**(i)**\n**(I)**\nrevise an existing survey conducted by the Secretary as of the date of enactment of this Act to incorporate the disclosures required under this subsection into such a survey; or\n**(II)**\ncollaborate with the Bureau of the Census to revise an existing survey conducted by the Bureau of the Census as of the date of enactment of this Act, or an existing survey conducted as of such date of enactment by the Secretary in partnership with the Bureau of the Census, to incorporate the disclosures required under this subsection into such a survey; and\n**(ii)**\nallow covered entities to comply with the requirements of this subsection by making such disclosures through such survey.\n**(B) Bureau of the Census surveys**\nIn the case the disclosures required under this subsection are incorporated pursuant to subparagraph (A) into a survey conducted by the Bureau of the Census that is not a survey conducted in partnership with the Secretary, the Bureau of the Census shall, for each quarter, share the data from such disclosures with the Secretary in order for the Secretary to prepare the reports required under subsection (b).\n##### (b) Department of Labor reports\nThe Secretary, in consultation with the Director of the Office of Management and Budget and the Director of the Office of Personnel Management, shall\u2014\n**(1)**\nfor each quarter, prepare a report\u2014\n**(A)**\nsummarizing the data from disclosures submitted under subsection (a) during the quarter; and\n**(B)**\nfor the quarter ending on December 31, summarizing such data for the calendar year;\n**(2)**\nfor every other quarter, prepare a report analyzing the net impact of the data contained in the report under paragraph (1) for such quarter and for the preceding quarter, and any other relevant data available to the Secretary with respect to artificial intelligence-related job impacts; and\n**(3)**\nnot more than 60 days after the last day of each quarter\u2014\n**(A)**\npublish each report prepared for the quarter under paragraph (1) and, as applicable, paragraph (2), and the data underlying such reports on the website of the Bureau of Labor Statistics; and\n**(B)**\nsubmit each such report to Congress.\n##### (c) Application to non-Publicly-Traded companies\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary, in consultation with the Securities and Exchange Commission and the Secretary of the Treasury, shall issue regulations to determine the extent to which non-publicly-traded companies shall be included as subject to the reporting requirements under subsection (a).\n**(2) Scope of rulemaking**\nThe regulations issued under this subsection shall\u2014\n**(A)**\nidentify for such inclusion categories of non-publicly-traded companies that have a significant workforce, estimated enterprise value, or employment impact on a regional or national basis;\n**(B)**\nconsider for such inclusion thresholds with respect to non-publicly-traded companies, such as\u2014\n**(i)**\nthe number of employees employed by such companies;\n**(ii)**\nthe annual revenue of such companies; or\n**(iii)**\nthe industry classification under the North American Industry Classification System for such companies;\n**(C)**\nensure that any reporting requirements under subsection (a) applicable to a non-publicly-traded company are proportionate to the size and capacity of such company; and\n**(D)**\nestablish procedures for the confidential submission and publication of data of non-publicly-traded companies in order to protect the proprietary or personally identifiable information of such companies.\n**(3) Public comment**\nIn issuing the regulations under this subsection, the Secretary shall provide for notice and comment in accordance with section 553 of title 5, United States Code.\n##### (d) Definitions\nIn this section:\n**(1) Artificial intelligence**\nThe term artificial intelligence has the meaning given the term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(2) Covered entity**\nThe term covered entity means\u2014\n**(A)**\nan entity that is\u2014\n**(i)**\na publicly-traded company; or\n**(ii)**\nan agency, as defined in section 551 of title 5, United States Code; and\n**(B)**\nan entity that\u2014\n**(i)**\nis a non-publicly-traded company; and\n**(ii)**\nis identified by the Secretary through regulations issued under subsection (c) for inclusion as subject to the requirements under subsection (a).\n**(3) Non-publicly-traded company**\n**(A) In general**\nThe term non-publicly-traded company means a business entity engaged in interstate commerce that\u2014\n**(i)**\nis not an issuer, the securities of which are listed on a national securities exchange; and\n**(ii)**\nis not otherwise required to file reports with the Securities and Exchange Commission under section 13 or 15(d) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78m ; 78o(d)).\n**(B) Securities definitions**\nIn this paragraph\u2014\n**(i)**\nthe terms exchange , issuer , and security have the meanings given those terms in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) ); and\n**(ii)**\nthe term national securities exchange means an exchange registered pursuant to section 6 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78f ).\n**(4) Publicly-traded company**\nThe term publicly-traded company has the meaning given the term in section 5003(a) of the American Rescue Plan Act of 2021 ( 15 U.S.C. 9009c(a) ).\n**(5) Quarter**\nThe term quarter has the meaning given the term calendar quarter in section 5061(d)(4)(C) of the Internal Revenue Code of 1986.\n**(6) Secretary**\nThe term Secretary means the Secretary of Labor, acting through the Commissioner of Labor Statistics.",
      "versionDate": "2025-11-05",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-11-19T15:37:55Z"
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
      "date": "2025-11-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3108is.xml"
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
      "title": "AI-Related Job Impacts Clarity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AI-Related Job Impacts Clarity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-08T05:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require reports regarding artificial intelligence-related job impacts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-08T05:33:18Z"
    }
  ]
}
```
