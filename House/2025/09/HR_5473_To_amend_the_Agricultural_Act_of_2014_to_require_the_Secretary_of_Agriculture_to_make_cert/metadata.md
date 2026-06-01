# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5473?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5473
- Title: Farm Rescue Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5473
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2025-11-25T16:09:56Z
- Update date including text: 2025-11-25T16:09:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5473",
    "number": "5473",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "L000595",
        "district": "5",
        "firstName": "Julia",
        "fullName": "Rep. Letlow, Julia [R-LA-5]",
        "lastName": "Letlow",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Farm Rescue Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-25T16:09:56Z",
    "updateDateIncludingText": "2025-11-25T16:09:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5473ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5473\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Ms. Letlow introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Act of 2014 to require the Secretary of Agriculture to make certain advance partial price loss coverage payments for crop year 2025.\n#### 1. Short title\nThis Act may be cited as the Farm Rescue Act of 2025 .\n#### 2. Availability of advance partial price loss coverage payments for crop year 2025\n##### (a) In general\nSection 1116(e) of the Agricultural Act of 2014 ( 7 U.S.C. 9016(e) ) is amended\u2014\n**(1)**\nby striking If the Secretary and inserting the following:\n(1) In general Subject to paragraph (2), if the Secretary ; and\n**(2)**\nby adding at the end the following:\n(2) Availability of advance partial payments for crop year 2025 (A) In general Not later than 90 days after the date of the enactment of this paragraph, if the Secretary determines, based on the best available data and projections of national average market prices, that price loss coverage payments for the 2025 crop year will be required to be provided under subsection (a) with respect to a covered commodity, the Secretary shall\u2014 (i) give producers on a farm the option to receive partial payments of the price loss coverage payment to be made for that covered commodity for the 2025 crop year with respect to payment acres for the covered commodity on the farm; and (ii) to each producer that opts to receive such payments under clause (i), provide\u2014 (I) a one-time partial payment in accordance with subparagraph (B); and (II) a subsequent payment in accordance with section 1115(j). (B) Amount Notwithstanding section 1115(a), a partial payment under subparagraph (A)(ii)(I) shall be in an amount that is not less than 40 percent and not greater than 50 percent of the projected price loss coverage payment for the covered commodity for the 2025 crop year, as determined by the Secretary. (C) Recovery of erroneous payment If the Secretary determines that a partial payment made under subparagraph (A) was not required with respect to a covered commodity for the 2025 crop year the Secretary may recover the amount of the partial payment in such a manner as the Secretary determines appropriate. .\n##### (b) Subsequent payment for crop year 2025\nSection 1115 of the Agricultural Act of 2014 ( 7 U.S.C. 9015 ) is amended by adding at the end the following:\n(j) Subsequent payment for crop year 2025 In the case of a producer on a farm that receives a partial payment under section 1116(e)(2)(A) for a covered commodity for the 2025 crop year with respect to payment acres for the covered commodity on the farm, the Secretary shall, as soon as practicable after the end of the applicable marketing year for the covered commodity, provide a subsequent payment to the producer in an amount equal to\u2014 (1) the payment amount for such payment acres for the covered commodity determined under subsection (i) for the 2025 crop year; minus (2) the amount provided for such payment acres for the covered commodity under section 1116(e)(2)(B) for the 2025 crop year. .\n##### (c) Rulemaking\nNot later than 60 days after the date of the enactment of this Act, the Secretary of Agriculture shall issue such rules as are necessary to carry out the amendments made by this section.",
      "versionDate": "2025-09-18",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-11-25T16:09:56Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5473ih.xml"
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
      "title": "Farm Rescue Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Farm Rescue Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Act of 2014 to require the Secretary of Agriculture to make certain advance partial price loss coverage payments for crop year 2025.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:19Z"
    }
  ]
}
```
