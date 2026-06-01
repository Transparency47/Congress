# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2705?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2705
- Title: Keep Violent Criminals Off Our Streets Act
- Congress: 119
- Bill type: S
- Bill number: 2705
- Origin chamber: Senate
- Introduced date: 2025-09-04
- Update date: 2026-05-07T01:49:01Z
- Update date including text: 2026-05-07T01:49:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in Senate
- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-09-04: Introduced in Senate

## Actions

- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2705",
    "number": "2705",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Keep Violent Criminals Off Our Streets Act",
    "type": "S",
    "updateDate": "2026-05-07T01:49:01Z",
    "updateDateIncludingText": "2026-05-07T01:49:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-04",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T15:15:36Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sponsorshipDate": "2025-09-04",
      "state": "TX"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-10-07",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2705is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2705\nIN THE SENATE OF THE UNITED STATES\nSeptember 4, 2025 Mrs. Blackburn (for herself and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to prohibit the award of Edward Byrne Memorial Justice Assistance Grants to States or units of local government that limit the use of cash bail.\n#### 1. Short title\nThis Act may be cited as the Keep Violent Criminals Off Our Streets Act .\n#### 2. Prohibition on grants for certain entities\nSection 502 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10153 ) is amended\u2014\n**(1)**\nin the matter designated as subsection (A), by striking (A) In general and inserting (a) In general ; and\n**(2)**\nby adding at the end the following:\n(c) Ineligibility (1) Covered offense defined In this subsection, the term covered offense means a criminal offense that poses a clear threat to public safety and order, including\u2014 (A) an offense involving a violent or sexual act, such as murder, rape, sexual assault, carjacking, robbery, burglary, and assault; and (B) an offense that promote public disorder, such as looting, vandalism, destruction of property, rioting or inciting to riot, or fleeing from a law enforcement officer. (2) Prohibition With respect to the fiscal year beginning on the first October 1 occurring after the date of enactment of the Keep Violent Criminals Off Our Streets Act , and each fiscal year thereafter, the Attorney General may not award, renew, or extend a grant under this subpart to a State or unit of local government that has in effect a policy or law that substantially limits cash bail as a potential condition for every individual charged with a covered offense in the State or the area under the jurisdiction of the unit of local government. .",
      "versionDate": "2025-09-04",
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
        "actionDate": "2026-05-04",
        "text": "Placed on the Union Calendar, Calendar No. 554."
      },
      "number": "5213",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "No Federal Funds for Cashless Bail Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2026-03-10T18:47:34Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-03-10T18:47:34Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-03-10T18:47:34Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2026-03-10T18:47:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-23T14:33:32Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2705is.xml"
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
      "title": "Keep Violent Criminals Off Our Streets Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-08T11:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Keep Violent Criminals Off Our Streets Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to prohibit the award of Edward Byrne Memorial Justice Assistance Grants to States or units of local government that limit the use of cash bail.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:03:25Z"
    }
  ]
}
```
