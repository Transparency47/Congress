# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2209?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2209
- Title: Warrior Right to Repair Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2209
- Origin chamber: Senate
- Introduced date: 2025-07-08
- Update date: 2025-12-05T22:57:13Z
- Update date including text: 2025-12-05T22:57:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-08: Introduced in Senate
- 2025-07-08 - IntroReferral: Introduced in Senate
- 2025-07-08 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-07-08: Introduced in Senate

## Actions

- 2025-07-08 - IntroReferral: Introduced in Senate
- 2025-07-08 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-08",
    "latestAction": {
      "actionDate": "2025-07-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2209",
    "number": "2209",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Warrior Right to Repair Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:57:13Z",
    "updateDateIncludingText": "2025-12-05T22:57:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-08",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-08",
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
          "date": "2025-07-08T21:28:06Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2209is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2209\nIN THE SENATE OF THE UNITED STATES\nJuly 8, 2025 Ms. Warren (for herself and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require contractors to provide reasonable access to repair materials, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Warrior Right to Repair Act of 2025 .\n#### 2. Requirement for contractors to provide reasonable access to repair materials\n##### (a) In general\nChapter 363 of title 10, United States Code, is amended by adding at the end the following new section:\n4663. Requirement for contractors to provide reasonable access to repair materials (a) Requirement The head of an agency may not enter into a contract for the procurement of goods unless the contractor agrees in writing to provide the Department of Defense fair and reasonable access to all the repair materials, including parts, tools, and information, used by the manufacturer or provider or their authorized repair providers to diagnose, maintain, or repair the goods. (b) Waiver authority for existing programs The head of an agency may waive the requirement under subsection (a) for a contract that is related to a program that began before the date of the enactment of this section upon submitting to the congressional defense committees a justification for the waiver based on an independent technical risk assessment identifying likely impacts to the program\u2019s costs, schedule, or technical performance, including consideration and reporting of quantifiable, cost, schedule, and technical performance implications. (c) Definitions In this section: (1) Fair and reasonable access The term fair and reasonable access means\u2014 (A) terms and conditions that allow the Department of Defense to provide the repair materials to an authorized contractor for the purpose of diagnosing, maintaining, or repairing the good; (B) provision at prices, terms, and conditions that are equivalent to the most favorable prices, terms, and conditions under which the manufacturer or an authorized reseller or distributor offers the part, tool, or information to an authorized repair provider, accounting for any discount, rebate, convenient and timely means of delivery, means of enabling fully restored and updated functionality, rights of use, or other incentive or preference the manufacturer or an authorized reseller or distributor offers to an authorized repair provider; and (C) if a manufacturer does not offer, directly or through an authorized reseller or distributor, the part, tool, or information to any authorized repair provider, then provision of such part, tool, or information at prices, terms, and conditions that are otherwise determined by the United States Government to be fair and reasonable in accordance with this title. (2) Part The term part means any replacement part, either new or used, made available by or to an original equipment manufacturer (OEM) for purposes of effecting the services of maintenance or repair of digital electronic equipment manufactured by or on behalf of, sold, or otherwise supplied by the OEM. (3) Tool The term tool means any software program, hardware implement, or other apparatus used for diagnosis, maintenance, or repair of digital electronic equipment, including software or other mechanisms that provision, program, or pair a part, calibrate functionality, or perform any other function required to bring the equipment back to fully functional condition. .\n##### (b) Report\nNot later than 1 year after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the congressional defense committees a report on the implementation of section 4663 of title 10, United States Code, as added by this section, including a description of compliance by the Department of Defense with the requirements of such section.\n#### 3. Requirement for contract modifications related to repair capabilities\n##### (a) In general\nThe Secretary of Defense shall conduct a review to identify contract modifications necessary to remove intellectual property constraints that limit the ability of the Department of Defense to conduct maintenance and access the repair materials, including parts, tools, and information, used by the manufacturer or provider or their authorized repair providers to diagnose, maintain, or repair goods covered by a contract.\n##### (b) Definitions\nIn this section:\n**(1) Part**\nThe term part means any replacement part, either new or used, made available by or to an original equipment manufacturer (OEM) for purposes of effecting the services of maintenance or repair of digital electronic equipment manufactured by or on behalf of, sold, or otherwise supplied by the OEM.\n**(2) Tool**\nThe term tool means any software program, hardware implement, or other apparatus used for diagnosis, maintenance, or repair of digital electronic equipment, including software or other mechanisms that provision, program, or pair a part, calibrate functionality, or perform any other function required to bring the equipment back to fully functional condition.",
      "versionDate": "2025-07-08",
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
        "actionDate": "2025-09-04",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "5155",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Warrior Right to Repair Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-08-07T18:37:08Z"
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
      "date": "2025-07-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2209is.xml"
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
      "title": "Warrior Right to Repair Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T01:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Warrior Right to Repair Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require contractors to provide reasonable access to repair materials, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:48:30Z"
    }
  ]
}
```
