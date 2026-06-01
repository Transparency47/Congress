# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3972?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3972
- Title: Highway Formula Fairness Act
- Congress: 119
- Bill type: S
- Bill number: 3972
- Origin chamber: Senate
- Introduced date: 2026-03-03
- Update date: 2026-03-23T20:24:06Z
- Update date including text: 2026-03-23T20:24:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in Senate
- 2026-03-03 - IntroReferral: Introduced in Senate
- 2026-03-03 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2026-03-03: Introduced in Senate

## Actions

- 2026-03-03 - IntroReferral: Introduced in Senate
- 2026-03-03 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3972",
    "number": "3972",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Highway Formula Fairness Act",
    "type": "S",
    "updateDate": "2026-03-23T20:24:06Z",
    "updateDateIncludingText": "2026-03-23T20:24:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-03",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T20:20:02Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "TX"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "AZ"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3972is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3972\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2026 Mr. Cruz (for himself, Mr. Cornyn , Mr. Kelly , and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo modify a provision relating to adjustments of certain State apportionments for Federal highway programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Highway Formula Fairness Act .\n#### 2. Adjustments to certain State apportionment amounts\nSection 104 of title 23, United States Code, is amended by striking subsection (c) and inserting the following:\n(c) Calculation of amounts (1) State share For fiscal year 2027 and each fiscal year thereafter, the amount for each State of combined apportionments for the national highway performance program under section 119, the surface transportation block grant program under section 133, the highway safety improvement program under section 148, the congestion mitigation and air quality improvement program under section 149, the national highway freight program under section 167, the carbon reduction program under section 175, to carry out subsection (c) of the PROTECT program under section 176, and to carry out section 134 shall be determined as follows: (A) Initial amount The initial amount for each State shall be determined by multiplying the total amount available for apportionment by the share for each State, which shall be equal to the proportion that\u2014 (i) the amount of apportionments that the State received for fiscal year 2012; bears to (ii) the amount of those apportionments received by all States for that fiscal year. (B) Adjustments to amounts (i) In general The initial amounts resulting from the calculation under subparagraph (A) shall be adjusted to ensure that, for each State, the amount of combined apportionments for the programs shall not be less than an amount equal to\u2014 (I) 95 percent of the applicable percentage; multiplied by (II) the total amount of funds available for apportionment. (ii) Applicable percentage For purposes of this subparagraph, the applicable percentage shall be an amount, expressed as a percentage, equal to the quotient of\u2014 (I) the estimated tax payments attributable to highway users in the State that were paid into the Highway Trust Fund (other than the Mass Transit Account) for the most recent fiscal year for which data are available; divided by (II) the estimated total tax payments attributable to users in all States that were paid into the Highway Trust Fund (other than the Mass Transit Account) for that fiscal year. (2) State apportionment On October 1 of each fiscal year described in paragraph (1), the Secretary shall apportion the sum authorized to be appropriated for expenditure on the national highway performance program under section 119, the surface transportation block grant program under section 133, the highway safety improvement program under section 148, the congestion mitigation and air quality improvement program under section 149, the national highway freight program under section 167, the carbon reduction program under section 175, to carry out subsection (c) of the PROTECT program under section 176, and to carry out section 134 in accordance with paragraph (1). .",
      "versionDate": "",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-03-23T20:24:06Z"
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
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3972is.xml"
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
      "title": "Highway Formula Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T03:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Highway Formula Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to modify a provision relating to adjustments of certain State apportionments for Federal highway programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:44Z"
    }
  ]
}
```
