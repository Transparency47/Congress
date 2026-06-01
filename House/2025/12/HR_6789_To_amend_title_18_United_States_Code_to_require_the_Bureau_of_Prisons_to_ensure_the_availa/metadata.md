# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6789?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6789
- Title: Federal Prisons Naloxone Access Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6789
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-01-22T15:04:44Z
- Update date including text: 2026-01-22T15:04:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6789",
    "number": "6789",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "F000477",
        "district": "4",
        "firstName": "Valerie",
        "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
        "lastName": "Foushee",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Federal Prisons Naloxone Access Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-22T15:04:44Z",
    "updateDateIncludingText": "2026-01-22T15:04:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:05:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "GA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "GA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NY"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6789ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6789\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Mrs. Foushee (for herself, Mrs. McBath , and Mr. Johnson of Georgia ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to require the Bureau of Prisons to ensure the availability of opioid antagonists at Federal correctional facilities.\n#### 1. Short title\nThis Act may be cited as the Federal Prisons Naloxone Access Act of 2025 .\n#### 2. Availability of opioid antagonists\nChapter 303 of title 18, United States Code, is amended\u2014\n**(1)**\nby adding at the end the following:\n4052. Availability of opioid antagonists (a) In general The Director of the Bureau of Prisons shall ensure that\u2014 (1) an adequate number of opioid antagonist kits are maintained at each correctional facility administered by the Bureau, and such kits are available in\u2014 (A) medical housing units; (B) staff breakrooms; and (C) visiting areas, living quarters, recreation spaces, dining halls, housing units, work and program locations, hallways, corridor posts, security checkpoints, any area where incarcerated people congregate, and educational and religious areas; (2) that each such opioid antagonist kit is maintained appropriately, including storage\u2014 (A) in appropriate conditions at room temperature and out of direct sunlight; and (B) in a secure area that is accessible to personnel of the facility; (3) that incarcerated persons are able to access such opioid antagonist kits to administer to those who are overdosing; and (4) in the case of any opioid antagonist kit with an expiration date, that such kit is regularly checked to determine if there is a need to replace it. (b) Training The Director shall ensure that the personnel and incarcerated persons of each correctional facility administered by the Bureau receive annual training from medical staff of the Bureau of Prisons on the administration of opioid antagonists, including guidance on recognizing any signs or symptoms of an opioid overdose. (c) Documentation The Director shall ensure that, with regard to each administration of an opioid antagonist at a correctional facility, the following are recorded: (1) The location of the administration. (2) The time of the administration. (3) The name of the individual that the opioid antagonist was administered to. (4) The name and title of the person that administered the opioid antagonist and the status of the individual to whom the opioid antagonist was administered. (d) No liability for administration No incarcerated person may be held liable for the administration of an opioid antagonist kit in good faith. (e) Report The Director of the Bureau of Prisons shall submit a report each year to Congress detailing compliance with the requirements of this section, including\u2014 (1) the amount of opioid antagonists available at each correctional facility; (2) the number of opioid overdoses at each such facility; (3) the number of trainings under subsection (b) at each such facility; and (4) the number of expired opioid antagonist kits. (f) Definitions In this section: (1) The term opioid antagonist means a medication approved by the Federal Food and Drug Administration that, when administered, neutralizes in whole or in part the pharmacological effects of an opioid in the human body. (2) The term opioid overdose prevention kit means a kit containing\u2014 (A) an opioid antagonist; and (B) a pamphlet or other written notice that provides guidance on how to recognize the signs or symptoms of an opioid overdose and identifies the steps to take in response to a suspected opioid overdose. (3) The term personnel includes correctional officers, medical staff, counselors, and other employees of the Bureau of Prisons. (g) Authorization of appropriations There are authorized to be appropriated: (1) for fiscal year 2026, $6,000,000, for training, purchase of opioid antagonists, and the initial report; (2) for each of fiscal years 2027 and 2028, $2,000,000, for maintenance of opioid antagonist kits and training, and for additional reporting on the effectiveness of the program. ; and\n**(2)**\nin the table of sections for such chapter, by adding at the end the following:\n4052. Availability of opioid antagonists. .",
      "versionDate": "2025-12-17",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-01-22T15:04:44Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6789ih.xml"
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
      "title": "Federal Prisons Naloxone Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Prisons Naloxone Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to require the Bureau of Prisons to ensure the availability of opioid antagonists at Federal correctional facilities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:25Z"
    }
  ]
}
```
