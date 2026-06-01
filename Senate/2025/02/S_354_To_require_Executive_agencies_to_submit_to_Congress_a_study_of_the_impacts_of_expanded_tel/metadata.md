# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/354?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/354
- Title: SHOW UP Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 354
- Origin chamber: Senate
- Introduced date: 2025-02-03
- Update date: 2025-06-20T18:47:56Z
- Update date including text: 2025-06-20T18:47:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-03: Introduced in Senate
- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-03: Introduced in Senate

## Actions

- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-03",
    "latestAction": {
      "actionDate": "2025-02-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/354",
    "number": "354",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "SHOW UP Act of 2025",
    "type": "S",
    "updateDate": "2025-06-20T18:47:56Z",
    "updateDateIncludingText": "2025-06-20T18:47:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-03",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-03",
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
          "date": "2025-02-03T20:39:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "ID"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "IA"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "LA"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "NE"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s354is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 354\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2025 Mrs. Blackburn (for herself, Mr. Crapo , Ms. Ernst , Mr. Cassidy , Mr. Tillis , Mr. Ricketts , and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require Executive agencies to submit to Congress a study of the impacts of expanded telework and remote work by agency employees during the COVID\u201319 pandemic and a plan for the agency\u2019s future use of telework and remote work, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stopping Home Office Work\u2019s Unproductive Problems Act of 2025 or the SHOW UP Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Agency**\nThe term agency has the meaning given the term Executive agency in section 105 of title 5, United States Code.\n**(2) Director**\nThe term Director means the Director of the Office of Personnel Management.\n**(3) Locality pay**\nThe term locality pay means locality pay provided for under section 5304 or 5304a of title 5, United States Code.\n**(4) Telework; teleworking**\nThe terms telework and teleworking \u2014\n**(A)**\nhave the meaning given those terms in section 6501 of title 5, United States Code; and\n**(B)**\ninclude remote work.\n#### 3. Reinstatement of pre-pandemic telework policies, practices, and levels for Executive agencies\n##### (a) In general\nNot later than 30 days after the date of enactment of this Act, the head of each agency shall reinstate and apply the telework policies, practices, and levels of the agency that were in effect on December 31, 2019.\n##### (b) Prohibition\nThe head of an agency may not expand any policy, practice, or level described in subsection (a) until the date on which the head of the agency submits to Congress\u2014\n**(1)**\nan agency plan under section 4(a)(2); and\n**(2)**\na certification under section 4(a)(3).\n#### 4. Study, plan, and certification regarding Executive agency telework policies, practices, and levels for Executive agencies\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the head of each agency, in consultation with the Director, shall submit to Congress\u2014\n**(1)**\na study on the impacts on the agency and the mission of the agency of expanding telework for employees as a result of the public health emergency relating to the Coronavirus Disease 2019 (COVID\u201319) pandemic declared under section 319 of the Public Health Service Act ( 42 U.S.C. 247d ) on January 31, 2020, including an analysis of\u2014\n**(A)**\nany adverse impacts of that expansion on the performance by the agency of the mission of the agency, including the performance of customer service by the agency;\n**(B)**\nany costs to the agency during that expansion attributable to\u2014\n**(i)**\nowning, leasing, or maintaining underutilized real property; or\n**(ii)**\npaying higher rates of locality pay to teleworking employees as a result of incorrectly classifying those employees as teleworkers rather than remote workers;\n**(C)**\nany degree to which the agency failed during that expansion to provide teleworking employees with secure network capacity, communications tools, necessary and secure access to appropriate agency data assets and Federal records, and equipment sufficient to enable teleworking employee to be fully productive;\n**(D)**\nany degree to which that expansion facilitated dispersal of the agency workforce around the United States; and\n**(E)**\nany other impacts of that expansion that the head of the agency or the Director considers appropriate;\n**(2)**\nany agency plan to expand telework policies, practices, or levels beyond the telework policies, practices, and levels of the agency that were in effect on December 31, 2019; and\n**(3)**\na certification by the Director that the agency plan described in paragraph (2) will\u2014\n**(A)**\nhave a substantial positive effect on\u2014\n**(i)**\nthe performance of the mission of the agency, including the performance of customer service;\n**(ii)**\nincreasing the level of dispersal of agency personnel throughout the United States; and\n**(iii)**\nthe reversal of any adverse impacts described in paragraph (1)(A);\n**(B)**\nsubstantially lower the costs of the agency relating to owning, leasing, or maintaining real property;\n**(C)**\nsubstantially lower the costs of the agency attributable to paying locality pay to agency personnel working from locations outside the pay locality of their position\u2019s official worksite; and\n**(D)**\nensure that teleworking employees will be provided with secure network capacity, communications tools, necessary and secure access to appropriate agency data assets and Federal records, and equipment sufficient to enable each teleworking employee to be fully productive, without substantially increasing the agency\u2019s overall costs for secure network capacity, communications tools, and equipment.\n##### (b) Limitation\n**(1) In general**\nThe head of an agency may not implement an agency plan described in subsection (a)(2) for which the Director does not issue a certification described in subsection (a)(3).\n**(2) Subsequent plans**\nIf the head of an agency unsuccessfully submits an agency plan described in subsection (a)(2) to the Director for the certification described in subsection (a)(3), the head of the agency may\u2014\n**(A)**\nsubmit to the Director subsequent agency plans until the head of the agency receives the certification; and\n**(B)**\nsubmit a subsequent agency plan described in subparagraph (A) that is certified by the Director to Congress.",
      "versionDate": "2025-02-03",
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
            "name": "Commuting",
            "updateDate": "2025-06-20T18:47:34Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-06-20T18:47:29Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-20T18:47:51Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-20T18:47:40Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-06-20T18:47:56Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-06-20T18:47:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-13T14:27:33Z"
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
      "date": "2025-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s354is.xml"
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
      "title": "SHOW UP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T03:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SHOW UP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T03:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stopping Home Office Work\u2019s Unproductive Problems Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T03:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require Executive agencies to submit to Congress a study of the impacts of expanded telework and remote work by agency employees during the COVID-19 pandemic and a plan for the agency's future use of telework and remote work, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T03:03:35Z"
    }
  ]
}
```
