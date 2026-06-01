# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2125?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2125
- Title: PICTURES Act
- Congress: 119
- Bill type: S
- Bill number: 2125
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2026-05-15T11:03:25Z
- Update date including text: 2026-05-15T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Select Committee on Intelligence.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Select Committee on Intelligence.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2125",
    "number": "2125",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "PICTURES Act",
    "type": "S",
    "updateDate": "2026-05-15T11:03:25Z",
    "updateDateIncludingText": "2026-05-15T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Intelligence (Select) Committee",
          "systemCode": "slin00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Select Committee on Intelligence.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-18",
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
            "date": "2025-06-18T17:54:14Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-18T17:54:14Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Intelligence (Select) Committee",
      "systemCode": "slin00",
      "type": "Select"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "LA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "TN"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2125is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2125\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Scott of Florida (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Select Committee on Intelligence\nA BILL\nTo require a report on the wealth of the leadership of the Chinese Communist Party, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prying Into Chinese Tyrants' Unreported Riches, Earnings, and Secrets Act or the PICTURES Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe Chinese Communist Party (CCP) operates as an opaque, authoritarian regime in which political power is concentrated in the hands of a relatively small group of senior officials.\n**(2)**\nThe leadership of the CCP, including full members of the Central Committee and the Central Committee\u2019s Politburo (also known as the Political Bureau) and Politburo Standing Committee, exert significant control over economic, military, and political affairs both within the People's Republic of China and externally.\n**(3)**\nNumerous credible reports and investigations have revealed that senior CCP officials and their families have amassed substantial wealth, often hidden through opaque financial structures, foreign holdings, and proxies.\n**(4)**\nA report issued by the Office of the Director of National Intelligence (ODNI) in March 2025 provided an important initial assessment of the financial assets of CCP leaders. A subsequent report, incorporating photographic evidence of CCP leaders\u2019 wealth and corruption, could build upon that work to further expose the hypocrisy and duplicity of the Chinese Communist Party.\n**(5)**\nUnderstanding the financial interests, personal assets, and overseas holdings of CCP leaders is essential to informing United States foreign policy, national security, and economic security decision-making.\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe effectiveness and credibility of intelligence reporting on sensitive subjects, including the wealth of senior CCP officials, depends upon the full cooperation of all relevant components of the United States intelligence community; and\n**(2)**\nall related nonpublic information, including classified intelligence, financial data, and foreign partner reporting, must be made available within the United States intelligence community to support such assessments to the fullest extent possible consistent with the protection of sources and methods.\n#### 4. Report on the wealth of the leadership of the Chinese Communist Party\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, and not later than 180 days following the appointment of a new Central Committee within the CCP, the Director of National Intelligence shall post on a publicly available website of the Office of the Director of National Intelligence and submit to the Select Committee on Intelligence of the Senate and the Permanent Select Committee on Intelligence of the House of Representatives a report on the wealth of the leadership of the Chinese Communist Party.\n##### (b) Elements\nThe report required under subsection (a) shall include the following elements:\n**(1)**\nA detailed assessment of the personal wealth, financial holdings, and business interests of full Central Committee members and the head of the Central Commission for Discipline Inspection, including all immediate family members of such foreign persons, prioritizing the following individuals:\n**(A)**\nThe General Secretary of the Chinese Communist Party.\n**(B)**\nMembers of the Politburo Standing Committee.\n**(C)**\nMembers of the full Politburo.\n**(D)**\nProvincial-level Party Secretaries.\n**(E)**\nMembers of the Central Military Commission.\n**(2)**\nDocumentation and, as available, photographic evidence of physical and financial assets owned or controlled directly or indirectly by such officials and their immediate family members, including, at a minimum\u2014\n**(A)**\nreal estate holdings inside and outside the People's Republic of China, including the Special Administrative Regions of Hong Kong and Macau;\n**(B)**\nhigh-value personal assets, such as yachts, luxury vehicles, private aircraft; and\n**(C)**\nbusiness holdings, investments, and financial accounts held in foreign jurisdictions.\n**(3)**\nIdentification of financial proxies, business associates, or other entities used to obscure the ownership of such wealth and assets, including those referenced in ODNI\u2019s March 20, 2025, report as a baseline.\n**(4)**\nAn assessment by the Director of National Intelligence regarding the level of cooperation and responsiveness of each relevant component of the intelligence community in providing information, analysis, and support for the preparation of the report, including whether any component failed to fully cooperate or provide requested nonpublic information.\n**(5)**\nNonpublic information related to the wealth of the leadership of the Chinese Communist Party, to the extent possible consistent with the protection of intelligence sources and methods, including information derived from classified sources, foreign partner reporting, financial intelligence, human sources, or other intelligence community holdings.\n##### (c) Form\nThe report posted and submitted under subsection (a) shall be in unclassified form, but the version submitted to Congress may include a classified annex as necessary.\n#### 5. Intelligence community defined\nIn this Act, the term intelligence community has the meaning given such term in section 3(4) of the National Security Act of 1947 ( 50 U.S.C. 3003(4) ).",
      "versionDate": "2025-06-18",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-21T19:55:03Z"
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
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2125is.xml"
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
      "title": "PICTURES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PICTURES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Prying Into Chinese Tyrants' Unreported Riches, Earnings, and Secrets Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a report on the wealth of the leadership of the Chinese Communist Party, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-02T01:34:13Z"
    }
  ]
}
```
