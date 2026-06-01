# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4045?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4045
- Title: Food and Nutrition Delivery Safety Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4045
- Origin chamber: Senate
- Introduced date: 2026-03-10
- Update date: 2026-04-09T17:09:45Z
- Update date including text: 2026-04-09T17:09:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-10: Introduced in Senate
- 2026-03-10 - IntroReferral: Introduced in Senate
- 2026-03-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-03-10: Introduced in Senate

## Actions

- 2026-03-10 - IntroReferral: Introduced in Senate
- 2026-03-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-10",
    "latestAction": {
      "actionDate": "2026-03-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4045",
    "number": "4045",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000479",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Fetterman, John [D-PA]",
        "lastName": "Fetterman",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Food and Nutrition Delivery Safety Act of 2026",
    "type": "S",
    "updateDate": "2026-04-09T17:09:45Z",
    "updateDateIncludingText": "2026-04-09T17:09:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-10",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-10",
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
          "date": "2026-03-10T21:37:04Z",
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "CA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "CO"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4045is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4045\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2026 Mr. Fetterman (for himself, Mr. Schiff , Mr. Bennet , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food and Nutrition Act of 2008 to establish online and delivery standards, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Food and Nutrition Delivery Safety Act of 2026 .\n#### 2. Online and delivery standards\nSection 9 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2018 ) is amended by adding at the end the following:\n(k) Online and delivery standards (1) In general Not later than 18 months after the date of enactment of this subsection, the Administrator of the Food and Nutrition Service, in consultation with the Administrator of the Food Safety and Inspection Service, the Commissioner of Food and Drugs, the Director of the Office of Science and Technology Policy, and relevant stakeholders, shall establish\u2014 (A) for any retail food store or wholesale food concern authorized to accept and redeem benefits under the supplemental nutrition assistance program that accepts benefits through an online or mobile platform, standards for the safe and secure online use of the online or mobile platforms by participants in the supplemental nutrition assistance program and retail participants, including with respect to digital privacy and cybersecurity of the user; and (B) for any retail food store or wholesale food concern authorized to accept and redeem benefits under the supplemental nutrition assistance program that provides delivery services for foods purchased using those benefits, delivery standards that aim\u2014 (i) to promote fair and safe working conditions for the employees of that delivery service, including paying prevailing wages; and (ii) to keep food safe and secure during delivery. (2) Report requirement Not later than 18 months after the date on which the Administrator of the Food and Nutrition Service establishes standards under paragraph (1), the Secretary shall promulgate regulations that require a retail food store or wholesale food concern seeking authorization under this section to accept and redeem benefits under the supplemental nutrition assistance program to submit to the Secretary a report describing compliance with the standards established under paragraph (1). (3) Effects of noncompliance If a retail food store or wholesale food concern does not comply with the standards established under paragraph (1), that retail food store or wholesale food concern\u2014 (A) shall lose authorization to participate in the supplemental nutrition assistance program; and (B) may reapply for that authorization upon demonstrating that the retail food store or wholesale food concern, as applicable, is in compliance with those standards. .",
      "versionDate": "2026-03-10",
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
        "actionDate": "2026-03-24",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "8046",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Food and Nutrition Delivery Safety Act of 2026",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-03-30T17:30:37Z"
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
      "date": "2026-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4045is.xml"
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
      "title": "Food and Nutrition Delivery Safety Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T04:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Food and Nutrition Delivery Safety Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food and Nutrition Act of 2008 to establish online and delivery standards, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T04:18:36Z"
    }
  ]
}
```
