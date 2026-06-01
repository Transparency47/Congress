# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7776?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7776
- Title: Highway Formula Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 7776
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-03-24T20:09:32Z
- Update date including text: 2026-03-24T20:09:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-03-03: Introduced in House

## Actions

- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7776",
    "number": "7776",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Highway Formula Fairness Act",
    "type": "HR",
    "updateDate": "2026-03-24T20:09:32Z",
    "updateDateIncludingText": "2026-03-24T20:09:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "TX"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7776ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7776\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Mr. Roy (for himself, Mr. Weber of Texas , and Mr. Cuellar ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo modify a provision relating to adjustments of certain State apportionments for Federal highway programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Highway Formula Fairness Act .\n#### 2. Adjustments to certain State apportionment amounts\nSection 104 of title 23, United States Code, is amended by striking subsection (c) and inserting the following:\n(c) Calculation of amounts (1) State share For fiscal year 2026 and each fiscal year thereafter, the amount for each State of combined apportionments for sections 119, 133, 148, 149, 167, 175, 176(c), and to carry out section 134 shall be determined as follows: (A) Initial amount The initial amount for each State shall be determined by multiplying the total amount available for apportionment by the share for each State, which shall be equal to the proportion that\u2014 (i) the amount of apportionments that the State received for fiscal year 2012; bears to (ii) the amount of those apportionments received by all States for that fiscal year. (B) Adjustments to amounts (i) In general The initial amounts resulting from the calculation under subparagraph (A) shall be adjusted to ensure that, for each State, the amount of combined apportionments for the programs shall not be less than an amount equal to\u2014 (I) 95 percent of the applicable percentage; multiplied by (II) the total amount of funds available for apportionment. (ii) Applicable percentage For purposes of this subparagraph, the applicable percentage shall be an amount, expressed as a percentage, equal to the quotient of\u2014 (I) the estimated tax payments attributable to highway users in the State that were paid into the Highway Trust Fund (other than the Mass Transit Account) for the most recent fiscal year for which data are available; divided by (II) the estimated total tax payments attributable to users in all States that were paid into the Highway Trust Fund (other than the Mass Transit Account) for that fiscal year. (2) State apportionment On October 1 of each fiscal year described in paragraph (1), the Secretary shall apportion the sum authorized to be appropriated for expenditure on the programs under sections 119, 133, 148, 149, 167, 175, 176(c), and to carry out section 134 in accordance with paragraph (1). .",
      "versionDate": "2026-03-03",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-03-24T20:09:31Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7776ih.xml"
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
      "title": "Highway Formula Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T08:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Highway Formula Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T08:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To modify a provision relating to adjustments of certain State apportionments for Federal highway programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T08:18:26Z"
    }
  ]
}
```
