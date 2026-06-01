# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2625?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2625
- Title: Independent BROKERS TIME Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2625
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-09-18T19:12:08Z
- Update date including text: 2025-09-18T19:12:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2625",
    "number": "2625",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Independent BROKERS TIME Act of 2025",
    "type": "S",
    "updateDate": "2025-09-18T19:12:08Z",
    "updateDateIncludingText": "2025-09-18T19:12:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T20:31:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2625is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2625\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Rounds (for himself and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo require the Secretary of Health and Human Services to carry out certain activities relating to the regulation of independent agents and brokers and third-party marketing organizations under parts C and D of the Medicare program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Independent Broker Relief and Oversight of Knowingly Egregious and Repetitive Sales Tactics In Medicare Enrollment Act of 2025 or the Independent BROKERS TIME Act of 2025 .\n#### 2. Required rulemaking proceedings\n##### (a) Updating the definition of a third-Party marketing organization (TPMO) under parts C and D of the Medicare program\n**(1) Definition**\n**(A) In general**\nThe Secretary of Health and Human Services (in this section referred to as the Secretary ) shall conduct a rulemaking proceeding with respect to the definition of third-party marketing organization to\u2014\n**(i)**\naddress how to distinguish between a third-party marketing organization and an independent agent or broker for purposes of applying regulatory requirements under sections 422.2274(g)(2)(ii) and 423.2274(g)(2)(ii) of title 42, Code of Federal Regulations (or any successor regulation); and\n**(ii)**\ndetermine the factors that should be taken into consideration when regulating various agent and broker entities.\n**(B) Requirements**\n**(i) Third-party marketing organizations**\nIn carrying out subparagraph (A), the Secretary shall\u2014\n**(I)**\ntake into account whether third-party marketing organizations include call centers that are not physically located in the continental United States, publicly traded marketing companies, private equity financed marketing companies, and companies that generate the majority of their revenue by generating leads; and\n**(II)**\nensure that the lead generation aspects of third-party marketing organizations are held to licensed insurance agent compliance standards.\n**(ii) Independent agents and brokers**\nIn carrying out subparagraph (A), the Secretary shall take into account that independent agents and brokers include individuals who enroll and service clients, insurance agencies that represent multiple carriers, public agencies, and privately held agencies that in effect are variable cost sales offices for the carriers.\n##### (b) Oversight of predatory call centers\nThe Secretary shall conduct a rulemaking proceeding to amend section 420.405 of title 42, Code of Federal Regulations (or any successor regulation), to provide for a monetary reward to individuals who submit information on call centers engaging in, or that have engaged in, marketing scams related to the Medicare program.\n##### (c) Standardized registration process for independent agents and brokers\nThe Secretary shall conduct a rulemaking proceeding to\u2014\n**(1)**\nrequire that PDP sponsors under part D of the Medicare program and MA organizations under part C of such program provide a standardized registration process for independent agents and brokers;\n**(2)**\nensure that such standardized registration process includes a transparent mechanism to distinguish independent agents and brokers from third-party marketing organizations; and\n**(3)**\nreduce regulatory burdens facing independent agents and brokers with respect to existing customers versus new business.\n##### (d) Application\n**(1) Procedures**\nIn conducting the rulemaking proceeding under each of subsections (a), (b), and (c), the Secretary shall\u2014\n**(A)**\npublish a notice in the Federal Register;\n**(B)**\nestablish a comment period to allow interested persons to submit written data, views, and arguments for at least a 90-day period beginning on the date on which the notice is published in the Federal Register; and\n**(C)**\nmake all such submissions publicly available.\n**(2) Timing**\nThe Secretary shall issue a final rule to complete the rulemaking proceeding under each of subsections (a), (b), and (c) not later than 1 year after the date of enactment of this section.\n**(3) Review**\nAny review of the rulemaking proceeding under subsection (a), (b), or (c) that is conducted by the Office of Information and Regulatory Affairs in accordance with Executive Order 12866 shall be limited to 60 days.\n#### 3. Nullification of 48-hour waiting period requirement for independent agents and brokers\nSection 1851(j)(2)(A) of the Social Security Act ( 42 U.S.C. 1395w\u201321(j)(2)(A) ) is amended\u2014\n**(1)**\nby striking appointments .\u2014The scope of and inserting \u201c appointments .\u2014\n(i) In general Subject to clause (ii), the scope of ; and\n**(2)**\nby adding at the end the following new clause:\n(ii) Nullification of 48-hour waiting period requirement for independent agents and brokers The Secretary shall not take any action to enforce an extended waiting period (including the 48-hour waiting period described in sections 422.2264(c)(3)(i) and 423.2264(c)(3)(i) of title 42, Code of Federal Regulations (or any successor regulation)) or require a specific period of time to pass between a Scope of Appointment agreement and an independent agent or brokers meeting with a Medicare beneficiary. .\n#### 4. Inspector General review and report on predatory call centers\n##### (a) Review\nThe Inspector General of the Department of Health and Human Services (in this section referred to as the Inspector General ) shall conduct a review of potentially fraudulent or misleading marketing practices of predatory call centers that are related to the Medicare program.\n##### (b) Report\nNot later than 1 year after the date of enactment of this section, the Inspector General shall submit to Congress a report containing the results of the review conducted under subsection (a), together with recommendations for such legislation and administrative action as the Inspector General determines appropriate.",
      "versionDate": "2025-07-31",
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
        "name": "Health",
        "updateDate": "2025-09-18T19:12:08Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2625is.xml"
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
      "title": "Independent BROKERS TIME Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:53:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Independent BROKERS TIME Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Independent Broker Relief and Oversight of Knowingly Egregious and Repetitive Sales Tactics In Medicare Enrollment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Health and Human Services to carry out certain activities relating to the regulation of independent agents and brokers and third-party marketing organizations under parts C and D of the Medicare program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:48:28Z"
    }
  ]
}
```
