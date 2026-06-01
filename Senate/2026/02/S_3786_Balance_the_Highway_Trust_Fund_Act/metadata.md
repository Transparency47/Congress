# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3786?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3786
- Title: Balance the Highway Trust Fund Act
- Congress: 119
- Bill type: S
- Bill number: 3786
- Origin chamber: Senate
- Introduced date: 2026-02-05
- Update date: 2026-02-26T16:31:20Z
- Update date including text: 2026-02-26T16:31:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-05: Introduced in Senate
- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2026-02-05: Introduced in Senate

## Actions

- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-05",
    "latestAction": {
      "actionDate": "2026-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3786",
    "number": "3786",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Balance the Highway Trust Fund Act",
    "type": "S",
    "updateDate": "2026-02-26T16:31:20Z",
    "updateDateIncludingText": "2026-02-26T16:31:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-05",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-05",
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
          "date": "2026-02-05T18:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3786is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3786\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2026 Mr. Lee introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo limit spending from the Highway Trust Fund, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Balance the Highway Trust Fund Act .\n#### 2. Obligation limitation\n##### (a) General limitation\nSubject to subsection (d) and notwithstanding any other provision of law, for each fiscal year, the obligations for Federal-aid highway and highway safety construction programs shall not exceed the net highway receipts most recently estimated by the Secretary of the Treasury for that fiscal year under section 9503(d)(1)(B) of the Internal Revenue Code of 1986.\n##### (b) Distribution of obligation authority\nFor each fiscal year, the Secretary of Transportation (referred to in this section as the Secretary )\u2014\n**(1)**\nshall not distribute obligation authority provided by subsection (a) for the fiscal year for\u2014\n**(A)**\namounts authorized for administrative expenses and programs by section 104(a) of title 23, United States Code; and\n**(B)**\namounts authorized for the Bureau of Transportation Statistics;\n**(2)**\nshall not distribute an amount of obligation authority provided by subsection (a) that is equal to the unobligated balance of amounts\u2014\n**(A)**\nmade available from the Highway Trust Fund (other than the Mass Transit Account) for Federal-aid highway and highway safety construction programs for previous fiscal years the funds for which are allocated by the Secretary (or apportioned by the Secretary under section 202 or 204 of title 23, United States Code); and\n**(B)**\nfor which obligation authority was provided in a previous fiscal year;\n**(3)**\nshall determine the proportion that\u2014\n**(A)**\nthe obligation authority provided by subsection (a) for the fiscal year, less the aggregate of amounts not distributed under paragraphs (1) and (2) of this subsection; bears to\n**(B)**\nthe total of the sums authorized to be appropriated for the Federal-aid highway and highway safety construction programs, less the aggregate of the amounts not distributed under paragraphs (1) and (2) of this subsection;\n**(4)**\nshall distribute the obligation authority provided by subsection (a), less the aggregate amounts not distributed under paragraphs (1) and (2), for each of the programs (other than programs to which paragraph (1) applies) that are allocated by the Secretary under this Act and title 23, United States Code, or apportioned by the Secretary under section 202 or 204 of that title, by multiplying\u2014\n**(A)**\nthe proportion determined under paragraph (3); by\n**(B)**\nthe amounts authorized to be appropriated for each such program for the fiscal year; and\n**(5)**\nshall distribute the obligation authority provided by subsection (a), less the aggregate amounts not distributed under paragraphs (1) and (2) and the amounts distributed under paragraph (4), for Federal-aid highway and highway safety construction programs that are apportioned by the Secretary under title 23, United States Code (other than the amounts apportioned under sections 202 and 204 of title 23, United States Code) in the proportion that\u2014\n**(A)**\namounts authorized to be appropriated for the programs that are apportioned under title 23, United States Code, to each State for the fiscal year; bears to\n**(B)**\nthe total of the amounts authorized to be appropriated for the programs that are apportioned under title 23, United States Code, to all States for the fiscal year.\n##### (c) Redistribution of unused obligation authority\nNotwithstanding subsection (b), the Secretary shall, after August 1 of each fiscal year\u2014\n**(1)**\nrevise a distribution of the obligation authority made available under subsection (b) if an amount distributed cannot be obligated during that fiscal year; and\n**(2)**\nredistribute sufficient amounts to those States able to obligate amounts in addition to those previously distributed during that fiscal year, giving priority to those States having large unobligated balances of funds apportioned under sections 144 (as in effect on the day before the date of enactment of MAP\u201321 ( Public Law 112\u2013141 )) and 104 of title 23, United States Code.\n##### (d) Applicability of obligation limitations to transportation research programs\n**(1) In general**\nExcept as provided in paragraph (2), obligation limitations imposed by subsection (a) shall apply to contract authority for transportation research programs carried out under chapter 5 of title 23, United States Code.\n**(2) Exception**\nObligation authority made available under paragraph (1) shall\u2014\n**(A)**\nremain available for a period of 4 fiscal years; and\n**(B)**\nbe in addition to the amount of any limitation imposed on obligations for Federal-aid highway and highway safety construction programs for future fiscal years.\n##### (e) Redistribution of certain authorized funds\n**(1) In general**\nNot later than 30 days after the date of distribution of obligation authority under subsection (b) for each fiscal year, the Secretary shall distribute to the States any funds (excluding funds authorized for the program under section 202 of title 23, United States Code) that\u2014\n**(A)**\nare authorized to be appropriated for the fiscal year for Federal-aid highway programs; and\n**(B)**\nthe Secretary determines will not be allocated to the States (or will not be apportioned to the States under section 204 of title 23, United States Code), and will not be available for obligation, for the fiscal year because of the imposition of any obligation limitation for the fiscal year.\n**(2) Ratio**\nFunds shall be distributed under paragraph (1) in the same proportion as the distribution of obligation authority under subsection (b)(5).\n**(3) Availability**\nFunds distributed to each State under paragraph (1) shall be available for any purpose described in section 133(b) of title 23, United States Code.\n#### 3. Obligation limitation\nSection 5338 of title 49, United States Code, is amended by adding at the end the following:\n(f) Obligation limitation Notwithstanding subsection (a) or any other provision of law, for each fiscal year, the total of all obligations from amounts made available from the Mass Transit Account of the Highway Trust Fund by subsection (a) and any other provision of law shall not exceed the net mass transit receipts most recently estimated for that fiscal year by the Secretary of the Treasury under section 9503(e)(4) of the Internal Revenue Code of 1986. .\n#### 4. Effective date\nThis Act and the amendments made by this Act take effect October 1, 2027.",
      "versionDate": "2026-02-05",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-02-26T16:31:20Z"
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
      "date": "2026-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3786is.xml"
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
      "title": "Balance the Highway Trust Fund Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-21T04:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Balance the Highway Trust Fund Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to limit spending from the Highway Trust Fund, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-21T04:48:26Z"
    }
  ]
}
```
