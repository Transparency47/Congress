# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2023?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2023
- Title: Bicycle Commuter Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2023
- Origin chamber: Senate
- Introduced date: 2025-06-11
- Update date: 2025-12-05T21:56:26Z
- Update date including text: 2025-12-05T21:56:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in Senate
- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-11: Introduced in Senate

## Actions

- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2023",
    "number": "2023",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "Bicycle Commuter Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:56:26Z",
    "updateDateIncludingText": "2025-12-05T21:56:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
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
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T16:02:24Z",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2023is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2023\nIN THE SENATE OF THE UNITED STATES\nJune 11, 2025 Mr. Welch (for himself and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to modify employer-provided fringe benefits for bicycle commuting.\n#### 1. Short title\nThis Act may be cited as the Bicycle Commuter Act of 2025 .\n#### 2. Reinstatement and expansion of employer-provided fringe benefits for bicycle commuting\n##### (a) Repeal of suspension of exclusion for qualified bicycle commuting benefits\nSection 132(f) of the Internal Revenue Code of 1986 is amended by striking paragraph (8).\n##### (b) Expansion of bicycle commuting benefits\nSection 132(f)(5)(F) of such Code is amended to read as follows:\n(F) Definitions related to bicycle commuting benefits (i) Qualified bicycle commuting benefit The term qualified bicycle commuting benefit means, with respect to any calendar year\u2014 (I) any employer reimbursement during the 15-month period beginning with the first day of such calendar year for reasonable expenses incurred by the employee during such calendar year for the purchase (including associated finance charges), lease, rental (including a bikeshare), improvement, repair, or storage of qualified commuting property, or (II) the direct or indirect provision by the employer to the employee during such calendar year of the use (including a bikeshare), improvement, repair, or storage of qualified commuting property, if the employee regularly uses such qualified commuting property for travel between the employee\u2019s residence, place of employment, a qualified parking facility, or a mass transit facility that connects the employee to their residence or place of employment. (ii) Qualified commuting property The term qualified commuting property means\u2014 (I) any bicycle (other than a bicycle equipped with any motor), (II) any electric bicycle, (III) any 2- or 3-wheel scooter (other than a scooter equipped with any motor), and (IV) any 2- or 3-wheel scooter propelled by an electric motor if such motor does not provide assistance if the speed of such scooter exceeds 20 miler per hour (or if the speed of such scooter is not capable of exceeding 20 miles per hour) and the weight of such scooter does not exceed 100 pounds. (iii) Electric bicycle The term electric bicycle means a bicycle which is\u2014 (I) equipped with\u2014 (aa) fully operable pedals, (bb) a saddle or seat for the rider, and (cc) an electric motor which is less than 750 watts, designed to provide assistance in propelling the bicycle, and\u2014 (AA) does not provide such assistance if the bicycle is moving in excess of 20 miler per hour, or (BB) if such motor only provides such assistance when the rider is pedaling, does not provide such assistance if the bicycle is moving in excess of 28 miles per hour, and (II) certified by the manufacturer, importer, or distributor of such bicycle to comply with the requirements under part 1512 of title 16, Code of Federal Regulations (or any successor regulations issued by the Consumer Product Safety Commission). (iv) Bikeshare The term bikeshare means a rental operation at which qualified commuting property is made available to customers to pick up and drop off for point-to-point use within a defined geographic area. .\n##### (c) Limitation on exclusion\nSection 132(f)(2)(C) of such Code is amended to read as follows:\n(C) 30 percent of the dollar amount in effect under subparagraph (B) per month in the case of any qualified bicycle commuting benefit. .\n##### (d) No constructive receipt\nSection 132(f)(4) of such Code is amended by striking (other than a qualified bicycle commuting reimbursement) .\n##### (e) Conforming amendments\n**(1)**\nSection 132(f)(1)(D) of such Code is amended by striking reimbursement and inserting benefit .\n**(2)**\nSection 274(l) of such Code is amended by striking paragraph (2).\n##### (f) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-06-11",
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
        "actionDate": "2025-06-11",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "3936",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Bicycle Commuter Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-06-30T18:00:17Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2023is.xml"
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
      "title": "Bicycle Commuter Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-21T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Bicycle Commuter Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to modify employer-provided fringe benefits for bicycle commuting.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:25Z"
    }
  ]
}
```
