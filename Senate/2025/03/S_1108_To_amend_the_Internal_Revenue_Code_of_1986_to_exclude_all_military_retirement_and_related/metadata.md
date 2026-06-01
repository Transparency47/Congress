# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1108?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1108
- Title: Tax Cuts for Veterans Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1108
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2025-12-17T16:31:15Z
- Update date including text: 2025-12-17T16:31:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1108",
    "number": "1108",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Tax Cuts for Veterans Act of 2025",
    "type": "S",
    "updateDate": "2025-12-17T16:31:15Z",
    "updateDateIncludingText": "2025-12-17T16:31:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T15:41:01Z",
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
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NV"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1108is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1108\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Ricketts (for himself and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude all military retirement and related benefits from Federal income tax.\n#### 1. Short title\nThis Act may be cited as the Tax Cuts for Veterans Act of 2025 .\n#### 2. Exclusion of all military retirement and related benefits\n##### (a) In general\nSection 122 of the Internal Revenue Code of 1986 is amended to read as follows:\n122. Certain uniformed services retirement pay and related benefits (a) General rule In the case of a member or former member of the armed forces of the United States, gross income does not include\u2014 (1) any retired or retainer pay paid under title 10 or 14, United States Code, or (2) any amounts not described in section 104(a)(4) received as monthly compensation, pension, pay, annuity, or allowance paid under title 10, 14, 37, or 38, United States Code, in connection with a disability or combat-related injury or disability or death of a member of the armed forces. (b) Certain reduced uniformed services retirement pay (1) In general In the case of a member or former member of the uniformed services of the United States other than a member or former member of the armed forces, gross income does not include the amount of any reduction in retired or retainer pay pursuant to the provisions of chapter 73 of title 10, United States Code. (2) Special rule (A) Amount excluded from gross income In the case of any individual referred to in paragraph (1), all amounts received as retired or retainer pay shall be excluded from gross income until there has been so excluded an amount equal to the consideration for the contract. The preceding sentence shall apply only to the extent that the amounts received would, but for such sentence, be includible in gross income. (B) Consideration for the contract For purposes of subparagraph (A) and section 72(n), the term consideration for the contract means, in respect of any individual, the sum of\u2014 (i) the total amount of the reductions before January 1, 1966, in the individual's retired or retainer pay by reason of an election under chapter 73 of title 10 of the United States Code, and (ii) any amounts deposited at any time by the individual pursuant to section 1438 or 1452(d) of such title 10. (c) Definitions For purposes of this section, the terms armed forces and uniformed services have the respective meanings given such terms by section 101 of title 10, United States Code. .\n##### (b) Conforming amendments\n**(1) Conforming repeal**\n**(A) In general**\nSection 1403 of title 10, United States Code, is repealed.\n**(B) Clerical amendment**\nThe table of sections at the beginning of chapter 71 of such title is amended by striking the item relating to section 1403.\n**(2) Annuities**\nSubsection (n) of section 72 of the Internal Revenue Code of 1986 is amended by striking Subsection (b) and inserting In the case of any member or former member of the uniformed services of the United States other than a member or former member of the armed forces, subsection (b) .\n##### (c) Clerical amendment\nThe item relating to section 122 in the table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended to read as follows:\nSec. 122. Certain uniformed services retirement pay and related benefits. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-03-25",
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
        "actionDate": "2025-11-20",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "6190",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Tax Cuts for Veterans Act of 2025",
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
        "updateDate": "2025-05-08T19:26:50Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1108is.xml"
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
      "title": "Tax Cuts for Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T02:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tax Cuts for Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to exclude all military retirement and related benefits from Federal income tax.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T02:48:21Z"
    }
  ]
}
```
