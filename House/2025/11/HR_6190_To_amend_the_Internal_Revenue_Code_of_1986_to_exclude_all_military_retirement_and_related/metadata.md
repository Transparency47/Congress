# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6190?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6190
- Title: Tax Cuts for Veterans Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6190
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-03-17T08:05:29Z
- Update date including text: 2026-03-17T08:05:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6190",
    "number": "6190",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001098",
        "district": "8",
        "firstName": "Abraham",
        "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
        "lastName": "Hamadeh",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Tax Cuts for Veterans Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-17T08:05:29Z",
    "updateDateIncludingText": "2026-03-17T08:05:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:07:05Z",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "AL"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "KY"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "MP"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NC"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "PR"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6190ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6190\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Hamadeh of Arizona (for himself, Mr. Moore of Alabama , Mr. Levin , and Mr. Massie ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude all military retirement and related benefits from Federal income tax.\n#### 1. Short title\nThis Act may be cited as the Tax Cuts for Veterans Act of 2025 .\n#### 2. Exclusion of all military retirement and related benefits\n##### (a) In general\nSection 122 of the Internal Revenue Code of 1986 is amended to read as follows:\n122. Certain uniformed services retirement pay and related benefits (a) General rule In the case of a member or former member of the Armed Forces of the United States, gross income does not include\u2014 (1) any retired or retainer pay paid under title 10 or 14, United States Code, or (2) any amounts not described in section 104(a)(4) received as monthly compensation, pension, pay, annuity, or allowance paid under title 10, 14, 37, or 38, United States Code, in connection with a disability or combat-related injury or disability or death of a member of the Armed Forces. (b) Certain reduced uniformed services retirement pay (1) In general In the case of a member or former member of the uniformed services of the United States other than a member or former member of the Armed Forces, gross income does not include the amount of any reduction in retired or retainer pay pursuant to the provisions of chapter 73 of title 10, United States Code. (2) Special rule (A) Amount excluded from gross income In the case of any individual referred to in paragraph (1), all amounts received as retired or retainer pay shall be excluded from gross income until there has been so excluded an amount equal to the consideration for the contract. The preceding sentence shall apply only to the extent that the amounts received would, but for such sentence, be includible in gross income. (B) Consideration for the contract For purposes of subparagraph (A) and section 72(n), the term consideration for the contract means, in respect of any individual, the sum of\u2014 (i) the total amount of the reductions before January 1, 1966, in the individual's retired or retainer pay by reason of an election under chapter 73 of title 10 of the United States Code, and (ii) any amounts deposited at any time by the individual pursuant to section 1438 or 1452(d) of such title 10. (c) Definitions For purposes of this section, the terms armed forces and uniformed services have the respective meanings given such terms by section 101 of title 10, United States Code. .\n##### (b) Conforming amendments\n**(1) Conforming repeal**\n**(A) In general**\nSection 1403 of title 10, United States Code, is repealed.\n**(B) Clerical amendment**\nThe table of sections at the beginning of chapter 71 of such title is amended by striking the item relating to section 1403.\n**(2) Annuities**\nSubsection (n) of section 72 of the Internal Revenue Code of 1986 is amended by striking Subsection (b) and inserting In the case of any member or former member of the uniformed services of the United States other than a member or former member of the armed forces, subsection (b) .\n##### (c) Clerical amendment\nThe item relating to section 122 in the table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended to read as follows:\nSec. 122. Certain uniformed services retirement pay and related benefits. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-03-25",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1108",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Tax Cuts for Veterans Act of 2025",
      "type": "S"
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
        "updateDate": "2025-12-04T21:31:12Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6190ih.xml"
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
      "title": "Tax Cuts for Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T08:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tax Cuts for Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T08:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude all military retirement and related benefits from Federal income tax.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T08:33:33Z"
    }
  ]
}
```
