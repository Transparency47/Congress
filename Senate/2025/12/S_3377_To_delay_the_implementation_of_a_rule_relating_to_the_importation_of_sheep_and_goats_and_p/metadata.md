# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3377?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3377
- Title: A bill to delay the implementation of a rule relating to the importation of sheep and goats and products derived from sheep and goats, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 3377
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-01-08T17:46:52Z
- Update date including text: 2026-01-08T17:46:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S8514)
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S8514)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3377",
    "number": "3377",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "A bill to delay the implementation of a rule relating to the importation of sheep and goats and products derived from sheep and goats, and for other purposes.",
    "type": "S",
    "updateDate": "2026-01-08T17:46:52Z",
    "updateDateIncludingText": "2026-01-08T17:46:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S8514)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-S",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T20:39:36Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "WY"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3377is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3377\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mr. Barrasso (for himself, Ms. Lummis , and Mr. Hoeven ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo delay the implementation of a rule relating to the importation of sheep and goats and products derived from sheep and goats, and for other purposes.\n#### 1. Delayed implementation of rule relating to importation of sheep and goats and products derived from sheep and goats\n##### (a) In general\nDuring the period beginning on the date of the enactment of this Act and ending on the date that is 1 year after the date on which the report is submitted under subsection (b), the Secretary of Agriculture, and any other Federal official, may not finalize, implement, administer, or enforce the proposed rule entitled Importation of Sheep, Goats, and Certain Other Ruminants (81 Fed. Reg. 46619) and dated July 18, 2016.\n##### (b) Study and report\n**(1) Study**\n**(A) In general**\nThe Secretary of Agriculture shall conduct a study on the potential costs and benefits of the rule referred to in subsection (a).\n**(B) Contents**\nThe study required by subparagraph (A) shall assess\u2014\n**(i)**\nthe estimated amount of sheep and goat meat imported into the United States as a result of the implementation of the rule referred to in subsection (a);\n**(ii)**\nthe estimated increase in the number of live sheep and goats imported into the United States as a result of the rule;\n**(iii)**\nthe estimated demand for sheep and goat meat in the United States during the 10-year period beginning on the date of the enactment of this Act, disaggregated by region and State;\n**(iv)**\nthe impact of the COVID\u201319 pandemic on the economic data and market conditions for imports of sheep and goat meat and live sheep and goats;\n**(v)**\nthe potential effects of the rule on\u2014\n**(I)**\nthe supply and prices of live sheep and goats in the United States;\n**(II)**\nproducers of and markets for live sheep and goats in the United States, disaggregated by region and State;\n**(III)**\nexport opportunities for United States producers of sheep and goat meat;\n**(IV)**\nthe competitiveness of the sheep and goat industries in the United States;\n**(V)**\nconsumer confidence in sheep and goat meat;\n**(VI)**\nthe health of sheep and goat herds in the United States; and\n**(VII)**\ndisease outbreaks across species of animals;\n**(vi)**\nthe estimated amount of direct payments made by foreign countries to producers of live sheep and goats in such countries as a result of the implementation of the rule referred to in subsection (a); and\n**(vii)**\nany negative impacts that could result from the implementation of the rule referred to in subsection (a) not covered by clauses (i) through (vi).\n**(2) Report**\n**(A) In general**\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Agriculture shall submit to the committees specified in subparagraph (B) a report that includes\u2014\n**(i)**\nan analysis of the results of the study conducted under paragraph (1); and\n**(ii)**\nrecommendations for changes to the rule referred to in subsection (a) to eliminate or mitigate any negative effects of the implementation of the rule.\n**(B) Committees specified**\nThe committees specified in this subparagraph are\u2014\n**(i)**\nthe Committee on Agriculture, Nutrition, and Forestry, the Committee on Foreign Relations, the Committee on Finance, and the Committee on Homeland Security and Governmental Affairs of the Senate; and\n**(ii)**\nthe Committee on Agriculture, the Committee on Foreign Affairs, and the Committee on Oversight and Reform of the House of Representatives.",
      "versionDate": "2025-12-04",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-01-08T17:46:52Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3377is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to delay the implementation of a rule relating to the importation of sheep and goats and products derived from sheep and goats, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:48:19Z"
    },
    {
      "title": "A bill to delay the implementation of a rule relating to the importation of sheep and goats and products derived from sheep and goats, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-05T11:56:22Z"
    }
  ]
}
```
