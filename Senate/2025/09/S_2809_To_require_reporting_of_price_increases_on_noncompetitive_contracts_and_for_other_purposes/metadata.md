# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2809?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2809
- Title: Transparency in Contracting Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2809
- Origin chamber: Senate
- Introduced date: 2025-09-16
- Update date: 2025-09-29T18:27:24Z
- Update date including text: 2025-09-29T18:27:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in Senate
- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-09-16: Introduced in Senate

## Actions

- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2809",
    "number": "2809",
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
    "title": "Transparency in Contracting Act of 2025",
    "type": "S",
    "updateDate": "2025-09-29T18:27:24Z",
    "updateDateIncludingText": "2025-09-29T18:27:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-16",
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
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T15:01:01Z",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "IA"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "IA"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2809is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2809\nIN THE SENATE OF THE UNITED STATES\nSeptember 16, 2025 Ms. Warren (for herself, Mr. Grassley , Ms. Ernst , and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require reporting of price increases on noncompetitive contracts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transparency in Contracting Act of 2025 .\n#### 2. Reporting of price increases\n##### (a) Reporting of increases above specified prices\nChapter 271 of title 10, United States Code, is amended by adding at the end the following new section:\n3709. Reporting of increases above specified prices (a) In general An offeror shall be required to report to the relevant contracting officer not later than 30 days after becoming aware that the price of a product or service under a covered contract reaches or exceeds\u2014 (1) 25 percent above the price specified in the contract bid or the government paid for that product or service the previous calendar year; or (2) 50 percent above the price paid for such a product or service 5 years earlier. (b) Covered contract defined In this section, the term covered contract means a contract awarded without competition under section 3204 of this title and as defined under section 6.302 of the Federal Acquisition Regulation. .\n##### (b) Inclusion of noncompliance information in FAPIIS\nChapter 271 of title 10, United States Code, as amended by subsection (a), is further amended by adding at the end the following new section:\n3710. Inclusion of noncompliance information in Federal Awardee Performance and Integrity Information System The Director of the Defense Contract Audit Agency or the relevant service acquisition executive shall report in the Federal Awardee Performance and Integrity Information System (FAPIIS) housed within the System for Award Management the following information: (1) Contractors who fail to report price increases as required under 3705(a)(2) of this title. (2) Updated findings from audits conducted by the Agency regarding noncompliance with the requirement. (3) With respect to unreported product or service price increases, the product or service\u2019s National Stock Number, order quantity, unit cost, total cost, purchasing or reimbursing entity, and date of the order. .",
      "versionDate": "2025-09-16",
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
        "updateDate": "2025-09-29T18:27:24Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2809is.xml"
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
      "title": "Transparency in Contracting Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-27T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Transparency in Contracting Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require reporting of price increases on noncompetitive contracts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T03:33:24Z"
    }
  ]
}
```
