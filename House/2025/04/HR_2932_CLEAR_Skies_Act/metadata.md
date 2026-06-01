# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2932?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2932
- Title: CLEAR Skies Act
- Congress: 119
- Bill type: HR
- Bill number: 2932
- Origin chamber: House
- Introduced date: 2025-04-17
- Update date: 2025-05-28T15:20:38Z
- Update date including text: 2025-05-28T15:20:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-17: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-17: Introduced in House

## Actions

- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-17",
    "latestAction": {
      "actionDate": "2025-04-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2932",
    "number": "2932",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "G000598",
        "district": "42",
        "firstName": "Robert",
        "fullName": "Rep. Garcia, Robert [D-CA-42]",
        "lastName": "Garcia",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "CLEAR Skies Act",
    "type": "HR",
    "updateDate": "2025-05-28T15:20:38Z",
    "updateDateIncludingText": "2025-05-28T15:20:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-17",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-17",
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
          "date": "2025-04-17T13:32:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2932ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2932\nIN THE HOUSE OF REPRESENTATIVES\nApril 17, 2025 Mr. Garcia of California (for himself and Mr. Obernolte ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a tax credit for the production of aviation gasoline that is free of tetra-ethyl-lead.\n#### 1. Short title\nThis Act may be cited as the Cutting Lead Exposure and Aviation Relief Skies Act or the CLEAR Skies Act .\n#### 2. Aviation gasoline production credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Aviation gasoline production credit (a) Amount of credit (1) In general For purposes of section 38, the aviation gasoline production credit determined under this section for the taxable year is an amount equal to the product of\u2014 (A) the number of gallons of qualified aviation gasoline produced by the taxpayer and sold by the taxpayer in the manner described in paragraph (5) during the taxable year, multiplied by (B) the applicable amount with respect to such gasoline. (2) Applicable amount The applicable amount under this paragraph is equal to\u2014 (A) in the case of qualified aviation gasoline sold during calendar year 2026, $1.25, (B) in the case of qualified aviation gasoline sold during calendar year 2027, $1.20, (C) in the case of qualified aviation gasoline sold during calendar year 2028, $1.15, (D) in the case of qualified aviation gasoline sold during calendar year 2029, $1.10, and (E) in the case of qualified aviation gasoline sold during calendar year 2030, $1.05. (3) Qualified aviation gasoline For purposes of this section, the term qualified aviation gasoline means aviation gasoline\u2014 (A) which is\u2014 (i) defined in section 436.101 of title 10, Code of Federal Regulations, (ii) free from tetra-ethyl-lead, and (iii) produced by the taxpayer in the United States, (B) which meets the requirements of any aviation fuel standards promulgated pursuant to section 44714 of title 49, United States Code, and (C) the transfer of which to the fuel tank of an aircraft occurs in the United States. (4) Sale For purposes of paragraph (1), the qualified aviation gasoline is sold in a manner described in this paragraph if such gasoline is sold by the taxpayer to an unrelated person\u2014 (A) for use by such person in a trade or business, or (B) who sells such fuel at retail to another person and places such fuel in the fuel tank of such other person. (b) Registration of qualified aviation gasoline producers No credit shall be allowed under this section with respect to any aviation gasoline unless the producer of such fuel\u2014 (1) is registered with the Secretary under section 4101, and (2) provides certification (in such form or manner as the Secretary shall prescribe after consultation with the Secretary of Transportation) demonstrating that such gasoline is qualified aviation gasoline. (c) Regulations and guidance Not later than 180 days after the date of the enactment of this section, the Secretary shall, after consultation with the Secretary of Transportation, prescribe such regulations and guidance as are necessary to carry out the purposes of this section. (d) Termination This section shall not apply to any sale after December 31, 2030. .\n##### (b) Credit made part of general business credit\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by inserting after paragraph (41) the following new paragraph:\n(42) the aviation gasoline production credit determined under section 45BB. .\n##### (c) Certification of producers\nSection 4101(a)(1) of such Code is amended by striking and every person producing second generation biofuel (as defined in section 40(b)(6)(E)) and inserting every person producing second generation biofuel (as defined in section 40(b)(6)(E)), and every person producing qualified aviation gasoline (as defined in section 45BB(a)(4)) .\n##### (d) Qualified aviation gasoline taxed as aviation gasoline\nSection 4081(a)(2)(A)(ii) of such Code is amended by inserting (including qualified aviation gasoline as defined in section 45BB(a)(4)) after aviation gasoline .\n##### (e) Clerical amendment\nThe table of sections for subpart D of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 45AA the following new item:\nSec. 45BB. Aviation gasoline credit. .\n##### (f) Effective date\nThe amendments made by this section shall apply to fuel sold or used after December 31, 2025.\n#### 3. GAO Study\n##### (a) Study\nThe Comptroller General of the United States shall carry out a study relating to the price of unleaded aviation gas, including\u2014\n**(1)**\nthe price differential of leaded aviation gas at the consumer point of sale as compared with unleaded aviation gas, including unleaded aviation gas at different octane levels,\n**(2)**\nthe major drivers of the price differential between leaded and unleaded gas, including research and development, refining, transportation and delivery and storage,\n**(3)**\nwhether the aviation gasoline credit under section 45BB of the Internal Revenue Code of 1986 (as added by section 1) results in cost savings that are passed along to the end-user consumer,\n**(4)**\nrecommendations, if any, for changes to such credit to ensure the highest amount of cost savings is passed along to the end-user consumer, and\n**(5)**\nthe amount and percentage of unleaded aviation gas in the overall aviation gas market and future market projections for such amount and percentage.\n##### (b) Report\nNot later than one year after the date of the enactment of this Act, the Comptroller General of the United States shall issue a report to Congress describing the findings and determinations made in carrying out the study required under subsection (a).",
      "versionDate": "2025-04-17",
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
        "name": "Taxation",
        "updateDate": "2025-05-28T15:20:38Z"
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
      "date": "2025-04-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2932ih.xml"
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
      "title": "CLEAR Skies Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-03T03:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CLEAR Skies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cutting Lead Exposure and Aviation Relief Skies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a tax credit for the production of aviation gasoline that is free of tetra-ethyl-lead.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:48:32Z"
    }
  ]
}
```
